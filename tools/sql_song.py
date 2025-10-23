import json
langs=["ar","cs","da","de","en","es","fi","fr","id","it","ja","ko","nl","pl","pt","ru","th","tr","zh","vi"]
for l in langs:
    # === CẤU HÌNH ===
    input_json = "output_songs/song-"+l+".json"          # Tên file JSON đầu vào
    output_sql = "sql/songs/insert_song_"+l+".sql"    # Tên file SQL đầu ra
    table_name = "song"                  # Tên bảng D1

    # === HÀM XỬ LÝ CHUỖI ===
    def escape_sql(value: str) -> str:
        if value is None:
            return ""
        # Thay ' bằng '' và xuống dòng thành \n để không lỗi SQL
        return str(value).replace("'", "''").replace("\n", "\\n")

    # === ĐỌC FILE JSON ===
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_items = data.get("all_item", [])
    if not all_items:
        raise ValueError("Không tìm thấy dữ liệu trong 'all_item'.")

    # === GHI FILE SQL ===
    with open(output_sql, "w", encoding="utf-8") as f:
        for item in all_items:
            fields = [
                "id", "name", "artist", "album", "genre", "lang",
                "year", "date", "publishedAt", "link_ytb",
                "mp3", "avatar", "lyrics"
            ]
            values = [escape_sql(item.get(field, "")) for field in fields]

            sql = f"INSERT OR REPLACE INTO {table_name} ({','.join(fields)}) VALUES ('" + "','".join(values) + "');\n"
            f.write(sql)

    print(f"✅ Đã tạo file SQL: {output_sql}")
