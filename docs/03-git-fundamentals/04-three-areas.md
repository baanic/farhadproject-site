# سه ناحیه Git

## 🎓 مفهوم

یکی از **مهم‌ترین** مفاهیم Git، درک **سه ناحیه** است:

```
Working Directory  →  Staging Area  →  Repository
    (کاری)           (میانی)          (ذخیره)
```

اگر این سه ناحیه را نفهمی، Git برایت مثل یک جعبه سیاه است.

## 🎓 ناحیه ۱: Working Directory

**Working Directory** — پوشه‌ای که فایل‌های پروژه در آن است.

مثال: `~/Documents/Projects/farhadproject/`

**در این ناحیه:**

- فایل‌ها را ویرایش می‌کنی.
- فایل جدید می‌سازی.
- فایل حذف می‌کنی.

**وضعیت:** هر تغییر اینجا، هنوز توسط Git «ثبت‌نشده» است.

## 🎓 ناحیه ۲: Staging Area

**Staging Area** — یک ناحیه میانی که تغییرات را **آماده Commit** می‌کند.

**چرا این ناحیه وجود دارد؟**

تصور کن ۵ فایل را تغییر داده‌ای. اما فقط ۳ تا مربوط به یک ویژگی جدید است. می‌خواهی فقط همان ۳ تا را Commit کنی.

**با Staging Area:**
- فقط ۳ فایل موردنظر را «Stage» می‌کنی.
- بعد Commit می‌زنی.
- آن ۳ فایل در Commit می‌آیند.

**در این ناحیه:**

- فایل‌هایی که «Stage» شده‌اند.
- آماده برای Commit بعدی.

**وضعیت:** تغییرات اینجا، «ثبت‌شده ولی Commit نشده» است.

## 🎓 ناحیه ۳: Repository

**Repository** — تاریخچه دائمی Git.

**در این ناحیه:**

- Commit‌های ثبت‌شده.
- تاریخچه کامل.
- همه چیز امن و دائمی.

**وضعیت:** Commit‌های اینجا، «ثبت‌شده و ماندگار» است.

## 🎓 قیاس روزمره

تصور کن در یک رستوران هستی:

| مرحله | Git | رستوران |
|---|---|---|
| **۱** | Working Directory | آشپزخانه — مواد آماده، اما خام |
| **۲** | Staging Area | سینی — غذا آماده سرو |
| **۳** | Repository | انبار — غذای سرو شده، ثبت شده |

**مراحل:**
1. آشپز غذا را می‌پزد (Working).
2. غذا را روی سینی می‌گذارد (Staging).
3. پیش مشتری می‌برد (Commit).

## 🎓 جریان تغییرات

```
┌───────────────────────┐
│   Working Directory   │
│   (فایل‌های پروژه)     │
└───────────┬───────────┘
            │  git add
            ▼
┌───────────────────────┐
│    Staging Area       │
│   (تغییرات آماده)      │
└───────────┬───────────┘
            │  git commit
            ▼
┌───────────────────────┐
│     Repository        │
│   (تاریخچه دائمی)      │
└───────────────────────┘
```

## 🛠 دستورهای مربوطه

### بررسی وضعیت

```bash
git status
```

خروجی نشان می‌دهد فایل‌ها در چه ناحیه‌ای هستند.

### افزودن به Staging

```bash
# یک فایل خاص
git add file.txt

# چند فایل
git add file1.txt file2.txt

# همه فایل‌ها
git add .

# همه فایل‌های .md
git add *.md

# همه فایل‌های یک پوشه
git add src/
```

### حذف از Staging

```bash
git reset file.txt
```

**یا:**

```bash
git restore --staged file.txt
```

### Commit کردن

```bash
git commit -m "پیام Commit"
```

تغییرات از Staging به Repository می‌رود.

## 🎓 مثال واقعی از پروژه ما

فرض کن در فایل `index.astro` تغییر دادی.

### گام ۱: بررسی وضعیت

```bash
git status
```

خروجی:

```
On branch main
Changes not staged for commit:
  modified:   src/pages/index.astro
```

کلمه **`not staged`** یعنی تغییر در Working Directory است، هنوز Stage نشده.

### گام ۲: افزودن به Staging

```bash
git add src/pages/index.astro
```

یا:

```bash
git add .
```

### گام ۳: بررسی مجدد

```bash
git status
```

خروجی:

```
On branch main
Changes to be committed:
  modified:   src/pages/index.astro
```

کلمه **`to be committed`** یعنی Stage شده، آماده Commit.

### گام ۴: Commit

```bash
git commit -m "Update homepage title"
```

### گام ۵: بررسی تاریخچه

```bash
git log --oneline
```

Commit جدید در بالای لیست.

## 🎓 حالت‌های مختلف در `git status`

### ۱. Untracked Files

فایل‌های جدیدی که Git نمی‌شناسد:

```
Untracked files:
  new-file.txt
```

**راه‌حل:** `git add new-file.txt`.

### ۲. Modified

فایل‌های موجود که تغییر کرده‌اند:

```
Changes not staged for commit:
  modified:   existing-file.txt
```

**راه‌حل:** `git add existing-file.txt`.

### ۳. Staged

فایل‌های آماده Commit:

```
Changes to be committed:
  modified:   staged-file.txt
```

**راه‌حل:** `git commit -m "..."`.

### ۴. Deleted

فایل‌های حذف‌شده:

```
Changes not staged for commit:
  deleted:    old-file.txt
```

**راه‌حل:** `git add old-file.txt` (تأیید حذف) یا `git checkout old-file.txt` (بازگردانی).

### ۵. Clean

هیچ تغییری نیست:

```
nothing to commit, working tree clean
```

## 🎓 ترفند: Stage تعاملی

اگر فایل‌های زیادی داری و می‌خواهی بخشی را Stage کنی:

```bash
git add -p
```

Git هر تغییر را نشان می‌دهد و می‌پرسد: «این را Stage کنم؟»

گزینه‌ها:
- `y` = بله
- `n` = نه
- `s` = Split (تقسیم)
- `q` = خروج

## 🎓 ترفند: `git diff`

برای دیدن تغییرات قبل از `git add`:

```bash
git diff
```

برای تغییرات Stage شده:

```bash
git diff --staged
```

## 💡 چرا سه ناحیه؟

شاید بپرسی «چرا این‌قدر پیچیده؟». جواب: **انعطاف.**

**مثال:**

فرض کن در یک روز، این کارها را کردی:
1. باگ صفحه About را درست کردی.
2. ویژگی جدید صفحه Contact اضافه کردی.
3. فایل README را اصلاح کردی.

می‌خواهی این‌ها در ۳ Commit جدا باشند:

```bash
# Commit 1: باگ About
git add src/pages/about.astro
git commit -m "Fix About page bug"

# Commit 2: ویژگی Contact
git add src/pages/contact.astro
git commit -m "Add contact form validation"

# Commit 3: README
git add README.md
git commit -m "Update README"
```

**بدون Staging Area، این کار ممکن نبود.**

## 🎁 خلاصه

| ناحیه | کار | دستور |
|---|---|---|
| Working Directory | ویرایش فایل | (مستقیم) |
| Staging Area | آماده‌سازی | `git add` |
| Repository | ثبت دائمی | `git commit` |

| دستور | کار |
|---|---|
| `git status` | بررسی وضعیت |
| `git add file` | افزودن به Stage |
| `git add .` | افزودن همه |
| `git reset file` | حذف از Stage |
| `git diff` | دیدن تغییرات |
| `git diff --staged` | دیدن تغییرات Stage |

## آماده‌ای؟ برو به `05-commit-workflow.md`.