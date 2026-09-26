# Sitemap

## 🎓 مفهوم

**Sitemap** یک فایل **XML** است که لیست **همه صفحات سایت** را به موتورهای جستجو می‌دهد.

## 🎓 چرا Sitemap؟

### ۱. کمک به Google

Google خودش سایت را Crawl می‌کند، اما Sitemap:
- سریع‌تر ایندکس می‌کند.
- صفحات تازه را سریع‌تر می‌فهمد.
- صفحات پنهان را هم می‌بیند.

### ۲. SEO

سایت با Sitemap، ایندکس بهتری دارد.

### ۳. استاندارد

همه سایت‌های حرفه‌ای Sitemap دارند.

## 🎓 انواع Sitemap

| نوع | کاربرد |
|---|---|
| **XML** ✅ | موتورهای جستجو |
| HTML | کاربران |
| TXT | ساده |
| RSS/Atom | بلاگ |

**ما از XML استفاده می‌کنیم.**

## 🛠 گام ۱: نصب `@astrojs/sitemap`

Astro یک Integration رسمی برای Sitemap دارد.

```bash
cd ~/Documents/Projects/farhadproject/astro-site
npx astro add sitemap
```

### سؤالات Astro

```
✔ Install the dependencies? ... Yes
✔ Update astro.config.mjs? ... Yes
```

**نتیجه:**
- پکیج `@astrojs/sitemap` نصب می‌شود.
- `astro.config.mjs` به‌روز می‌شود.

## 🛠 گام ۲: تنظیم `astro.config.mjs`

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://farhadproject.ir',
  integrations: [sitemap()],
});
```

### توضیح

| بخش | معنی |
|---|---|
| `site:` | URL سایت (اجباری) |
| `integrations: [sitemap()]` | فعال‌سازی Sitemap |

**نکته:** بدون `site`، Sitemap کار نمی‌کند.

## 🛠 گام ۳: Build

```bash
npm run build
```

**خروجی:**
```
dist/
├── sitemap-index.xml
├── sitemap-0.xml
└── ...
```

**نکته:** Astro دو فایل می‌سازد:
- `sitemap-index.xml` — ایندکس.
- `sitemap-0.xml` — خود Sitemap.

## 🎓 محتوای Sitemap

### `sitemap-index.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://farhadproject.ir/sitemap-0.xml</loc>
  </sitemap>
</sitemapindex>
```

### `sitemap-0.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://farhadproject.ir/</loc>
  </url>
  <url>
    <loc>https://farhadproject.ir/about/</loc>
  </url>
  <url>
    <loc>https://farhadproject.ir/portfolio/</loc>
  </url>
  <url>
    <loc>https://farhadproject.ir/portfolio/media-building-phase1/</loc>
  </url>
  <!-- بقیه صفحات -->
</urlset>
```

## 🎓 تست Sitemap

### در Dev Server

آدرس: `http://localhost:4321/sitemap-index.xml`.

### در Build

```bash
npm run build
npm run preview
```

آدرس: `http://localhost:4321/sitemap-index.xml`.

### در سایت نهایی

بعد از Deploy: `https://farhadproject.ir/sitemap-index.xml`.

## 🎓 فیلتر کردن Sitemap

اگر نخواهی صفحه‌ای در Sitemap باشد:

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://farhadproject.ir',
  integrations: [
    sitemap({
      filter: (page) =>
        page !== 'https://farhadproject.ir/private/' &&
        !page.includes('/404'),
    }),
  ],
});
```

**نکته:** صفحه `404` به‌طور خودکار فیلتر می‌شود.

## 🎓 Sitemap با i18n

اگر سایت چندزبانه داری:

```javascript
sitemap({
  i18n: {
    defaultLocale: 'fa',
    locales: {
      fa: 'fa-IR',
      en: 'en-US',
    },
  },
})
```

**توجه:** فعلاً ما تک‌زبانه هستیم.

## 🎓 افزودن Sitemap به robots.txt

فایل `public/robots.txt`:

```
User-agent: *
Allow: /

Sitemap: https://farhadproject.ir/sitemap-index.xml
```

**نکته:** این خط به Google می‌گوید Sitemap کجاست.

## 🎓 ثبت در Google Search Console

### گام ۱: ثبت سایت

1. برو به [search.google.com/search-console](https://search.google.com/search-console).
2. **Add Property**.
3. URL سایت را وارد کن.
4. تأیید مالکیت (از طریق DNS یا فایل HTML).

### گام ۲: ثبت Sitemap

1. در پنل، **Sitemaps** را باز کن.
2. URL Sitemap را وارد کن:
   ```
   https://farhadproject.ir/sitemap-index.xml
   ```
3. **Submit**.

**نتیجه:** Google شروع به Crawl می‌کند.

### گام ۳: بررسی

بعد از چند روز، تب **Coverage** نشان می‌دهد چند صفحه ایندکس شده.

## 🎓 محدودیت‌ها

| مورد | محدودیت |
|---|---|
| تعداد URL در هر Sitemap | ۵۰,۰۰۰ |
| حجم فایل | ۵۰ MB |
| تعداد Sitemap در Index | ۵۰,۰۰۰ |

**برای ما مشکلی نیست.**

## 🛑 عیب‌یابی

### مشکل ۱: Sitemap ساخته نمی‌شود

**علت:** `site` در `astro.config.mjs` نبوده.

**راه‌حل:**

```javascript
export default defineConfig({
  site: 'https://farhadproject.ir',  // ← اجباری
  integrations: [sitemap()],
});
```

### مشکل ۲: Sitemap خالی است

**علت:** صفحات Build نشده.

**راه‌حل:** `npm run build` بزن.

### مشکل ۳: در Google ثبت نمی‌شود

**علت:** URL اشتباه.

**راه‌حل:** از `sitemap-index.xml` استفاده کن، نه `sitemap-0.xml`.

### مشکل ۴: صفحات تازه در Sitemap نیستند

**علت:** Build دوباره اجرا نشده.

**راه‌حل:** هر بار که پروژه جدید اضافه می‌کنی، `npm run build` بزن.

## 🎓 فایل‌های تولیدی

```
dist/
├── sitemap-index.xml
├── sitemap-0.xml
└── ...
```

**نکته:** در Deploy، این دو فایل خودکار روی Liara می‌روند.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | `npx astro add sitemap` |
| ۲ | تنظیم `site` در Config |
| ۳ | `npm run build` |
| ۴ | تست |
| ۵ | ثبت در Google Search Console |

| فایل | کاربرد |
|---|---|
| `sitemap-index.xml` | ایندکس |
| `sitemap-0.xml` | URLها |

## آماده‌ای؟ برو به `05-robots-txt.md`.