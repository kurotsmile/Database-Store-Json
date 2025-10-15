import os
from PIL import Image

def resize_and_crop_center(folder_path, output_folder, size=(300, 300)):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, filename)

            try:
                img = Image.open(img_path)

                # Nếu ảnh có alpha (RGBA, LA, v.v.) → chuyển sang RGB (nền trắng)
                if img.mode in ("RGBA", "LA"):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                elif img.mode != "RGB":
                    img = img.convert("RGB")

                # Tính tỉ lệ scale theo chiều lớn hơn để đảm bảo full 300x300
                img_ratio = img.width / img.height
                target_ratio = size[0] / size[1]

                if img_ratio > target_ratio:
                    # Ảnh ngang → scale theo chiều cao
                    new_height = size[1]
                    new_width = int(new_height * img_ratio)
                else:
                    # Ảnh đứng → scale theo chiều rộng
                    new_width = size[0]
                    new_height = int(new_width / img_ratio)

                # Resize giữ tỉ lệ
                img = img.resize((new_width, new_height), Image.LANCZOS)

                # Crop giữa
                left = (new_width - size[0]) // 2
                top = (new_height - size[1]) // 2
                right = left + size[0]
                bottom = top + size[1]
                img_cropped = img.crop((left, top, right, bottom))

                # Đặt lại tên file .jpg
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.jpg")

                # Lưu ra JPEG chất lượng cao
                img_cropped.save(output_path, "JPEG", quality=95, optimize=True)

                print(f"✅ {filename} → saved as {base_name}.jpg ({size[0]}x{size[1]})")

            except Exception as e:
                print(f"❌ Lỗi xử lý {filename}: {e}")

    print("\n🎯 Hoàn tất resize + crop giữa + lưu .JPG toàn bộ ảnh!")

# ================================
# 🔧 Cấu hình
# ================================
input_folder = "images"           # Thư mục ảnh gốc
output_folder = "output_images"   # Thư mục xuất ảnh
resize_and_crop_center(input_folder, output_folder, (300, 300))
