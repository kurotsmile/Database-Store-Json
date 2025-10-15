import os
import json
import requests

def download_file(url, save_path):
    """Tải file từ URL và lưu vào đường dẫn"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Tải xong: {save_path}")
    except Exception as e:
        print(f"❌ Lỗi khi tải {url}: {e}")

def main():
    json_path = "output_songs/song-vi.json"  # file json của bạn
    output_folder = "downloads"
    audio_folder = os.path.join(output_folder, "audio")
    image_folder = os.path.join(output_folder, "image")

    # Tạo thư mục
    os.makedirs(audio_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)

    # Đọc JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Duyệt từng bài hát
    for item in data.get("all_item", []):
        name = item.get("name", "unknown").strip().replace("/", "_")
        artist = item.get("artist", "unknown").strip().replace("/", "_")

        # Tên file hợp lệ
        base_name = f"{artist} - {name}".replace(" ", "_")

        # Tải mp3
        mp3_url = item.get("mp3")
        if mp3_url:
            mp3_path = os.path.join(audio_folder, f"{base_name}.mp3")
            if not os.path.exists(mp3_path):
                download_file(mp3_url, mp3_path)
            else:
                print(f"⚠️ Đã tồn tại: {mp3_path}")

        # Tải ảnh bìa
        img_url = item.get("avatar")
        if img_url:
            ext = os.path.splitext(img_url.split("?")[0])[1] or ".jpg"
            img_path = os.path.join(image_folder, f"{base_name}{ext}")
            if not os.path.exists(img_path):
                download_file(img_url, img_path)
            else:
                print(f"⚠️ Đã tồn tại: {img_path}")

if __name__ == "__main__":
    main()
