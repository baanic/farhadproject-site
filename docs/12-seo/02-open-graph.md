# Open Graph

## 🎓 مفهوم

**Open Graph** پروتکلی است که به شبکه‌های اجتماعی می‌گوید وقتی کاربر لینک سایت را به اشتراک گذاشت، **چه چیزی نمایش دهد**.

## 🎓 بدون Open Graph

وقتی لینک سایت را در تلگرام پیست می‌کنی:

```
https://farhadproject.ir
```

فقط این URL نمایش داده می‌شود. خشک و بی‌روح.

## 🎓 با Open Graph

یک **کارت زیبا** نمایش داده می‌شود:
- تصویر
- عنوان
- توضیح

## 🎓 تگ‌های اصلی

| تگ | کاربرد | مثال |
|---|---|---|
| `og:title` | عنوان | «پرتفولیو فرهاد» |
| `og:description` | توضیح | «دفتر فنی، کنترل پروژه» |
| `og:image` | تصویر | `/images/og.jpg` |
| `og:url` | URL | `https://farhadproject.ir` |
| `og:type` | نوع | `website` |
| `og:locale` | زبان | `fa_IR` |
| `og:site_name` | نام سایت | «پرتفولیو فرهاد» |

## 🎓 تگ `og:image`

**مهم‌ترین تگ** Open Graph.

### ابعاد

| اندازه | کاربرد |
|---|---|
| **۱۲۰۰×۶۳۰** ✅ | استاندارد |
| ۱۲۰۰×۱۲۰۰ | مربعی (اینستاگرام) |
| ۶۰۰×۳۱۵ | کوچک |

### فایل

- **فرمت:** JPG یا PNG
- **حجم:** کمتر از ۱ مگابایت
- **نسبت:** 1.91:1

## 🎓 تگ `og:type`

| نوع | کاربرد |
|---|---|
| `website` | سایت |
| `article` | مقاله |
| `profile` | پروفایل |
| `video.movie` | ویدیو |

**ما `website` استفاده می‌کنیم.**

## 🎓 تگ `og:locale`

```html
<meta property="og:locale" content="fa_IR" />
```

**`fa_IR`** = **fa**rsi-**IR**an.

**نکته:** این به تلگرام و لینکدین می‌گوید که متن **فارسی** است.

## 🛠 پیاده‌سازی

```astro
---
const { title, description, ogImage = "/images/og-image.jpg" } = Astro.props;
const siteName = "پرتفولیو فرهاد";
const siteUrl = "https://farhadproject.ir";

const pageTitle = title ? `${title} | ${siteName}` : siteName;
const canonicalUrl = new URL(Astro.url.pathname, siteUrl).toString();
const ogImageUrl = new URL(ogImage, siteUrl).toString();
---

<head>
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content={canonicalUrl} />
  <meta property="og:title" content={pageTitle} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={ogImageUrl} />
  <meta property="og:locale" content="fa_IR" />
  <meta property="og:site_name" content={siteName} />
</head>
```

## 🎓 Twitter Card

توییتر (X) از استاندارد خودش استفاده می‌کند، اما Open Graph را هم می‌فهمد.

```astro
<head>
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={pageTitle} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={ogImageUrl} />
</head>
```

### انواع `twitter:card`

| نوع | کاربرد |
|---|---|
| `summary` | کارت کوچک |
| `summary_large_image` ✅ | کارت بزرگ |
| `app` | اپ |
| `player` | ویدیو |

**ما `summary_large_image` استفاده می‌کنیم.**

## 🎓 ساخت تصویر OG

### ابزارها

| ابزار | مزیت |
|---|---|
| **Figma** | طراحی حرفه‌ای |
| **Canva** | قالب آماده |
| **InDesign** | برای طراحان |
| **og-image.vercel.app** | ساخت آنلاین |

### محتوای پیشنهادی

```
┌──────────────────────────────────────┐
│                                      │
│  ▬▬▬  (نوار مسی)                     │
│                                      │
│  پرتفولیو مهندسی فرهاد                │
│                                      │
│  دفتر فنی | کنترل پروژه | متره | آکوستیک  │
│                                      │
│                        farhadproject.ir │
└──────────────────────────────────────┘
```

**رنگ‌ها:** سرمه‌ای `#1B2A4A` + مسی `#B8763E` + کرم `#F5F0E6`.

