with open('store/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original length:", len(content))

# 1. Clear heroSlider
start_tag = '<div class="hero-slider" id="heroSlider">'
end_tag = '<div class="hero-dots">'
start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx)
print("Hero slider:", start_idx, end_idx)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx + len(start_tag)] + '\n  ' + content[end_idx:]

# 2. Clear hero-dots
start_tag2 = '<div class="hero-dots">'
end_tag2 = '</section>'
start_idx2 = content.find(start_tag2)
end_idx2 = content.find(end_tag2, start_idx2)
print("Hero dots:", start_idx2, end_idx2)
if start_idx2 != -1 and end_idx2 != -1:
    content = content[:start_idx2 + len(start_tag2)] + '\n' + content[end_idx2:]

# 3. Clear productGrid
start_tag3 = '<div class="product-grid" id="productGrid">'
end_tag3 = '</div><!-- /product-grid -->'
start_idx3 = content.find(start_tag3)
end_idx3 = content.find(end_tag3, start_idx3)
print("Product grid:", start_idx3, end_idx3)
if start_idx3 != -1 and end_idx3 != -1:
    content = content[:start_idx3 + len(start_tag3)] + '\n      ' + content[end_idx3:]

print("New length:", len(content))

with open('store/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
