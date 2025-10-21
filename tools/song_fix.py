import json
import re

langs=["ar","cs","da","de","en","es","fi","fr","id","it","ja","ko","nl","pl","pt","ru","th","tr","zh"]
for l in langs:
    input_path = "output_songs/song-"+l+".json"
    output_path = "output_songs/song-"+l+".json"

    def clean_lyrics(text):
        if not isinstance(text, str):
            return text

        # Thay các thẻ xuống dòng bằng ký hiệu đặc biệt để giữ vị trí
        text = re.sub(r'(?i)<br\s*/?>', '\\n', text)
        text = re.sub(r'(?i)</p\s*>', '\\n', text)
        text = re.sub(r'(?i)<p\s*>', '\\n', text)
        text = re.sub(r'(?i)<div\s*>', '\\n', text)
        text = re.sub(r'(?i)</div\s*>', '\\n', text)
        text = re.sub(r'(?i)<li\s*>', '\\n- ', text)
        text = re.sub(r'(?i)</li\s*>', '', text)

        # Loại bỏ các thẻ HTML còn lại
        text = re.sub(r'<[^>]*>', '', text)

        # Làm sạch chuỗi (xóa khoảng trắng dư, giữ \\n)
        text = re.sub(r'\r', '', text)
        text = re.sub(r'\n+', '\\n', text)   # nếu có xuống dòng thật
        text = text.strip()

        return text

    # Đọc dữ liệu
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Làm sạch lyrics
    for item in data.get("all_item", []):
        if "lyrics" in item and item["lyrics"]:
            item["lyrics"] = clean_lyrics(item["lyrics"])

    # Ghi ra file JSON gọn gàng
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã xóa HTML và giữ chỗ ngắt dòng bằng ký hiệu '\\\\n' trong lyrics: {output_path}")
