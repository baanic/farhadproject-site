# نصب Astro

## 🎓 پیش‌نیاز

- Node.js نصب
- npm نصب
- Terminal

**بررسی:**

```bash
node --version
npm --version
```

باید نسخه نشان دهند.

## 🛠 گام ۱: رفتن به پوشه پروژه

```bash
cd ~/Documents/Projects/farhadproject
mkdir -p astro-site
cd astro-site
```

**چرا `astro-site` جدا؟**

پروژه ما **مونوریپو** است:
- `python-scripts/` — کد Python
- `astro-site/` — کد سایت
- `docs/` — مستندات

**مزیت:** همه چیز در یک مخزن GitHub.

## 🛠 گام ۲: اجرای دستور Astro

```bash
npm create astro@latest .
```

### آناتومی دستور

| بخش | معنی |
|---|---|
| `npm create` | اجرای یک اسکریپت ساخت پروژه |
| `astro@latest` | آخرین نسخه Astro |
| `.` | در پوشه فعلی نصب کن |

**نکته:** اگر `.` نگذاری، Astro یک پوشه جدید می‌سازد.

## 🛠 گام ۳: پاسخ به سؤالات

Astro چند سؤال می‌پرسد:

### سؤال ۱: How would you like to start?

```
◯ Include sample files (recommended)
◯ Use blog template
◯ Empty
```

**انتخاب:** **Empty**

**چرا؟**
- می‌خواهیم از صفر یاد بگیریم.
- فایل‌های نمونه، گیج‌کننده هستند.
- کنترل کامل داریم.

**حرکت:** فلش پایین → Enter.

### سؤال ۲: Install dependencies?

```
◯ Yes
◯ No
```

**انتخاب:** **Yes**

**چرا؟** npm پکیج‌های لازم را نصب می‌کند.

### سؤال ۳: Initialize a git repository?

```
◯ Yes
◯ No
```

**انتخاب:** **No** ⚠️

**چرا؟** ما در پوشه `farhadproject` یک مخزن Git داریم. اگر اینجا هم `git init` شود، **دو مخزن** می‌شود و تداخل پیش می‌آید.

### سؤال ۴: Do you plan to write TypeScript?

```
◯ Yes
◯ No
```

**انتخاب:** **Yes**

**چرا؟** TypeScript به کد **Type Safety** می‌دهد. کمک می‌کند خطاها را زودتر بگیری.

**نکته:** TypeScript **جایگزین** JavaScript است، اما سخت‌گیرتر.

### سؤال ۵: How strict?

```
◯ Strict
◯ Strictest
◯ Relaxed
```

**انتخاب:** **Strict** (پیش‌فرض)

**چرا؟** برای پروژه‌های جدی، Strict بهتر است.

## 🎓 چه اتفاقی می‌افتد؟

بعد از پاسخ‌ها:

1. **Astro کد را نصب می‌کند.**
2. **پکیج‌ها نصب می‌شوند** (۱–۳ دقیقه).
3. **فایل‌ها ساخته می‌شوند:**

```
astro-site/
├── .gitignore
├── astro.config.mjs
├── package.json
├── tsconfig.json
├── public/
├── src/
│   ├── pages/
│   └── assets/
└── node_modules/
```

## 🛠 گام ۴: بررسی نصب

```bash
ls -la
```

باید ببینی:

```
.gitignore
astro.config.mjs
package.json
public/
src/
tsconfig.json
node_modules/
```

## 🛠 گام ۵: بررسی `package.json`

```bash
cat package.json
```

**خروجی نمونه:**

```json
{
  "name": "astro-site",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^5.x.x"
  }
}
```

**بخش مهم: `scripts`**

| اسکریپت | کار |
|---|---|
| `dev` | اجرای سرور توسعه |
| `build` | ساخت خروجی نهایی |
| `preview` | پیش‌نمایش خروجی Build |

## 🛠 گام ۶: حذف فایل‌های اضافه

Astro در نسخه‌های جدید، فایل‌هایی برای هوش مصنوعی می‌سازد:

```bash
rm AGENTS.md CLAUDE.md
```

**این‌ها فایل‌های راهنما برای AI Agents هستند، ربطی به پروژه ما ندارند.**

## 🛠 گام ۷: بررسی `.gitignore`

```bash
cat .gitignore
```

باید ببینی:

```
node_modules/
dist/
.astro/
.env
.DS_Store
```

**آسترو خودش این‌ها را نادیده می‌گیرد.** ✅

## 🎓 در VS Code

```bash
code .
```

پروژه در VS Code باز می‌شود. ساختار را در سایدبار ببین.

## 🛑 عیب‌یابی

### مشکل ۱: `npm create astro@latest` کند است

**علت:** دانلود از سرورهای خارجی.

**راه‌حل:** صبر کن.

### مشکل ۲: خطای network

**علت:** فیلتر.

**راه‌حل:** از VPN استفاده کن.

### مشکل ۳: Astro خطای Node version می‌دهد

**علت:** Node قدیمی.

**راه‌حل:**

```bash
nvm install --lts
nvm use --lts
```

### مشکل ۴: می‌خواهم Astro را حذف و دوباره نصب کنم

```bash
cd ~/Documents/Projects/farhadproject
rm -rf astro-site
mkdir astro-site
cd astro-site
npm create astro@latest .
```

## 🎓 در پروژه ما

دقیقاً همین مراحل را انجام دادیم. Astro در `astro-site/` نصب شد و همه پکیج‌ها آماده شدند.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | پوشه `astro-site` بساز |
| ۲ | `npm create astro@latest .` |
| ۳ | Empty، Yes، No، Yes، Strict |
| ۴ | بررسی فایل‌ها |
| ۵ | حذف فایل‌های AI |
| ۶ | باز کردن در VS Code |

## آماده‌ای؟ برو به `04-project-structure.md`.