# Job Requirements Framework

A comprehensive framework for creating skill progression requirements across various professional disciplines, with interactive tracking and assessment tools.

## Overview

This repository contains a template-based system for developing clear career advancement paths with practical learning resources and assessment frameworks for different professions.

## Features

- **Universal Template System**: Adaptable framework for any profession
- **Interactive Tracking**: HTML-based progress tracking with checkboxes and visual progress bars
- **Multiple Export Formats**: CSV and JSON export functionality
- **Localization Support**: Multi-language versions (English, Ukrainian)
- **Professional Categories**: Organized skill development across 5-7 core categories per profession

## Structure

```
Requirements/
├── README.md                           # This file
├── template-guide.md                   # Master template framework
├── requirements_to_workbook.py         # Utility to convert requirements to spreadsheets
├── QA Requirements/                    # Quality Assurance profession
│   ├── CLAUDE.md                      # QA-specific AI instructions and guidance
│   ├── Enhanced_QA_Requirements.html  # Interactive English QA requirements
│   ├── Ukrainian_QA_Requirements.html # Interactive Ukrainian QA requirements
│   ├── QA_Skills_Requirements.md      # Markdown version of QA requirements
│   └── qa_req_example.html           # Original QA requirements example
├── Engineering Requirements/          # Software Engineering profession
│   └── CLAUDE.md                     # Engineering-specific guidance
└── Marketing Requirements/            # Marketing profession
    └── CLAUDE.md                     # Marketing-specific guidance
```

## Professions Currently Supported

### Quality Assurance (QA)
- **Levels**: 5 progression levels from Trainee to Principal QA Engineer
- **Categories**: 7 core skill areas including Requirement Analysis, Test Design, Test Execution, Defect Management, API & Technical Testing, Domain Knowledge, and Automation & Leadership
- **Languages**: English and Ukrainian versions available
- **Requirements**: 30-35 detailed requirements for Level 1, scaling appropriately for higher levels

### Engineering & Marketing
- Template frameworks established, ready for content development

## Getting Started

### For Organizations
1. Review the `template-guide.md` for framework understanding
2. Copy the appropriate profession-specific `CLAUDE.md` file
3. Customize categories and levels for your organization
4. Use the interactive HTML versions for team skill tracking

### For Individual Learning
1. Open the relevant HTML file in your browser
2. Use checkboxes to track your progress
3. Export your progress to CSV or JSON for records
4. Follow the learning resources provided for each skill

## Template Framework

The system follows a structured approach:

### Level Progression (Typical)
- **Level 1**: Entry/Trainee → Junior (High detail: 30-35 requirements)
- **Level 2**: Junior → Professional (Moderate detail: 15-20 requirements)  
- **Level 3**: Professional → Senior (Moderate detail: 20-25 requirements)
- **Level 4**: Senior → Lead (Strategic focus: 20-25 requirements)
- **Level 5**: Lead → Principal (Strategic focus: 15-20 requirements)

### Universal Categories (Adapted per profession)
1. **Foundation Knowledge** → *Profession-specific core concepts*
2. **Technical Skills** → *Hands-on abilities and tool proficiency*
3. **Process & Methodology** → *Industry practices and frameworks*
4. **Communication & Documentation** → *Professional communication skills*
5. **Problem Solving** → *Analytical and troubleshooting capabilities*
6. **Domain Expertise** → *Field-specific knowledge areas*
7. **Leadership & Mentoring** → *(Senior levels) Team development skills*

## Resource Quality Standards

All learning resources prioritize:
- **Tutorial-based learning** with step-by-step examples
- **Real-world scenarios** and case studies
- **Tool-specific tutorials** with hands-on exercises
- **Industry best practices** with implementation examples
- **Current content** (updated within 3 years for technical fields)

## Usage Examples

### For HR and Management
- Performance review frameworks
- Hiring and promotion criteria
- Training program development
- Career progression planning

### For Team Leads
- Skill gap analysis
- Mentoring program structure
- Team development planning
- Individual contributor guidance

### for Individual Contributors
- Self-assessment and goal setting
- Learning path identification
- Progress tracking and motivation
- Career advancement planning

## Contributing

To add a new profession or enhance existing ones:

1. Follow the `template-guide.md` framework
2. Create profession-specific `CLAUDE.md` with detailed guidance
3. Develop interactive HTML version using existing templates
4. Ensure learning resources meet quality standards
5. Test with practitioners in the field

## Tools and Utilities

### requirements_to_workbook.py
Python utility to convert CLAUDE.md files into Excel-compatible CSV workbooks with multiple sheets.

**Usage:**
```bash
python requirements_to_workbook.py [path_to_CLAUDE.md]
```

**Features:**
- Automatic parsing of categories and levels
- Multi-sheet CSV generation
- README with import instructions

## Localization

The framework supports multiple languages:

- **English**: Primary language with comprehensive resources
- **Ukrainian**: Full translation with localized learning resources
- **Template**: Ready for additional language adaptations

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Quality Assurance content developed with guidance from experienced QA leads
- Template framework designed for universal applicability across professions
- Interactive features inspired by modern learning management systems

## Contact

For questions, suggestions, or contributions, please open an issue in this repository.

---

**Built for professional development and organizational excellence** 🚀