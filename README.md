# Test_BTGD2

Dự án kiểm thử hệ thống Thông tin Thủy lợi Bến Tre tại [https://thuyloi.opengis.vn/](https://thuyloi.opengis.vn/).

---

## 📋 Giới thiệu

Repository này chứa script kiểm thử tự động và báo cáo kết quả kiểm thử cho hệ thống **WebGIS Thủy lợi Bến Tre** – một ứng dụng bản đồ trực tuyến phục vụ quản lý và cung cấp thông tin ngành thủy lợi tỉnh Bến Tre.

---

## 📁 Cấu trúc thư mục

```
Test_BTGD2/
├── run_tests.py          # Script kiểm thử tự động bằng Selenium
├── test_report.md        # Báo cáo kết quả kiểm thử chi tiết
├── screenshots/          # Hình ảnh chụp màn hình trong quá trình kiểm thử
│   ├── homepage_load_*.png
│   ├── login_page_load_*.png
│   ├── login_form_visible_*.png
│   ├── login_fields_filled_*.png
│   ├── map_page_after_login_*.png
│   ├── dashboard_page_load_*.png
│   ├── news_page_load_*.png
│   ├── homepage_mobile_view_*.png
│   └── thuyloi_testing_session_*.webp  # Video ghi hình phiên kiểm thử
└── README.md
```

---

## 🛠️ Công cụ sử dụng

| Công cụ | Phiên bản | Mục đích |
|---------|-----------|----------|
| Python | 3.12 | Ngôn ngữ lập trình |
| Selenium | 4.44.0 | Tự động hóa trình duyệt |
| Google Chrome | 149+ | Trình duyệt kiểm thử |
| ChromeDriver | Auto | WebDriver cho Chrome |

---

## 🚀 Cách chạy script kiểm thử

### Yêu cầu

- Python 3.12 trở lên
- Google Chrome đã cài đặt
- Cài đặt thư viện Selenium:

```bash
pip install selenium
```

### Thực thi

```bash
python run_tests.py
```

Sau khi chạy, script sẽ:
1. Mở trình duyệt Chrome (chế độ headless)
2. Điều hướng đến trang đăng nhập
3. Đăng nhập bằng tài khoản kiểm thử
4. Chụp màn hình tại từng bước
5. Thu thập console logs của trình duyệt

Kết quả (ảnh chụp màn hình và logs) được lưu vào thư mục `screenshots/`.

---

## 📊 Kết quả kiểm thử

| Chỉ số | Số lượng |
|--------|----------|
| Tổng test case | **8** |
| ✅ Pass | **5** |
| ⚠️ Pass có cảnh báo | **2** |
| ❌ Fail | **1** |
| 🐛 Lỗi phát hiện | **3** |

### Các lỗi chính phát hiện được

| ID | Mức độ | Mô tả |
|----|--------|-------|
| BUG-001 | 🔴 Critical | Lỗi 404 – Lớp WMS vùng tưới tiêu `bentre_vungtuoitieu_v2` không tải được |
| BUG-002 | 🟠 High | Tab "Tin tức" trong menu nội bộ click không phản hồi |
| UX-001 | 🟡 Medium | Form đăng nhập bị ẩn mặc định (accordion), gây nhầm lẫn cho người dùng mới |

Xem chi tiết tại file [test_report.md](test_report.md).

---

## 📅 Thông tin kiểm thử

| | |
|---|---|
| **Ngày kiểm thử** | 15/06/2026 |
| **Tài khoản** | dtlong@vnsc.org.vn |
| **Hệ thống** | https://thuyloi.opengis.vn/ |
| **Tester** | AI Tester – Antigravity IDE |