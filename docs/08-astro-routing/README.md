# 🗺️ مسیریابی Astro

## این بخش چیست؟

در این بخش، **Routing** (مسیریابی) در Astro را یاد می‌گیری.

## Routing چیست؟

**Routing** یعنی: «چه URL چه صفحه‌ای را نشان دهد؟»

**مثال:**

| URL | صفحه |
|---|---|
| `/` | صفحه اصلی |
| `/about` | درباره من |
| `/portfolio` | لیست پروژه‌ها |
| `/portfolio/media-building-phase1` | جزئیات پروژه |

## چرا Routing مهم است؟

بدون Routing، سایت فقط یک صفحه دارد. **Routing سایت را به یک وب‌سایت چندصفحه‌ای تبدیل می‌کند.**

## فلسفه Astro: File-Based Routing

Astro از **File-Based Routing** استفاده می‌کند:

> **ساختار پوشه‌ها = ساختار URL**

**مثال:**

```
src/pages/
├── index.astro              → /
├── about.astro              → /about
├── contact.astro            → /contact
└── portfolio/
    ├── index.astro          → /portfolio
    └── [slug].astro         → /portfolio/:slug
```

## چه چیزی یاد می‌گیری؟

| فایل | موضوع |
|---|---|
| [01 - File-Based Routing](./01-file-based-routing.md) | مسیریابی از روی فایل |
| [02 - Dynamic Routes](./02-dynamic-routes.md) | `[slug].astro` |
| [03 - getStaticPaths](./03-get-static-paths.md) | ساخت مسیرهای داینامیک |
| [04 - Nested Routes](./04-nested-routes.md) | مسیرهای تودرتو |

## مسیرهای سایت ما

```
/                                   → صفحه اصلی
/about                              → درباره من
/services                           → خدمات
/contact                            → تماس
/portfolio                          → لیست پروژه‌ها
/portfolio/media-building-phase1    → پروژه شاخص
```

## آماده‌ای؟ برو به `01-file-based-routing.md`.