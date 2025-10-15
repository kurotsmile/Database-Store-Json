import os
from PIL import Image

def resize_and_crop_center(folder_path, output_folder, size=(300, 300)):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)

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

            # Resize ảnh (vẫn giữ tỉ lệ)
            img = img.resize((new_width, new_height), Image.LANCZOS)

            # Crop từ giữa
            left = (new_width - size[0]) // 2
            top = (new_height - size[1]) // 2
            right = left + size[0]
            bottom = top + size[1]
            img_cropped = img.crop((left, top, right, bottom))

            # Lưu
            output_path = os.path.join(output_folder, filename)
            img_cropped.save(output_path)

            print(f"✅ {filename} → resized & center-cropped to {size[0]}x{size[1]}")

    print("\n🎯 Hoàn tất resize + crop giữa toàn bộ ảnh!")

# ================================
# 🔧 Cấu hình
# ================================
input_folder = "images"     # thư mục chứa ảnh gốc
output_folder = "output_images"   # thư mục lưu ảnh sau xử lý
resize_and_crop_center(input_folder, output_folder, (300, 300))
