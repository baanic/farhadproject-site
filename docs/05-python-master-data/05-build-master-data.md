# ساخت Master Data

## 🎓 مفهوم

حالا که ساختار را می‌دانی، به کد واقعی `master_data_builder.py` نگاه می‌کنیم.

## 🎓 ساختار کلی اسکریپت

```python
# master_data_builder.py

# ۱. Import کتابخانه‌ها
import json
import pandas as pd
from datetime import datetime

# ۲. تنظیمات
VERSION = "1.0.0"
BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M")

# ۳. داده‌ها
PROJECTS = [...]
SPACES_RAW = [...]
ACOUSTIC_LAYERS = [...]
# ... ۲۳ بخش دیگر

# ۴. توابع کمکی
def enrich_spaces(spaces_raw):
    ...

# ۵. توابع ساخت فایل
def build_excel(filename="Master_Data.xlsx"):
    ...

def build_json(filename="master_data.json"):
    ...

# ۶. اجرا
if __name__ == "__main__":
    build_excel()
    build_json()
```

## 🛠 بخش ۱: Import

```python
import json
import pandas as pd
from datetime import datetime
```

| Import | کاربرد |
|---|---|
| `json` | کتابخانه استاندارد برای JSON |
| `pandas as pd` | پردازش داده (با نام کوتاه) |
| `from datetime import datetime` | کار با تاریخ |

**نکته:** `import pandas as pd` یعنی «pandas را با نام `pd` استفاده کن». یک استاندارد.

## 🛠 بخش ۲: تنظیمات

```python
VERSION = "1.0.0"
BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M")
```

**متغیرهای سراسری** (Global). با حروف بزرگ، نشانه **ثابت** (Constant).

**`strftime` چیست؟**

تابع فرمت‌دهی زمان. `%Y-%m-%d %H:%M` یعنی:

| کد | معنی |
|---|---|
| `%Y` | سال ۴ رقمی |
| `%m` | ماه ۲ رقمی |
| `%d` | روز |
| `%H` | ساعت |
| `%M` | دقیقه |

**خروجی:** `2026-09-26 14:30`.

## 🛠 بخش ۳: داده‌ها

### `PROJECTS`

```python
PROJECTS = [
    {
        "project_id": "P-001",
        "slug": "media-building-phase1",
        ...
    }
]
```

### `SPACES_RAW`

```python
SPACES_RAW = [
    {
        "space_id": "S-001",
        "name_fa": "استودیو رادیویی A",
        "length_m": 10.31,
        "width_m": 6.83,
        ...
    },
    # ... ۱۲۱ رکورد
]
```

**نکته:** این داده‌ها را دستی نوشتیم، چون در Excel پراکنده بودند.

## 🛠 بخش ۴: توابع کمکی

```python
def enrich_spaces(spaces_raw):
    """محاسبه area_m2 و perimeter_m"""
    result = []
    for s in spaces_raw:
        s = s.copy()
        s["project_id"] = "P-001"
        s["area_m2"] = round(s["length_m"] * s["width_m"], 2)
        s["perimeter_m"] = round(2 * (s["length_m"] + s["width_m"]), 2)
        s["floor_finish"] = "موزائیک ایرانی + کفپوش ونیل"
        s["wall_finish"] = "تایل آکوستیک + MDF ازاره"
        s["ceiling_finish"] = "کناف آکوستیک + وول‌پنل"
        s["is_public"] = True
        s["notes_fa"] = ""

        # ترتیب ستون‌ها
        ordered = {
            "space_id": s["space_id"],
            "project_id": s["project_id"],
            "name_fa": s["name_fa"],
            # ... همه فیلدها به ترتیب
        }
        result.append(ordered)
    return result

SPACES = enrich_spaces(SPACES_RAW)
```

### توضیح خط به خط

| خط | کار |
|---|---|
| `def enrich_spaces(...):` | تعریف تابع |
| `result = []` | لیست خالی برای جمع‌آوری |
| `for s in spaces_raw:` | حلقه روی هر رکورد |
| `s = s.copy()` | کپی رکورد |
| `s["project_id"] = "P-001"` | افزودن فیلد |
| `s["area_m2"] = ...` | محاسبه مساحت |
| `round(..., 2)` | گرد کردن |
| `ordered = {...}` | ترتیب ستون‌ها |
| `result.append(ordered)` | افزودن به لیست |
| `return result` | برگرداندن |

**چرا ترتیب؟**

در Excel، ترتیب ستون‌ها مهم است. با `ordered`، مطمئن می‌شویم که همیشه یک ترتیب ثابت دارند.

## 🛠 بخش ۵: ساخت Excel

```python
def build_excel(filename="Master_Data.xlsx"):
    from openpyxl import load_workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

    # ساخت DataFrames
    df_projects = pd.DataFrame(PROJECTS)
    df_spaces = pd.DataFrame(SPACES)
    # ... بقیه

    # نوشتن به Excel
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df_projects.to_excel(writer, sheet_name="Projects", index=False)
        df_spaces.to_excel(writer, sheet_name="Spaces", index=False)
        # ... بقیه

    # فرمت‌دهی
    wb = load_workbook(filename)
    header_font = Font(name="Tahoma", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
    # ... بقیه
```

