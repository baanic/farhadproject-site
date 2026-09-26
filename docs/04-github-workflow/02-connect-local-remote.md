# اتصال مخزن محلی به GitHub

## 🎓 مفهوم

الان دو چیز داری:

| | محل | وضعیت |
|---|---|---|
| **مخزن محلی** | کامپیوتر خودت | Git init شده |
| **مخزن ریموت** | GitHub | خالی |

برای اینکه این دو با هم همگام شوند، باید **محلی به ریموت وصل شود**.

## 🎓 مفهوم: Remote

**Remote** یعنی «دور». در Git، Remote یک **نام مستعار** برای آدرس مخزن آنلاین است.

**نام‌های مرسوم:**

| نام | معنی |
|---|---|
| `origin` | نام پیش‌فرض برای مخزن اصلی |
| `upstream` | در Forkها، مخزن اصلی |

**معمولاً مخزن اول را `origin` می‌نامیم.**

## 🛠 گام ۱: رفتن به پوشه پروژه

```bash
cd ~/Documents/Projects/farhadproject
```

**بررسی:**

```bash
pwd
```

باید `~/Documents/Projects/farhadproject` باشد.

## 🛠 گام ۲: بررسی وضعیت Git

```bash
git status
```

خروجی:

```
On branch main
nothing to commit, working tree clean
```

**یا:**

```
On branch main
Changes not staged for commit:
  ...
```

اگر `not a git repository` دیدی، Git init نکرده‌ای:

```bash
git init
```

## 🛠 گام ۳: افزودن Remote

```bash
git remote add origin https://github.com/baanic/farhadproject-site.git
```

**آناتومی دستور:**

| بخش | معنی |
|---|---|
| `git remote` | مدیریت Remoteها |
| `add` | افزودن |
| `origin` | نامی که انتخاب می‌کنیم |
| `https://...` | آدرس مخزن |

**پس از اجرا، هیچ پیامی نشان داده نمی‌شود.** این یعنی موفق.

## 🛠 گام ۴: بررسی

```bash
git remote -v
```

خروجی:

```
origin  https://github.com/baanic/farhadproject-site.git (fetch)
origin  https://github.com/baanic/farhadproject-site.git (push)
```

**ترجمه:**

- `origin` = نام Remote.
- `(fetch)` = برای کشیدن از GitHub.
- `(push)` = برای فرستادن به GitHub.

## 🎓 دستورهای مهم Remote

| دستور | کار |
|---|---|
| `git remote` | لیست نام‌های Remote |
| `git remote -v` | لیست با آدرس |
| `git remote add NAME URL` | افزودن |
| `git remote remove NAME` | حذف |
| `git remote rename OLD NEW` | تغییر نام |
| `git remote set-url NAME URL` | تغییر آدرس |

## 🎓 تغییر آدرس Remote

اگر URL را اشتباه نوشتی:

```bash
git remote set-url origin https://github.com/baanic/correct-repo.git
```

## 🎓 حذف Remote

```bash
git remote remove origin
```

سپس یکی جدید اضافه کن.

## 🎓 چند Remote (سناریوی Fork)

اگر Fork کرده‌ای:

```bash
# مخزن فورک خودت
git remote add origin https://github.com/baanic/forked-repo.git

# مخزن اصلی (upstream)
git remote add upstream https://github.com/original-owner/original-repo.git
```

از این پس:

- `git push origin main` → فورک خودت.
- `git pull upstream main` → مخزن اصلی.

## 🎓 مفهوم: `origin` انتخاب است، نه الزام

می‌توانی اسم دیگری بگذاری:

```bash
git remote add github https://github.com/baanic/repo.git
```

از این پس:

```bash
git push github main
```

**اما `origin` استاندارد است.** از این استفاده کن.

## 🎓 در پروژه ما

ما دقیقاً این دستور را زدیم:

```bash
git remote add origin https://github.com/baanic/farhadproject-site.git
```

**بررسی:**

```bash
git remote -v
```

خروجی:

```
origin  https://github.com/baanic/farhadproject-site.git (fetch)
origin  https://github.com/baanic/farhadproject-site.git (push)
```

## 🛑 عیب‌یابی

### مشکل ۱: `error: remote origin already exists`

**علت:** قبلاً یک Remote به نام `origin` داری.

**راه‌حل ۱: تغییر URL**

```bash
git remote set-url origin https://github.com/baanic/new-url.git
```

**راه‌حل ۲: حذف و افزودن**

```bash
git remote remove origin
git remote add origin https://github.com/baanic/correct-url.git
```

### مشکل ۲: `fatal: not a git repository`

**علت:** در پوشه‌ای نیستی که Git init شده باشد.

**راه‌حل:**

```bash
cd ~/Documents/Projects/farhadproject
git init
```

### مشکل ۳: آدرس را اشتباه نوشتم

**بررسی:**

```bash
git remote -v
```

اگر URL اشتباه است:

```bash
git remote set-url origin https://github.com/CORRECT-URL.git
```

### مشکل ۴: می‌خواهم بین HTTPS و SSH سوئیچ کنم

**HTTPS:**

```bash
git remote set-url origin https://github.com/user/repo.git
```

**SSH:**

```bash
git remote set-url origin git@github.com:user/repo.git
```

## 🎓 آزمایش اتصال

قبل از Push، می‌توانی اتصال را تست کنی:

```bash
git ls-remote origin
```

**اگر مخزن خالی باشد:** هیچ خروجی ندارد (یعنی موفق، اما چیزی نیست).

**اگر مخزن محتوا داشته باشد:** لیست Branchها و Commit‌ها را نشان می‌دهد.

**اگر خطا بدهی:**
- `Authentication failed` → Token اشتباه.
- `Repository not found` → URL اشتباه یا مخزن وجود ندارد.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `git remote -v` | لیست Remoteها |
| `git remote add origin URL` | افزودن |
| `git remote set-url origin URL` | تغییر URL |
| `git remote remove origin` | حذف |
| `git ls-remote origin` | تست اتصال |

## آماده‌ای؟ برو به `03-first-push.md`.