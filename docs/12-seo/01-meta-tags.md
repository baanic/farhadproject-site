# Meta Tags

## 🎓 مفهوم

**Meta Tags** تگ‌های HTML هستند که اطلاعات **درباره صفحه** را به مرورگر و موتورهای جستجو می‌دهند.

## 🎓 انواع Meta Tags

| تگ | کاربرد |
|---|---|
| `<title>` | عنوان صفحه |
| `description` | توضیح کوتاه |
| `author` | نویسنده |
| `viewport` | تنظیمات موبایل |
| `charset` | انکودینگ |
| `canonical` | URL اصلی |
| `robots` | راهنمای موتور جستجو |
| `theme-color` | رنگ نوار مرورگر |

## 🎓 تگ `<title>`

**مهم‌ترین تگ** برای SEO.

### ساختار

```html
<title>عنوان صفحه | نام سایت</title>
```

### قواعد

| قاعده | مثال |
|---|---|
| **حداکثر ۶۰ کاراکتر** | نه بیشتر |
| **شامل کلمه کلیدی** | «پرتفولیو مهندسی» |
| **یکتا** در هر صفحه | نه تکراری |
| **خوانا** برای انسان | نه فقط کلمات کلیدی |

### در Astro

```astro
---
const { title } = Astro.props;
const siteName = "پرتفولیو فرهاد";
---

<title>{title ? `${title} | ${siteName}` : siteName}</title>
```

**نتیجه:**

| `title` | خروجی |
|---|---|
| `"خانه"` | `خانه \| پرتفولیو فرهاد` |
| `undefined` | `پرتفولیو فرهاد` |

## 🎓 تگ `description`

**دومین تگ مهم** برای SEO.

### ساختار

```html
<meta name="description" content="توضیح کوتاه صفحه" />
```

### قواعد

| قاعده | مثال |
|---|---|
| **حداکثر ۱۶۰ کاراکتر** | نه بیشتر |
| **شامل کلمه کلیدی** | بله |
| **مفید برای کاربر** | نه فقط کلمات کلیدی |
| **یکتا** در هر صفحه | بله |

### در Astro

```astro
---
const { description = "پرتفولیو تخصصی در حوزه دفتر فنی، کنترل پروژه، متره و برآورد و آکوستیک." } = Astro.props;
---

<meta name="description" content={description} />
```

## 🎓 تگ `viewport`

**ضروری برای موبایل.**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

**ترجمه:**
- `width=device-width`: عرض صفحه = عرض دستگاه.
- `initial-scale=1.0`: زوم اولیه ۱۰۰٪.

**بدون آن:** سایت روی موبایل کوچک نمایش داده می‌شود.

## 🎓 تگ `charset`

**ضروری برای فارسی.**

```html
<meta charset="UTF-8" />
```

**UTF-8** = استاندارد برای پشتیبانی از همه زبان‌ها (فارسی، عربی، چینی و ...).

**بدون آن:** کاراکترهای فارسی «??????» نمایش داده می‌شوند.

## 🎓 تگ `author`

```html
<meta name="author" content="فرهاد رضائی" />
```

**کاربرد:** نسبت دادن محتوا به نویسنده.

## 🎓 تگ `canonical`

**مشکل تکراری بودن محتوا:**

اگر صفحه `example.com/products` و `example.com/products?page=1` محتوای یکسان داشته باشند، Google نمی‌داند کدام **اصلی** است.

**راه‌حل:**

```html
<link rel="canonical" href="https://farhadproject.ir/about" />
```

**ترجمه:** «این URL اصلی است.»

## 🎓 تگ `robots`

```html
<meta name="robots" content="index, follow" />
```

| مقدار | معنی |
|---|---|
| `index` | صفحه را ایندکس کن |
| `noindex` | ایندکس نکن |
| `follow` | لینک‌ها را دنبال کن |
| `nofollow` | دنبال نکن |

**پیش‌فرض:** `index, follow`.

**استفاده `noindex`:** برای صفحات محرمانه.

## 🎓 تگ `theme-color`

```html
<meta name="theme-color" content="#1B2A4A" />
```

