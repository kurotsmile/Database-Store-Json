import os
import json
from datetime import datetime

langs = ["de", "en", "es", "ja", "pt", "ru", "zh"]
output_path = "sql/users/insert_users.sql"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

def esc(val):
    if val is None:
        return ""
    return str(val).replace("'", "''").strip()

# Mở file 1 lần để ghi tất cả
with open(output_path, "w", encoding="utf-8") as f_out:
    for l in langs:
        input_path = f"output_user/user-{l}.json"
        if not os.path.exists(input_path):
            print(f"⚠️  File '{input_path}' không tồn tại, bỏ qua.")
            continue

        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        users = data.get("all_item", [])
        if not users:
            print(f"⚠️  Không có user trong '{input_path}', bỏ qua.")
            continue

        for u in users:
            # Xử lý logic tự động
            u["lang"] = l
            if not u.get("created_at") or str(u.get("created_at")).strip() == "":
                u["created_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            if "role" not in u or not str(u["role"]).strip():
                u["role"] = "user"

            sql = (
                "INSERT INTO users (address, avatar, created_at, email, lang, name, password, phone, role, sex, status_share, type) "
                f"VALUES ('{esc(u.get('address',''))}', '{esc(u.get('avatar',''))}', "
                f"'{esc(u.get('created_at',''))}', '{esc(u.get('email',''))}', '{esc(u.get('lang',''))}', "
                f"'{esc(u.get('name',''))}', '{esc(u.get('password',''))}', '{esc(u.get('phone',''))}', "
                f"'{esc(u.get('role','user'))}', '{esc(u.get('sex',''))}', '{esc(u.get('status_share',''))}', "
                f"'{esc(u.get('type',''))}');\n"
            )
            f_out.write(sql)

        print(f"✅ Đã thêm {len(users)} user từ '{input_path}' vào '{output_path}'")

print(f"🎯 Hoàn tất! Tất cả dữ liệu user đã được chèn vào: {output_path}")
