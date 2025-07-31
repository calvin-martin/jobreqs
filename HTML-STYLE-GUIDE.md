# Requirements HTML Style Guide

This guide ensures consistent styling and formatting across all requirements HTML documents in this repository.

## Standard Template

Use the `standard-requirements-template.html` file as the base for all new requirements documents.

## Core Style Elements

### Color Scheme
- **Primary Blue**: `#3498db` (buttons, links, borders)
- **Dark Blue**: `#2980b9` (hover states)
- **Dark Gray**: `#2c3e50` (headings, titles)
- **Medium Gray**: `#7f8c8d` (subtitles)
- **Light Gray**: `#f5f5f5` (background)
- **White**: `#ffffff` (content backgrounds)
- **Success Green**: `#27ae60` (assessments, export button)

### Typography
- **Font Family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Base Font Size**: 16px (1em)
- **Line Height**: 1.6
- **Heading Sizes**:
  - H1: 2.5em
  - H2: 1.8em
  - H3: 1.3em

### Layout Structure
1. **Container**: Max-width 1200px, centered with 20px padding
2. **Cards**: White background with 10px border-radius and subtle shadow
3. **Grid Layout**: Responsive grid for progress cards and skills
4. **Tabs**: Horizontal tabs for level navigation (vertical on mobile)

### Component Styles

#### Header Section
```css
header {
    text-align: center;
    margin-bottom: 30px;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
```

#### Progress Cards
- Gradient background: `linear-gradient(45deg, #3498db, #2980b9)`
- White text and progress bar
- Responsive grid layout

#### Skill Items
- Light background: `#f8f9fa`
- Border: `1px solid #e9ecef`
- Hover effect with shadow and slight upward movement
- Checkbox scaled to 1.2x for better visibility

#### Resource Links
- Pill-shaped buttons with primary blue background
- White text with hover effect
- Flexible wrapping layout

#### Assessment Box
- Light green background: `#e8f5e8`
- Left border: `4px solid #27ae60`
- Darker green text: `#2d5a2d`

### JavaScript Functionality

#### Progress Tracking
- LocalStorage key format: `[profession]SkillsProgress`
- Automatic progress calculation and display
- Real-time updates on checkbox changes

#### Tab Navigation
- Active tab highlighted with primary blue
- Smooth transitions between tabs
- Mobile-responsive behavior

#### Export Feature
- CSV format with headers: Level, Category, Skill, Completed, Assessment
- Filename format: `[profession]-skills-progress.csv`

### Responsive Design
- Breakpoint at 768px
- Mobile adaptations:
  - Vertical tab layout
  - Single-column progress grid
  - Reduced padding

## Implementation Checklist

When creating a new requirements HTML document:

1. [ ] Copy `standard-requirements-template.html`
2. [ ] Replace all `[PROFESSION]` placeholders
3. [ ] Update level names and descriptions
4. [ ] Add skill categories and items
5. [ ] Verify all resource links are working
6. [ ] Test progress tracking functionality
7. [ ] Ensure mobile responsiveness
8. [ ] Validate CSV export functionality

## File Naming Convention

- Use format: `[Profession]_Skills_Matrix.html`
- Examples: 
  - `QA_Skills_Matrix.html`
  - `Developer_Skills_Matrix.html`
  - `DevOps_Skills_Matrix.html`

## Maintenance Notes

- Keep all styling inline within the HTML file for portability
- Use semantic HTML elements where possible
- Ensure all interactive elements are keyboard accessible
- Test in major browsers: Chrome, Firefox, Safari, Edge