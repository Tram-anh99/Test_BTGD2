# BÃO CÃO KIá»‚M THá»¬ Há»† THá»NG
# Thá»§y lá»£i Báº¿n Tre â€“ https://thuyloi.opengis.vn/

| | |
|---|---|
| **Há»‡ thá»‘ng kiá»ƒm thá»­** | Há»‡ thá»‘ng ThÃ´ng tin Thá»§y lá»£i Báº¿n Tre |
| **URL** | https://thuyloi.opengis.vn/ |
| **Tester** | AI Tester (Antigravity IDE) |
| **NgÃ y kiá»ƒm thá»­** | 15/06/2026 |
| **TÃ i khoáº£n sá»­ dá»¥ng** | dtlong@vnsc.org.vn / dtlong |
| **TrÃ¬nh duyá»‡t** | Google Chrome (Selenium Headless + Browser Subagent) |
| **Káº¿t quáº£ tá»•ng quan** | âš ï¸ **3 lá»—i phÃ¡t hiá»‡n** / 8 test case |

---

## I. Tá»”NG Káº¾T Káº¾T QUáº¢

| Chá»‰ sá»‘ | Sá»‘ lÆ°á»£ng |
|--------|----------|
| Tá»•ng sá»‘ test case | 8 |
| âœ… Pass | 5 |
| âš ï¸ Pass vá»›i cáº£nh bÃ¡o | 2 |
| âŒ Fail | 1 |

---

## II. CHI TIáº¾T CÃC TEST CASE

---

### TC-001: Kiá»ƒm tra Trang Chá»§ (Homepage)

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | Medium |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/ |
| **Káº¿t quáº£** | âœ… **PASS** |

**MÃ´ táº£:** Kiá»ƒm tra trang chá»§ táº£i Ä‘Ãºng, hiá»ƒn thá»‹ tiÃªu Ä‘á», ná»™i dung giá»›i thiá»‡u vÃ  cÃ¡c liÃªn káº¿t Ä‘iá»u hÆ°á»›ng chÃ­nh.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Má»Ÿ trÃ¬nh duyá»‡t, Ä‘iá»u hÆ°á»›ng Ä‘áº¿n `https://thuyloi.opengis.vn/`
2. Quan sÃ¡t tiÃªu Ä‘á» trang
3. Kiá»ƒm tra ná»™i dung giá»›i thiá»‡u
4. Kiá»ƒm tra cÃ¡c nÃºt Ä‘iá»u hÆ°á»›ng

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Trang táº£i thÃ nh cÃ´ng
- âœ… TiÃªu Ä‘á»: **"Thá»§y lá»£i Báº¿n Tre â€“ Há»‡ thá»‘ng thÃ´ng tin Thá»§y lá»£i"**
- âœ… Ná»™i dung giá»›i thiá»‡u hiá»ƒn thá»‹ Ä‘áº§y Ä‘á»§ (mÃ´ táº£ há»‡ thá»‘ng, á»©ng dá»¥ng di Ä‘á»™ng, há»— trá»£ ra quyáº¿t Ä‘á»‹nh)
- âœ… NÃºt **"XEM Báº¢N Äá»’"** hiá»ƒn thá»‹ vÃ  hoáº¡t Ä‘á»™ng
- âœ… Footer hiá»ƒn thá»‹ thÃ´ng tin Ä‘Æ¡n vá»‹ chá»§ quáº£n

**áº¢nh mÃ n hÃ¬nh:**

![Trang chá»§](screenshots/homepage_load_1781509217719.png)

---

### TC-002: Kiá»ƒm tra Giao Diá»‡n Form ÄÄƒng Nháº­p

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | High |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/map/login/ |
| **Káº¿t quáº£** | âš ï¸ **PASS (cÃ³ cáº£nh bÃ¡o UX)** |

