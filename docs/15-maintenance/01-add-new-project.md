# افزودن پروژه جدید

## 🎓 مفهوم

**افزودن پروژه جدید** = اضافه کردن یک ردیف به `PROJECTS` در اسکریپت Python.

## 🎓 چرا این روش خوب است؟

- **یک منبع:** همه داده در یک جا.
- **خودکار:** Excel و JSON خودکار ساخته می‌شوند.
- **کم‌خطا:** نیازی به ویرایش دستی چند فایل نیست.

## 🛠 گام ۱: باز کردن اسکریپت

```bash
cd ~/Documents/Projects/farhadproject/python-scripts
source venv/bin/activate
code master_data_builder.py
```

## 🛠 گام ۲: پیدا کردن لیست `PROJECTS`

```python
PROJECTS = [
    {
        "project_id": "P-001",
        "slug": "media-building-phase1",
        # ... ۳۰ فیلد
    }
]
```

## 🛠 گام ۳: افزودن رکورد جدید

بعد از `P-001`، یک Object جدید اضافه کن:

```python
PROJECTS = [
    # پروژه اول
    {
        "project_id": "P-001",
        # ...
    },
    # پروژه دوم (جدید)
    {
        "project_id": "P-002",
        "slug": "highway-project-1404",
        "title_fa": "پروژه احداث بزرگراه",
        "title_en": "Highway Construction Project",
        "subtitle_fa": "احداث ۱۵ کیلومتر بزرگراه",
        "client_fa": "کارفرمای دولتی",
        "client_en": "Public Client",
        "contractor_fa": "پیمانکار اصلی",
        "consultant_fa": "مشاور",
        "location_fa": "محرمانه",
        "location_en": "Restricted",
        "area_m2": 0,              # یا مقدار مناسب
        "contract_amount_rial": 500000000000,
        "contract_amount_display_fa": "حدود ۵۰ میلیارد تومان",
        "duration_months": 24,
        "extension_months": 0,
        "total_duration_months": 24,
        "status_fa": "در حال اجرا",
        "status_en": "In Progress",
        "year_start_fa": "سال اول",
        "year_end_fa": "سال دوم",
        "scope_fa": "ابنیه، تأسیسات",
        "blocks": "",
        "total_floors": 0,
        "role_fa": "دفتر فنی، کنترل پروژه",
        "role_en": "Technical Office, Project Controls",
        "key_achievements_fa": "...",
        "cover_image": "/assets/covers/P-002.jpg",
        "is_public": True,
        "is_featured": False,  # پروژه دوم ویژه نیست
    },
]
```

## 🎓 فیلدهای مهم

| فیلد | مقدار | نکته |
|---|---|---|
| `project_id` | یکتا | P-002 |
| `slug` | URL-friendly | فقط حروف کوچک |
| `title_fa` | عنوان فارسی | — |
| `is_featured` | False | فقط یکی True |
| `is_public` | True | برای نمایش |

## 🛠 گام ۴: اجرای اسکریپت

```bash
python master_data_builder.py
```

**خروجی:**

```
✅ فایل Master_Data.xlsx ساخته شد (2 پروژه، 122 فضا)
✅ فایل master_data.json ساخته شد
```

## 🛠 گام ۵: کپی JSON به سایت

```bash
cp master_data.json ../astro-site/src/data/master_data.json
```

**نکته:** JSON باید در پوشه سایت باشد.

## 🛠 گام ۶: تصاویر پروژه جدید

تصاویر پروژه در `public/images/portfolio/` می‌گذاریم. اگر پروژه دوم تصاویر خودش را دارد:

```
astro-site/public/images/portfolio/
├── P-001/
│   ├── project-exterior.jpg
│   └── ...
└── P-002/
    ├── project-exterior.jpg
    └── ...
```

**نکته:** می‌توانی هم‌اکنون همه تصاویر در یک پوشه نگه داری. برای سادگی، نام پروژه را در نام فایل بگذار.

## 🛠 گام ۷: تست محلی

```bash
cd ../astro-site
npm run dev
```

برو به `http://localhost:4321/portfolio`.

**باید ببینی:** دو کارت پروژه.

روی کارت جدید کلیک کن. **صفحه داینامیک خودکار ساخته می‌شود.**

## 🛠 گام ۸: Build

```bash
npm run build
```

**خروجی:** `dist/portfolio/highway-project-1404/index.html`.

## 🛠 گام ۹: Commit و Push

```bash
cd ~/Documents/Projects/farhadproject
git add .
git commit -m "Add new project: Highway 1404"
git push
```

**Auto Deploy Liara:** ۲–۵ دقیقه بعد، سایت آپدیت می‌شود.

## 🎓 چک‌لیست افزودن پروژه

- [ ] رکورد در `PROJECTS`
- [ ] `project_id` یکتا
- [ ] `slug` یکتا
- [ ] `is_featured = False`
- [ ] اجرای `master_data_builder.py`
- [ ] کپی JSON به سایت
- [ ] تصاویر در پوشه
- [ ] تست محلی
- [ ] Commit + Push

## 🎓 محدودیت‌های فعلی

**در Componentهای پرتفولیو، داده ثابت است.** مثلاً `Zoning.astro` برای پروژه فعلی نوشته شده.

**اگر پروژه جدید کاملاً متفاوت باشد:**

- یا باید Component جدید بسازی.
- یا Component را داینامیک کنی.

**برای اولین نسخه:** همان ۱۵ بخش برای همه پروژه‌ها.

**برای آینده:** می‌توانی `sections` را در `PROJECTS` تعریف کنی و هر پروژه بخش‌های خودش را داشته باشد.

## 🛑 عیب‌یابی

### مشکل ۱: پروژه دوم در سایت نمایش داده نمی‌شود

**علت:** JSON کپی نشده.

**راه‌حل:**

```bash
cp master_data.json ../astro-site/src/data/master_data.json
```

### مشکل ۲: صفحه داینامیک ۴۰۴ می‌دهد

**علت:** `getStaticPaths` داده جدید را نمی‌بیند.

**راه‌حل:** Dev Server را Restart کن.

### مشکل ۳: Slug تکراری

**علت:** `slug` یکتا نیست.

**راه‌حل:** Slug جدید بگذار.

## 🎓 در پروژه ما

پروژه اول (`P-001`) ساخته شد. برای پروژه‌های بعدی، همین مراحل را تکرار می‌کنی.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | باز کردن اسکریپت |
| ۲ | افزودن رکورد در `PROJECTS` |
| ۳ | `python master_data_builder.py` |
| ۴ | کپی JSON |
| ۵ | تصاویر |
| ۶ | تست محلی |
| ۷ | Commit + Push |

## آماده‌ای؟ برو به `02-add-new-section.md`.