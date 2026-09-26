# نصب و راه‌اندازی VS Code

## 🎓 VS Code چیست؟

**Visual Studio Code** — یا به‌اختصار **VS Code** — یک **ویرایشگر کد** رایگان از مایکروسافت.

### چرا VS Code؟

| مزیت | توضیح |
|---|---|
| **رایگان** | کاملاً باز و رایگان |
| **سبک** | سریع‌تر از Visual Studio کامل |
| **افزونه‌پذیر** | بیش از ۵۰,۰۰۰ افزونه |
| **چند زبانه** | JavaScript، Python، HTML، CSS و ... |
| **یکپارچه با Git** | Commit و Push داخل VS Code |
| **Terminal داخلی** | بدون رفتن به Terminal جدا |
| **محبوب** | استاندارد صنعت |

## 🛠 گام ۱: دانلود و نصب

### مک

1. برو به [code.visualstudio.com](https://code.visualstudio.com).
2. روی **Download for macOS** کلیک کن.
3. نسخه **Apple Silicon** یا **Intel** را انتخاب کن (بر اساس مک خودت).
4. فایل `.dmg` دانلود می‌شود.
5. فایل را باز کن.
6. آیکون VS Code را به پوشه **Applications** بکش.
7. VS Code را باز کن.

### ویندوز

1. برو به [code.visualstudio.com](https://code.visualstudio.com).
2. نسخه **Windows** را دانلود کن.
3. نصب کن (Next → Next → Install).

## 🛠 گام ۲: دستور `code` در ترمینال

برای اینکه بتوانی از ترمینال، فایل‌ها را در VS Code باز کنی:

### مک

1. VS Code را باز کن.
2. `Cmd + Shift + P` بزن.
3. تایپ کن: `Shell Command: Install 'code' command in PATH`.
4. Enter بزن.
5. VS Code پیغام موفقیت می‌دهد.

**بررسی:**

```bash
code --version
```

باید نسخه‌ای مثل `1.85.0` نشان دهد.

**مثال استفاده:**

```bash
code ~/Documents/Projects/farhadproject/README.md
```

یا:

```bash
code .
```

(پوشه فعلی را در VS Code باز می‌کند)

## 🎓 افزونه‌های ضروری برای این پروژه

بعد از نصب VS Code، این افزونه‌ها را نصب کن:

### ۱. Astro

**چرا:** پشتیبانی از فایل‌های `.astro` (رنگ‌آمیزی، Autocomplete، Format).

**نصب:**
1. `Cmd + Shift + X` (باز کردن Extensions).
2. جستجو کن: `Astro`.
3. تأیید شده توسط Astro Team.
4. Install.

### ۲. Shabnam Font

**چرا:** فونت فارسی.

**نصب:**
- فونت Shabnam را در سیستم نصب کن (از سایت اصلی).
- در تنظیمات VS Code، فونت را Shabnam بگذار.

**تنظیمات:**

1. `Cmd + ,` (باز کردن Settings).
2. جستجو: `font family`.
3. مقدار را بگذار: `'Shabnam', Menlo, Monaco, 'Courier New', monospace`.

### ۳. Markdown All in One

**چرا:** نوشتن مستندات راحت‌تر.

**نصب:**
- Extensions → `Markdown All in One` → Install.

**ویژگی‌ها:**
- پیش‌نمایش زنده (Cmd + K, V).
- Format خودکار.
- Toggle checkbox با `Cmd + Alt + X`.

### ۴. GitLens

**چرا:** مشاهده تاریخچه Git هر خط کد.

**نصب:**
- Extensions → `GitLens` → Install.

**ویژگی‌ها:**
- چه کسی این خط را نوشته و کی؟
- مقایسه نسخه‌ها.

### ۵. Prettier

**چرا:** Format خودکار کد.

**نصب:**
- Extensions → `Prettier` → Install.

**تنظیمات:**

1. Settings → جستجو: `format on save`.
2. تیک **Editor: Format On Save**.

## 🎓 آشنایی با رابط VS Code

وقتی VS Code باز می‌کنی، این بخش‌ها را می‌بینی:

```
┌─────────────────────────────────────────────────┐
│  File  Edit  View  ...              ← منوی بالا  │
├──────┬──────────────────────────────────────────┤
│      │                                          │
│      │                                          │
│ Side │        Editor Area                       │
│ bar  │        (محل کد نوشتن)                    │
│      │                                          │
│      │                                          │
├──────┴──────────────────────────────────────────┤
│  Terminal / Problems / Output      ← پنل پایین   │
└─────────────────────────────────────────────────┘
```

### Activity Bar (نوار کناری)

آیکون‌های عمودی در سمت چپ:

| آیکون | کار |
|---|---|
| 📁 | Explorer (فایل‌ها) |
| 🔍 | Search |
| 🔀 | Source Control (Git) |
| 🐛 | Run and Debug |
| 🧩 | Extensions |

### Command Palette

**مهم‌ترین ویژگی VS Code.** با `Cmd + Shift + P` باز می‌شود.

هر کاری که VS Code می‌تواند بکند، از اینجا قابل اجرا است.

**مثال:**
- `format document` → Format کردن فایل.
- `git commit` → Commit زدن.
- `change language mode` → تغییر زبان فایل.

## 🎓 تنظیمات پیشنهادی برای این پروژه

فایل `.vscode/settings.json` در پروژه ما:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000
}
```

این فایل در VS Code تنظیمات را اعمال می‌کند.

## 🛠 کارهای روزمره در VS Code

### باز کردن یک پروژه

```bash
cd ~/Documents/Projects/farhadproject
code .
```

### باز کردن یک فایل خاص

```bash
code src/pages/index.astro
```

### اجرای ترمینال داخلی

- `Cmd + `` ` (Backtick)
- یا **View → Terminal**

### جستجو در کل پروژه

- `Cmd + Shift + F`
- جستجو در همه فایل‌ها.

### رفتن به فایل سریع

- `Cmd + P`
- تایپ کن اسم فایل.
- Enter.

### رفتن به خط خاص

- `Ctrl + G`
- شماره خط.

### کامنت کردن خط

- `Cmd + /`
- برای تک‌خطی.
- `Shift + Alt + A` برای بلوک کامنت.

### کپی خط

- `Shift + Option + ↓`
- یا `Shift + Option + ↑`

### حرکت خط

- `Option + ↓` یا `Option + ↑`

## 🎓 ترفند: Multi-Cursor

می‌خواهی چند جا با هم تایپ کنی؟

**راه ۱:** `Option + Click` — هرجا کلیک کنی، یک Cursor اضافه می‌شود.

**راه ۲:** `Cmd + D` — کلمه فعلی را انتخاب کن، دوباره بزن، کلمه بعدی مشابه انتخاب می‌شود.

**راه ۳:** `Cmd + Shift + L` — همه کلمات مشابه در فایل انتخاب می‌شوند.

## 🛑 عیب‌یابی

### مشکل ۱: `code: command not found`

**راه‌حل:**
- `Cmd + Shift + P` → `Shell Command: Install 'code' command in PATH`.
- ترمینال را ببند و باز کن.

### مشکل ۲: فونت فارسی به‌هم‌ریخته است

**راه‌حل:**
- فونت Shabnam را در سیستم نصب کن.
- در Settings، Font Family را Shabnam بگذار.
- `Cmd + ,` → `editor.fontFamily`.

### مشکل ۳: VS Code کند است

**راه‌حل:**
- افزونه‌های غیرضروری را حذف کن.
- `Cmd + Shift + P` → `Developer: Reload Window`.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `code .` | باز کردن پوشه فعلی |
| `code file.txt` | باز کردن فایل |
| `Cmd + Shift + P` | Command Palette |
| `Cmd + P` | پیدا کردن فایل |
| `Cmd + `` ` | Terminal داخلی |
| `Cmd + /` | کامنت |
| `Cmd + D` | انتخاب کلمه مشابه |

## 🎉 پایان بخش ۰۲

تبریک! محیط توسعه کامل نصب شد. حالا می‌توانی:
- Node.js بنویسی و اجرا کنی.
- پکیج‌های npm نصب کنی.
- کد را در VS Code ویرایش کنی.

## گام بعدی: `../03-git-fundamentals/`.