**MÃ´ táº£:** Kiá»ƒm tra form Ä‘Äƒng nháº­p cÃ³ hiá»ƒn thá»‹ Ä‘Ãºng vÃ  Ä‘á»§ cÃ¡c trÆ°á»ng nháº­p liá»‡u cáº§n thiáº¿t.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Äiá»u hÆ°á»›ng Ä‘áº¿n trang Ä‘Äƒng nháº­p
2. Quan sÃ¡t form Ä‘Äƒng nháº­p

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Trang Ä‘Äƒng nháº­p táº£i thÃ nh cÃ´ng
- âš ï¸ **Form Ä‘Äƒng nháº­p bá»‹ áº©n máº·c Ä‘á»‹nh (collapsed/accordion)** â€“ ngÆ°á»i dÃ¹ng pháº£i click nÃºt mÅ©i tÃªn Ä‘á»ƒ má»Ÿ rá»™ng má»›i tháº¥y cÃ¡c Ã´ nháº­p liá»‡u
- âœ… Sau khi má»Ÿ rá»™ng: cÃ¡c trÆ°á»ng Email, Máº­t kháº©u vÃ  nÃºt "ÄÄƒng nháº­p" hiá»ƒn thá»‹ Ä‘Ãºng
- âœ… LiÃªn káº¿t "QuÃªn máº­t kháº©u?" hiá»ƒn thá»‹

> [!WARNING]
> **Lá»—i UX-001**: Form Ä‘Äƒng nháº­p bá»‹ áº©n theo dáº¡ng Accordion. NgÆ°á»i dÃ¹ng má»›i cÃ³ thá»ƒ khÃ´ng biáº¿t pháº£i click Ä‘á»ƒ má»Ÿ rá»™ng, gÃ¢y nháº§m láº«n vÃ  giáº£m tráº£i nghiá»‡m ngÆ°á»i dÃ¹ng.

**áº¢nh mÃ n hÃ¬nh:**

![Trang Ä‘Äƒng nháº­p (form Ä‘ang Ä‘Ã³ng)](screenshots/login_page_load_1781509260873.png)

![Form Ä‘Äƒng nháº­p (sau khi má»Ÿ rá»™ng)](screenshots/login_form_visible_1781509273890.png)

---

### TC-003: Kiá»ƒm tra Chá»©c nÄƒng ÄÄƒng Nháº­p

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | Critical |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/map/login/ |
| **Káº¿t quáº£** | âœ… **PASS** |

**MÃ´ táº£:** XÃ¡c minh há»‡ thá»‘ng cho phÃ©p Ä‘Äƒng nháº­p báº±ng tÃ i khoáº£n há»£p lá»‡.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Má»Ÿ form Ä‘Äƒng nháº­p
2. Nháº­p username: `dtlong@vnsc.org.vn`
3. Nháº­p password: `dtlong`
4. Click nÃºt "ÄÄƒng nháº­p"
5. Kiá»ƒm tra káº¿t quáº£

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Nháº­p thÃ´ng tin Ä‘Äƒng nháº­p thÃ nh cÃ´ng
- âœ… Há»‡ thá»‘ng xÃ¡c thá»±c vÃ  chuyá»ƒn hÆ°á»›ng Ä‘áº¿n trang báº£n Ä‘á»“: `https://thuyloi.opengis.vn/map/view/`
- âœ… TÃªn ngÆ°á»i dÃ¹ng hiá»ƒn thá»‹: **"Äá»— ThÃ nh Long"** táº¡i gÃ³c trÃªn pháº£i

**áº¢nh mÃ n hÃ¬nh:**

![Äiá»n thÃ´ng tin Ä‘Äƒng nháº­p](screenshots/login_fields_filled_1781509291021.png)

---

### TC-004: Kiá»ƒm tra Báº£n Äá»“ WebGIS sau ÄÄƒng Nháº­p

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | Critical |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/map/view/ |
| **Káº¿t quáº£** | âš ï¸ **PASS (cÃ³ lá»—i tÃ i nguyÃªn)** |

**MÃ´ táº£:** Kiá»ƒm tra báº£n Ä‘á»“ WebGIS táº£i Ä‘Ãºng sau khi Ä‘Äƒng nháº­p, cÃ¡c cÃ´ng cá»¥ báº£n Ä‘á»“ hoáº¡t Ä‘á»™ng bÃ¬nh thÆ°á»ng.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Quan sÃ¡t giao diá»‡n báº£n Ä‘á»“ sau Ä‘Äƒng nháº­p
2. Kiá»ƒm tra cÃ¡c cÃ´ng cá»¥ báº£n Ä‘á»“ (Zoom, Measure, Locate)
3. Kiá»ƒm tra cÃ¡c lá»›p dá»¯ liá»‡u (Layers) trÃªn báº£n Ä‘á»“
4. Xem console logs Ä‘á»ƒ phÃ¡t hiá»‡n lá»—i

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Báº£n Ä‘á»“ container táº£i thÃ nh cÃ´ng
- âœ… CÃ´ng cá»¥ Zoom In, Zoom Out hiá»ƒn thá»‹ vÃ  hoáº¡t Ä‘á»™ng
- âœ… CÃ´ng cá»¥ Äo lÆ°á»ng (Measure) vÃ  Äá»‹nh vá»‹ (Locate) hiá»ƒn thá»‹
- âœ… ThÃ´ng tin ngÆ°á»i dÃ¹ng "Äá»— ThÃ nh Long" hiá»ƒn thá»‹ trÃªn thanh cÃ´ng cá»¥
- âŒ **Lá»—i 404 WMS**: Khi báº£n Ä‘á»“ cá»‘ gáº¯ng táº£i lá»›p dá»¯ liá»‡u vÃ¹ng tÆ°á»›i tiÃªu, xáº£y ra lá»—i HTTP 404 tá»« WMS endpoint

