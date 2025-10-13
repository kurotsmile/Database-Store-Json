import json
from pathlib import Path

# Đường dẫn file gốc
input_file = "song.json"

# Đọc dữ liệu từ file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Tạo thư mục xuất nếu chưa có
output_dir = Path("output_songs")
output_dir.mkdir(exist_ok=True)

# Kiểm tra dữ liệu
if "all_item" not in data or not isinstance(data["all_item"], list):
    raise ValueError("Dữ liệu không hợp lệ hoặc thiếu key 'all_item'.")

# Gom nhóm theo ngôn ngữ
lang_groups = {}
for item in data["all_item"]:
    lang = item.get("lang", "unknown").strip().lower()
    lang_groups.setdefault(lang, []).append(item)

# Ghi từng nhóm ra file riêng
for lang, items in lang_groups.items():
    output_data = {"all_item": items}
    output_path = output_dir / f"song-{lang}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo file: {output_path}")

print("Hoàn tất tách dữ liệu theo ngôn ngữ!")
