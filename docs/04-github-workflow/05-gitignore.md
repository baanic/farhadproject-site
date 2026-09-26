# فایل .gitignore

## 🎓 مفهوم

**`.gitignore`** فایلی است که به Git می‌گوید: «این فایل‌ها و پوشه‌ها را **نادیده بگیر**».

## 🎓 چرا .gitignore لازم است؟

### ۱. فایل‌های حجیم

مثل `node_modules` که می‌تواند ۲۰۰–۵۰۰ مگابایت باشد.

### ۲. فایل‌های حساس

مثل `.env` که رمزها را دارد.

### ۳. فایل‌های سیستم

مثل `.DS_Store` در macOS.

### ۴. فایل‌های موقت

مثل `*.log`، `dist/`.

## 🎓 قواعد `.gitignore`

### هر خط، یک الگو

```
node_modules/
*.log
.env
```

### علامت `/` در انتها

```
build/
```

پوشه `build` را نادیده بگیر. (نه فایلی به نام `build`).

### علامت `*`

```
*.log
```

همه فایل‌های `.log`.

```
*~
```

همه فایل‌ها با `~` در انتها.

### علامت `?`

```
file?.txt
```

فایل‌های `file1.txt`, `file2.txt`.

### علامت `!`

```
*.log
!important.log
```

همه `.log` را نادیده بگیر، **جز** `important.log`.

### مسیر مطلق (از ریشه)

```
/node_modules
```

فقط `node_modules` در ریشه پروژه را نادیده بگیر، نه زیرپوشه‌ها.

### مسیر نسبی

```
docs/notes/
```

هر `notes` در هر `docs`.

## 🎓 ساخت `.gitignore`

### روش ۱: دستی

```bash
touch .gitignore
code .gitignore
```

محتوا را پیست کن.

### روش ۲: با GitHub Templates

[github.com/github/gitignore](https://github.com/github/gitignore)

Templateهای آماده برای زبان‌ها.

### روش ۳: در VS Code

اگر Extension `.gitignore` نصب کنی، خودکار.

## 🎓 `.gitignore` ما

در پروژه ما، این محتوا را ساختیم:

```gitignore
# macOS
.DS_Store
.AppleDouble
.LSOverride

# Node
node_modules/
npm-debug.log*
yarn-error.log*
.pnpm-debug.log*

# Astro
dist/
.astro/

# Env
.env
.env.local
.env.*.local

# IDE
.vscode/*
!.vscode/extensions.json
.idea/

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
env/

# Excel temp
~$*.xlsx

# Output
*.log
```

### توضیح هر بخش

| بخش | توضیح |
|---|---|
| `# macOS` | فایل‌های سیستم |
| `.DS_Store` | فایل Finder مک |
| `node_modules/` | پوشه پکیج‌های Node |
| `dist/` | خروجی Build Astro |
| `.astro/` | کش Astro |
| `.env` | فایل رمزها |
| `.vscode/*` | تنظیمات VS Code |
| `!.vscode/extensions.json` | **استثنا:** این یکی نگه‌دار |
| `__pycache__/` | کش Python |
| `*.log` | همه فایل‌های لاگ |

## 🎓 نکته: `!` برای استثنا

```
.vscode/*
!.vscode/extensions.json
```

**ترجمه:**

- همه چیز در `.vscode` را نادیده بگیر.
- **اما** `extensions.json` را نگه‌دار.

**چرا؟**
- تنظیمات شخصی (مثل تم) را نمی‌خواهیم با تیم به اشتراک بگذاریم.
- اما Extensions موردنیاز پروژه را می‌خواهیم.

## 🎓 مشکل: فایل‌های Tracked که می‌خواهیم نادیده بگیریم

اگر فایلی **قبلاً Commit شده**، `.gitignore` روی آن اثر نمی‌کند.

**مثال:** `node_modules` را Commit کردی، الان می‌خواهی نادیده بگیریش.

**راه‌حل:**

```bash
# حذف از Git (اما نگه‌داشتن در سیستم)
git rm -r --cached node_modules

# اضافه به .gitignore
echo "node_modules/" >> .gitignore

# Commit
git add .gitignore
git commit -m "Remove node_modules from tracking"
```

**نکته مهم:** `--cached` یعنی «از Git حذف کن، اما فایل را از دیسک پاک نکن».

## 🎓 `.gitignore_global`

اگر می‌خواهی یک `.gitignore` سراسری داشته باشی (برای همه پروژه‌ها):

```bash
touch ~/.gitignore_global
code ~/.gitignore_global
```

محتوا:

```
.DS_Store
.Spotlight-V100
.Trashes
```

سپس تنظیم کن:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

## 🎓 بررسی اینکه چه چیزی ignore شده

```bash
git status --ignored
```

فایل‌های ignored را با رنگ متفاوت نشان می‌دهد.

**یا:**

```bash
git check-ignore -v node_modules
```

می‌گوید کدام rule آن را ignore کرده.

## 🛑 عیب‌یابی

### مشکل ۱: `.gitignore` کار نمی‌کند

**علت‌ها:**
- فایل قبلاً Commit شده.
- rule اشتباه است.

**راه‌حل:**

```bash
git rm -r --cached .
git add .
git commit -m "Refresh .gitignore"
```

⚠️ **هشدار:** این کار همه فایل‌ها را دوباره Stage می‌کند، اما commit history می‌ماند.

### مشکل ۲: `.env` را اشتباهاً Commit کردم

**فوراً:**

1. رمزها را عوض کن (چون در Git history هستند).
2. فایل را از Git حذف کن:

   ```bash
   git rm --cached .env
   echo ".env" >> .gitignore
   git add .gitignore
   git commit -m "Remove .env and add to gitignore"
   ```

⚠️ **نکته:** فایل در **تاریخچه** باقی می‌ماند. اگر خیلی حساس است، باید history را بازنویسی کنی (پیچیده).

### مشکل ۳: پوشه‌ای که می‌خواهم، نادیده گرفته می‌شود

**علت:** ممکن است یک rule گسترده آن را گرفته باشد.

**بررسی:**

```bash
git check-ignore -v path/to/folder
```

## 🎓 Templates آماده

GitHub یک مجموعه از `.gitignore` آماده دارد:

[github.com/github/gitignore](https://github.com/github/gitignore)

| فایل | محتوا |
|---|---|
| `Node.gitignore` | Node.js |
| `Python.gitignore` | Python |
| `macOS.gitignore` | macOS |
| `Global/` | سراسری |

می‌توانی ترکیب کنی.

**سایت مفید:** [gitignore.io](https://www.toptal.com/developers/gitignore)

## 🎁 خلاصه

| الگو | معنی |
|---|---|
| `node_modules/` | پوشه در هر عمق |
| `*.log` | همه `.log`ها |
| `/build` | فقط در ریشه |
| `!important.log` | استثنا |
| `file?.txt` | یک کاراکتر |

| دستور | کار |
|---|---|
| `git status --ignored` | نمایش ignoredها |
| `git check-ignore -v file` | بررسی یک فایل |
| `git rm -r --cached folder` | حذف از tracking |

## آماده‌ای؟ برو به `06-daily-workflow.md`.