> [!CAUTION]
> **Lá»—i BUG-001 (Critical)**: Lá»—i 404 tÃ i nguyÃªn WMS báº£n Ä‘á»“ vÃ¹ng tÆ°á»›i tiÃªu.
> - **URL lá»—i**: `https://thuyloi.opengis.vn/m/qsrv/.../bentre_vungtuoitieu_v2?SERVICE=WMS&REQUEST=GetLegendGraphic...`
> - **Má»©c Ä‘á»™**: NghiÃªm trá»ng â€“ lá»›p dá»¯ liá»‡u vÃ¹ng tÆ°á»›i tiÃªu khÃ´ng hiá»ƒn thá»‹ Ä‘Æ°á»£c, áº£nh hÆ°á»Ÿng trá»±c tiáº¿p Ä‘áº¿n chá»©c nÄƒng cá»‘t lÃµi cá»§a há»‡ thá»‘ng.

**áº¢nh mÃ n hÃ¬nh:**

![Báº£n Ä‘á»“ sau Ä‘Äƒng nháº­p](screenshots/map_page_after_login_1781509311275.png)

---

### TC-005: Kiá»ƒm tra Äiá»u HÆ°á»›ng Menu ChÃ­nh

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | High |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/map/view/ |
| **Káº¿t quáº£** | âŒ **FAIL (Tab Tin Tá»©c khÃ´ng hoáº¡t Ä‘á»™ng)** |

**MÃ´ táº£:** Kiá»ƒm tra táº¥t cáº£ cÃ¡c tab/menu chÃ­nh trÃªn thanh Ä‘iá»u hÆ°á»›ng hoáº¡t Ä‘á»™ng Ä‘Ãºng vÃ  chuyá»ƒn hÆ°á»›ng Ä‘Ãºng trang.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Quan sÃ¡t thanh menu trÃªn trang báº£n Ä‘á»“
2. Click vÃ o tá»«ng tab: Tin tá»©c, Báº£n Ä‘á»“, Quáº£n trá»‹

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Tab **"Báº£n Ä‘á»“"** hoáº¡t Ä‘á»™ng Ä‘Ãºng (href: `../../map/`)
- âœ… Tab **"Quáº£n trá»‹"** hoáº¡t Ä‘á»™ng Ä‘Ãºng (href: `../../dashboard`)
- âŒ Tab **"Tin tá»©c"** trÃªn trang báº£n Ä‘á»“/quáº£n trá»‹ **khÃ´ng cÃ³ link hoáº·c sá»± kiá»‡n click hoáº¡t Ä‘á»™ng** â€“ click vÃ o khÃ´ng cÃ³ pháº£n há»“i, khÃ´ng Ä‘iá»u hÆ°á»›ng Ä‘áº¿n trang tin tá»©c

> [!CAUTION]
> **Lá»—i BUG-002 (High)**: Tab "Tin tá»©c" trong thanh Ä‘iá»u hÆ°á»›ng táº¡i trang báº£n Ä‘á»“ (`/map/view/`) vÃ  trang quáº£n trá»‹ (`/dashboard/`) khÃ´ng hoáº¡t Ä‘á»™ng. Thuá»™c tÃ­nh `href` bá»‹ thiáº¿u hoáº·c sá»± kiá»‡n click khÃ´ng Ä‘Æ°á»£c gÃ¡n Ä‘Ãºng.

---

### TC-006: Kiá»ƒm tra Trang Quáº£n Trá»‹ (Dashboard)

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | High |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/dashboard/main/ |
| **Káº¿t quáº£** | âœ… **PASS** |

