# File-Based Routing

## 🎓 مفهوم

**File-Based Routing** یعنی: هر **فایل** در پوشه `src/pages/` = یک **صفحه** در سایت.

## 🎓 قاعده ساده

```
src/pages/index.astro       →  /
src/pages/about.astro       →  /about
src/pages/contact.astro     →  /contact
src/pages/blog/index.astro  →  /blog
```

**قاعده:**
- نام فایل = نام URL.
- `index.astro` = صفحه اصلی همان پوشه.
- پوشه = بخشی از URL.

## 🛠 مثال‌های مختلف

### ۱. صفحه ریشه

```
src/pages/index.astro
```

**URL:** `/`

**کد:**

```astro
---
const title = "خانه";
---

<html>
  <head><title>{title}</title></head>
  <body>
    <h1>صفحه اصلی</h1>
  </body>
</html>
```

### ۲. صفحه ساده

```
src/pages/about.astro
```

**URL:** `/about`

### ۳. صفحه در پوشه

```
src/pages/blog/index.astro
```

**URL:** `/blog`

**نکته:** `index.astro` یعنی «صفحه اصلی این پوشه».

### ۴. صفحه تودرتو

```
src/pages/portfolio/projects.astro
```

**URL:** `/portfolio/projects`

**نکته:** `projects.astro` یعنی یک فایل با نام `projects`. نام فایل = نام URL.

### ۵. صفحه در پوشه عمیق

```
src/pages/portfolio/2024/q1/index.astro
```

**URL:** `/portfolio/2024/q1`

## 🎓 نام‌گذاری فایل‌ها

### قاعده

| نام فایل | URL |
|---|---|
| `index.astro` | `/` |
| `about.astro` | `/about` |
| `contact-us.astro` | `/contact-us` |
| `blog/post-1.astro` | `/blog/post-1` |

### نکات مهم

1. **حروف کوچک:** `about.astro`، نه `About.astro`.
2. **kebab-case:** `contact-us.astro`، نه `contact_us.astro`.
3. **بدون فاصله:** `my-page.astro`.

## 🎓 URL نهایی

هر فایل `.astro` در `pages/`، در Build به HTML تبدیل می‌شود:

| فایل | خروجی |
|---|---|
| `index.astro` | `dist/index.html` |
| `about.astro` | `dist/about/index.html` |
| `blog/index.astro` | `dist/blog/index.html` |
| `blog/post-1.astro` | `dist/blog/post-1/index.html` |

**نکته:** Astro پوشه می‌سازد تا URL تمیز باشد:

- `/about` (نه `/about.html`).

## 🛠 ساخت صفحه جدید

### گام ۱: ساخت فایل

```bash
cd ~/Documents/Projects/farhadproject/astro-site
code src/pages/new-page.astro
```

### گام ۲: کد حداقلی

```astro
---
const title = "صفحه جدید";
---

<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <title>{title}</title>
  </head>
  <body>
    <h1>صفحه جدید</h1>
  </body>
</html>
```

### گام ۳: تست

مرورگر: `http://localhost:4321/new-page`

**Hot Reload** خودکار صفحه را نشان می‌دهد.

## 🎓 Link بین صفحات

### لینک معمولی (HTML)

```astro
<a href="/about">درباره من</a>
```

**نکته:** URL در `href` بدون `.html`.

### لینک با Navbar

```astro
---
const menu = [
  { label: "خانه", href: "/" },
  { label: "درباره", href: "/about" },
  { label: "تماس", href: "/contact" },
];
---

<nav>
  {menu.map(item => (
    <a href={item.href}>{item.label}</a>
  ))}
</nav>
```

### لینک به صفحه داینامیک

```astro
<a href={`/portfolio/${project.slug}`}>
  {project.title_fa}
</a>
```

## 🎓 صفحه 404

Astro خودکار یک صفحه 404 دارد. برای سفارشی‌سازی:

```bash
code src/pages/404.astro
```

```astro
---
const title = "صفحه پیدا نشد";
---

<html lang="fa" dir="rtl">
  <head>
    <title>{title}</title>
  </head>
  <body style="text-align: center; padding: 100px 20px;">
    <h1 style="font-size: 72px; color: #1B2A4A;">۴۰۴</h1>
    <p>صفحه‌ای که می‌خواهید پیدا نشد.</p>
    <a href="/" style="color: #B8763E;">بازگشت به خانه</a>
  </body>
</html>
```

## 🎓 صفحه‌های خاص

### `src/pages/sitemap.xml.ts`

می‌توانی فایل‌های غیر Astro هم بسازی (`.ts`, `.js`) که خروجی مختلف بدهند:

```typescript
// sitemap.xml.ts
export async function GET() {
  const sitemap = `<?xml version="1.0"?>
    <urlset>
      <url><loc>https://farhadproject.ir</loc></url>
    </urlset>
  `;

  return new Response(sitemap, {
    headers: { "Content-Type": "application/xml" },
  });
}
```

**URL:** `/sitemap.xml`.

**نکته:** ما از پکیج `@astrojs/sitemap` استفاده می‌کنیم که این کار را خودکار انجام می‌دهد.

## 🎓 اولویت مسیرها

اگر دو فایل باشند که یک URL بسازند:

```
src/pages/about.astro
src/pages/about/index.astro
```

**Astro خطا می‌دهد.** URL تکراری نمی‌شود.

## 🎓 فایل‌های غیرصفحه‌ای

اگر فایلی بخواهی که **صفحه نباشد** (مثل Utility)، در `src/pages/` نگذار.

**محل‌های دیگر:**

- `src/components/` — Componentها
- `src/lib/` — توابع کمکی
- `src/utils/` — Utilityها

## 🎓 مثال کامل از پروژه ما

### ساختار `src/pages/`

```
src/pages/
├── index.astro
├── about.astro
├── services.astro
├── contact.astro
├── 404.astro
└── portfolio/
    ├── index.astro
    └── [slug].astro
```

### URLهای حاصل

| URL | فایل |
|---|---|
| `/` | `index.astro` |
| `/about` | `about.astro` |
| `/services` | `services.astro` |
| `/contact` | `contact.astro` |
| `/portfolio` | `portfolio/index.astro` |
| `/portfolio/media-building-phase1` | `portfolio/[slug].astro` |

## 🎓 در VS Code

- VS Code هر فایل `.astro` را با رنگ‌آمیزی نشان می‌دهد.
- Extension **Astro** رسمی را نصب کن.

## 🛑 عیب‌یابی

### مشکل ۱: صفحه 404 می‌دهد

**علت‌ها:**
- نام فایل اشتباه.
- مسیر اشتباه.
- Dev Server نیاز به Restart.

**راه‌حل:**
- فایل را بررسی کن.
- Dev Server را ببند و باز کن.

### مشکل ۲: Link کار نمی‌کند

**علت:** `href` اشتباه.

**راه‌حل:**
- URL نسبی از `/` شروع شود.
- بدون `.html`.

### مشکل ۳: فایل `.astro` کامپایل نمی‌شود

**علت:** خطای Syntax.

**راه‌حل:** خطای ترمینال را بخوان و اصلاح کن.

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| فایل = URL | `about.astro` = `/about` |
| `index.astro` | صفحه اصلی پوشه |
| پوشه | بخشی از URL |
| Link | `<a href="/about">` |
| 404 | `src/pages/404.astro` |

## آماده‌ای؟ برو به `02-dynamic-routes.md`.