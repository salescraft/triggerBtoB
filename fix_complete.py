#!/usr/bin/env python3
import re

print("="*80)
print("COMPLETE FIX: Layout + lemlist Intent Tab Styling")
print("="*80)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================================
# FIX 1: Move lemlist Intent tab to FIRST position (far left)
# ============================================================================
print("\n1. Moving lemlist Intent tab to first position...")

# Find the tabs section and reorder
tabs_pattern = r'(<div class="tab-container inline-flex flex-wrap gap-2">)(.*?)(</div>\s*</div>)'

def reorder_tabs(match):
    opening = match.group(1)
    tabs_content = match.group(2)
    closing = match.group(3)
    
    # Extract lemlist tab
    lemlist_tab_pattern = r'(<button class="tab-button"[^>]*data-tab="lemlist"[^>]*>.*?</button>)'
    lemlist_match = re.search(lemlist_tab_pattern, tabs_content, re.DOTALL)
    
    if not lemlist_match:
        return match.group(0)
    
    lemlist_tab = lemlist_match.group(1)
    
    # Remove lemlist from current position
    tabs_without_lemlist = re.sub(lemlist_tab_pattern, '', tabs_content, flags=re.DOTALL)
    
    # Style lemlist tab with premium gold styling
    lemlist_tab_styled = lemlist_tab.replace(
        '<button class="tab-button"',
        '<button class="tab-button lemlist-premium"'
    ).replace('🔍', '🔥')
    
    # Place lemlist first
    new_tabs = opening + '\n                    ' + lemlist_tab_styled + tabs_without_lemlist + closing
    
    return new_tabs

html = re.sub(tabs_pattern, reorder_tabs, html, flags=re.DOTALL)
print("✓ lemlist Intent tab moved to first position with 🔥 icon")

# ============================================================================
# FIX 2: Add premium gold styling for lemlist tab
# ============================================================================
print("\n2. Adding premium gold CSS styling...")

# Find the CSS section and add lemlist premium styles
css_insert_point = r'(\.tab-button:hover:not\(\.active\) \{[^}]+\})'

premium_css = r'''\1
        
        /* Premium lemlist Intent tab styling */
        .tab-button.lemlist-premium {
            background: linear-gradient(135deg, #FFD666 0%, #FFAB00 100%);
            color: #1f2937;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(255, 214, 102, 0.4);
            border: 2px solid #FFAB00;
        }
        
        .tab-button.lemlist-premium:hover {
            background: linear-gradient(135deg, #FFAB00 0%, #FF8F00 100%);
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(255, 214, 102, 0.6);
        }
        
        .tab-button.lemlist-premium.active {
            background: linear-gradient(135deg, #FFD666 0%, #FFAB00 100%);
            color: #1f2937;
            box-shadow: 0 6px 20px rgba(255, 214, 102, 0.6);
        }
        
        .tab-button.lemlist-premium .badge-count {
            background: rgba(31, 41, 55, 0.2);
            color: #1f2937;
        }'''

html = re.sub(css_insert_point, premium_css, html, flags=re.DOTALL)
print("✓ Premium gold styling added for lemlist tab")

# ============================================================================
# FIX 3: Ensure ALL grid layouts are correct
# ============================================================================
print("\n3. Verifying grid layouts...")

# Find all tab-content divs and ensure they have proper grid
grid_pattern = r'(<div id="[^"]*-content" class="tab-content[^"]*">\s*<div class=")([^"]*)(">)'

def fix_grid(match):
    opening = match.group(1)
    classes = match.group(2)
    closing = match.group(3)
    
    # Ensure grid classes are present
    if 'grid' not in classes:
        classes = 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'
    elif 'lg:grid-cols-3' not in classes:
        classes = 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'
    
    return opening + classes + closing

# Apply to all content sections EXCEPT the lemlist intro banner
html_lines = html.split('\n')
fixed_lines = []
in_lemlist_banner = False

for i, line in enumerate(html_lines):
    # Detect lemlist banner section
    if 'id="lemlist-content"' in line:
        in_lemlist_banner = True
    
    # Skip grid fix for the banner div (first div after lemlist-content)
    if in_lemlist_banner and 'bg-gradient-to-r from-blue-50 to-yellow-50' in line:
        fixed_lines.append(line)
        in_lemlist_banner = False
        continue
    
    # Fix other divs
    if '<div class="grid' in line or ('<div class="' in line and 'grid' not in line and i > 0 and 'tab-content' in html_lines[i-1]):
        line = re.sub(r'<div class="([^"]*)">', r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">', line)
    
    fixed_lines.append(line)

html = '\n'.join(fixed_lines)
print("✓ Grid layouts verified and fixed")

# ============================================================================
# FIX 4: Ensure Tailwind CDN is loaded
# ============================================================================
print("\n4. Verifying Tailwind CSS...")

if 'tailwindcss' in html:
    print("✓ Tailwind CSS CDN already present")
else:
    print("✗ Tailwind CSS missing - adding CDN")
    head_pattern = r'(<head>)'
    tailwind_cdn = r'''\1
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">'''
    html = re.sub(head_pattern, tailwind_cdn, html)

# ============================================================================
# Save and verify
# ============================================================================
print("\n5. Saving changes...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ File saved")

# ============================================================================
# Final verification
# ============================================================================
print("\n" + "="*80)
print("VERIFICATION")
print("="*80)

with open('index.html', 'r', encoding='utf-8') as f:
    final_html = f.read()

# Count elements
tab_buttons = len(re.findall(r'<button class="tab-button', final_html))
lemlist_premium = 'tab-button lemlist-premium' in final_html
grid_3cols = len(re.findall(r'lg:grid-cols-3', final_html))
lemlist_first = final_html.find('data-tab="lemlist"') < final_html.find('data-tab="company"')
flame_icon = '🔥' in re.search(r'data-tab="lemlist".*?</button>', final_html, re.DOTALL).group(0) if re.search(r'data-tab="lemlist".*?</button>', final_html, re.DOTALL) else False

print(f"\n✓ Total tabs: {tab_buttons}")
print(f"✓ lemlist has premium styling: {lemlist_premium}")
print(f"✓ Grid 3-column layouts: {grid_3cols}")
print(f"✓ lemlist is first tab: {lemlist_first}")
print(f"✓ lemlist has 🔥 icon: {flame_icon}")

if tab_buttons == 7 and lemlist_premium and grid_3cols >= 6 and lemlist_first and flame_icon:
    print("\n" + "="*80)
    print("✅ ALL FIXES APPLIED SUCCESSFULLY!")
    print("="*80)
else:
    print("\n⚠️ Some fixes may need manual verification")

