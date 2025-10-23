import os
import json
from datetime import datetime

langs = ["ar","cs","da","de","en","es","fi","fr","id","it","ja","ko","nl","pl","pt","ru","th","tr","vi","zh"]

for l in langs:
    input_file = "user-" + l + ".json"
    output_file = "output_user/user-" + l + ".json"

    if not os.path.exists(input_file):
        print(f"⚠️  File '{input_file}' không tồn tại, bỏ qua.")
        continue

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = data.get("all_item", [])
    filtered_users = []

    for user in users:
        avatar = user.get("avatar", "")
        email = user.get("email", "")

        # Bỏ qua user trống avatar + email
        if not email.strip():
            continue

        # Xử lý address nếu là object
        addr = user.get("address")
        if isinstance(addr, dict):
            user["address"] = (addr.get("name") or "").strip()
        elif addr is None:
            user["address"] = ""

        # Xóa trường không cần thiết
        user.pop("id_import", None)
        user.pop("backup_contact", None)

        # Nếu có trường 'date_create' thì đổi tên thành 'created_at'
        if "date_create" in user:
            # Nếu giá trị rỗng hoặc None thì gán ngày hiện tại
            if not user["date_create"] or str(user["date_create"]).strip() == "":
                user["created_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            else:
                user["created_at"] = user["date_create"]

            # Xóa trường cũ
            del user["date_create"]
        else:
            # Nếu không có thì thêm 'created_at' mới
            user["created_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        if "role" not in user or not str(user["role"]).strip():
            user["role"] = "user"
            
        if "type" not in user or not str(user["type"]).strip():
            user["type"] = "basic"

        filtered_users.append(user)

    # Ghi ra file JSON mới
    os.makedirs("output_user", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"all_item": filtered_users}, f, ensure_ascii=False, indent=2)

    print(f"✅ [{l}] Đã xử lý {len(filtered_users)} user hợp lệ, lưu vào '{output_file}'")
