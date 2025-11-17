#!/usr/bin/env python3
import re

print("="*80)
print("FINAL FIX: Adding explicit CSS grid rules")
print("="*80)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The solution: Add EXPLICIT CSS grid rules that will DEFINITELY work
# regardless of Tailwind loading issues

explicit_grid_css = '''
        /* EXPLICIT GRID FIX - Override any conflicts */
        .grid {
            display: grid !important;
        }
        
        .grid-cols-1 {
            grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
        }
        
        @media (min-width: 768px) {
            .md\\:grid-cols-2 {
                grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
            }
        }
        
        @media (min-width: 1024px) {
            .lg\\:grid-cols-3 {
                grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
            }
        }
        
        .gap-6 {
            gap: 1.5rem !important;
        }
        
        .gap-8 {
            gap: 2rem !important;
        }
'''

# Insert this CSS right after the existing trigger-card styles
insertion_point = r'(\.trigger-card:hover \{[^}]+\})'
html = re.sub(insertion_point, r'\1\n' + explicit_grid_css, html, count=1)

print("✓ Added explicit grid CSS rules with !important")

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ File saved")
print("\nThis should FORCE the grid layout to work regardless of Tailwind loading")