**کاربرد:** رنگ نوار بالای مرورگر موبایل (Android Chrome).

## 🛠 پیاده‌سازی در `BaseLayout.astro`

```astro
---
import "../styles/global.css";
import Footer from "../components/Footer.astro";

const {
  title,
  description,
  ogImage = "/images/og-image.jpg",
} = Astro.props;

const siteName = "پرتفولیو فرهاد";
const siteUrl = "https://farhadproject.ir";
const defaultDescription = "پرتفولیو تخصصی در حوزه دفتر فنی، کنترل پروژه، متره و برآورد و طراحی و اجرای آکوستیک.";

const pageTitle = title ? `${title} | ${siteName}` : siteName;
const pageDescription = description || defaultDescription;
const canonicalUrl = new URL(Astro.url.pathname, siteUrl).toString();
---

<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>{pageTitle}</title>
    <meta name="description" content={pageDescription} />
    <meta name="author" content="فرهاد رضائی" />
    <link rel="canonical" href={canonicalUrl} />

    <meta name="theme-color" content="#1B2A4A" />
  </head>
  <body>
    <slot />
    <Footer />
  </body>
</html>
```

## 🎓 آناتومی کد

### `new URL(Astro.url.pathname, siteUrl)`

**`Astro.url.pathname`** = مسیر فعلی (مثل `/about`).

**`new URL(...)`** = ساخت URL کامل.

**نتیجه:** `https://farhadproject.ir/about`.

## 🎓 بررسی Meta Tags

### در Chrome

1. `F12`.
2. تب **Elements**.
3. تگ `<head>` را باز کن.
4. Meta Tags را می‌بینی.

### ابزار آنلاین

- [metatags.io](https://metatags.io) — پیش‌نمایش
- [metatag.io](https://metatag.io) — بررسی

### Google Search Console

- [search.google.com/search-console](https://search.google.com/search-console)
- بعد از Deploy، سایت را ثبت کن.
- Google خودش تحلیل می‌کند.

## 🎓 بهترین تمرین‌ها

### ۱. عنوان توصیفی

```html
<!-- ✅ خوب -->
<title>دفتر فنی و کنترل پروژه | پرتفولیو فرهاد</title>

<!-- ❌ بد -->
<title>صفحه اصلی</title>
```

### ۲. توضیح مفید

```html
<!-- ✅ خوب -->
<meta name="description" content="تجربه اجرایی در دفتر فنی، کنترل پروژه، متره و برآورد و طراحی آکوستیک." />

<!-- ❌ بد -->
<meta name="description" content="بهترین سایت. همه چیز. تماس." />
```

### ۳. Canonical درست

```html
<link rel="canonical" href="https://farhadproject.ir/about" />
```

**نکته:** از `https` و `www` یا بدون آن، **ثابت** استفاده کن.

## 🛑 عیب‌یابی

### مشکل ۱: فارسی «??????» نمایش داده می‌شود

**علت:** `<meta charset="UTF-8">` نبوده.

**راه‌حل:** اضافه کن.

### مشکل ۲: سایت روی موبایل کوچک است

**علت:** `<meta name="viewport">` نبوده.

**راه‌حل:** اضافه کن.

### مشکل ۳: عنوان در Google نمایش داده نمی‌شود

**علت:** Google ممکن است **خودش** عنوان بسازد (اگر مطابق نباشد).

**راه‌حل:** عنوان توصیفی و شامل کلمه کلیدی.

### مشکل ۴: سایت در نتایج جستجو نیست

**علت‌ها:**
- سایت تازه Deploy شده.
- Index نشده.
- `robots.txt` بلاک کرده.

**راه‌حل:**
- Google Search Console → Request Indexing.
- صبر کن (۱–۷ روز).

## 🎁 خلاصه

| تگ | کاربرد |
|---|---|
| `<title>` | عنوان صفحه |
| `description` | توضیح |
| `viewport` | موبایل |
| `charset` | انکودینگ |
| `canonical` | URL اصلی |
| `robots` | راهنمای ربات |
| `theme-color` | رنگ مرورگر |

## آماده‌ای؟ برو به `02-open-graph.md`.