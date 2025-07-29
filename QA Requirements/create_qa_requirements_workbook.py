import csv
import os

# Create a workbook with multiple CSV files that can be imported into Excel as separate sheets

def create_qa_requirements_workbook():
    base_dir = r"C:\Users\CalvinMartin\Requirements\QA Requirements\QA_Requirements_Workbook"
    
    # Create directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Level 1 Requirements
    level1_data = [
        ["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"],
        ["Requirement Analysis", "User Story Analysis", "Understand basic user story structure and acceptance criteria", "Tutorial on user story writing and analysis", "Quiz on identifying acceptance criteria", "High"],
        ["Requirement Analysis", "Requirements Traceability", "Basic understanding of linking requirements to test cases", "Step-by-step guide on requirements traceability matrix", "Create simple traceability matrix", "Medium"],
        ["Test Design", "Basic Test Case Writing", "Write simple test cases with clear steps and expected results", "Tutorial on test case structure and best practices", "Review test cases written by trainee", "High"],
        ["Test Design", "Test Data Preparation", "Identify and prepare basic test data sets", "Practical guide on test data creation", "Create test data for sample scenarios", "High"],
        ["Test Design", "Boundary Value Testing", "Understand and apply boundary value analysis", "Real-world examples of boundary testing", "Apply boundary testing to given scenarios", "Medium"],
        ["Test Execution", "Manual Test Execution", "Execute test cases and document results accurately", "Step-by-step execution tutorial with screenshots", "Execute provided test suite", "High"],
        ["Test Execution", "Test Result Documentation", "Properly document test results and observations", "Template-based documentation guide", "Review documentation quality", "High"],
        ["Test Execution", "Basic Environment Setup", "Set up basic test environments and understand configurations", "Environment setup tutorials for common tools", "Set up test environment independently", "Medium"],
        ["Defect Management", "Bug Identification", "Recognize and identify software defects during testing", "Case studies of common bug types", "Bug hunting exercise on sample application", "High"],
        ["Defect Management", "Bug Reporting", "Write clear and detailed bug reports", "Bug report template and examples", "Review quality of bug reports written", "High"],
        ["Defect Management", "Bug Lifecycle Understanding", "Understand basic bug lifecycle and status transitions", "Tutorial on bug lifecycle with real examples", "Quiz on bug status transitions", "Medium"],
        ["API & Technical Testing", "Basic API Concepts", "Understand REST API basics and HTTP methods", "Beginner-friendly API tutorial", "Quiz on API concepts", "Low"],
        ["Domain Knowledge", "Application Under Test", "Understand the application being tested and its business logic", "Domain-specific training materials", "Knowledge check on application features", "High"],
        ["Domain Knowledge", "Basic Testing Tools", "Familiarity with basic testing tools (browser dev tools etc)", "Tool-specific tutorials", "Demonstrate tool usage", "Medium"]
    ]
    
    # Level 2 Requirements
    level2_data = [
        ["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"],
        ["Requirement Analysis", "Complex User Story Analysis", "Analyze complex user stories with multiple acceptance criteria", "Advanced user story analysis workshop", "Analyze complex requirement documents", "High"],
        ["Requirement Analysis", "Requirements Review", "Participate in requirements review meetings effectively", "Meeting facilitation guide for QA", "Participate in mock review sessions", "Medium"],
        ["Requirement Analysis", "Ambiguity Detection", "Identify ambiguous or incomplete requirements", "Case studies of requirement issues", "Review requirements and identify gaps", "High"],
        ["Test Design", "Test Strategy Development", "Develop test strategies for features or modules", "Test strategy template and examples", "Create test strategy for assigned project", "High"],
        ["Test Design", "Equivalence Partitioning", "Apply equivalence partitioning technique effectively", "Tutorial with practical examples", "Design test cases using equivalence partitioning", "High"],
        ["Test Design", "Negative Testing", "Design comprehensive negative test scenarios", "Negative testing guide with examples", "Create negative test scenarios", "Medium"],
        ["Test Design", "Test Case Review", "Review and improve test cases written by others", "Best practices for test case reviews", "Conduct test case review session", "Medium"],
        ["Test Execution", "Test Plan Execution", "Execute comprehensive test plans across multiple areas", "Test execution best practices guide", "Execute full test cycle independently", "High"],
        ["Test Execution", "Cross-Browser Testing", "Perform testing across different browsers and platforms", "Cross-browser testing tutorial", "Execute cross-browser test scenarios", "Medium"],
        ["Test Execution", "Performance Basics", "Understand basic performance testing concepts", "Performance testing fundamentals", "Identify performance bottlenecks", "Low"],
        ["Defect Management", "Root Cause Analysis", "Perform basic root cause analysis for defects", "RCA methodology tutorial", "Conduct RCA for sample defects", "High"],
        ["Defect Management", "Defect Triage", "Participate in defect triage meetings", "Defect triage process guide", "Participate in triage simulation", "Medium"],
        ["Defect Management", "Severity Assessment", "Accurately assess defect severity and priority", "Severity classification guide with examples", "Classify defects by severity", "High"],
        ["API & Technical Testing", "API Testing with Postman", "Perform API testing using Postman", "Postman tutorial with hands-on exercises", "Create and execute API test suite", "High"],
        ["API & Technical Testing", "Database Testing", "Basic database testing and SQL queries", "SQL tutorial for testers", "Write queries to validate data", "Medium"],
        ["Domain Knowledge", "Business Process Testing", "Test complete business processes end-to-end", "Business process testing methodology", "Test complete user workflows", "High"],
        ["Domain Knowledge", "Testing Tools Proficiency", "Proficient use of test management tools (Jira TestRail etc)", "Tool-specific training and certification", "Demonstrate advanced tool usage", "High"]
    ]
    
    # Level 3 Requirements
    level3_data = [
        ["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"],
        ["Requirement Analysis", "Requirements Validation", "Lead requirements validation sessions", "Requirements validation framework", "Facilitate validation workshops", "High"],
        ["Requirement Analysis", "Impact Analysis", "Assess impact of requirement changes on testing", "Change impact analysis methodology", "Conduct impact analysis for changes", "High"],
        ["Test Design", "Test Architecture", "Design test architecture for complex applications", "Test architecture patterns and examples", "Design test architecture document", "High"],
        ["Test Design", "Risk-Based Testing", "Implement risk-based testing approach", "Risk-based testing methodology", "Create risk-based test plan", "High"],
        ["Test Design", "Test Optimization", "Optimize test suites for efficiency and coverage", "Test optimization strategies", "Optimize existing test suite", "Medium"],
        ["Test Execution", "Regression Testing Strategy", "Develop and execute regression testing strategies", "Regression testing best practices", "Implement regression strategy", "High"],
        ["Test Execution", "Integration Testing", "Plan and execute integration testing", "Integration testing patterns", "Execute integration test scenarios", "High"],
        ["Test Execution", "Environment Management", "Manage complex test environments", "Environment management best practices", "Set up complex test environment", "Medium"],
        ["Defect Management", "Defect Prevention", "Implement defect prevention strategies", "Defect prevention methodologies", "Design defect prevention plan", "High"],
        ["Defect Management", "Metrics and Reporting", "Create and analyze testing metrics", "Testing metrics guide with examples", "Create comprehensive test report", "High"],
        ["API & Technical Testing", "API Test Automation", "Automate API testing using tools", "API automation tutorial (REST Assured etc)", "Implement automated API tests", "High"],
        ["API & Technical Testing", "Security Testing Basics", "Understand and perform basic security testing", "Security testing guide for QA", "Conduct security test scenarios", "Medium"],
        ["Domain Knowledge", "Process Improvement", "Identify and implement testing process improvements", "Process improvement methodologies", "Lead process improvement initiative", "High"],
        ["Automation & Leadership", "Test Automation Basics", "Understand test automation principles and tools", "Automation framework tutorials", "Create basic automated tests", "High"],
        ["Automation & Leadership", "Team Mentoring", "Mentor junior team members", "Mentoring best practices for technical leads", "Mentor junior QA engineer", "Medium"]
    ]
    
    # Level 4 Requirements
    level4_data = [
        ["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"],
        ["Requirement Analysis", "Requirements Engineering", "Lead requirements engineering activities", "Requirements engineering best practices", "Design requirements process", "High"],
        ["Test Design", "Testing Standards", "Establish testing standards and guidelines", "Testing standards development guide", "Create team testing standards", "High"],
        ["Test Design", "Test Framework Design", "Design reusable test frameworks", "Test framework architecture patterns", "Design custom test framework", "High"],
        ["Test Execution", "Release Management", "Manage testing activities in release cycles", "Release management for QA leads", "Lead release testing activities", "High"],
        ["Test Execution", "Multi-Project Coordination", "Coordinate testing across multiple projects", "Project coordination methodologies", "Manage multiple project testing", "High"],
        ["Defect Management", "Quality Gates", "Implement quality gates and exit criteria", "Quality gates implementation guide", "Design quality gate process", "High"],
        ["Defect Management", "Quality Metrics Program", "Establish quality metrics and KPI programs", "Quality metrics framework", "Implement metrics program", "High"],
        ["API & Technical Testing", "Performance Testing", "Lead performance testing initiatives", "Performance testing leadership guide", "Design performance test strategy", "Medium"],
        ["API & Technical Testing", "Test Tool Evaluation", "Evaluate and select testing tools", "Tool evaluation methodology", "Conduct tool evaluation project", "Medium"],
        ["Domain Knowledge", "Quality Assurance Strategy", "Develop organizational QA strategy", "QA strategy development framework", "Create comprehensive QA strategy", "High"],
        ["Automation & Leadership", "Automation Strategy", "Develop test automation strategy", "Automation strategy best practices", "Create automation roadmap", "High"],
        ["Automation & Leadership", "Team Leadership", "Lead QA teams and initiatives", "Technical leadership for QA", "Lead team through major project", "High"]
    ]
    
    # Level 5 Requirements
    level5_data = [
        ["Category", "Requirement", "Description", "Learning Resources", "Assessment Method", "Priority"],
        ["Requirement Analysis", "Enterprise Requirements", "Manage enterprise-level requirements processes", "Enterprise requirements management", "Design enterprise requirements process", "High"],
        ["Test Design", "Quality Architecture", "Design enterprise quality architecture", "Quality architecture frameworks", "Create enterprise quality architecture", "High"],
        ["Test Design", "Innovation in Testing", "Drive innovation in testing practices", "Innovation management in QA", "Lead testing innovation initiative", "Medium"],
        ["Test Execution", "Global Testing Coordination", "Coordinate testing across global teams", "Global coordination best practices", "Manage global testing project", "Medium"],
        ["Defect Management", "Organizational Quality Culture", "Build quality culture across organization", "Quality culture transformation guide", "Lead quality culture initiative", "High"],
        ["API & Technical Testing", "Emerging Technologies", "Evaluate testing for emerging technologies", "Emerging tech testing strategies", "Assess new technology testing needs", "Low"],
        ["Domain Knowledge", "Industry Expertise", "Develop deep industry domain expertise", "Industry-specific quality standards", "Demonstrate industry expertise", "High"],
        ["Automation & Leadership", "Strategic Vision", "Develop strategic vision for QA organization", "Strategic planning for QA leaders", "Create 3-year QA vision", "High"],
        ["Automation & Leadership", "Executive Communication", "Communicate QA value to executive leadership", "Executive communication for QA", "Present QA strategy to executives", "High"]
    ]
    
    # Summary data
    summary_data = [
        ["Level", "Title", "Target Position", "Key Focus Areas", "Total Requirements"],
        ["Level 1", "Trainee → Junior QA Engineer", "Junior QA Engineer", "Basic testing fundamentals, manual testing, bug reporting", "14"],
        ["Level 2", "Junior → QA Engineer", "QA Engineer", "Advanced testing techniques, API testing, process participation", "17"],
        ["Level 3", "QA Engineer → Senior QA Engineer", "Senior QA Engineer", "Test architecture, automation basics, mentoring", "15"],
        ["Level 4", "Senior → Lead QA Engineer", "Lead QA Engineer", "Team leadership, strategy development, quality programs", "12"],
        ["Level 5", "Lead → Principal QA Engineer", "Principal QA Engineer", "Enterprise architecture, strategic vision, executive communication", "9"]
    ]
    
    # Write CSV files
    files_created = []
    
    with open(os.path.join(base_dir, "Summary.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(summary_data)
        files_created.append("Summary.csv")
    
    with open(os.path.join(base_dir, "Level_1_Requirements.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(level1_data)
        files_created.append("Level_1_Requirements.csv")
    
    with open(os.path.join(base_dir, "Level_2_Requirements.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(level2_data)
        files_created.append("Level_2_Requirements.csv")
    
    with open(os.path.join(base_dir, "Level_3_Requirements.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(level3_data)
        files_created.append("Level_3_Requirements.csv")
    
    with open(os.path.join(base_dir, "Level_4_Requirements.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(level4_data)
        files_created.append("Level_4_Requirements.csv")
    
    with open(os.path.join(base_dir, "Level_5_Requirements.csv"), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(level5_data)
        files_created.append("Level_5_Requirements.csv")
    
    # Create instructions file
    instructions = """QA Requirements Workbook - Instructions

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

Sheet Structure:
- Summary: Overview of all QA levels and progression
- Level_1_Requirements: Entry level QA requirements (Trainee → Junior)
- Level_2_Requirements: Junior → QA Engineer requirements
- Level_3_Requirements: QA Engineer → Senior requirements
- Level_4_Requirements: Senior → Lead requirements
- Level_5_Requirements: Lead → Principal requirements

Categories covered:
1. Requirement Analysis
2. Test Design
3. Test Execution
4. Defect Management
5. API & Technical Testing
6. Domain Knowledge
7. Automation & Leadership (Levels 3+)
"""
    
    with open(os.path.join(base_dir, "README.txt"), 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print(f"Created QA Requirements workbook files in: {base_dir}")
    print("\nFiles created:")
    for file in files_created:
        print(f"  - {file}")
    print("  - README.txt")
    
    return base_dir

if __name__ == "__main__":
    create_qa_requirements_workbook()