import re

with open('store/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clear hero-slider
content = re.sub(
    r'(<div class="hero-slider" id="heroSlider">).*?(<div class="hero-dots" id="heroDots">)',
    r'\1\n    \2',
    content,
    flags=re.DOTALL
)

# 2. Clear hero-dots
content = re.sub(
    r'(<div class="hero-dots" id="heroDots">).*?(</div>\s*</div>\s*<div class="hero-content">)',
    r'\1\n    \2',
    content,
    flags=re.DOTALL
)

# 3. Replace product-grid and clear it
content = re.sub(
    r'<div class="product-grid">.*?</div><!-- /product-grid -->',
    r'<div class="product-grid" id="productGrid">\n      </div><!-- /product-grid -->',
    content,
    flags=re.DOTALL
)

with open('store/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating store/index.html")
