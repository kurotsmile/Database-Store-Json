import os
import json
import re
import requests

def safe_filename(name: str) -> str:
    """Chuyển app_id thành tên file an toàn."""
    name = name.strip().lower()
    name = re.sub(r"[^\w\s-]", "", name)  # bỏ ký tự đặc biệt
    name = re.sub(r"\s+", "_", name)      # khoảng trắng → "_"
    return name or "unknown"

def download_best_icon(json_file, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_items = data.get("all_item", [])

    for item in all_items:
        app_name = item.get("app_id", "unknown")
        app_safe_name = safe_filename(app_name)
        icons = item.get("icons", {})

        # Ưu tiên lần lượt icon_gg → icon_ms → icon_itch → icon_amazon
        icon_url = (
            icons.get("icon_gg")
            or icons.get("icon_ms")
            or icons.get("icon_itch")
            or icons.get("icon_amazon")
        )

        if icon_url:
            try:
                print(f"⬇️  Đang tải icon cho: {app_name}")
                response = requests.get(icon_url, timeout=10)
                response.raise_for_status()

                # Lấy phần mở rộng ảnh (png, jpg,...)
                ext = os.path.splitext(icon_url.split("?")[0])[1].lower()
                if ext not in [".jpg", ".jpeg", ".png", ".webp", ".bmp"]:
                    ext = ".jpg"

                output_path = os.path.join(output_folder, f"{app_safe_name}{ext}")

                with open(output_path, "wb") as f_out:
                    f_out.write(response.content)

                print(f"✅ Lưu thành công: {output_path}")

            except Exception as e:
                print(f"⚠️  Lỗi tải {app_name}: {e}")
        else:
            print(f"⚠️  Không có icon nào khả dụng cho {app_name}")

    print("\n🎯 Hoàn tất tải tất cả icon khả dụng!")

# ================================
# 🔧 Cấu hình
# ================================
download_best_icon("app_carrotstore.json", "images")
