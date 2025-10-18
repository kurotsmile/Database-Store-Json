import json
import re

# 🧩 HÀM CHUYỂN LINK GOOGLE DRIVE VIEW → DOWNLOAD
def convert_drive_link(view_url):
    match = re.search(r"https://drive\.google\.com/file/d/([^/]+)/view", view_url)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    return view_url

# 🗂️ CÁC TRƯỜNG CẦN CHUYỂN
fields_to_convert = ["dmg_file", "deb_file", "apk_file", "exe_file", "ipa_file"]

# 📖 ĐỌC FILE JSON
with open("app_carrotstore.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 🔄 DUYỆT TẤT CẢ ITEM VÀ CHUYỂN LINK
for item in data.get("all_item", []):
    for field in fields_to_convert:
        url = item.get(field, "")
        if "https://drive.google.com" in url and "/view" in url:
            new_url = convert_drive_link(url)
            print(f"✅ Converted: {url} → {new_url}")
            item[field] = new_url

# 💾 GHI LẠI FILE JSON ĐÃ CẬP NHẬT
with open("app_carrotstore_converted.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n🎉 Done! File đã được lưu thành 'app_carrotstore_converted.json'")
