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

### ❌ **Avoid These Reference Types:**
- Academic papers without practical application
- Outdated resources (>3 years old for technical fields)
- Theoretical standards documents without implementation guides
- Basic definitions without depth or examples
- Paywalled content without free alternatives

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