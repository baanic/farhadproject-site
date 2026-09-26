# عملیات فایل و پوشه

## 🎓 مفهوم

در این فایل، کارهای روزمره با فایل‌ها و پوشه‌ها را یاد می‌گیری:
- ساخت
- کپی
- جابه‌جا کردن
- حذف کردن
- خواندن محتوا

## 🛠 دستور ۱: `mkdir` — ساخت پوشه

**M**a**k**e **Dir**ectory

### ساخت یک پوشه

```bash
mkdir my-folder
```

### ساخت چند پوشه با هم

```bash
mkdir folder1 folder2 folder3
```

### ساخت پوشه‌های تو در تو با `-p`

```bash
mkdir -p a/b/c/d
```

**چرا `-p` مهم است؟**
- بدون `-p`: اگر پوشه والد وجود نداشته باشد، خطا می‌دهد.
- با `-p`: خودش والدها را هم می‌سازد.

**مثال از پروژه ما:**

```bash
mkdir -p src/components/portfolio
```

این دستور، اگر `src` یا `components` نباشند، خودش می‌سازد.

## 🛠 دستور ۲: `touch` — ساخت فایل خالی

```bash
touch README.md
```

فایل جدید خالی می‌سازد.

**مثال از پروژه:**

```bash
touch docs/README.md
```

## 🛠 دستور ۳: `cp` — کپی کردن

**C**o**p**y

### کپی یک فایل

```bash
cp source.txt destination.txt
```

### کپی یک فایل به پوشه

```bash
cp file.txt Documents/
```

### کپی پوشه با `-r`

```bash
cp -r source-folder destination-folder
```

`-r` = Recursive (بازگشتی). برای پوشه‌ها الزامی است.

**مثال از پروژه ما:**

```bash
cp data/master_data.json astro-site/src/data/
```

## 🛠 دستور ۴: `mv` — جابه‌جا کردن یا تغییر نام

**M**o**v**e

### جابه‌جا کردن

```bash
mv file.txt Documents/
```

### تغییر نام

```bash
mv old-name.txt new-name.txt
```

### هر دو با هم

```bash
mv old-name.txt Documents/new-name.txt
```

**نکته:** `mv` برخلاف `cp`، فایل اصلی را حذف می‌کند.

## 🛠 دستور ۵: `rm` — حذف کردن

**R**e**m**ove

### حذف یک فایل

```bash
rm file.txt
```

### حذف پوشه با محتوا (خطرناک!)

```bash
rm -r folder-name
```

`-r` = Recursive.

### حذف با تأیید

```bash
rm -i file.txt
```

`-i` = Interactive (قبل از حذف می‌پرسد).

### حذف کامل بدون تأیید (خطر!)

```bash
rm -rf folder-name
```

⚠️ **هشدار جدی:** `rm -rf` بدون تأیید همه چیز را حذف می‌کند. **هیچ راه بازگشتی نیست.** از این دستور با احتیاط استفاده کن.

**مثال امن از پروژه ما:**

```bash
rm AGENTS.md CLAUDE.md
```

فقط دو فایل مشخص را حذف کردیم.

## 🛠 دستور ۶: `cat` — خواندن محتوا

**Con**catenate — نمایش محتوای فایل در ترمینال

```bash
cat file.txt
```

**مثال:**

```bash
cat package.json
```

محتوای فایل `package.json` را نشان می‌دهد.

### نسخه بهتر با `less`

اگر فایل بزرگ است:

```bash
less file.txt
```

با `Space` صفحه بعد، با `q` خارج شو.

## 🛠 دستور ۷: `code` — باز کردن در VS Code

اگر VS Code نصب است و در PATH قرار دارد:

```bash
code file.txt
```

فایل را در VS Code باز می‌کند.

### باز کردن کل پوشه

```bash
code .
```

`.` یعنی پوشه فعلی. این دستور، VS Code را با پوشه فعلی باز می‌کند.

**در این پروژه، هر جا خواستیم فایل بسازیم، اول `touch` زدیم، بعد `code`.**

## 🛠 تمرین: ساختار کامل پروژه

بیا ساختار پروژه‌مان را با هم بازسازی کنیم:

```bash
# از Home شروع
cd ~/Documents/Projects/farhadproject

# ساخت ساختار
mkdir -p docs/01-terminal-basics
mkdir -p docs/02-dev-environment
mkdir -p docs/03-git-fundamentals
mkdir -p python-scripts/outputs
mkdir -p data

# ساخت فایل‌ها
touch docs/README.md
touch docs/00-introduction.md
touch docs/01-terminal-basics/README.md
touch docs/01-terminal-basics/01-what-is-terminal.md

# بررسی
ls -la docs/
ls -la docs/01-terminal-basics/
```

## 🎓 ترفند: ترکیب چند دستور با `&&`

با `&&` می‌توانی چند دستور را پشت هم اجرا کنی. اگر اولی موفق باشد، دومی اجرا می‌شود.

```bash
cd ~/Documents/Projects/farhadproject && ls
```

**مثال پیچیده‌تر:**

```bash
mkdir -p docs/01-terminal-basics && cd docs/01-terminal-basics && touch README.md
```

اگر ساخت پوشه موفق باشد، واردش می‌شود، بعد فایل می‌سازد.

## 🎓 ترفند: History و Ctrl+R

هر دستوری که زدی، ذخیره می‌شود. برای جستجو:

- `Ctrl + R` بزن.
- شروع تایپ کن.
- Shell به‌طور هوشمند دستورهای قبلی را پیدا می‌کند.
- Enter برای اجرا، `Ctrl + C` برای انصراف.

## 🛑 خطاهای رایج

### `mkdir: file exists`

پوشه قبلاً ساخته شده. با `-p` دیگر خطا نمی‌دهد.

### `rm: permission denied`

اجازه حذف نداری. با `sudo rm` (خطرناک!) یا بررسی مجوزها.

### `cp: is a directory`

می‌خواهی فایل را کپی کنی، اما هدف پوشه است. با `cp -r` یا مقصد درست.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `mkdir name` | ساخت پوشه |
| `mkdir -p a/b/c` | ساخت پوشه تو در تو |
| `touch file.txt` | ساخت فایل خالی |
| `cp src dst` | کپی |
| `cp -r src dst` | کپی پوشه |
| `mv src dst` | جابه‌جایی یا تغییر نام |
| `rm file.txt` | حذف فایل |
| `rm -r folder` | حذف پوشه (خطرناک) |
| `rm -rf folder` | حذف کامل (خیلی خطرناک) |
| `cat file.txt` | نمایش محتوا |
| `less file.txt` | نمایش با اسکرول |
| `code file.txt` | باز کردن در VS Code |
| `code .` | باز کردن پوشه فعلی |

## آماده‌ای؟ برو به `04-command-cheatsheet.md`.