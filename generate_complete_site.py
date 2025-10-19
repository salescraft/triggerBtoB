#!/usr/bin/env python3
"""
Generate complete HTML site with all 95 buying signals from JSON data.
This script reads signals_complete.json and generates all signal cards.
"""

import json

# Load signals data
with open('signals_complete.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_fire_emoji(strength):
    """Convert strength number to fire emoji display"""
    return '🔥' * strength

def generate_signal_card(signal_data):
    """Generate HTML for a single signal card"""
    fires = get_fire_emoji(signal_data['strength'])
    
    # Determine if detectable with lemlist
    has_lemlist = 'lemlist' in ' '.join(signal_data['tools']).lower()
    intent_badge = '<span class="intent-badge">Detectable with lemlist</span>' if has_lemlist else ''
    
    # Generate tool tags
    tool_tags = []
    for tool in signal_data['tools']:
        if 'lemlist' in tool.lower():
            tool_tags.append(f'<span class="tool-tag lemlist-tool">{tool}</span>')
        elif tool.lower() in ['linkedin', 'twitter/x', 'google alerts', 'g2']:
            tool_tags.append(f'<span class="tool-tag free-tool">{tool}</span>')
        else:
            tool_tags.append(f'<span class="tool-tag paid-tool">{tool}</span>')
    
    tools_html = '\n                                '.join(tool_tags)
    
    card_html = f'''
                    <!-- {signal_data['signal']} -->
                    <div class="trigger-card">
                        <div class="flex items-center justify-between mb-3">
                            {intent_badge}
                            <div class="strength-badge"><span class="text-red-600 font-bold">{fires}</span></div>
                        </div>
                        
                        <div class="flex items-center mb-4">
                            <i class="fas {signal_data['icon']} text-3xl mr-3 text-blue-600"></i>
                            <h3 class="text-xl font-bold">{signal_data['signal']}</h3>
                        </div>
                        
                        <p class="text-gray-600 mb-4 text-sm leading-relaxed">
                            {signal_data['why']}
                        </p>
                        
                        <div class="mb-4">
                            <h4 class="font-semibold mb-2 text-sm text-gray-700">How to Detect:</h4>
                            <div class="flex flex-wrap gap-2">
                                {tools_html}
                            </div>
                        </div>
                        
                        <div class="bg-blue-50 p-4 rounded-lg mb-4">
                            <h4 class="font-semibold mb-2 text-sm text-gray-700">Message Template:</h4>
                            <p class="text-sm text-gray-700 italic">
                                "{signal_data['template']}"
                            </p>
                        </div>
                        
                        <div class="bg-yellow-50 p-3 rounded-lg border-l-4 border-yellow-400">
                            <h4 class="font-semibold mb-1 text-xs text-gray-600">💡 Example:</h4>
                            <p class="text-xs text-gray-700">
                                {signal_data['example']}
                            </p>
                        </div>
                    </div>
'''
    return card_html

# Generate cards for each category
categories = {
    'company': 'Company-Level Triggers',
    'person': 'Person-Level Triggers', 
    'tech': 'Tech Stack Triggers',
    'product': 'Product-Led Triggers',
    'community': 'Community Engagement Triggers',
    'event': 'Event-Based Triggers'
}

category_cards = {}
for category, title in categories.items():
    cards_html = []
    for signal in data[category]:
        cards_html.append(generate_signal_card(signal))
    category_cards[category] = '\n'.join(cards_html)

# Read the base HTML template
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Generate the complete HTML with all signal cards injected
complete_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>95 Buying Signals - salesCraft x lemlist</title>
    <meta name="description" content="Discover 95+ proven buying signals with detailed examples, templates, and detection methods">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --lemlist-blue: #318BFF;
            --lemlist-dark: #143CDD;
            --lemlist-light: #E3F3FF;
            --lemlist-yellow: #FFD666;
            --text-dark: #1f2937;
            --text-light: #6b7280;
        }}
        
        * {{
            font-family: 'Inter', sans-serif;
        }}
        
        body {{
            background: linear-gradient(180deg, #FBFBFB 0%, #E6EAF4 100%);
            color: var(--text-dark);
        }}
        
        .lemlist-gradient {{
            background: linear-gradient(135deg, #255DEC 0%, #318BFF 100%);
        }}
        
        .trigger-card {{
            background: white;
            border-radius: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid #f0f0f0;
            height: 100%;
            display: flex;
            flex-direction: column;
            padding: 24px;
        }}
        
        .trigger-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 16px 32px rgba(49, 139, 255, 0.15);
            border-color: var(--lemlist-blue);
        }}
        
        .tab-button {{
            transition: all 0.3s ease;
            border-radius: 16px;
            font-weight: 600;
            padding: 14px 28px;
            border: 2px solid transparent;
            font-size: 15px;
        }}
        
        .tab-button.active {{
            background: linear-gradient(135deg, #318BFF 0%, #255DEC 100%);
            color: white;
            border-color: transparent;
            box-shadow: 0 4px 12px rgba(49, 139, 255, 0.3);
        }}
        
        .tab-button:not(.active) {{
            background-color: white;
            color: #1f2937;
            border-color: #e5e7eb;
        }}
        
        .tab-button:hover:not(.active) {{
            background-color: #E3F3FF;
            color: #143CDD;
            border-color: #318BFF;
        }}
        
        .cta-primary {{
            background: linear-gradient(135deg, #318BFF 0%, #255DEC 100%);
            color: white;
            transition: all 0.3s ease;
            border-radius: 16px;
            padding: 18px 36px;
            font-weight: 700;
            display: inline-block;
            text-decoration: none;
            font-size: 16px;
            box-shadow: 0 4px 12px rgba(49, 139, 255, 0.3);
        }}
        
        .cta-primary:hover {{
            background: linear-gradient(135deg, #255DEC 0%, #143CDD 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(49, 139, 255, 0.4);
        }}
        
        .cta-secondary {{
            background: white;
            color: var(--lemlist-blue);
            border: 2px solid var(--lemlist-blue);
            transition: all 0.3s ease;
            border-radius: 16px;
            padding: 16px 32px;
            font-weight: 700;
            display: inline-block;
            text-decoration: none;
            font-size: 16px;
        }}
        
        .cta-secondary:hover {{
            background: var(--lemlist-light);
            transform: translateY(-2px);
        }}
        
        .tool-tag {{
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            display: inline-block;
        }}
        
        .lemlist-tool {{
            background: var(--lemlist-blue);
            color: white;
        }}
        
        .free-tool {{
            background: #10b981;
            color: white;
        }}
        
        .paid-tool {{
            background: #f59e0b;
            color: white;
        }}
        
        .hidden {{
            display: none !important;
        }}
        
        .intent-badge {{
            background: linear-gradient(135deg, #FFD666 0%, #FFAB00 100%);
            color: var(--text-dark);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            display: inline-block;
        }}
        
        .strength-badge {{
            font-size: 14px;
        }}
        
        .collab-badge {{
            background: var(--lemlist-yellow);
            color: var(--text-dark);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .section-divider {{
            height: 2px;
            background: linear-gradient(90deg, #318BFF 0%, #FFD666 100%);
            margin: 60px 0;
        }}
        
        @media (max-width: 768px) {{
            .tab-button {{
                padding: 10px 16px;
                font-size: 14px;
            }}
            
            .trigger-card {{
                padding: 16px !important;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="lemlist-gradient text-white py-6 sticky top-0 z-50 shadow-lg">
        <div class="container mx-auto px-4">
            <div class="flex justify-between items-center">
                <div class="flex items-center gap-4">
                    <span class="text-2xl font-bold">salesCraft</span>
                    <span class="text-xl opacity-60">×</span>
                    <div class="bg-white px-4 py-2 rounded-lg shadow-sm">
                        <svg width="100" height="28" viewBox="0 0 100 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2" y="2" width="3" height="24" rx="1.5" fill="#318BFF"/>
                            <rect x="2" y="23" width="14" height="3" rx="1.5" fill="#318BFF"/>
                            <rect x="2" y="11" width="12" height="3" rx="1.5" fill="#318BFF"/>
                            <text x="22" y="20" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#318BFF">lemlist</text>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="lemlist-gradient text-white py-20">
        <div class="container mx-auto px-4 text-center">
            <div class="max-w-4xl mx-auto">
                <div class="mb-4">
                    <span class="collab-badge">Exclusive Collaboration</span>
                </div>
                <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                    95+ Buying Signals to Reach Prospects at the Perfect Moment
                </h1>
                <p class="text-xl md:text-2xl mb-10 text-blue-100">
                    Complete Guide with Examples, Templates & Detection Tools to Turn Intent Into Pipeline
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="https://www.lemlist.com/en/ads/contact-lemlist?utm_source=salescraft&utm_medium=collaboration&utm_campaign=100_buying_signals" target="_blank" class="cta-primary">
                        🚀 Start 14-Day Free Trial
                    </a>
                    <a href="https://calendly.com/ali-salescraft/30min" target="_blank" class="cta-secondary">
                        📅 Book a Call with Ali
                    </a>
                </div>
                <p class="text-sm text-blue-200 mt-6">
                    ✨ Automatic Signal Detection with lemlist Intent
                </p>
            </div>
        </div>
    </section>

    <!-- Triggers Section -->
    <section id="triggers" class="py-16">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-5xl font-bold mb-4 text-gray-900">
                    95 Buying Signals
                </h2>
                <p class="text-lg text-gray-600 max-w-3xl mx-auto">
                    Actionable signals organized by category, complete with detection tools and ready-to-use templates
                </p>
            </div>
            
            <!-- Tabs -->
            <div class="flex justify-center mb-12 overflow-x-auto">
                <div class="inline-flex flex-wrap gap-2 bg-white p-3 rounded-2xl shadow-lg">
                    <button class="tab-button active" data-tab="company" onclick="switchTab('company')">
                        🏢 Company (30)
                    </button>
                    <button class="tab-button" data-tab="person" onclick="switchTab('person')">
                        👤 Person (15)
                    </button>
                    <button class="tab-button" data-tab="tech" onclick="switchTab('tech')">
                        💻 Tech (10)
                    </button>
                    <button class="tab-button" data-tab="product" onclick="switchTab('product')">
                        🚀 Product-Led (20)
                    </button>
                    <button class="tab-button" data-tab="community" onclick="switchTab('community')">
                        👥 Community (15)
                    </button>
                    <button class="tab-button" data-tab="event" onclick="switchTab('event')">
                        📅 Events (5)
                    </button>
                </div>
            </div>
            
            <!-- Company Level Triggers -->
            <div id="company-content" class="tab-content">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['company']}
                </div>
            </div>
            
            <!-- Person Level Triggers -->
            <div id="person-content" class="tab-content hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['person']}
                </div>
            </div>
            
            <!-- Tech Triggers -->
            <div id="tech-content" class="tab-content hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['tech']}
                </div>
            </div>
            
            <!-- Product-Led Triggers -->
            <div id="product-content" class="tab-content hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['product']}
                </div>
            </div>
            
            <!-- Community Triggers -->
            <div id="community-content" class="tab-content hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['community']}
                </div>
            </div>
            
            <!-- Event Triggers -->
            <div id="event-content" class="tab-content hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {category_cards['event']}
                </div>
            </div>
        </div>
    </section>

    <div class="section-divider"></div>

    <!-- Intent Feature Section -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center">
                <div class="mb-6">
                    <span class="intent-badge text-base px-6 py-2">NEW</span>
                </div>
                <h2 class="text-3xl md:text-5xl font-bold mb-6">
                    Automate Signal Detection with lemlist Intent
                </h2>
                <p class="text-xl text-gray-600 mb-10">
                    Stop wasting time on manual research. lemlist Intent automatically detects buying signals and alerts you in real-time so you can engage prospects at exactly the right moment.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="https://www.lemlist.com/en/ads/contact-lemlist?utm_source=salescraft&utm_medium=collaboration&utm_campaign=intent_feature" target="_blank" class="cta-primary">
                        ✨ Explore lemlist Intent
                    </a>
                </div>
            </div>
        </div>
    </section>

    <div class="section-divider"></div>

    <!-- Method Section -->
    <section class="py-16 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">
                    How to Use These Signals
                </h2>
                <p class="text-lg text-gray-600">
                    A 4-Step Framework to Automate Your Prospecting
                </p>
            </div>
            
            <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-blue-100">
                    <div class="text-4xl font-bold text-blue-600 mb-4">1</div>
                    <h3 class="text-2xl font-bold mb-4">
                        Select Your Signals
                    </h3>
                    <p class="text-gray-600">
                        Choose the 5-10 most relevant signals that align with your ICP and value proposition.
                    </p>
                </div>

                <div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-blue-100">
                    <div class="text-4xl font-bold text-blue-600 mb-4">2</div>
                    <h3 class="text-2xl font-bold mb-4">
                        Configure Detection
                    </h3>
                    <p class="text-gray-600">
                        Connect lemlist Intent and set up automatic alerts for your highest-priority signals.
                    </p>
                </div>

                <div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-blue-100">
                    <div class="text-4xl font-bold text-blue-600 mb-4">3</div>
                    <h3 class="text-2xl font-bold mb-4">
                        Customize Templates
                    </h3>
                    <p class="text-gray-600">
                        Adapt our templates to match your brand voice and unique value proposition.
                    </p>
                </div>

                <div class="bg-white p-8 rounded-2xl shadow-lg border-2 border-blue-100">
                    <div class="text-4xl font-bold text-blue-600 mb-4">4</div>
                    <h3 class="text-2xl font-bold mb-4">
                        Measure & Optimize
                    </h3>
                    <p class="text-gray-600">
                        Track response rates by signal type and double down on what drives results.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="lemlist-gradient text-white py-20">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl md:text-5xl font-bold mb-6">
                Ready to Transform Your Prospecting?
            </h2>
            <p class="text-xl mb-10 text-blue-100">
                Start generating more pipeline with lemlist Intent and salesCraft
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <a href="https://www.lemlist.com/en/ads/contact-lemlist?utm_source=salescraft&utm_medium=collaboration&utm_campaign=final_cta" target="_blank" class="cta-primary">
                    🚀 Try lemlist Free
                </a>
                <a href="https://calendly.com/ali-salescraft/30min" target="_blank" class="cta-secondary">
                    📅 Talk to an Expert
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-8">
        <div class="container mx-auto px-4 text-center">
            <p class="text-gray-400">
                A Collaboration between salesCraft & lemlist • 95 Buying Signals to Boost Your Pipeline
            </p>
        </div>
    </footer>

    <script>
        // Tab switching
        function switchTab(tabName) {{
            // Hide all tab contents
            document.querySelectorAll('.tab-content').forEach(content => {{
                content.classList.add('hidden');
            }});
            
            // Remove active class from all buttons
            document.querySelectorAll('.tab-button').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            // Show selected tab and mark button as active
            document.getElementById(tabName + '-content').classList.remove('hidden');
            document.querySelector(`[data-tab="${{tabName}}"]`).classList.add('active');
            
            // Scroll to triggers section
            document.getElementById('triggers').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
        
        // Card animations on scroll
        const observerOptions = {{
            threshold: 0.05,
            rootMargin: '0px 0px -50px 0px'
        }};
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }}
            }});
        }}, observerOptions);
        
        // Animate trigger cards on load
        document.addEventListener('DOMContentLoaded', () => {{
            document.querySelectorAll('.trigger-card').forEach(card => {{
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            }});
        }});
    </script>
</body>
</html>
'''

# Write the complete HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

print(f"✅ Complete website generated successfully!")
print(f"📊 Signal counts:")
print(f"   - Company: {len(data['company'])} signals")
print(f"   - Person: {len(data['person'])} signals")
print(f"   - Tech: {len(data['tech'])} signals")
print(f"   - Product: {len(data['product'])} signals")
print(f"   - Community: {len(data['community'])} signals")
print(f"   - Event: {len(data['event'])} signals")
print(f"   - TOTAL: {sum(len(data[cat]) for cat in categories.keys())} signals")
