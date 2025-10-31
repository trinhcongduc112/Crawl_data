# Hướng Dẫn Import Release Notes vào Odoo

## Vấn đề hiện tại

Changelog có nhiều link trỏ tới `https://docs.abivin.com/changelog/...` nhưng cần trỏ tới các article trên Odoo (ví dụ: `https://test018.odoo.com/odoo/articles/346`)

## Giải pháp

Tôi đã tạo 2 scripts:

### 1. `import_release_notes_to_odoo.py`
- Import tất cả release notes vào Odoo
- Upload ảnh lên Odoo
- Tạo mapping từ title → Odoo article ID
- Lưu mapping vào `release_notes/odoo_article_mapping.json`

### 2. `update_changelog_with_odoo_links.py`
- Load mapping từ file JSON
- Cập nhật links trong changelog.json
- Chuyển từ Abivin URLs sang Odoo URLs

## Cách chạy

### Bước 1: Import release notes
```bash
python import_release_notes_to_odoo.py
```

Script sẽ:
1. Kết nối với Odoo (test018.odoo.com)
2. Import từng release note
3. Upload ảnh
4. Lưu mapping: `title` → `article_id`

### Bước 2: Update changelog
```bash
python update_changelog_with_odoo_links.py
```

Script sẽ:
1. Load mapping từ file JSON
2. Tìm và thay thế links Abivin bằng Odoo URLs
3. Lưu lại changelog.json

## Cấu hình Odoo

Script sử dụng cấu hình:
- **URL**: https://test018.odoo.com
- **DB**: test018
- **User**: trinhcongduc0112@gmail.com
- **API Key**: (đã được hardcode trong script)

## Mapping File

Sau khi chạy import, file `release_notes/odoo_article_mapping.json` sẽ có dạng:

```json
{
  "Jan 04, 2023 - Release Note": 345,
  "Jan 11, 2023 - Release Note": 346,
  ...
}
```

## Kết quả mong đợi

Sau khi hoàn tất, changelog.json sẽ có links dạng:
```html
<a href="https://test018.odoo.com/odoo/articles/346">Dec 28, 2022 - Release Notes</a>
```

Thay vì:
```html
<a href="https://docs.abivin.com/changelog/dec-28-2022-release-notes">Dec 28, 2022 - Release Notes</a>
```

## Lưu ý

- Các entries chưa được scrape (ví dụ entries 2022 cũ) sẽ không có trong mapping
- Các links đó sẽ vẫn trỏ tới Abivin hoặc bị disable
- Cần scrape thêm để có đầy đủ data

## Troubleshooting

### Lỗi connection timeout
- Kiểm tra network/firewall
- Thử chạy từ network khác

### Không tìm thấy mapping
- Đảm bảo đã chạy import trước
- Kiểm tra file `odoo_article_mapping.json` tồn tại

### Links không được update
- Kiểm tra title trong changelog khớp với title trong mapping
- Có thể cần manual mapping cho một số entries


