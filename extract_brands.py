#!/usr/bin/env python3
import json
import sys

# List of brands to extract with variations
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

# Read the JSON file
try:
    with open('/Users/kmonds/Work/72h_Project/72h-email-templates/brands.json', 'r') as f:
        data = json.load(f)
    
    extracted_brands = extract_brand_info(data, brands_to_find)
    
    # Print results in a structured format
    print("EXTRACTED BRAND INFORMATION:")
    print("=" * 50)
    
    template_groups = [
        ("Template 1", ["DEARGLAM", "ARTOIS", "Herbloom"]),
        ("Template 2", ["DeepOnde", "DearLauren", "DrReborn"]),
        ("Template 3", ["LabForYou", "LaMuse", "ECOBRICK"]),
        ("Template 4", ["GOODAL", "OOLU", "Holikatika"]),
        ("Template 5", ["SKIN79", "NEOGEN", "Genskin"]),
        ("Template 6", ["Equlib", "MILLAC", "WOLLYO"]),
        ("Template 7", ["VIVAKOREA", "OAVO", "MORAPO", "NUDY BEAUTY"]),
        ("Template 8", ["LUSIS", "ROBLUE", "Morethan8"]),
        ("Template 9", ["CHALLANS de PARIS", "SKANSKIN", "Bens Lab"]),
        ("Template 10", ["MEMINE", "UNGSAM", "TISHA"])
    ]
    
    for template_name, brand_list in template_groups:
        print(f"\n{template_name}:")
        print("-" * 30)
        for brand in brand_list:
            if brand in extracted_brands:
                info = extracted_brands[brand]
                print(f"  Brand: {info['name']}")
                print(f"  DocumentId: {info['documentId']}")
                print(f"  Hero Images: {len(info['hero_images'])} images")
                for i, url in enumerate(info['hero_images'], 1):
                    print(f"    Image {i}: {url}")
                print()
            else:
                print(f"  Brand: {brand} - NOT FOUND")
                print()
    
    # Summary
    found_brands = len(extracted_brands)
    total_brands = len(brands_to_find)
    print(f"\nSUMMARY: Found {found_brands}/{total_brands} brands")
    
    if found_brands < total_brands:
        missing = set(brands_to_find) - set(extracted_brands.keys())
        print(f"Missing brands: {', '.join(missing)}")

except Exception as e:
    print(f"Error: {e}")