## 🎓 تست Open Graph

### ابزارهای آنلاین

| ابزار | کاربرد |
|---|---|
| [metatags.io](https://metatags.io) | پیش‌نمایش تلگرام، لینکدین، توییتر |
| [opengraph.xyz](https://www.opengraph.xyz) | پیش‌نمایش همه شبکه‌ها |
| [Facebook Debugger](https://developers.facebook.com/tools/debug/) | فیسبوک |

### تست دستی

1. لینک سایت را در **تلگرام** پیست کن.
2. کارت نمایش داده می‌شود.
3. اگر تصویر نیست، Cache تلگرام را پاک کن:
   - یک پارامتر به URL اضافه کن: `?v=2`
   - تلگرام دوباره Fetch می‌کند.

## 🎓 Cache شبکه‌های اجتماعی

**مشکل:** اگر تصویر OG را عوض کنی، شبکه‌ها ممکن است **تصویر قدیمی** را نشان دهند.

**راه‌حل‌ها:**

### ۱. Cache Busting

URL را با یک پارامتر عوض کن:

```html
<meta property="og:image" content="https://farhadproject.ir/og-image.jpg?v=2" />
```

### ۲. Facebook Debugger

1. برو به [Facebook Debugger](https://developers.facebook.com/tools/debug/).
2. URL را وارد کن.
3. **Scrape Again** بزن.

### ۳. صبر

ممکن است ۲۴–۴۸ ساعت طول بکشد.

## 🎓 در پروژه ما

### `BaseLayout.astro`

```astro
---
const {
  title,
  description,
  ogImage = "/images/portfolio/og-image.jpg",
} = Astro.props;
---

<head>
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content={canonicalUrl} />
  <meta property="og:title" content={pageTitle} />
  <meta property="og:description" content={pageDescription} />
  <meta property="og:image" content={ogImageUrl} />
  <meta property="og:locale" content="fa_IR" />
  <meta property="og:site_name" content={siteName} />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={pageTitle} />
  <meta name="twitter:description" content={pageDescription} />
  <meta name="twitter:image" content={ogImageUrl} />
</head>
```

## 🛑 عیب‌یابی

### مشکل ۱: تصویر OG نمایش داده نمی‌شود

**علت‌ها:**
- مسیر اشتباه.
- حجم زیاد (> ۱MB).
- ابعاد نامناسب.
- HTTP به‌جای HTTPS.

**راه‌حل:**
- ابعاد: ۱۲۰۰×۶۳۰.
- حجم: < ۵۰۰KB.
- HTTPS.

### مشکل ۲: عنوان قدیمی نمایش داده می‌شود

**علت:** Cache شبکه.

**راه‌حل:** Cache Busting یا صبر.

### مشکل ۳: فارسی نمایش داده نمی‌شود

**علت:** `og:locale` اشتباه.

**راه‌حل:** `content="fa_IR"`.

### مشکل ۴: تصویر در تلگرام نیست

**علت:** تلگرام Cache قوی دارد.

**راه‌حل:**
- پارامتر `?v=N` به URL اضافه کن.
- یا از [@WebpageBot](https://t.me/webpagebot) در تلگرام استفاده کن.

## 🎓 بهترین تمرین‌ها

### ۱. تصویر جذاب

- طراحی تمیز.
- رنگ برند.
- عنوان بزرگ.

### ۲. عنوان کوتاه

حداکثر **۶۰ کاراکتر** (شبکه‌ها ممکن است کوتاه کنند).

### ۳. توضیح ۱۰۰ کاراکتری

### ۴. نسبت ابعاد 1.91:1

### ۵. فایل‌سبک

حداکثر **۵۰۰KB**.

## 🎁 خلاصه

| تگ | کاربرد |
|---|---|
| `og:title` | عنوان |
| `og:description` | توضیح |
| `og:image` | تصویر |
| `og:url` | URL |
| `og:type` | نوع |
| `og:locale` | زبان |
| `twitter:card` | Twitter |

| نکته | مقدار |
|---|---|
| ابعاد تصویر | ۱۲۰۰×۶۳۰ |
| حجم | < ۵۰۰KB |
| نسبت | 1.91:1 |

## آماده‌ای؟ برو به `03-favicon.md`.