# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a comprehensive framework for creating skill progression requirements across various professional disciplines. It uses a template-based system to generate interactive HTML requirements tracking tools and supporting documentation.

## Commands and Development

### Python Scripts
- **requirements_to_workbook.py**: Converts CLAUDE.md files to Excel-compatible CSV workbooks
  ```bash
  python requirements_to_workbook.py [path_to_CLAUDE.md]
  ```

- **create_qa_requirements_workbook.py**: Creates QA-specific workbook from markdown
  ```bash
  python "QA Requirements/create_qa_requirements_workbook.py"
  ```

### No Build/Test Commands
This is a documentation and requirements framework repository with no build, test, or lint commands.

## Architecture and Structure

### Directory Structure
```
Requirements/
├── CLAUDE.md                    # This file - general framework guidance
├── README.md                    # User-facing documentation
├── template-guide.md            # Master template for new professions
├── requirements_to_workbook.py  # Conversion utility
└── [Profession] Requirements/   # Profession-specific folders
    ├── CLAUDE.md               # Profession-specific guidance
    └── [Generated files]       # HTML, workbooks, etc.
```

### Key Components
1. **Template System**: Master framework for all professions
2. **Profession Folders**: Each contains profession-specific CLAUDE.md and generated outputs
3. **Conversion Tools**: Python scripts to generate various output formats

## Requirements Template Guide

### Template Purpose
- **Career Clarity**: Define clear progression paths from entry-level to senior positions
- **Skill Development**: Provide structured learning requirements with actionable references
- **Assessment Framework**: Enable objective evaluation of team member capabilities
- **Resource Guidance**: Offer practical, tutorial-based learning materials

### Document Structure Framework

#### Level Progression Template
Most disciplines follow a 4-5 level progression:

```
Level 1: Trainee/Intern → Junior
Level 2: Junior → Professional/Specialist  
Level 3: Professional → Senior
Level 4: Senior → Lead/Principal (if applicable to discipline)
Level 5: Lead/Principal → Expert/Director (if applicable)
```

#### Category Framework
Organize requirements into 5-7 core categories relevant to your discipline:

##### Universal Categories (adapt terminology):
- **Foundation Knowledge**: Core concepts and principles
- **Technical Skills**: Hands-on abilities and tool proficiency  
- **Process & Methodology**: Industry practices and frameworks
- **Communication & Documentation**: Professional communication skills
- **Problem Solving**: Analytical and troubleshooting capabilities
- **Domain Expertise**: Field-specific knowledge areas
- **Leadership & Mentoring**: (Senior levels only) Team development skills

### Granularity Guidelines

#### Level 1 (Entry → Junior): Maximum Detail
- Break down skills into very specific, actionable items
- Include 5-6 skills per major category
- Focus on hands-on, practical skills that can be immediately applied
- Provide step-by-step learning paths
- Example: "Understand HTTP status codes (200, 400, 401/403, 404, 500)" rather than "API basics"

#### Level 2-3: Moderate Detail
- 3-4 skills per category
- More complex, integrated skills
- Combination of technical and process skills

#### Level 4-5: Strategic Focus
- 2-3 high-level skills per category
- Leadership and architectural thinking
- Cross-functional and organizational impact

## Reference Selection Criteria

### ✅ **High-Quality References Include:**

#### **Tutorial-Based Learning**
- Step-by-step guides with practical examples
- Interactive tutorials with hands-on exercises
- Video courses with downloadable materials

#### **Practical Resources**
- Real-world case studies and examples
- Templates and frameworks that can be applied immediately
- Industry best practices with implementation guides

### Resource Validation Criteria:
- Must include practical examples
- Should have step-by-step instructions
- Include screenshots or code samples where relevant
- Updated within last 3 years for technical content
- From recognized industry sources
- **All links must be verified as working before inclusion**
- **Avoid sites with excessive advertisements that detract from content**
- **Prefer clean, professional educational sites**

### ❌ **Avoid These Reference Types:**
- Academic papers without practical application
- Outdated resources (>3 years old for technical fields)
- Theoretical standards documents without implementation guides
- Basic definitions without depth or examples
- Paywalled content without free alternatives
- **Broken or dead links**
- **Sites overwhelmed with pop-ups or intrusive ads**
- **Content farms with low-quality or copied material**

## Link Validation Protocol

