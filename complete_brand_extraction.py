#!/usr/bin/env python3
import json

# Read the JSON file
with open('/Users/kmonds/Work/72h_Project/72h-email-templates/brands.json', 'r') as f:
    data = json.load(f)

# Manual extraction of specific brands we found through grep
manual_brands = {
    "LaMuse": {
        'name': 'LaMuse',
        'documentId': 'qhm6rk6j0fvjqhttfxgf6jku',  # Found through grep
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/xe5pjmdfnkfavzsewx4m.webp',
            'https://72h-prod.b-cdn.net/uploads/l8thbajxf8w5f0m2u8g6.webp',
            'https://72h-prod.b-cdn.net/uploads/mwrjhxfb8r9n1j6o5cps.webp',
            'https://72h-prod.b-cdn.net/uploads/s3vlzwlgvd7r8fkeyqpn.webp'
        ]
    },
    "DearLauren": {
        'name': 'DearLauren',
        'documentId': 'd5kwlrex3cjt48tz26xksaon',  # Found through grep
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/lfzdgkr87zaahlmnfiao.webp',
            'https://72h-prod.b-cdn.net/uploads/lrvuahvppzx5kuzwyfmz.webp',
            'https://72h-prod.b-cdn.net/uploads/yksgnfmfgslqikzwrpmh.webp',
            'https://72h-prod.b-cdn.net/uploads/ykjz9lzidlvnlzcifvej.webp'
        ]
    },
    "Ecobrick": {
        'name': 'Ecobrick',
        'documentId': 'vbyq68zw7cz81rxnl7hk4a1y',  # Found through grep
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/aff9ce629afe48229f22546e93c7800b.jpg',
            'https://72h-prod.b-cdn.net/uploads/8102980fde714d249f61467051a291c7.jpg',
            'https://72h-prod.b-cdn.net/uploads/0f08cfce43db43ed8dc43ba8aa95d644.jpg',
            'https://72h-prod.b-cdn.net/uploads/6bd6f49b74514906b99c50b45c5536ad.jpg'
        ]
    },
    "MORAPO & NUDY BEAUTY": {
        'name': 'MORAPO & NUDY BEAUTY',
        'documentId': 'yqhd5f1hguo3we2f903ee7na',  # Found through grep
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/n1ffv1lrzppkeycy6pgg.png',
            'https://72h-prod.b-cdn.net/uploads/l4lkvv2dkumftoxccfn8.png',
            'https://72h-prod.b-cdn.net/uploads/bb6ed20iijolwzebor5p.png',
            'https://72h-prod.b-cdn.net/uploads/jvf0yjgmdqwq89vevoxl.png'
        ]
    }
}

def extract_brand_info(brands_data, brand_names):
    results = {}
    
    for brand_entry in brands_data.get('data', []):
        brand_name = brand_entry.get('name', '')
        
        # Check if this brand is in our list
        if brand_name in brand_names:
            hero_images = []
            if 'hero' in brand_entry and brand_entry['hero']:
                hero_images = [img.get('url', '') for img in brand_entry['hero']]
            
            results[brand_name] = {
                'name': brand_name,
                'documentId': brand_entry.get('documentId', ''),
                'hero_images': hero_images
            }
    
    return results

# List of brands to extract
brands_to_find = [
    "DEARGLAM", "ARTOIS", "Herbloom",
    "DeepOnde", "DearLauren", "DrReborn",
    "LabForYou", "LaMuse", "ECOBRICK", "Ecobrick",
    "GOODAL", "OOLU", "Holikatika",
    "SKIN79", "NEOGEN", "Genskin",
    "Equlib", "MILLAC", "WOLLYO",
    "VIVAKOREA", "OAVO", "MORAPO", "NUDY BEAUTY", "MORAPO & NUDY BEAUTY",
    "LUSIS", "ROBLUE", "Morethan8",
    "CHALLANS de PARIS", "SKANSKIN", "Bens Lab",
    "MEMINE", "UNGSAM", "TISHA"
]

extracted_brands = extract_brand_info(data, brands_to_find)

# Add manual brands
for brand_name, brand_info in manual_brands.items():
    extracted_brands[brand_name] = brand_info

# Print complete structured results
print("COMPLETE BRAND INFORMATION FOR SHOWCASE-MAGAZINE TEMPLATES")
print("=" * 65)

template_groups = [
    ("Template 1", ["DEARGLAM", "ARTOIS", "Herbloom"]),
    ("Template 2", ["DeepOnde", "DearLauren", "DrReborn"]),
    ("Template 3", ["LabForYou", "LaMuse", "Ecobrick"]),
    ("Template 4", ["GOODAL", "OOLU", "Holikatika"]),
    ("Template 5", ["SKIN79", "NEOGEN", "Genskin"]),
    ("Template 6", ["Equlib", "MILLAC", "WOLLYO"]),
    ("Template 7", ["VIVAKOREA", "OAVO", "MORAPO & NUDY BEAUTY"]),
    ("Template 8", ["LUSIS", "ROBLUE", "Morethan8"]),
    ("Template 9", ["CHALLANS de PARIS", "SKANSKIN", "Bens Lab"]),
    ("Template 10", ["MEMINE", "UNGSAM", "TISHA"])
]

for template_name, brand_list in template_groups:
    print(f"\n{template_name}:")
    print("-" * 40)
    for brand in brand_list:
        if brand in extracted_brands:
            info = extracted_brands[brand]
            print(f"  Brand: {info['name']}")
            print(f"  DocumentId: {info['documentId']}")
            print(f"  Hero Images ({len(info['hero_images'])} total):")
            for i, url in enumerate(info['hero_images'][:4], 1):  # Show first 4 images
                print(f"    Image {i}: {url}")
            if len(info['hero_images']) > 4:
                print(f"    ... and {len(info['hero_images']) - 4} more images")
            print()
        else:
            print(f"  Brand: {brand} - STILL NOT FOUND")
            print()

# Create a structured JSON output for easy use
output_data = {}
for template_name, brand_list in template_groups:
    template_key = template_name.lower().replace(' ', '_')
    output_data[template_key] = {}
    for brand in brand_list:
        if brand in extracted_brands:
            output_data[template_key][brand] = extracted_brands[brand]

# Summary
found_brands = len([brand for template_name, brand_list in template_groups 
                   for brand in brand_list if brand in extracted_brands])
total_brands = sum(len(brand_list) for template_name, brand_list in template_groups)
print(f"\nSUMMARY: Found {found_brands}/{total_brands} brands")

if found_brands < total_brands:
    missing = []
    for template_name, brand_list in template_groups:
        for brand in brand_list:
            if brand not in extracted_brands:
                missing.append(brand)
    print(f"Missing brands: {', '.join(missing)}")

# Save structured data to JSON file
with open('/Users/kmonds/Work/72h_Project/72h-email-templates/extracted_brands_data.json', 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"\nStructured data saved to: extracted_brands_data.json")