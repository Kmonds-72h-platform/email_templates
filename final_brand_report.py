#!/usr/bin/env python3
import json

# Complete manual brand data including newly found brands
all_brands_data = {
    # Template 1
    "DEARGLAM": {
        'name': 'DEARGLAM',
        'documentId': 'ozyf1bg4wyiim3zmkxr93g83',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/7a3bb8c0b84e406bb968a3ba94351cd6.webp',
            'https://72h-prod.b-cdn.net/uploads/fe44af358bfc41b68342d45eb5937af1.webp',
            'https://72h-prod.b-cdn.net/uploads/8bc1baf2a501442ea6e4913f67fc9df0.webp',
            'https://72h-prod.b-cdn.net/uploads/bfd560a0cb6d4774af268e97f466abfa.webp'
        ]
    },
    "ARTOIS": {
        'name': 'ARTOIS',
        'documentId': 'ie7fk0mhstfqzo0qj000tgvq',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/z5mvfuynrtejzgtceh9s.webp',
            'https://72h-prod.b-cdn.net/uploads/jyojhz72epd2kcn5818h.webp',
            'https://72h-prod.b-cdn.net/uploads/dfubu31oetzrlsczgr68.webp',
            'https://72h-prod.b-cdn.net/uploads/ymuirktsqtw6iltjt1al.webp'
        ]
    },
    "Herbloom": {
        'name': 'Herbloom',
        'documentId': 'q0c7icinmc0f8wiugu3ct0kg',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/yse8sttc19yrrneh2jyx.webp',
            'https://72h-prod.b-cdn.net/uploads/m3mumb3ob9auqfo7a2v8.webp',
            'https://72h-prod.b-cdn.net/uploads/ghyrj6d4ws4ejpkhxiil.webp',
            'https://72h-prod.b-cdn.net/uploads/kus05gssmac2wnteb2gt.webp'
        ]
    },
    
    # Template 2
    "Deeponde": {  # Note: Found as "Deeponde" not "DeepOnde"
        'name': 'Deeponde',
        'documentId': 'eo4f512qopu1a30gneifkb5h',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/shfrfm5dadgtkof9cwgt.webp',
            'https://72h-prod.b-cdn.net/uploads/jvf0yjgmdqwq89vevoxl.png',
            'https://72h-prod.b-cdn.net/uploads/teesukdxnau86ffpctwg.mp4',
            'https://72h-prod.b-cdn.net/uploads/hhheyushzgyaygwrt40t.mov'
        ]
    },
    "DearLauren": {
        'name': 'DearLauren',
        'documentId': 'd5kwlrex3cjt48tz26xksaon',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/lfzdgkr87zaahlmnfiao.webp',
            'https://72h-prod.b-cdn.net/uploads/lrvuahvppzx5kuzwyfmz.webp',
            'https://72h-prod.b-cdn.net/uploads/yksgnfmfgslqikzwrpmh.webp',
            'https://72h-prod.b-cdn.net/uploads/ykjz9lzidlvnlzcifvej.webp'
        ]
    },
    "DrReborn": {
        'name': 'DrReborn',
        'documentId': 'tsmvpmk8kw5hpvtm0l3b25wx',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/oyxytr9u7oh25fymicnz.png',
            'https://72h-prod.b-cdn.net/uploads/oquddqdfh8hqngvwcunf.png',
            'https://72h-prod.b-cdn.net/uploads/ktnamf4eqju1g0g4fl4p.png',
            'https://72h-prod.b-cdn.net/uploads/bfgdpby6qb09aggo9kfs.png',
            'https://72h-prod.b-cdn.net/uploads/ordiuypqjzqira6bvvg4.png',
            'https://72h-prod.b-cdn.net/uploads/axo2onqwxtphmrrzd6el.png',
            'https://72h-prod.b-cdn.net/uploads/uyys137pygi2fa3bkpec.png',
            'https://72h-prod.b-cdn.net/uploads/jyzkgarmpkqkeovnegsx.png'
        ]
    },
    
    # Template 3
    "LAB FOR YOU": {  # Note: Found as "LAB FOR YOU" not "LabForYou"
        'name': 'LAB FOR YOU',
        'documentId': 'a5kzpjs2zwnqlxs726c301kp',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/zyf6yzyv23qaztjovbue.jpg',
            'https://72h-prod.b-cdn.net/uploads/m0j71ckq8abmukufeziw.mp4',
            'https://72h-prod.b-cdn.net/uploads/t5qrdkpptg2xextii7xs.mp4',
            'https://72h-prod.b-cdn.net/uploads/g5uuc47wnuybxrmx32xs.webp'
        ]
    },
    "LaMuse": {
        'name': 'LaMuse',
        'documentId': 'qhm6rk6j0fvjqhttfxgf6jku',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/xe5pjmdfnkfavzsewx4m.webp',
            'https://72h-prod.b-cdn.net/uploads/l8thbajxf8w5f0m2u8g6.webp',
            'https://72h-prod.b-cdn.net/uploads/mwrjhxfb8r9n1j6o5cps.webp',
            'https://72h-prod.b-cdn.net/uploads/s3vlzwlgvd7r8fkeyqpn.webp'
        ]
    },
    "Ecobrick": {
        'name': 'Ecobrick',
        'documentId': 'vbyq68zw7cz81rxnl7hk4a1y',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/aff9ce629afe48229f22546e93c7800b.jpg',
            'https://72h-prod.b-cdn.net/uploads/8102980fde714d249f61467051a291c7.jpg',
            'https://72h-prod.b-cdn.net/uploads/0f08cfce43db43ed8dc43ba8aa95d644.jpg',
            'https://72h-prod.b-cdn.net/uploads/6bd6f49b74514906b99c50b45c5536ad.jpg'
        ]
    },
    
    # Template 6
    "Equlib": {
        'name': 'Equlib',
        'documentId': 'gp50ko6ihzzdga7x7jwomrem',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/s9ecerlpm7pfveottvm2.png',
            'https://72h-prod.b-cdn.net/uploads/wmgvpzp1tr9fl0odblgz.png',
            'https://72h-prod.b-cdn.net/uploads/snssko2wi1egs0fpsvt8.png',
            'https://72h-prod.b-cdn.net/uploads/fwroiqvtmxv9eke9ujfo.png',
            'https://72h-prod.b-cdn.net/uploads/cn7mxhkczdjy8yx8cxku.png',
            'https://72h-prod.b-cdn.net/uploads/opyc5e6p3q2mfvm5fj0h.jpg',
            'https://72h-prod.b-cdn.net/uploads/edufx4c3958gb77gsd3r.jpg'
        ]
    },
    "MILLAC": {
        'name': 'MILLAC',
        'documentId': 'ki3itebxw5ys480tbvkfxzr2',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/m74qm2zqkuyoqtgfm53m.jpg',
            'https://72h-prod.b-cdn.net/uploads/uepojdze66kcplqs9sua.jpg',
            'https://72h-prod.b-cdn.net/uploads/cnf1ymf14o7fs2chhcwv.jpg',
            'https://72h-prod.b-cdn.net/uploads/ufbicp9mguqd1kek4cnx.jpg',
            'https://72h-prod.b-cdn.net/uploads/fmbdqaaikfhftejwr8rs.jpg',
            'https://72h-prod.b-cdn.net/uploads/iiw5l7xucuyppmdwso11.jpg',
            'https://72h-prod.b-cdn.net/uploads/id3sl73e0bznwdvl9ej9.jpg',
            'https://72h-prod.b-cdn.net/uploads/dzy9sw3akekvxzanf1fz.jpg'
        ]
    },
    "WOLLYO": {
        'name': 'WOLLYO',
        'documentId': 'hn6unegzunjd5m9qtccms0h3',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/cmlmbrgkbw9drpkqpqm9.webp',
            'https://72h-prod.b-cdn.net/uploads/cwxbucdfad4qv3zf97vg.webp',
            'https://72h-prod.b-cdn.net/uploads/mlzftdbgpchcep2xyysq.webp',
            'https://72h-prod.b-cdn.net/uploads/xkyt3g1rgspvrw3tietu.webp'
        ]
    },
    
    # Template 7
    "VIVAKOREA": {
        'name': 'VIVAKOREA',
        'documentId': 'hiuznnc0mpyn626325sf3u2b',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/d8ygdstmsobvfb2cu4u5.jpg',
            'https://72h-prod.b-cdn.net/uploads/bb2d9lwwoyhfayg5zfc0.jpg',
            'https://72h-prod.b-cdn.net/uploads/w0cwa4wdcnkrqjlfwu9j.jpg',
            'https://72h-prod.b-cdn.net/uploads/lyi5xryuqzpsqke837wl.jpg',
            'https://72h-prod.b-cdn.net/uploads/bzjcgq8nggfferitiziq.jpg',
            'https://72h-prod.b-cdn.net/uploads/wnvurpvgm9blznryutic.jpg',
            'https://72h-prod.b-cdn.net/uploads/pwe4qtmdnh7pzygaincu.jpg',
            'https://72h-prod.b-cdn.net/uploads/xfsxbcmprugbv0avk9su.jpg'
        ]
    },
    "OAVO": {
        'name': 'OAVO',
        'documentId': 'vk0mu9nv4ctvc9n0labr524f',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/bjpzzomczxiiklpgqwnt.jpg',
            'https://72h-prod.b-cdn.net/uploads/xus3dddxe1xxkkntoke6.jpg',
            'https://72h-prod.b-cdn.net/uploads/z7ccre8z7jkml0ldkemy.jpg',
            'https://72h-prod.b-cdn.net/uploads/rp9dvgyoclut1trv23j6.jpg',
            'https://72h-prod.b-cdn.net/uploads/h3yrfal958qpaoellgj6.jpg',
            'https://72h-prod.b-cdn.net/uploads/pk6yrj9ebt8fddsteysa.jpg',
            'https://72h-prod.b-cdn.net/uploads/fzvlnuqmty62dn6cnkau.jpg',
            'https://72h-prod.b-cdn.net/uploads/ohyynybqf2rgzp9jxbkp.jpg'
        ]
    },
    "MORAPO & NUDY BEAUTY": {
        'name': 'MORAPO & NUDY BEAUTY',
        'documentId': 'yqhd5f1hguo3we2f903ee7na',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/n1ffv1lrzppkeycy6pgg.png',
            'https://72h-prod.b-cdn.net/uploads/l4lkvv2dkumftoxccfn8.png',
            'https://72h-prod.b-cdn.net/uploads/bb6ed20iijolwzebor5p.png',
            'https://72h-prod.b-cdn.net/uploads/jvf0yjgmdqwq89vevoxl.png'
        ]
    },
    
    # Template 8
    "LUSIS": {
        'name': 'LUSIS',
        'documentId': 'h0a2zbdm8bbs4ql7uoh15jlg',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/asblrawpuvv7ksjy8cf8.jpg',
            'https://72h-prod.b-cdn.net/uploads/ocerkrymoplvciaaugl0.jpg',
            'https://72h-prod.b-cdn.net/uploads/sjgvcosxyisjvq8cztvu.jpg',
            'https://72h-prod.b-cdn.net/uploads/nijpltiuuajsr3efeeqo.jpg'
        ]
    },
    "ROBLUE": {
        'name': 'ROBLUE',
        'documentId': 'umhgub35dgm7ccp1c8fkafqm',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/wwwrobkkinyca8uxlssb.jpg',
            'https://72h-prod.b-cdn.net/uploads/kay1ryiedxrxpuealwtu.jpg',
            'https://72h-prod.b-cdn.net/uploads/gixbpaohvg5qre5jcim5.png',
            'https://72h-prod.b-cdn.net/uploads/w6x2qcirogemzuezieao.png',
            'https://72h-prod.b-cdn.net/uploads/oyoyhnskslaikheewou9.png',
            'https://72h-prod.b-cdn.net/uploads/iil18bt7utx9nih8zdma.png',
            'https://72h-prod.b-cdn.net/uploads/totbwjk2jovgda3zdcfs.jpg',
            'https://72h-prod.b-cdn.net/uploads/wmd9jvc6kg13edqg90mw.jpg'
        ]
    },
    "Morethan8": {
        'name': 'Morethan8',
        'documentId': 'b9u7b6zckf7bf8qd8oag3jsp',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/cnn618onimoegeen2jii.png',
            'https://72h-prod.b-cdn.net/uploads/hs8puiql1dgqks7kxiqi.jpg',
            'https://72h-prod.b-cdn.net/uploads/bp6vtulpgs6ts4zzj7iw.png',
            'https://72h-prod.b-cdn.net/uploads/yigpkri7uekep3rskf2m.png',
            'https://72h-prod.b-cdn.net/uploads/ljbujsyuuzmaiwjpilgi.png',
            'https://72h-prod.b-cdn.net/uploads/gcyvkdubtdynwusoz17o.png',
            'https://72h-prod.b-cdn.net/uploads/nbjdmznuzllysqhblueq.png',
            'https://72h-prod.b-cdn.net/uploads/cerrydpondzraqsuy9ze.png'
        ]
    },
    
    # Template 9
    "CHALLANS de PARIS": {
        'name': 'CHALLANS de PARIS',
        'documentId': 'l6z8ahkpvz6f61237jd49op1',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/mryqtmwwtuilixel4l2z.jpg',
            'https://72h-prod.b-cdn.net/uploads/ebqi4nhf6qoetia4ip5h.jpg',
            'https://72h-prod.b-cdn.net/uploads/i07nc2r140yfrhdygysj.jpg',
            'https://72h-prod.b-cdn.net/uploads/a7jpnkcebhdtvdtrsrrf.jpg',
            'https://72h-prod.b-cdn.net/uploads/beonruwjzzsit0izydzk.jpg',
            'https://72h-prod.b-cdn.net/uploads/hatyz26nlwzgs9ulxdlf.jpg',
            'https://72h-prod.b-cdn.net/uploads/uq3af6qsqqael06ri7na.jpg',
            'https://72h-prod.b-cdn.net/uploads/xohr6hgvs8xm6iddtgcq.jpg'
        ]
    },
    "SKANSKIN": {
        'name': 'SKANSKIN',
        'documentId': 'u8ausibswywt29jfxfe3vvhk',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/nfp8ujfty14mqv4djfkr.jpg',
            'https://72h-prod.b-cdn.net/uploads/ajd8y6f5hrm3hivyel59.jpg',
            'https://72h-prod.b-cdn.net/uploads/mji63cobodi4fcg6sy9a.jpg',
            'https://72h-prod.b-cdn.net/uploads/lzued6gvvt4sgilsvvmm.jpg',
            'https://72h-prod.b-cdn.net/uploads/vmyj3eilvb8sk4tjxazi.jpg',
            'https://72h-prod.b-cdn.net/uploads/lbae6vyvuyhedci0xete.jpg',
            'https://72h-prod.b-cdn.net/uploads/sga5kflnbcauzevpqr1t.jpg',
            'https://72h-prod.b-cdn.net/uploads/vfjdgenlgobnvdhs1ekr.jpg'
        ]
    },
    "Bens Lab": {
        'name': 'Bens Lab',
        'documentId': 'vz0gr7b8sdag8gjkdvhwmrb0',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/cbullqzb0xkeagsrbbeq.jpg',
            'https://72h-prod.b-cdn.net/uploads/wolasndfipkpbmo7ec3f.jpg',
            'https://72h-prod.b-cdn.net/uploads/zlluyplkcqndopqmnfny.jpg',
            'https://72h-prod.b-cdn.net/uploads/h94yljb3zbze1zg8uhly.jpg',
            'https://72h-prod.b-cdn.net/uploads/zwkpo1raxs6jnydwbdk8.jpg',
            'https://72h-prod.b-cdn.net/uploads/jmhcxe0rfzgdgbcqsbtf.jpg',
            'https://72h-prod.b-cdn.net/uploads/zsbzm95z3ejdjarfobqs.jpg',
            'https://72h-prod.b-cdn.net/uploads/s9c7mkbxpu64u4vxmexn.jpg'
        ]
    },
    
    # Template 10
    "MEMINE": {
        'name': 'MEMINE',
        'documentId': 'a6obu4scsax1f0fnafiezcje',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/pjqj7iicialfe9bucfu3.jpg',
            'https://72h-prod.b-cdn.net/uploads/bouec1glf0zxwalvejhc.png',
            'https://72h-prod.b-cdn.net/uploads/gzwys6hhcxtakmwdv6ta.png',
            'https://72h-prod.b-cdn.net/uploads/jkgoape00j9xpnveijgq.png',
            'https://72h-prod.b-cdn.net/uploads/z9po1pcurd5c3ffosecx.png'
        ]
    },
    "UNGSAM": {
        'name': 'UNGSAM',
        'documentId': 'jrx7tw7z3n18djclsupbfha1',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/ozcl5npe21uq9y67gaax.png',
            'https://72h-prod.b-cdn.net/uploads/f6qglr8mrhyvaqtpv0x3.jpg',
            'https://72h-prod.b-cdn.net/uploads/tcua6b2nhnwpcq6msozv.jpg',
            'https://72h-prod.b-cdn.net/uploads/qjmklea7b6jon0kviqbz.png',
            'https://72h-prod.b-cdn.net/uploads/ytqwbv8ftojsgvdix6ud.png',
            'https://72h-prod.b-cdn.net/uploads/ugykqj35ko2xxzwhvipw.png',
            'https://72h-prod.b-cdn.net/uploads/a9crbedaakvxtjghhzjo.png',
            'https://72h-prod.b-cdn.net/uploads/ianmppryn2mgy4mbjyq3.png'
        ]
    },
    "TISHA": {
        'name': 'TISHA',
        'documentId': 'zb087hzc0rtmlbsrp9l8qal7',
        'hero_images': [
            'https://72h-prod.b-cdn.net/uploads/awu5pcrakh5qpbbd330o.webp',
            'https://72h-prod.b-cdn.net/uploads/mg82hl0abxieiabi8bml.webp',
            'https://72h-prod.b-cdn.net/uploads/mjednfnjwu1difmtxbhj.webp',
            'https://72h-prod.b-cdn.net/uploads/xdveldh3iswprklqunhg.webp'
        ]
    }
}

