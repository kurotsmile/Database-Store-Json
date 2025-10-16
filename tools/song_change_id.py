import json
import unicodedata
import re

lang="ar"

def generate_song_id(name, artist):
    """Tạo ID dạng slug từ tên bài hát và nghệ sĩ"""
    text = f"{name}-{artist}".lower()
    # Bỏ dấu tiếng Việt
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    # Giữ lại chữ và số, thay ký tự khác bằng dấu -
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Xóa dấu - ở đầu hoặc cuối
    text = text.strip('-')
    return text

# --- Đọc file JSON ---
input_file = 'output_songs/song-'+lang+'.json'
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# --- Cập nhật ID ---
for item in data.get("all_item", []):
    name = item.get("name", "")
    artist = item.get("artist", "")
    new_id = generate_song_id(name, artist)
    item["id"] = new_id
    if "id_import" in item:
        del item["id_import"]

# --- Ghi lại ra file mới (hoặc ghi đè) ---
output_file = "output_songs/song-"+lang+".json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Đã cập nhật ID thành công và lưu vào:", output_file)
