# تنظیمات اولیه Git

## 🎓 چرا تنظیمات اولیه لازم است؟

Git باید بداند **تو کی هستی**. هر Commit با نام و ایمیل تو ثبت می‌شود.

**اگر تنظیم نکنی:**

```
*** Please tell me who you are.
Run:
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```

## 🛠 گام ۱: تنظیم نام

```bash
git config --global user.name "Farhad Rezaei"
```

**نکات:**
- اسم واقعی یا نام مستعار بنویس.
- آنچه اینجا می‌نویسی، در هر Commit نمایش داده می‌شود.
- در GitHub، این نام بالای Commit‌هاست.

## 🛠 گام ۲: تنظیم ایمیل

```bash
git config --global user.email "farhadrezaei.eng@gmail.com"
```

**نکته مهم:** حتماً **همان ایمیل GitHub** را وارد کن. چرا؟

- GitHub از ایمیل برای تشخیص هویت استفاده می‌کند.
- اگر ایمیل متفاوت باشد، Commit‌ها به پروفایل GitHub وصل نمی‌شوند.
- روی آواتار تو در GitHub، آیکون‌ها سبز نمی‌شوند.

### بررسی ایمیل GitHub

1. برو به [github.com/settings/emails](https://github.com/settings/emails).
2. ایمیل اصلی را ببین.
3. همان را در Git تنظیم کن.

## 🛠 گام ۳: تنظیم Branch پیش‌فرض

```bash
git config --global init.defaultBranch main
```

**توضیح:**

| کلمه | معنی |
|---|---|
| `--global` | تنظیم سراسری (همه پروژه‌ها) |
| `init.defaultBranch` | نام Branch پیش‌فرض |
| `main` | نام جدید |

**چرا `main`؟**

- Git قدیمی از `master` استفاده می‌کرد.
- از سال ۲۰۲۰، استاندارد جدید `main` است.
- GitHub هم `main` را پیش‌فرض گذاشته.

**مقایسه:**

```
قبل: git init → master
حالا: git init → main
```

## 🛠 گام ۴: تنظیمات تکمیلی (اختیاری)

### تنظیم ویرایشگر

```bash
git config --global core.editor "code --wait"
```

**چرا؟**

بعضی وقت‌ها Git می‌خواهد پیامی طولانی بنویسی (مثلاً Merge). به‌جای ویرایشگر خط فرمان، VS Code باز می‌شود.

- `code` = VS Code
- `--wait` = Git صبر می‌کند تا فایل را ببندی.

### تنظیم رفتار Pull

```bash
git config --global pull.rebase false
```

**توضیح:** مشخص می‌کند که هنگام `git pull`، Merge انجام دهد یا Rebase. برای مبتدی، `false` (Merge) ساده‌تر است.

### رنگی کردن خروجی

```bash
git config --global color.ui auto
```

**چرا؟**
خروجی Git با رنگ نمایش داده می‌شود. تفاوت‌ها راحت‌تر دیده می‌شوند.

### مخفی کردن فایل‌های ناخواسته

```bash
git config --global core.excludesfile ~/.gitignore_global
```

**توضیح:** یک فایل `.gitignore_global` می‌سازی که در همه پروژه‌ها اعمال می‌شود. برای فایل‌های سیستم مثل `.DS_Store`.

## 🛠 گام ۵: بررسی تنظیمات

```bash
git config --list
```

خروجی نمونه:

```
user.name=Farhad Rezaei
user.email=farhadrezaei.eng@gmail.com
init.defaultbranch=main
core.editor=code --wait
pull.rebase=false
color.ui=auto
```

### بررسی یک تنظیم خاص

```bash
git config user.name
```

خروجی: `Farhad Rezaei`.

## 🎓 مفهوم: `--global` vs `--local`

| نوع | محل ذخیره | اعمال برای |
|---|---|---|
| `--global` | `~/.gitconfig` | همه پروژه‌ها |
| `--local` | `.git/config` در هر پروژه | فقط همان پروژه |
| `--system` | `/etc/gitconfig` | همه کاربران |

**توصیه:**

- برای نام و ایمیل: `--global` (یک بار برای همه).
- برای تنظیمات خاص پروژه (مثل URL متفاوت): `--local`.

## 🎓 تنظیمات پروژه‌ای (Local)

اگر خواستی برای یک پروژه، تنظیمات متفاوت داشته باشی:

```bash
cd ~/Documents/Projects/farhadproject
git config user.name "Farhad R."
git config user.email "work@example.com"
```

**بدون `--global`**. این تنظیمات فقط برای این پروژه اعمال می‌شود.

**بررسی:**

```bash
git config --list --local
```

## 🎓 ذخیره‌سازی تنظیمات

Git تنظیمات را کجا ذخیره می‌کند؟

### فایل `~/.gitconfig`

```bash
cat ~/.gitconfig
```

خروجی نمونه:

```
[user]
    name = Farhad Rezaei
    email = farhadrezaei.eng@gmail.com
[init]
    defaultBranch = main
[core]
    editor = code --wait
[pull]
    rebase = false
```

این فایل متنی است. می‌توانی مستقیم ویرایش کنی.

## 🛠 تمرین: تنظیمات ما

در پروژه ما، این دستورات اجرا شد:

```bash
git config --global user.name "Farhad Rezaei"
git config --global user.email "farhadrezaei.eng@gmail.com"
git config --global init.defaultBranch main
```

برای بررسی:

```bash
git config --list
```

## 🛑 عیب‌یابی

### مشکل ۱: نام فارسی نمایش داده نمی‌شود

**علت:** مشکل انکودینگ در ترمینال.

**راه‌حل:**
- نام را به انگلیسی بنویس.
- یا در GitHub، نام نمایشی فارسی بگذار (فایل `.gitconfig` را انگلیسی نگه دار).

### مشکل ۲: Commit‌ها در GitHub نمایش داده نمی‌شوند

**علت:** ایمیل Git با ایمیل GitHub مطابقت ندارد.

**راه‌حل:**

1. ایمیل GitHub را بررسی کن.
2. ایمیل Git را اصلاح کن:
   ```bash
   git config --global user.email "correct@email.com"
   ```
3. اگر Commit قبلاً ثبت شده، می‌توانی اصلاح کنی (پیچیده‌تر).

### مشکل ۳: تنظیمات اعمال نمی‌شود

**علت:** ممکن است تنظیمات Local روی Global را override کند.

**راه‌حل:**

```bash
git config --list --show-origin
```

این دستور نشان می‌دهد هر تنظیم از کجا می‌آید.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `git config --global user.name "..."` | نام |
| `git config --global user.email "..."` | ایمیل |
| `git config --global init.defaultBranch main` | Branch پیش‌فرض |
| `git config --list` | نمایش همه تنظیمات |
| `git config user.name` | نمایش یک تنظیم |

## آماده‌ای؟ برو به `04-three-areas.md`.