### مفهوم: `pd.DataFrame`

**DataFrame** ساختار جدولی pandas است. مثل یک جدول Excel در حافظه.

```python
df = pd.DataFrame([
    {"name": "A", "age": 30},
    {"name": "B", "age": 25},
])
```

**نتیجه:**

| name | age |
|---|---|
| A | 30 |
| B | 25 |

### `pd.ExcelWriter`

یک **Context Manager** که همه DataFrameها را در یک فایل Excel می‌نویسد.

```python
with pd.ExcelWriter("file.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
```

### `index=False`

اگر `index=True` (پیش‌فرض)، pandas یک ستون شماره به Excel اضافه می‌کند. `False` یعنی اضافه نکن.

### فرمت‌دهی

```python
wb = load_workbook(filename)

header_font = Font(name="Tahoma", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")

for ws in wb.worksheets:
    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
```

**چه کار می‌کند؟**
- ردیف اول هر شیت را **بولد سفید روی پس‌زمینه سرمه‌ای** می‌کند.
- عرض ستون‌ها را تنظیم می‌کند.
- سلول‌ها را وسط‌چین می‌کند.

## 🛠 بخش ۶: ساخت JSON

```python
def build_json(filename="master_data.json"):
    data = {
        "version": VERSION,
        "build_date": BUILD_DATE,
        "projects": PROJECTS,
        "spaces": SPACES,
        # ... ۲۳ بخش
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
```

### توضیح خطوط

| خط | کار |
|---|---|
| `data = {...}` | دیکشنری اصلی |
| `with open(...) as f:` | باز کردن فایل |
| `"w"` | حالت نوشتن (Write) |
| `encoding="utf-8"` | پشتیبانی فارسی |
| `json.dump(...)` | نوشتن JSON |
| `ensure_ascii=False` | فارسی به‌جای `\u0627...` |
| `indent=2` | ۲ فاصله برای خوانایی |

**`ensure_ascii=False` خیلی مهم است.** بدون آن، فارسی به شکل زیر نوشته می‌شود:

```json
"\u0633\u0644\u0627\u0645"
```

با آن:

```json
"سلام"
```

## 🛠 بخش ۷: اجرا

```python
if __name__ == "__main__":
    print("=" * 60)
    print(f"Master Data Builder - نسخه {VERSION}")
    print(f"تاریخ ساخت: {BUILD_DATE}")
    print("=" * 60)
    build_excel()
    build_json()
    print("=" * 60)
    print("🎉 همه فایل‌ها با موفقیت ساخته شدند")
    print("=" * 60)
```

### `if __name__ == "__main__":`

الگوی مهم Python.

**معنی:** «اگر این فایل مستقیماً اجرا شد، این کد را اجرا کن.»

**اگر کسی فایل را Import کند، این کد اجرا نمی‌شود.**

**مثال:**

`master_data_builder.py` مستقیماً → Build اجرا می‌شود.

`from master_data_builder import PROJECTS` در فایل دیگر → Build اجرا **نمی‌شود**.

## 🛠 اجرای اسکریپت

```bash
cd ~/Documents/Projects/farhadproject/python-scripts
source venv/bin/activate
python master_data_builder.py
```

**خروجی:**

```
============================================================
Master Data Builder - نسخه 1.0.0
تاریخ ساخت: 2026-09-26 14:30
============================================================
✅ فایل Master_Data.xlsx ساخته شد (1 پروژه، 122 فضا)
✅ فایل master_data.json ساخته شد
============================================================
🎉 همه فایل‌ها با موفقیت ساخته شدند
============================================================
```

## 🎓 ساختار پوشه نهایی

```
python-scripts/
├── venv/                            ← محیط مجازی
├── master_data_builder.py           ← اسکریپت اصلی
├── requirements.txt                  ← کتابخانه‌ها
├── Master_Data.xlsx                 ← خروجی Excel
└── master_data.json                 ← خروجی JSON
```

## 🎓 چرا این کار مفید است؟

### سناریوی ۱: اضافه کردن پروژه جدید

فقط کافی است یک رکورد جدید به `PROJECTS` اضافه کنی. دوباره اجرا کن. هر دو فایل (Excel و JSON) به‌روز می‌شوند.

### سناریوی ۲: تغییر ابعاد یک فضا

`length_m` را در `SPACES_RAW` عوض کن. `area_m2` خودکار محاسبه می‌شود.

### سناریوی ۳: افزودن بخش جدید

یک دیکشنری جدید مثل `DOORS = [...]` بساز. در `build_json` و `build_excel` اضافه کن.

### سناریوی ۴: استفاده در وب

فایل `master_data.json` مستقیماً در Astro استفاده می‌شود:

```javascript
import masterData from "./data/master_data.json";
```

## 🎁 خلاصه

| بخش | کار |
|---|---|
| Import | کتابخانه‌ها |
| تنظیمات | Version، Date |
| داده‌ها | لیست Dictها |
| Enrich | محاسبات |
| Build Excel | با pandas |
| Build JSON | با json |
| Main | اجرای همه |
