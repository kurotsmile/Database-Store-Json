import os
import json

langs = ["ar","cs","da","de","en","es","fi","fr","id","it","ja","ko","nl","pl","pt","ru","th","tr","vi","zh"]

# Tạo thư mục output nếu chưa có
os.makedirs("output_user", exist_ok=True)

output_all = "output_user/create_all_users.sql"

with open(output_all, "w", encoding="utf-8") as f_all:
    f_all.write("-- 📘 Tự động sinh lệnh CREATE TABLE cho tất cả ngôn ngữ người dùng\n\n")

    for l in langs:
        input_file = f"output_user/user-{l}.json"

        if not os.path.exists(input_file):
            print(f"⚠️  File '{input_file}' không tồn tại, bỏ qua.")
            continue

        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        users = data.get("all_item", [])
        if not users:
            print(f"⚠️  Không có user hợp lệ trong '{input_file}', bỏ qua.")
            continue

        # Lấy tất cả các field có trong dữ liệu
        all_fields = set()
        for u in users:
            all_fields.update(u.keys())
        fields_sorted = sorted(list(all_fields))

        # Ghi lệnh CREATE TABLE vào file tổng
        f_all.write(f"-- 🔹 Tạo bảng user_{l}\n")
        f_all.write(f"DROP TABLE IF EXISTS user_{l};\n")
        f_all.write(f"CREATE TABLE user_{l} (\n")
        f_all.write("  id INTEGER PRIMARY KEY AUTOINCREMENT,\n")

        for i, field in enumerate(fields_sorted):
            comma = "," if i < len(fields_sorted) - 1 else ""
            f_all.write(f"  {field} TEXT{comma}\n")

        f_all.write(");\n\n")

print(f"✅ Đã tạo file SQL tổng hợp: {output_all}")
