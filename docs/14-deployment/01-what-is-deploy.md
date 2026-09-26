# Deploy چیست؟

## 🎓 مفهوم

**Deploy** = انتقال سایت از کامپیوتر خودت به **سرور آنلاین**.

## 🎓 قبل از Deploy

```
[کامپیوتر خودت]
├── کد (src/)
├── Build (dist/)
└── localhost:4321

[هیچ‌کس نمی‌بیند]
```

## 🎓 بعد از Deploy

```
[سرور آنلاین]
├── فایل‌های Build
└── farhadproject.ir

[همه می‌بینند]
```

## 🎓 سه نوع Deploy

### ۱. Static Hosting

فایل‌های HTML/CSS/JS را روی یک سرور کپی می‌کنی.

**مثال:**
- Cloudflare Pages
- Netlify
- GitHub Pages
- Liara Static

**مناسب ما:** ✅ سایت ما Static است.

### ۲. Server (SSR)

سرور Node.js روی یک سرور اجرا می‌شود.

**مثال:**
- Liara
- Vercel
- Heroku

**مناسب ما:** ❌ (نیاز به SSR نداریم)

### ۳. Container (Docker)

کل اپ در یک Container.

**مثال:**
- Kubernetes
- AWS ECS

**مناسب ما:** ❌ (Over-engineering)

## 🎓 فلو Deploy

### مرحله ۱: Build

```bash
npm run build
```

**خروجی:** پوشه `dist/`.

### مرحله ۲: آپلود

فایل‌های `dist/` را به سرور می‌فرستی.

### مرحله ۳: DNS

دامنه `farhadproject.ir` به IP سرور اشاره می‌کند.

### مرحله ۴: SSL

گواهی HTTPS فعال می‌شود (Let's Encrypt).

### مرحله ۵: Deploy تمام

کاربر وارد `https://farhadproject.ir` می‌شود.

## 🎓 سه روش Deploy

### ۱. دستی (FTP/File Manager)

فایل‌ها را با FTP آپلود می‌کنی.

**مزیت:** ساده.
**عیب:** هر بار دستی.

### ۲. Git Push

GitHub → سرور خودکار Pull می‌کند.

**مزیت:** خودکار.
**عیب:** نیاز به Setup.

### ۳. CLI (توصیه‌شده)

با یک دستور:

```bash
liara deploy
```

**مزیت:** سریع، خودکار، ساده.

**ما از CLI استفاده می‌کنیم.**

## 🎓 مفهوم: Build Artifact

**Build Artifact** = فایل‌هایی که از Build می‌آید.

برای Astro:

```
dist/
├── index.html
├── about/index.html
├── portfolio/index.html
├── portfolio/media-building-phase1/index.html
├── _astro/                  ← CSS/JS
├── images/
├── fonts/
├── robots.txt
├── sitemap-index.xml
└── favicon.ico
```

**این پوشه، فقط HTML/CSS/JS است. بدون Node.js.**

## 🎓 چرا این روش خوب است؟

### ۱. سرعت

سرور فقط فایل می‌فرستد. بدون پردازش.

### ۲. امنیت

بدون Backend = بدون حمله.

### ۳. هزینه

ارزان، حتی رایگان.

### ۴. مقیاس‌پذیری

هر تعداد کاربر.

## 🎓 چرا Astro Static عالی است؟

- فایل‌های کوچک
- بدون سرور
- SSL ساده
- CDN-ready

## 🎓 انتخاب Platform

برای ما:

| Platform | مزیت | عیب |
|---|---|---|
| **Liara** ✅ | ایرانی، پشتیبانی Astro | پلن رایگان محدود |
| Vercel | رایگان، عالی | IP ایرانی ندارد |
| Netlify | رایگان | IP ایرانی ندارد |
| Cloudflare Pages | رایگان، سریع | IP ایرانی ندارد |
| GitHub Pages | رایگان | محدودیت |

**ما Liara انتخاب کردیم** چون:
- سرور داخل ایران
- سرعت بالا برای مخاطب ایرانی
- پشتیبانی فارسی
- Deploy ساده

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| Deploy | انتقال به سرور |
| Static Hosting | فایل‌های HTML |
| Build | `npm run build` |
| Artifact | خروجی `dist/` |
| CLI | ابزار خط فرمان |

## آماده‌ای؟ برو به `02-what-is-liara.md`.