# Template structure
template_groups = [
    ("Template 1", ["DEARGLAM", "ARTOIS", "Herbloom"]),
    ("Template 2", ["Deeponde", "DearLauren", "DrReborn"]),  # Note: Deeponde not DeepOnde
    ("Template 3", ["LAB FOR YOU", "LaMuse", "Ecobrick"]),  # Note: LAB FOR YOU not LabForYou
    ("Template 4", ["GOODAL", "OOLU", "Holikatika"]),  # These brands not found in JSON
    ("Template 5", ["SKIN79", "NEOGEN", "Genskin"]),  # These brands not found in JSON
    ("Template 6", ["Equlib", "MILLAC", "WOLLYO"]),
    ("Template 7", ["VIVAKOREA", "OAVO", "MORAPO & NUDY BEAUTY"]),
    ("Template 8", ["LUSIS", "ROBLUE", "Morethan8"]),
    ("Template 9", ["CHALLANS de PARIS", "SKANSKIN", "Bens Lab"]),
    ("Template 10", ["MEMINE", "UNGSAM", "TISHA"])
]

print("FINAL BRAND INFORMATION REPORT FOR SHOWCASE-MAGAZINE TEMPLATES")
print("=" * 75)
print()

# Print detailed information for each template
for template_name, brand_list in template_groups:
    print(f"{template_name}:")
    print("-" * 50)
    for brand in brand_list:
        if brand in all_brands_data:
            info = all_brands_data[brand]
            print(f"  ✓ Brand: {info['name']}")
            print(f"    DocumentId: {info['documentId']}")
            print(f"    Hero Images ({len(info['hero_images'])} available):")
            for i, url in enumerate(info['hero_images'][:4], 1):  # Show first 4
                print(f"      {i}. {url}")
            if len(info['hero_images']) > 4:
                print(f"      ... and {len(info['hero_images']) - 4} more images")
            print()
        else:
            print(f"  ✗ Brand: {brand} - NOT FOUND IN BRANDS.JSON")
            print(f"    Status: This brand does not exist in the current brands database")
            print()
    
