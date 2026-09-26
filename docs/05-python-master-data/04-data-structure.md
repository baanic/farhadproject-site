# ساختار داده Master Data

## 🎓 مفهوم

**Master Data** ما یک ساختار **دیکشنری تودرتو** است:

```python
{
    "projects": [...],
    "spaces": [...],
    "acoustic_layers": [...],
    ...
}
```

هر بخش، یک **لیست** از **دیکشنری** است.

## 🎓 چرا این ساختار؟

### ۱. سادگی

هر پروژه، یک دیکشنری است:

```python
{
    "project_id": "P-001",
    "title_fa": "پروژه ...",
    "area_m2": 11000,
    ...
}
```

### ۲. توسعه‌پذیری

هر فیلد جدید، آسان اضافه می‌شود:

```python
{
    "project_id": "P-001",
    "title_fa": "...",
    "new_field": "value"    # ← اضافه شد
}
```

### ۳. تبدیل به JSON

ساختار Python تقریباً یکسان با JSON است. تبدیل آسان.

## 🛠 ساختار کامل

```python
MASTER_DATA = {
    # بخش ۱: مشخصات پروژه
    "projects": [
        {
            "project_id": "P-001",
            "slug": "media-building-phase1",
            "title_fa": "...",
            ...
        }
    ],

    # بخش ۲: فضاها
    "spaces": [
        {
            "space_id": "S-001",
            "name_fa": "...",
            ...
        }
    ],

    # بخش ۳: آکوستیک
    "acoustic_layers": [...],

    # ... و ۲۳ بخش دیگر
}
```

## 🎓 ساختار یک رکورد

هر رکورد، یک **دیکشنری** با فیلدهای مشخص:

```python
PROJECT_001 = {
    "project_id": "P-001",           # str
    "slug": "media-building-phase1",  # str
    "title_fa": "پروژه ...",         # str
    "title_en": "Phase 1 ...",        # str
    "area_m2": 11000,                  # int
    "contract_amount_rial": 1337036052238,  # int
    "duration_months": 12,             # int
    "is_public": True,                 # bool
    "blocks": ["A", "B1", "B2", "B3"], # list
}
```

## 🎓 انواع داده در Python

| نوع | توضیح | مثال |
|---|---|---|
| **str** | رشته (متن) | `"سلام"` |
| **int** | عدد صحیح | `42` |
| **float** | عدد اعشاری | `3.14` |
| **bool** | بله/خیر | `True`, `False` |
| **None** | خالی | `None` |
| **list** | لیست | `[1, 2, 3]` |
| **dict** | دیکشنری | `{"a": 1}` |

## 🎓 ساختار `SPACES` (نمونه)

```python
SPACES = [
    {
        "space_id": "S-001",
        "project_id": "P-001",
        "name_fa": "استودیو رادیویی A",
        "name_en": "Radio Studio A",
        "block": "A",
        "floor": "همکف",
        "zone": "شرقی",
        "length_m": 10.31,
        "width_m": 6.83,
        "height_m": 5.40,
        "area_m2": 70.42,
        "acoustic_class": "full",
        "has_visor_window": False,
        "has_airlock": True,
        "has_silencer": True,
        "executed": True,
    },
    # ... ۱۲۱ رکورد دیگر
]
```

## 🎓 چرا `space_id` و `project_id`؟

**کلیدهای یکتا (Foreign Keys):**

- `project_id` → کلید به جدول Projects.
- `space_id` → کلید یکتا برای هر فضا.

**چرا؟**

در فایل‌های مرتبط، می‌توانیم ارجاع بدهیم:

```python
ACOUSTIC_LAYERS = [
    {
        "layer_id": "AL-001",
        "space_id": "S-001",    # ← ارجاع به فضا
        "element": "دیوار",
        ...
    }
]
```

**این ساختار، شبیه دیتابیس رابطه‌ای است.**

## 🎓 محاسبات خودکار

به‌جای وارد کردن دستی `area_m2`، خودکار محاسبه می‌کنیم:

```python
def enrich_spaces(spaces_raw):
    result = []
    for s in spaces_raw:
        s = s.copy()
        # محاسبه خودکار مساحت
        s["area_m2"] = round(s["length_m"] * s["width_m"], 2)
        # محاسبه خودکار محیط
        s["perimeter_m"] = round(2 * (s["length_m"] + s["width_m"]), 2)
        result.append(s)
    return result

SPACES = enrich_spaces(SPACES_RAW)
```

**مزیت:**

- داده تکراری نداریم.
- اگر طول را تغییر دهی، مساحت خودکار عوض می‌شود.
- خطا کمتر.

## 🎓 توضیح `enrich_spaces`

### `for s in spaces_raw:`

حلقه روی هر رکورد.

### `s = s.copy()`

**کپی** رکورد تا داده اصلی دست‌نخورده بماند. Python dictionaryها به‌طور پیش‌فرض **reference** هستند، نه کپی.

### `s["area_m2"] = ...`

محاسبه و ذخیره‌سازی.

### `round(..., 2)`

گرد کردن به ۲ رقم اعشار.

### `return result`

برگرداندن لیست جدید.

## 🎓 فیلدهای مشترک

بسیاری از فیلدها بین رکوردها مشترکند:

```python
# این خطوط، در همه رکوردها تکرار می‌شوند
s["project_id"] = "P-001"
s["floor_finish"] = "موزائیک ایرانی + کفپوش ونیل"
s["wall_finish"] = "تایل آکوستیک + MDF ازاره"
s["ceiling_finish"] = "کناف آکوستیک + وول‌پنل"
s["is_public"] = True
s["notes_fa"] = ""
```

**به‌جای تکرار در ۱۲۲ رکورد، در تابع یک بار می‌نویسیم.**

## 🎓 داده اصلی vs داده پردازش‌شده

| | نام | محتوا |
|---|---|---|
| **ورودی** | `SPACES_RAW` | فقط داده اصلی |
| **پردازش** | `enrich_spaces()` | محاسبات |
| **خروجی** | `SPACES` | داده کامل |

**الگو:**

```python
SPACES_RAW = [...]           # داده خام
SPACES = enrich_spaces(SPACES_RAW)  # داده کامل
```

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| ساختار کل | Dictionary تودرتو |
| هر بخش | List of Dicts |
| کلید یکتا | `space_id`، `project_id` |
| محاسبه | توابع `enrich_*` |
| داده خام vs کامل | `_RAW` vs نهایی |

## آماده‌ای؟ برو به `05-build-master-data.md`.