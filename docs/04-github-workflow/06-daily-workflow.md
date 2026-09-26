# Workflow روزمره GitHub

## 🎓 مفهوم

در این فایل، **چرخه کار روزمره** با GitHub را مرور می‌کنیم. کارهایی که هر روز یا هر بار تغییر انجام می‌دهی.

## 🎓 چرخه روزانه

```
صبح:                          در طول روز:               شب:
─────────────────             ──────────────            ──────────────
git pull (گرفتن تغییرات)       ویرایش کد                  git add .
                              (VS Code)                  git commit -m "..."
                                                         git push
```

## 🛠 صبح: شروع کار

### گام ۱: ورود به پوشه

```bash
cd ~/Documents/Projects/farhadproject
```

### گام ۲: بررسی وضعیت

```bash
git status
```

باید `working tree clean` باشد (اگر شب قبل Push کرده‌ای).

### گام ۳: گرفتن تغییرات از GitHub

اگر تیم داری یا از چند کامپیوتر کار می‌کنی:

```bash
git pull
```

**اگر تنها کار می‌کنی، نیازی نیست.** اما عادت خوبی است.

### گام ۴: شروع کار

```bash
code .
```

پروژه در VS Code باز می‌شود.

## 🛠 در طول روز: کار کردن

### کار در VS Code

- ویرایش فایل‌ها.
- ساخت فایل‌های جدید.
- حذف فایل‌ها.
- اجرای `npm run dev` برای دیدن نتیجه.

### توقف‌های میانی (Checkpoint)

هر ۳۰–۶۰ دقیقه، یا هر بار که یک بخش منطقی تمام می‌شود:

```bash
git add .
git commit -m "پیام"
```

**اما Push نزن.** Push را برای پایان روز نگه‌دار.

**چرا؟**

- Commit محلی سریع است.
- Push کند است (شبکه).
- Commit‌های مکرر محلی، تاریخچه بهتری می‌سازند.

## 🛠 شب: پایان کار

### گام ۱: بررسی

```bash
git status
```

باید همه چیز Commit شده باشد.

### گام ۲: اگر چیزی مانده

```bash
git add .
git commit -m "End of day: [توضیح]"
```

### گام ۳: Push

```bash
git push
```

همه Commit‌های روز به GitHub می‌رود.

### گام ۴: بررسی

```bash
git log --oneline | head -5
```

۵ Commit آخر.

در GitHub:

```
https://github.com/baanic/farhadproject-site/commits/main
```

## 🎓 تمرین روزمره از پروژه ما

بیایید یک روز فرضی در پروژه خودمان را مرور کنیم:

### صبح (۹:۰۰)

```bash
cd ~/Documents/Projects/farhadproject
git pull
code .
```

### کار (۹:۳۰ تا ۱۲:۰۰)

اضافه کردن یک Component جدید.

```bash
# بعد از اتمام
git add src/components/NewComponent.astro
git commit -m "Add NewComponent"
```

### کار (۱۲:۰۰ تا ۱۵:۰۰)

ویرایش صفحه About.

```bash
git add src/pages/about.astro
git commit -m "Update About page content"
```

### کار (۱۵:۰۰ تا ۱۸:۰۰)

رفع یک باگ در Navbar.

```bash
git add src/components/Navbar.astro
git commit -m "Fix mobile menu bug"
```

### عصر (۱۸:۰۰)

```bash
git push
```

سه Commit در یک Push به GitHub رفتند.

## 🎓 ترفند: Conventional Commits

یک استاندارد برای پیام Commit:

```
<type>(<scope>): <description>
```

| Type | کاربرد |
|---|---|
| `feat` | ویژگی جدید |
| `fix` | رفع باگ |
| `docs` | مستندات |
| `style` | تغییر ظاهری (بدون تغییر منطق) |
| `refactor` | بازنویسی کد |
| `test` | تست |
| `chore` | کارهای عمومی |

### مثال‌ها

```bash
git commit -m "feat(portfolio): add acoustic design section"
git commit -m "fix(navbar): mobile menu not closing"
git commit -m "docs(git): add commit workflow"
git commit -m "style(hero): change font size"
git commit -m "refactor(components): simplify StatCard"
```

**مزیت:**
- پیام‌ها استاندارد می‌شوند.
- ابزارها می‌توانند تحلیل کنند (CHANGELOG خودکار).

## 🎓 ترفند: دسته‌بندی Commit‌های روز

اگر روز پرکاری داشتی، Commit‌ها را **گروه‌بندی** کن:

```bash
# به‌جای ۱۰ Commit کوچک
git add .
git commit -m "Add documentation section

- Terminal basics (5 files)
- Dev environment (6 files)
- Git fundamentals (7 files)
- GitHub workflow (7 files)"
```

**اما نه خیلی بزرگ.** اگر ۵۰ فایل در یک Commit باشد، پیگیری سخت است.

**قاعده سرانگشتی:** Commit‌های منطقی، نه Commit‌های خیلی کوچک، نه خیلی بزرگ.

## 🎓 ترفند: بررسی قبل از Push

قبل از `git push`، این دستور را بزن:

```bash
git log origin/main..HEAD --oneline
```

**ترجمه:** چه Commit‌هایی در `main` محلی هست که در `origin/main` نیست؟

خروجی: لیست Commit‌های آماده Push.

## 🎓 ترفند: `git diff` قبل از Commit

قبل از `git add`:

```bash
git diff
```

دیدن تغییرات Working Directory.

بعد از `git add`:

```bash
git diff --staged
```

دیدن تغییرات Stage.

## 🎓 ترفند: بازگشت به عقب

### اگر Commit اشتباه زدی

```bash
git commit --amend -m "پیام صحیح"
```

⚠️ **فقط روی آخرین Commit، و اگر Push نکرده‌ای.**

### اگر می‌خواهی آخرین Commit را undo کنی (اما تغییرات بمانند)

```bash
git reset --soft HEAD~1
```

تغییرات به Stage برمی‌گردند.

### اگر می‌خواهی همه تغییرات را پاک کنی

```bash
git reset --hard HEAD
```

⚠️ **خطرناک.** همه تغییرات محلی از دست می‌رود.

### اگر می‌خواهی یک فایل را به نسخه قبل برگردانی

```bash
git checkout HEAD file.txt
```

## 🎓 یک روز تعطیل

اگر تعطیل بودی و کار نکردی:

- **هیچ کاری لازم نیست.**
- Git وضعیت را نگه می‌دارد.
- روز بعد ادامه بده.

## 🎓 اگر یک هفته کار نکردی

```bash
git status
git log --oneline | head -10
```

وضعیت را ببین. سپس ادامه بده.

## 🎁 خلاصه

| زمان | کار |
|---|---|
| صبح | `git pull` |
| در روز | Commit‌های منطقی |
| شب | `git push` |

| دستور | کار |
|---|---|
| `git status` | وضعیت |
| `git add .` | Stage همه |
| `git commit -m "msg"` | Commit |
| `git push` | فرستادن |
| `git pull` | گرفتن |
| `git log --oneline` | تاریخچه |

## 🎉 پایان بخش ۰۴

تبریک! کار با GitHub را یاد گرفتی.

**گام بعدی:** `../05-python-master-data/`.