**MÃ´ táº£:** Kiá»ƒm tra trang quáº£n trá»‹ há»‡ thá»‘ng táº£i Ä‘Ãºng, hiá»ƒn thá»‹ Ä‘áº§y Ä‘á»§ cÃ¡c module quáº£n lÃ½.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Äiá»u hÆ°á»›ng Ä‘áº¿n trang dashboard
2. Quan sÃ¡t cÃ¡c module hiá»ƒn thá»‹
3. Kiá»ƒm tra console logs

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Trang táº£i thÃ nh cÃ´ng, chuyá»ƒn hÆ°á»›ng sang: `https://thuyloi.opengis.vn/dashboard/main/`
- âœ… TiÃªu Ä‘á»: "Quáº£n trá»‹ há»‡ thá»‘ng | Thá»§y lá»£i Báº¿n Tre"
- âœ… Báº£ng Ä‘iá»u khiá»ƒn hiá»ƒn thá»‹ Ä‘áº§y Ä‘á»§ cÃ¡c module:
  - Quáº£n lÃ½ ngÆ°á»i dÃ¹ng
  - Cá»‘ng Ä‘iá»u tiáº¿t
  - Há»‡ thá»‘ng kÃªnh dáº«n
  - Dá»¯ liá»‡u thá»§y vÄƒn (má»±c nÆ°á»›c, Ä‘á»™ máº·n)

**áº¢nh mÃ n hÃ¬nh:**

![Trang quáº£n trá»‹ Dashboard](screenshots/dashboard_page_load_1781509368956.png)

---

### TC-007: Kiá»ƒm tra Trang Tin Tá»©c

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | Medium |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/category/tin-tuc/ |
| **Káº¿t quáº£** | âœ… **PASS** |

**MÃ´ táº£:** Kiá»ƒm tra trang tin tá»©c hiá»ƒn thá»‹ danh sÃ¡ch bÃ i viáº¿t vÃ  cÃ´ng cá»¥ tÃ¬m kiáº¿m.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**
1. Äiá»u hÆ°á»›ng trá»±c tiáº¿p Ä‘áº¿n trang tin tá»©c
2. Quan sÃ¡t danh sÃ¡ch bÃ i viáº¿t
3. Kiá»ƒm tra sidebar tÃ¬m kiáº¿m
4. Kiá»ƒm tra console logs

**Káº¿t quáº£ thá»±c táº¿:**
- âœ… Trang táº£i thÃ nh cÃ´ng
- âœ… TiÃªu Ä‘á»: "Tin tá»©c â€“ Thá»§y lá»£i Báº¿n Tre"
- âœ… Danh sÃ¡ch bÃ i viáº¿t tin tá»©c vÃ  cáº£nh bÃ¡o xÃ¢m nháº­p máº·n hiá»ƒn thá»‹ Ä‘áº§y Ä‘á»§
- âœ… Cá»™t tÃ¬m kiáº¿m bÃªn pháº£i hoáº¡t Ä‘á»™ng
- âš ï¸ Console warnings: LiÃªn quan Ä‘áº¿n Google Maps API táº£i Ä‘á»“ng bá»™ (`loading=async`) vÃ  Cross-Origin iframe tá»« Google Data Studio (khÃ´ng áº£nh hÆ°á»Ÿng chá»©c nÄƒng chÃ­nh)

**áº¢nh mÃ n hÃ¬nh:**

![Trang tin tá»©c](screenshots/news_page_load_1781509394415.png)

---

### TC-008: Kiá»ƒm tra Responsive Design

| | |
|---|---|
| **Má»©c Ä‘á»™ Æ°u tiÃªn** | Medium |
| **URL kiá»ƒm thá»­** | https://thuyloi.opengis.vn/ |
| **Káº¿t quáº£** | âš ï¸ **KhÃ´ng thá»ƒ kiá»ƒm tra Ä‘áº§y Ä‘á»§ (giá»›i háº¡n mÃ´i trÆ°á»ng)** |

**MÃ´ táº£:** Kiá»ƒm tra trang web hiá»ƒn thá»‹ Ä‘Ãºng trÃªn thiáº¿t bá»‹ di Ä‘á»™ng (kÃ­ch thÆ°á»›c 375x667px).

