# بروزرسانی محتوا

## 🎓 مفهوم

**بروزرسانی محتوا** = تغییر متن، تصویر، یا داده.

## 🎓 سه نوع محتوا

### ۱. داده پروژه

در `master_data_builder.py`.

**مثال:** مساحت، مدت، مبلغ.

### ۲. متن ثابت

در Componentها.

**مثال:** درباره من، خدمات.

### ۳. تصویر

در `public/images/`.

**مثال:** عکس پروژه.

## 🛠 نوع ۱: تغییر داده پروژه

### گام ۱: باز کن

```bash
cd ~/Documents/Projects/farhadproject/python-scripts
source venv/bin/activate
code master_data_builder.py
```

### گام ۲: پیدا کن

```python
PROJECTS = [
    {
        "project_id": "P-001",
        "area_m2": 11000,   # ← این را عوض کن
        # ...
    }
]
```

### گام ۳: تغییر بده

```python
"area_m2": 12500,   # ← جدید
```

### گام ۴: اجرا

```bash
python master_data_builder.py
cp master_data.json ../astro-site/src/data/master_data.json
```

### گام ۵: تست + Push

```bash
cd ../astro-site
npm run dev
# بررسی کن
cd ..
git add .
git commit -m "Update project area to 12500"
git push
```

## 🛠 نوع ۲: تغییر متن ثابت

### گام ۱: پیدا کن

```bash
cd ~/Documents/Projects/farhadproject/astro-site
```

**کجا متن‌ها هستند؟**

| متن | فایل |
|---|---|
| درباره من | `AboutMini.astro` |
| خدمات | `ServicesMini.astro` |
| دفتر فنی | `TechnicalOfficeSection.astro` |
| کنترل پروژه | `ProjectControlsSection.astro` |
| متره | `QSSection.astro` |
| آکوستیک طراحی | `AcousticDesignSection.astro` |
| آکوستیک اجرا | `AcousticExecutionSection.astro` |
| نتایج | `ResultsSection.astro` |
| تحویل‌ها | `DeliveriesSection.astro` |
| آموخته‌ها | `LessonsSection.astro` |
| تماس | `ContactSection.astro` |

### گام ۲: عوض کن

```bash
code src/components/portfolio/AboutMini.astro
```

متن را در Frontmatter یا Template پیدا کن.

**مثال:**

```astro
<p>
  فرهاد رضائی هستم؛ ورودی ۱۳۸۸ مهندسی عمران...
</p>
```

متن را عوض کن.

### گام ۳: ذخیره + تست

Dev Server خودکار Reload می‌کند.

### گام ۴: Commit + Push

```bash
cd ~/Documents/Projects/farhadproject
git add .
git commit -m "Update About section"
git push
```

## 🛠 نوع ۳: تغییر تصویر

### گام ۱: پیدا کردن تصویر

```bash
cd ~/Documents/Projects/farhadproject/astro-site
ls public/images/portfolio/
```

**خروجی:** همه تصاویر.

### گام ۲: عوض کردن

تصویر جدید را در همان مسیر با همان نام بگذار:

```bash
cp ~/Desktop/new-portrait.jpg public/images/portfolio/portrait.jpg
```

**نکته:** نام فایل **یکسان** باشد.

### گام ۳: تست

Hard Refresh: `Cmd + Shift + R`.

### گام ۴: Commit

```bash
git add .
git commit -m "Update portrait image"
git push
```

**نکته:** اگر نام فایل را عوض کردی، باید در Component هم عوض کنی.

## 🎓 مثال واقعی: تغییر بیوگرافی

### قبل

```astro
<p style="font-size: 16px; line-height: 2;">
  فرهاد رضائی هستم؛ ورودی ۱۳۸۸ مهندسی عمران دانشگاه آزاد اسلامی.
  این افتخار را داشته‌ام که در کنار بزرگان این رشته، فن و علم مهندسی عمران را بیاموزم.
</p>
```

### بعد

```astro
<p style="font-size: 16px; line-height: 2;">
  فرهاد رضائی هستم؛ مهندس عمران با ۱۲ سال تجربه در دفتر فنی و کنترل پروژه.
  در این سال‌ها، در پروژه‌های بزرگ رسانه‌ای و عمرانی فعالیت داشته‌ام.
</p>
```

## 🎓 تغییر رنگ

اگر خواستی رنگ پروژه را عوض کنی:

### در `global.css`

```css
/* قبل */
--primary: #1B2A4A;

/* بعد */
--primary: #2D5C8A;
```

**اما** ما از Color مستقیم استفاده می‌کنیم، نه CSS Variable.

**پس باید همه جا عوض کنی.**

**راه بهتر:** استفاده از Find & Replace در VS Code:

1. `Cmd + Shift + F`.
2. جستجو: `#1B2A4A`.
3. جایگزین: `#2D5C8A`.
4. **Replace All**.

## 🎓 تغییر فونت

اگر خواستی فونت را عوض کنی:

### گام ۱: فایل‌های فونت جدید

```
public/fonts/
├── NewFont-Light.woff2
├── NewFont-Regular.woff2
├── NewFont-Medium.woff2
└── NewFont-Bold.woff2
```

### گام ۲: عوض در `global.css`

```css
@font-face {
  font-family: 'NewFont';  /* ← عوض کن */
  src: url('/fonts/NewFont-Regular.woff2') format('woff2');
  font-weight: 400;
}

html {
  font-family: 'NewFont', Tahoma, sans-serif;
}
```

## 🎓 چک‌لیست تغییر

- [ ] فایل مناسب را پیدا کردی
- [ ] متن/داده را عوض کردی
- [ ] ذخیره کردی
- [ ] Hard Refresh
- [ ] تست
- [ ] Commit + Push

## 🛑 عیب‌یابی

### مشکل ۱: تغییر نمایش داده نمی‌شود

**علت:** Cache یا Build نشده.

**راه‌حل:**
- Hard Refresh.
- Dev Server را Restart کن.

### مشکل ۲: متن می‌شکند

**علت:** فاصله یا کاراکتر مشکل‌دار.

**راه‌حل:** از نیم‌فاصله (`‌`) استفاده کن.

### مشکل ۳: تصویر جدید نمایش داده نمی‌شود

**علت:** نام فایل.

**راه‌حل:** نام باید **دقیقاً** یکسان باشد.

## 🎓 نکته: نیم‌فاصله

در فارسی، بین کلمات مرکب **نیم‌فاصله** می‌گذاریم:

| اشتباه | درست |
|---|---|
| دفترفنی | دفتر‌فنی |
| می‌روم | می‌روم |
| کتابها | کتاب‌ها |

**نیم‌فاصله:** `‌` — کاراکتر Unicode.

**در Mac:** `Shift + Space`.

## 🎓 بهترین تمرین

**قبل از هر تغییر:**

```bash
git status
```

اگر تغییرات قبلی Commit نشده، اول آن‌ها را Commit کن.

**سپس تغییر بده.**

## 🎁 خلاصه

| نوع تغییر | فایل |
|---|---|
| داده پروژه | `master_data_builder.py` |
| متن ثابت | `src/components/portfolio/*.astro` |
| تصویر | `public/images/portfolio/` |
| رنگ | همه‌جا (Find & Replace) |
| فونت | `global.css` |

## آماده‌ای؟ برو به `04-troubleshooting.md`.