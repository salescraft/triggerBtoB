#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("="*80)
print("DEEP ANALYSIS: Grid Layout Issue")
print("="*80)

# Find all tab-content sections
tab_sections = re.findall(
    r'<div id="([^"]+)-content" class="([^"]*)">(.*?)</div>\s*</div>\s*</div>',
    html,
    re.DOTALL
)

print(f"\nFound {len(tab_sections)} tab sections")

for tab_name, tab_classes, tab_content in tab_sections:
    print(f"\n{'='*80}")
    print(f"TAB: {tab_name}")
    print(f"{'='*80}")
    print(f"Classes on tab-content: '{tab_classes}'")
    
    # Find the first div inside (should be the grid container)
    first_div = re.search(r'<div class="([^"]*)">', tab_content)
    if first_div:
        grid_classes = first_div.group(1)
        print(f"Classes on first inner div: '{grid_classes}'")
        
        # Check if it's a proper grid
        has_grid = 'grid' in grid_classes
        has_cols_3 = 'lg:grid-cols-3' in grid_classes
        has_cols_2 = 'md:grid-cols-2' in grid_classes
        has_cols_1 = 'grid-cols-1' in grid_classes
        has_gap = 'gap-' in grid_classes
        
        print(f"  ✓ Has 'grid': {has_grid}")
        print(f"  ✓ Has 'grid-cols-1': {has_cols_1}")
        print(f"  ✓ Has 'md:grid-cols-2': {has_cols_2}")
        print(f"  ✓ Has 'lg:grid-cols-3': {has_cols_3}")
        print(f"  ✓ Has 'gap-X': {has_gap}")
        
        if not (has_grid and has_cols_3 and has_cols_2 and has_cols_1):
            print(f"  ❌ PROBLEM: Missing grid classes!")
        else:
            print(f"  ✅ Grid classes look correct")
            
        # Count cards in this section
        cards = len(re.findall(r'<div class="trigger-card', tab_content))
        print(f"  → Cards in section: {cards}")
    else:
        print("  ❌ PROBLEM: No first div found!")

# Check for any inline styles that might override
inline_styles = re.findall(r'style="[^"]*"', html)
if inline_styles:
    print(f"\n⚠️  Found {len(inline_styles)} inline styles that might interfere")
    for style in inline_styles[:5]:
        print(f"  - {style}")

# Check if there are any duplicate or conflicting classes
print("\n" + "="*80)
print("Checking for class conflicts...")
print("="*80)

# Look for trigger-card classes
trigger_cards = re.findall(r'<div class="trigger-card([^"]*)"', html)
unique_card_classes = set(trigger_cards)
print(f"\nFound {len(trigger_cards)} trigger-cards with {len(unique_card_classes)} unique class combinations:")
for classes in list(unique_card_classes)[:10]:
    count = trigger_cards.count(classes)
    print(f"  - 'trigger-card{classes}' ({count} cards)")

