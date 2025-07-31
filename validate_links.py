#!/usr/bin/env python3
"""
Link Validation Script for Requirements Documents
Validates all links in HTML requirements documents across all profession folders.
"""

import os
import re
import requests
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from urllib.parse import urlparse
import time

def extract_links_from_html(file_path: str) -> List[Tuple[str, int]]:
    """Extract all links from an HTML file with line numbers."""
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Find all href attributes
                href_pattern = r'href=["\']([^"\']+)["\']'
                matches = re.findall(href_pattern, line)
                for match in matches:
                    if match.startswith('http'):
                        links.append((match, line_num))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return links

def validate_link(url: str, timeout: int = 10) -> Dict:
    """Validate a single link and return status information."""
    result = {
        'url': url,
        'status': 'unknown',
        'status_code': None,
        'error': None,
        'content_type': None,
        'title': None
    }
    
    try:
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        result['status_code'] = response.status_code
        result['content_type'] = response.headers.get('content-type', '')
        
        if response.status_code == 200:
            result['status'] = 'valid'
            # Try to extract title for content validation
            if 'text/html' in result['content_type']:
                title_match = re.search(r'<title[^>]*>([^<]+)</title>', response.text, re.IGNORECASE)
                if title_match:
                    result['title'] = title_match.group(1).strip()
        elif response.status_code in [301, 302, 303, 307, 308]:
            result['status'] = 'redirect'
        elif response.status_code == 403:
            result['status'] = 'forbidden'
        elif response.status_code == 404:
            result['status'] = 'not_found'
        else:
            result['status'] = 'error'
            
    except requests.exceptions.Timeout:
        result['status'] = 'timeout'
        result['error'] = 'Request timed out'
    except requests.exceptions.ConnectionError:
        result['status'] = 'connection_error'
        result['error'] = 'Connection failed'
    except requests.exceptions.RequestException as e:
        result['status'] = 'error'
        result['error'] = str(e)
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f"Unexpected error: {str(e)}"
    
    return result

def find_html_files(base_dir: str) -> List[str]:
    """Find all HTML files in the requirements directory structure."""
    html_files = []
    base_path = Path(base_dir)
    
    # Look for HTML files in all subdirectories
    for html_file in base_path.rglob("*.html"):
        html_files.append(str(html_file))
    
    return html_files

def validate_all_links(base_dir: str = ".", output_file: str = None, verbose: bool = False):
    """Validate all links in all HTML files."""
    print("🔍 Finding HTML files...")
    html_files = find_html_files(base_dir)
    
    if not html_files:
        print("❌ No HTML files found in the directory structure.")
        return
    
    print(f"📁 Found {len(html_files)} HTML files to validate")
    
    all_results = []
    total_links = 0
    
    for html_file in html_files:
        print(f"\n📄 Processing: {html_file}")
        links = extract_links_from_html(html_file)
        
        if not links:
            print("   No links found")
            continue
            
        print(f"   Found {len(links)} links")
        total_links += len(links)
        
        for url, line_num in links:
            if verbose:
                print(f"   🔗 Checking: {url}")
                
            result = validate_link(url)
            result['file'] = html_file
            result['line'] = line_num
            all_results.append(result)
            
            # Add delay to avoid overwhelming servers
            time.sleep(0.5)
    
    # Generate report
    print(f"\n📊 VALIDATION REPORT")
    print(f"=" * 50)
    print(f"Total files processed: {len(html_files)}")
    print(f"Total links checked: {total_links}")
    
    # Categorize results
    valid = [r for r in all_results if r['status'] == 'valid']
    broken = [r for r in all_results if r['status'] in ['not_found', 'error', 'connection_error', 'timeout']]
    forbidden = [r for r in all_results if r['status'] == 'forbidden']
    redirects = [r for r in all_results if r['status'] == 'redirect']
    
    print(f"✅ Valid links: {len(valid)}")
    print(f"❌ Broken links: {len(broken)}")
    print(f"🚫 Forbidden/Access denied: {len(forbidden)}")
    print(f"🔄 Redirects: {len(redirects)}")
    
    # Show problematic links
    if broken:
        print(f"\n❌ BROKEN LINKS:")
        for result in broken:
            print(f"   {result['file']}:{result['line']} - {result['url']}")
            print(f"      Status: {result['status']} - {result.get('error', 'No error message')}")
    
    if forbidden:
        print(f"\n🚫 FORBIDDEN LINKS:")
        for result in forbidden:
            print(f"   {result['file']}:{result['line']} - {result['url']}")
    
    # Save detailed report if requested
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Link Validation Report\n")
            f.write("=" * 50 + "\n\n")
            
            for result in all_results:
                f.write(f"File: {result['file']}:{result['line']}\n")
                f.write(f"URL: {result['url']}\n")
                f.write(f"Status: {result['status']}\n")
                if result['status_code']:
                    f.write(f"HTTP Code: {result['status_code']}\n")
                if result['title']:
                    f.write(f"Title: {result['title']}\n")
                if result['error']:
                    f.write(f"Error: {result['error']}\n")
                f.write("-" * 30 + "\n")
        
        print(f"\n📝 Detailed report saved to: {output_file}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate links in HTML requirements documents")
    parser.add_argument("--dir", default=".", help="Base directory to search (default: current directory)")
    parser.add_argument("--output", help="Save detailed report to file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    print("🔗 Requirements Link Validator")
    print("=" * 50)
    
    validate_all_links(args.dir, args.output, args.verbose)