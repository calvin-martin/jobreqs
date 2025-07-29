#!/usr/bin/env python3
"""
Requirements to Workbook Converter
Converts CLAUDE.md requirements files into Excel-compatible CSV workbooks

Usage: python requirements_to_workbook.py [path_to_CLAUDE.md]
"""

import csv
import os
import sys
import re
from pathlib import Path


class RequirementsParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
        self.profession = ""
        self.categories = []
        self.levels = []
        self.requirements = {}
        
    def parse_file(self):
        """Read and parse the CLAUDE.md file"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        
        # Extract profession from title
        title_match = re.search(r'#\s*(.+?)\s*Requirements', self.content)
        if title_match:
            self.profession = title_match.group(1).strip()
        else:
            self.profession = "Generic"
        
        # Extract categories
        self._extract_categories()
        
        # Extract level progression
        self._extract_levels()
        
        # Generate requirements structure
        self._generate_requirements()
    
    def _extract_categories(self):
        """Extract categories from the file"""
        # Look for numbered list of categories
        categories_section = re.search(r'##[^#]*Categories\s*\n([\s\S]*?)(?=##|\Z)', self.content)
        if categories_section:
            category_text = categories_section.group(1)
            # Find numbered items with descriptions
            category_matches = re.findall(r'\d+\.\s*\*\*(.+?)\*\*:\s*(.+?)(?=\n\d+\.|\n##|\Z)', category_text, re.DOTALL)
            for cat_name, cat_desc in category_matches:
                self.categories.append({
                    'name': cat_name.strip(),
                    'description': cat_desc.strip().replace('\n', ' ')
                })
    
    def _extract_levels(self):
        """Extract level progression from the file"""
        levels_section = re.search(r'##[^#]*Level Progression\s*\n([\s\S]*?)(?=##|\Z)', self.content)
        if levels_section:
            level_text = levels_section.group(1)
            # Find level definitions
            level_matches = re.findall(r'-\s*\*\*Level\s*(\d+)\*\*:\s*(.+?)(?=\n-|\n##|\Z)', level_text)
            for level_num, level_desc in level_matches:
                self.levels.append({
                    'number': int(level_num),
                    'description': level_desc.strip()
                })
    
    def _generate_requirements(self):
        """Generate requirements based on categories and levels"""
        # This generates a template structure - in a real implementation,
        # you might parse actual requirements from the file or a database
        
        for level in self.levels:
            level_num = level['number']
            self.requirements[f'Level {level_num}'] = []
            
            # Generate requirements for each category at this level
            for category in self.categories:
                # Create 2-3 sample requirements per category per level
                for i in range(2, 4):
                    req = {
                        'category': category['name'],
                        'requirement': f"{category['name']} Skill {i-1}",
                        'description': f"Level {level_num} proficiency in {category['name'].lower()}",
                        'learning_resources': f"{category['name']} tutorials and guides",
                        'assessment_method': f"Practical assessment of {category['name'].lower()} skills",
                        'priority': 'High' if i == 2 else 'Medium'
                    }
                    self.requirements[f'Level {level_num}'].append(req)
    
    def create_workbook(self, output_dir=None):
        """Create CSV files that can be imported as Excel sheets"""
        if output_dir is None:
            output_dir = Path(self.file_path).parent / f"{self.profession}_Requirements_Workbook"
        else:
            output_dir = Path(output_dir)
        
        # Create output directory
        output_dir.mkdir(exist_ok=True)
        
        files_created = []
        
        # Create summary sheet
        summary_data = [["Level", "Description", "Number of Categories", "Total Requirements"]]
        for level in self.levels:
            level_num = level['number']
            req_count = len(self.requirements.get(f'Level {level_num}', []))
            summary_data.append([
                f"Level {level_num}",
                level['description'],
                str(len(self.categories)),
                str(req_count)
            ])
        
        summary_file = output_dir / "Summary.csv"
        with open(summary_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(summary_data)
        files_created.append("Summary.csv")
        
        # Create categories sheet
        categories_data = [["Category", "Description"]]
        for cat in self.categories:
            categories_data.append([cat['name'], cat['description']])
        
        categories_file = output_dir / "Categories.csv"
        with open(categories_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(categories_data)
        files_created.append("Categories.csv")
        
        # Create requirements sheets for each level
        for level_key, reqs in self.requirements.items():
            if reqs:  # Only create sheet if there are requirements
                req_data = [["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"]]
                for req in reqs:
                    req_data.append([
                        req['category'],
                        req['requirement'],
                        req['description'],
                        req['learning_resources'],
                        req['assessment_method'],
                        req['priority']
                    ])
                
                filename = f"{level_key.replace(' ', '_')}_Requirements.csv"
                req_file = output_dir / filename
                with open(req_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(req_data)
                files_created.append(filename)
        
        # Create README
        self._create_readme(output_dir, files_created)
        
        return output_dir, files_created
    
    def _create_readme(self, output_dir, files_created):
        """Create README with instructions"""
        readme_content = f"""{self.profession} Requirements Workbook - Instructions

This folder contains CSV files that can be imported into Excel as a workbook with multiple sheets.

To create the Excel workbook:
1. Open Excel
2. Create a new blank workbook
3. For each CSV file:
   - Click on a sheet tab (or create a new sheet)
   - Go to Data > From Text/CSV
   - Select the CSV file
   - Import the data
   - Rename the sheet to match the file name (without .csv)

Alternative method (Windows):
1. Select all CSV files in this folder
2. Right-click and select "Open with" > "Excel"
3. Excel will open each file as a separate workbook
4. Copy sheets into a single workbook

Files included:
"""
        for file in files_created:
            readme_content += f"- {file}\n"
        
        readme_content += f"""
Categories covered:
"""
        for i, cat in enumerate(self.categories, 1):
            readme_content += f"{i}. {cat['name']}\n"
        
        readme_content += f"""
Profession: {self.profession}
Total Levels: {len(self.levels)}
"""
        
        readme_file = output_dir / "README.txt"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)


def main():
    """Main function to run the converter"""
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default to CLAUDE.md in current directory
        file_path = "CLAUDE.md"
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        print("\nUsage: python requirements_to_workbook.py [path_to_CLAUDE.md]")
        sys.exit(1)
    
    print(f"Parsing requirements from: {file_path}")
    
    parser = RequirementsParser(file_path)
    parser.parse_file()
    
    output_dir, files = parser.create_workbook()
    
    print(f"\nSuccessfully created {parser.profession} requirements workbook!")
    print(f"Output directory: {output_dir}")
    print(f"\nFiles created:")
    for file in files:
        print(f"  - {file}")
    print("  - README.txt")
    
    print("\nYou can now import these CSV files into Excel to create a multi-sheet workbook.")


if __name__ == "__main__":
    main()