### **MANDATORY: Verify All Links Before Inclusion**

Before adding any reference link to requirements documents, **ALWAYS**:

1. **Test the Link**: Click and verify it loads the expected content
2. **Validate Content Relevance**: Ensure the page content directly relates to the skill topic
3. **Check Content Quality**: Verify it contains practical, actionable information
4. **Assess User Experience**: Confirm the site is professional and not overwhelmed with ads

### **Known Problematic Sites** (as of 2024):
- **guru99.com**: Many pages return CSS/JavaScript instead of content
- **Some tutorialspoint.com pages**: May have outdated or generic content
- **Sites with excessive pop-ups**: Detract from learning experience
- **Content aggregation sites**: Often have low-quality, copied material

### **Trusted Resource Categories**:

#### **Official Documentation**
- Technology vendor official docs (e.g., Selenium, Chrome DevTools)
- Standards bodies (OWASP, W3C, ISTQB official sites)
- Platform documentation (Atlassian, GitHub, major cloud providers)

#### **Recognized Educational Platforms**
- University courses and materials
- Professional training organizations
- Industry-recognized certification bodies
- Established technology companies' learning resources

#### **Quality Technical Content**
- Martin Fowler's articles (software architecture/testing)
- Nielsen Norman Group (UX/usability)
- Mozilla Developer Network (web standards)
- Test Automation University (automation learning)

### **Link Validation Action Plan**:

1. **If link is broken/invalid**: Remove it entirely
2. **If content is irrelevant**: Find appropriate replacement or leave blank
3. **If no quality resources exist**: Leave resource section empty with comment
4. **Better no link than bad link**: Empty resource sections are acceptable

### **Documentation Format for Missing Resources**:
```html
<div class="skill-resources">
    <!-- No validated links found for this topic -->
</div>
```

### **Maintenance Schedule**:
- **Quarterly**: Spot-check 25% of all links across all profession documents
- **Annual**: Full link validation audit of entire repository  
- **Before release**: Validate all new links added to documents
- **User reports**: Address broken link reports within 48 hours

### **Link Validation Tools**:
- **Manual Validation**: Follow the checklist in `LINK_VALIDATION_README.md`
- **Automated Validation**: Use `validate_links.py` script for bulk link checking
- **Integration**: Run validation before committing changes to repository

## Content Structure Guidelines

### Skill Description Format:
Use action-oriented, specific descriptions:
- Good: "Write clear, detailed, and reproducible bug reports"
- Bad: "Understanding bug reporting"
- Good: "Execute test cases systematically and document results"
- Bad: "Test execution knowledge"

### Assessment Method Examples:
- "Write 15 high-quality bug reports" (specific number)
- "Execute 50 test cases with documentation" (measurable)
- "Set up test environment independently" (observable)
- "Create test strategy for assigned project" (deliverable-based)

## Interactive Implementation Guidance

### For HTML Implementations:
- Include progress tracking with checkboxes
- Visual progress bars showing completion percentage
- Tab-based organization by level
- Export functionality to CSV/Excel
- Category-based color coding
- Sticky headers for large tables

### For Spreadsheet Implementations:
- Separate sheets for each level
- Summary sheet with overall progress
- Categories sheet for reference
- Filterable columns
- Conditional formatting for completion status

## Implementation Instructions

1. **Copy this template** to your discipline-specific folder
2. **Adapt the categories** to match your field's core skills
3. **Customize the levels** based on your organization's structure
4. **Write specific requirements** using action-oriented language
5. **Find quality references** that provide practical, tutorial-based learning
6. **Test with practitioners** to ensure accuracy and completeness
7. **Maintain regularly** to keep content current and relevant

## Success Metrics by Profession Type

Different professions should define success metrics relevant to their field:
- Technical roles: Performance improvements, bug reduction, automation adoption
- Creative roles: Portfolio quality, campaign effectiveness, design impact
- Management roles: Team growth, project success rates, process improvements

## Working with This Repository

1. When creating new profession requirements, use this framework as your guide
2. Each profession should have its own folder with a profession-specific CLAUDE.md
3. Use the Python utilities to generate workbooks and other formats
4. Maintain consistency with the framework while allowing profession-specific adaptations
5. Focus on practical, actionable requirements with quality learning resources
6. Keep profession-specific content in the respective profession folders
7. This file contains only the general framework applicable to all professions