print("\n" + "=" * 75)
print("SUMMARY STATISTICS")
print("=" * 75)

found_count = sum(1 for _, brand_list in template_groups for brand in brand_list if brand in all_brands_data)
total_count = sum(len(brand_list) for _, brand_list in template_groups)
not_found = [brand for _, brand_list in template_groups for brand in brand_list if brand not in all_brands_data]

print(f"Found brands: {found_count}/{total_count}")
print(f"Success rate: {found_count/total_count*100:.1f}%")
print(f"Missing brands: {', '.join(not_found)}")

print("\n" + "=" * 75)
print("NOTES ON BRAND NAME VARIATIONS")
print("=" * 75)
print("• DeepOnde → Found as 'Deeponde' in database")
print("• LabForYou → Found as 'LAB FOR YOU' in database")
print("• ECOBRICK → Found as 'Ecobrick' in database")
print("• MORAPO & NUDY BEAUTY → Found as combined brand in database")
print("• 6 brands (GOODAL, OOLU, Holikatika, SKIN79, NEOGEN, Genskin) not present in brands.json")

# Save complete data to JSON for easy import
structured_output = {}
for template_name, brand_list in template_groups:
    template_key = template_name.lower().replace(' ', '_')
    structured_output[template_key] = {}
    for brand in brand_list:
        if brand in all_brands_data:
            structured_output[template_key][brand] = all_brands_data[brand]

with open('/Users/kmonds/Work/72h_Project/72h-email-templates/final_brands_data.json', 'w') as f:
    json.dump(structured_output, f, indent=2)

print(f"\nComplete structured data exported to: final_brands_data.json")
print("This file contains all found brand information organized by template for easy integration.")