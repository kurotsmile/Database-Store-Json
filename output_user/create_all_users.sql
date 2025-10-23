-- 📘 Tự động sinh lệnh CREATE TABLE cho tất cả ngôn ngữ người dùng

-- 🔹 Tạo bảng user_de
DROP TABLE IF EXISTS user_de;
CREATE TABLE user_de (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_en
DROP TABLE IF EXISTS user_en;
CREATE TABLE user_en (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  id TEXT,
  id_doc TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_es
DROP TABLE IF EXISTS user_es;
CREATE TABLE user_es (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  id TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_ja
DROP TABLE IF EXISTS user_ja;
CREATE TABLE user_ja (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_pt
DROP TABLE IF EXISTS user_pt;
CREATE TABLE user_pt (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_ru
DROP TABLE IF EXISTS user_ru;
CREATE TABLE user_ru (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

-- 🔹 Tạo bảng user_zh
DROP TABLE IF EXISTS user_zh;
CREATE TABLE user_zh (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT,
  avatar TEXT,
  created_at TEXT,
  email TEXT,
  lang TEXT,
  name TEXT,
  password TEXT,
  phone TEXT,
  role TEXT,
  sex TEXT,
  status_share TEXT,
  type TEXT
);

