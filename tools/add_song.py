import json
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext

# ======== Hàm xử lý JSON ========
def add_song_to_json(song_data, filename="song.json"):
    try:
        # Đọc file hiện tại (nếu có)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"all_item": []}

        # Thêm bài hát mới
        data["all_item"].append(song_data)

        # Ghi lại file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        messagebox.showinfo("✅ Thành công", f"Đã thêm bài hát '{song_data['name']}' vào {filename}")
    except Exception as e:
        messagebox.showerror("❌ Lỗi", str(e))


# ======== Giao diện GUI ========
root = tk.Tk()
root.title("🎵 Song JSON Editor")
root.geometry("600x700")
root.configure(bg="#f9f9f9")

# Tạo các trường nhập liệu
fields = {
    "name": "Tên bài hát",
    "artist": "Ca sĩ",
    "album": "Album",
    "year": "Năm",
    "genre": "Thể loại",
    "lang": "Ngôn ngữ (vi, en, ko...)",
    "mp3": "Link MP3",
    "avatar": "Ảnh đại diện",
    "link_ytb": "Link YouTube",
    "date": "Ngày thêm (VD: 2023-10-13)"
}

entries = {}

frame = tk.Frame(root, bg="#f9f9f9")
frame.pack(padx=15, pady=10, fill="both", expand=True)

for key, label in fields.items():
    tk.Label(frame, text=label, bg="#f9f9f9", anchor="w").pack(fill="x", pady=(8, 0))
    entry = tk.Entry(frame, width=70)
    entry.pack(pady=2)
    entries[key] = entry

# Lyrics (dạng dài)
tk.Label(frame, text="Lời bài hát (HTML / text):", bg="#f9f9f9", anchor="w").pack(fill="x", pady=(8, 0))
lyrics_box = scrolledtext.ScrolledText(frame, height=10, width=70)
lyrics_box.pack(pady=4)

# Chọn file JSON đầu vào
def choose_file():
    file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file:
        filename_var.set(file)

filename_var = tk.StringVar(value="song.json")
tk.Label(frame, text="File JSON:", bg="#f9f9f9", anchor="w").pack(fill="x", pady=(10, 0))
file_entry = tk.Entry(frame, textvariable=filename_var, width=60)
file_entry.pack(side="left", padx=(0, 5))
tk.Button(frame, text="Chọn file", command=choose_file, bg="#ddd").pack(side="left")

# Nút thêm bài hát
def on_submit():
    song = {key: entries[key].get().strip() for key in entries}
    song["lyrics"] = lyrics_box.get("1.0", tk.END).strip()

    if not song["name"] or not song["artist"]:
        messagebox.showwarning("⚠️ Thiếu thông tin", "Vui lòng nhập ít nhất Tên bài hát và Ca sĩ.")
        return

    add_song_to_json(song, filename_var.get())

tk.Button(root, text="💾 Thêm bài hát vào JSON", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=15, ipadx=10, ipady=5)

root.mainloop()
