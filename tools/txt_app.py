
import os
import json

lang="ja"
def main():
    json_path = "app.json"  # đường dẫn đến file json
    output_folder = "txt_app"           # thư mục lưu các file .txt

    # Tạo thư mục nếu chưa có
    os.makedirs(output_folder, exist_ok=True)

    # Đọc nội dung JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Duyệt qua tất cả các phần tử trong mảng all_item
    for item in data.get("all_item", []):
        app_id = item.get("app_id", "unknown").strip()
        if app_id == "unknown" :
            app_id = item.get("id_import", "unknown").strip()

        describe_en = item.get("describe_"+lang, "").strip()

        # Bỏ ký tự không hợp lệ trong tên file (Windows, Linux)
        safe_name = "".join(c for c in app_id if c.isalnum() or c in (" ", "_", "-")).rstrip()
        filename = f"{safe_name}_{lang}.txt"

        # Đường dẫn lưu file
        file_path = os.path.join(output_folder, filename)

        # Ghi nội dung vào file
        with open(file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(describe_en)

        print(f"✅ Đã tạo: {file_path}")

if __name__ == "__main__":
    main()
