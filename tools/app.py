import json

def remove_describe_field(json_path="app_carrotstore.json"):
    # Đọc file JSON gốc
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Duyệt qua từng phần tử trong all_item và xóa trường 'describe_en'
    for item in data.get("all_item", []):
        if "describe_en" in item:
            del item["describe_en"]

    # Ghi đè lại file JSON (có định dạng đẹp)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã xóa thuộc tính 'describe_en' và lưu lại file: {json_path}")

if __name__ == "__main__":
    remove_describe_field()