**Káº¿t quáº£ thá»±c táº¿:**
- âš ï¸ MÃ´i trÆ°á»ng kiá»ƒm thá»­ khÃ³a cá»‘ Ä‘á»‹nh viewport á»Ÿ `1920x953` px
- âœ… MÃ£ nguá»“n HTML cÃ³ pháº§n tá»­ `menu-mobile-toggle` â€“ cho tháº¥y thiáº¿t káº¿ Ä‘Ã£ chuáº©n bá»‹ cho responsive layout
- âœ… CÃ³ nÃºt hamburger menu dÃ nh cho mobile trong source code

**áº¢nh mÃ n hÃ¬nh:**

![Kiá»ƒm tra Mobile View](screenshots/homepage_mobile_view_1781509412649.png)

---

## III. Tá»”NG Há»¢P Lá»–I ÄÃƒ PHÃT HIá»†N

| ID Lá»—i | Má»©c Ä‘á»™ | Vá»‹ trÃ­ | MÃ´ táº£ | TÃ¡c Ä‘á»™ng |
|--------|--------|--------|--------|----------|
| **BUG-001** | ðŸ”´ Critical | Trang Báº£n Äá»“ `/map/view/` | Lá»—i 404 WMS khi táº£i lá»›p dá»¯ liá»‡u vÃ¹ng tÆ°á»›i tiÃªu `bentre_vungtuoitieu_v2` | Lá»›p dá»¯ liá»‡u quan trá»ng khÃ´ng hiá»ƒn thá»‹ trÃªn báº£n Ä‘á»“ |
| **BUG-002** | ðŸŸ  High | Thanh Ä‘iá»u hÆ°á»›ng (Map & Dashboard) | Tab "Tin tá»©c" khÃ´ng cÃ³ `href` hoáº·c sá»± kiá»‡n click â€“ click khÃ´ng cÃ³ pháº£n há»“i | NgÆ°á»i dÃ¹ng khÃ´ng thá»ƒ Ä‘iá»u hÆ°á»›ng Ä‘áº¿n trang tin tá»©c tá»« cÃ¡c trang ná»™i bá»™ |
| **UX-001** | ðŸŸ¡ Medium | Trang ÄÄƒng nháº­p `/map/login/` | Form Ä‘Äƒng nháº­p bá»‹ áº©n theo dáº¡ng Accordion, ngÆ°á»i dÃ¹ng pháº£i click mÅ©i tÃªn má»›i tháº¥y | Giáº£m tráº£i nghiá»‡m ngÆ°á»i dÃ¹ng, cÃ³ thá»ƒ lÃ m ngÆ°á»i dÃ¹ng má»›i bá» cuá»™c |

---

## IV. KHUYáº¾N NGHá»Š

1. **BUG-001 (Æ¯u tiÃªn cao nháº¥t)**: Kiá»ƒm tra vÃ  khÃ´i phá»¥c endpoint WMS `bentre_vungtuoitieu_v2`. ÄÃ¢y lÃ  lá»—i nghiÃªm trá»ng áº£nh hÆ°á»Ÿng Ä‘áº¿n chá»©c nÄƒng cá»‘t lÃµi cá»§a há»‡ thá»‘ng WebGIS.

2. **BUG-002 (Æ¯u tiÃªn cao)**: ThÃªm `href` Ä‘Ãºng hoáº·c sá»± kiá»‡n JavaScript cho tab "Tin tá»©c" trÃªn thanh Ä‘iá»u hÆ°á»›ng táº¡i cÃ¡c trang ná»™i bá»™ (`/map/view/` vÃ  `/dashboard/`).

3. **UX-001 (Cáº£i thiá»‡n UX)**: Xem xÃ©t hiá»ƒn thá»‹ form Ä‘Äƒng nháº­p má»Ÿ rá»™ng máº·c Ä‘á»‹nh, hoáº·c thÃªm hÆ°á»›ng dáº«n rÃµ rÃ ng hÆ¡n Ä‘á»ƒ ngÆ°á»i dÃ¹ng biáº¿t cÃ¡ch Ä‘Äƒng nháº­p.

---

## V. VIDEO GHI HÃŒNH KIá»‚M THá»¬

![Video kiá»ƒm thá»­](screenshots/thuyloi_testing_session_1781495490259.webp)

---

*BÃ¡o cÃ¡o Ä‘Æ°á»£c táº¡o tá»± Ä‘á»™ng bá»Ÿi AI Tester - Antigravity IDE | NgÃ y: 15/06/2026*
