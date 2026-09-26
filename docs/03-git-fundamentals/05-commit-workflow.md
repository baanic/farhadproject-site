# Workflow روزمره Git

## 🎓 مفهوم

در این فایل، **چرخه کار روزمره** با Git را یاد می‌گیری.

## 🎓 چرخه سه‌مرحله‌ای

هر بار که تغییری می‌دهی:

```
۱. git add        ۲. git commit        ۳. git push
   (Stage)           (ثبت)              (فرستادن)
```

## 🛠 گام ۱: `git add`

تغییرات را از Working Directory به Staging منتقل می‌کند.

### افزودن یک فایل

```bash
git add src/pages/index.astro
```

### افزودن همه تغییرات

```bash
git add .
```

**نکته:** نقطه یعنی «همه چیز در پوشه فعلی».

### افزودن گروه خاص

```bash
# همه فایل‌های Markdown
git add "*.md"

# همه فایل‌های یک پوشه
git add docs/

# فایل‌های جدید و تغییرات، اما بدون حذف
git add --ignore-removal .
```

## 🛠 گام ۲: `git commit`

تغییرات Stage شده را در Repository ثبت می‌کند.

### Commit با پیام کوتاه

```bash
git commit -m "Add homepage hero section"
```

### Commit با پیام چند خطی

```bash
git commit -m "Add contact form

- Add form fields
- Connect to Web3Forms
- Add validation"
```

### Commit با ویرایشگر

```bash
git commit
```

ویرایشگر باز می‌شود (VS Code با تنظیمات ما).

### Commit همه تغییرات Tracked بدون Stage

```bash
git commit -am "پیام"
```

**نکته:** فقط برای فایل‌های **قبلاً Tracked**. فایل‌های جدید Stage نمی‌شوند.

## 🎓 آناتومی یک Commit خوب

یک Commit خوب سه بخش دارد:

### ۱. پیام کوتاه (Subject)

- حداکثر ۵۰ کاراکتر.
- با فعل شروع شود.
- زمان حال (Add, Fix, Update).
- بدون نقطه در انتها.

**خوب:**
```
Add portfolio page
Fix navbar on mobile
Update README
```

**بد:**
```
changes
fixed it
لطفاً ببین
```

### ۲. بدنه (Body) — اختیاری

اگر Commit پیچیده است، توضیح بده:

```
Add Web3Forms integration

- Create access key
- Add form submit handler
- Style success message
- Test locally
```

### ۳. Footer — اختیاری

برای ارجاع به Issue:

```
Add homepage

Closes #12
```

## 🎓 قواعد پیام Commit

### قاعده ۱: فعل امری

- ✅ `Add component`
- ❌ `Added component`

### قاعده ۲: کوتاه و مشخص

- ✅ `Fix navbar mobile menu`
- ❌ `Changes`

### قاعده ۳: یک موضوع در هر Commit

- ✅ Commit 1: `Add homepage`
- ✅ Commit 2: `Add navbar`
- ❌ Commit 1: `Add homepage, navbar, footer, contact form` (بیش از حد)

### قاعده ۴: اگر ممکن نیست کوتاه، از بدنه استفاده کن

```
Add comprehensive documentation

- Terminal basics (5 files)
- Dev environment (6 files)
- Git fundamentals (7 files)

This completes phase 1 of documentation.
```

## 🛠 گام ۳: `git push`

Commit‌های محلی را به GitHub می‌فرستد.

### Push به Branch اصلی

```bash
git push
```

اگر بار اول است:

```bash
git push -u origin main
```

**معنی:**
- `-u` = Upstream (ثبت رابطه).
- `origin` = نام مخزن ریموت.
- `main` = نام Branch.

پس از این، فقط `git push` کافی است.

### Push به Branch دیگر

```bash
git push origin feature-branch
```

## 🎓 مثال کامل چرخه

فرض کن فایل `index.astro` را ویرایش کردی.

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

### گام ۲: دیدن تغییرات

```bash
git diff src/pages/index.astro
```

خروجی: تفاوت‌های دقیق.

### گام ۳: Stage کردن

```bash
git add src/pages/index.astro
```

### گام ۴: بررسی مجدد

```bash
git status
```

خروجی:

```
On branch main
Changes to be committed:
  modified:   src/pages/index.astro
```

### گام ۵: Commit

```bash
git commit -m "Update homepage title"
```

خروجی:

```
[main abc1234] Update homepage title
 1 file changed, 3 insertions(+), 2 deletions(-)
```

### گام ۶: Push

```bash
git push
```

### گام ۷: بررسی

```bash
git log --oneline
```

Commit جدید در بالای لیست.

## 🎓 چرخه روزمره در پروژه ما

در پروژه ما، هر بار اضافه کردن یک بخش جدید، این چرخه را طی کردیم:

```bash
# ۱. فایل‌ها را ساختم (via code, editor)
code src/components/portfolio/NewSection.astro

# ۲. بررسی وضعیت
git status

# ۳. Stage کردن
git add .

# ۴. Commit
git commit -m "Add new section"

# ۵. Push
git push
```

## 🎓 ترفند: `git log` زیبا

### لاگ کوتاه

```bash
git log --oneline
```

خروجی:

```
abc1234 Add new section
def5678 Fix bug
ghi9012 Update README
```

### لاگ با نمودار

```bash
git log --oneline --graph --all
```

نمایش گرافیکی Branch‌ها.

### لاگ با فیلتر نویسنده

```bash
git log --author="Farhad"
```

### لاگ Commit‌های امروز

```bash
git log --since="1 day ago"
```

### لاگ با آمار

```bash
git log --stat
```

نمایش تعداد فایل‌ها و خطوط تغییریافته.

## 🎓 ترفند: `git show`

برای دیدن جزئیات یک Commit:

```bash
git show abc1234
```

یا آخرین Commit:

```bash
git show HEAD
```

**خروجی:**
- پیام Commit.
- نویسنده.
- تاریخ.
- تفاوت‌های دقیق.

## 🎓 ترفند: Alias

اگر دستورهای زیادی می‌زنی، Alias بساز:

```bash
git config --global alias.st "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.ci "commit"
git config --global alias.lg "log --oneline --graph --all"
```

از این پس:

```bash
git st      # به جای git status
git co main # به جای git checkout main
git lg      # لاگ زیبا
```

## 🎓 قواعد طلایی

### ۱. کم و پرتکرار Commit کن

- بعد از هر تغییر منطقی، Commit بزن.
- نه هر روز یک Commit بزرگ.

### ۲. قبل از Push، Pull کن

اگر چند نفر روی پروژه کار می‌کنند:

```bash
git pull
git push
```

### ۳. پیام Commit را جدی بگیر

پیام خوب، در آینده وقت زیادی ذخیره می‌کند.

### ۴. Commit را کامل کن

اگر وسط کار Commit می‌زنی، مطمئن شو پروژه کار می‌کند. Commit نباید پروژه را خراب کند.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `git status` | وضعیت |
| `git diff` | تفاوت‌ها |
| `git add file` | Stage |
| `git commit -m "msg"` | Commit |
| `git push` | فرستادن |
| `git log --oneline` | تاریخچه |
| `git show HEAD` | جزئیات آخرین Commit |

## آماده‌ای؟ برو به `06-personal-access-token.md`.