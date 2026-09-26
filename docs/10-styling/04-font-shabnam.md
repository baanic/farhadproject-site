# فونت Shabnam

## 🎓 چرا فونت مهم است؟

- **خوانایی:** فونت درست، متن راحت خوانده می‌شود.
- **شخصیت:** فونت، لحن برند را می‌سازد.
- **فارسی:** فونت‌های فارسی، طراحی متفاوت دارند.

## 🎓 چرا Shabnam؟

| مزیت | توضیح |
|---|---|
| **رایگان** | Open Source |
| **مدرن** | طراحی روز |
| **فارسی** | پشتیبانی کامل |
| **وزن‌ها** | Light, Regular, Medium, Bold |
| **کاملاً استاندارد** | در پروژه‌های حرفه‌ای |
| **سازگار** | با همه مرورگرها |

## 🎓 منابع Shabnam

**سازنده:** صابر راستی‌کردار.

**سایت رسمی:** [github.com/rastikerdar/shabnam-font](https://github.com/rastikerdar/shabnam-font).

## 🛠 گام ۱: دانلود

از GitHub یا سایت‌های زیر:

- [font.ir](https://font.ir)
- [github.com/rastikerdar/shabnam-font](https://github.com/rastikerdar/shabnam-font)

**وزن‌های موردنیاز:**

- `Shabnam-Light.woff2`
- `Shabnam.woff2` (Regular)
- `Shabnam-Medium.woff2`
- `Shabnam-Bold.woff2`

**توصیه:** فرمت `woff2` (سریع‌تر، سبک‌تر).

## 🛠 گام ۲: قرار دادن در پروژه

```
astro-site/
└── public/
    └── fonts/
        ├── Shabnam-Light.woff2
        ├── Shabnam.woff2
        ├── Shabnam-Medium.woff2
        └── Shabnam-Bold.woff2
```

**چرا `public/` و نه `src/`؟**

- فونت‌ها **پردازش** نمی‌خواهند.
- `public/` بدون تغییر به خروجی می‌رود.
- سریع‌تر.

## 🛠 گام ۳: تعریف در CSS

### `src/styles/global.css`

```css
@font-face {
  font-family: 'Shabnam';
  src: url('/fonts/Shabnam-Light.woff2') format('woff2');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Shabnam';
  src: url('/fonts/Shabnam.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Shabnam';
  src: url('/fonts/Shabnam-Medium.woff2') format('woff2');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Shabnam';
  src: url('/fonts/Shabnam-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

### توضیح

| خط | معنی |
|---|---|
| `font-family: 'Shabnam'` | نام فونت |
| `src: url(...)` | مسیر فایل |
| `font-weight: 400` | وزن |
| `font-display: swap` | اگر لود نشد، موقتاً فونت پیش‌فرض |

## 🛠 گام ۴: اعمال روی بدنه

```css
html {
  font-family: 'Shabnam', Tahoma, sans-serif;
  direction: rtl;
}

body {
  font-family: 'Shabnam', Tahoma, sans-serif;
  font-size: 16px;
  line-height: 1.7;
}
```

**نکته:** `Tahoma` یک Fallback است. اگر Shabnam لود نشد، Tahoma نمایش داده می‌شود.

## 🛠 گام ۵: Import در Layout

### `src/layouts/BaseLayout.astro`

```astro
---
import "../styles/global.css";
// ...
---

<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <!-- ... -->
  </head>
  <body>
    <slot />
  </body>
</html>
```

**نکته:** Import در Frontmatter.

## 🎓 چطور چک کنم فونت لود شده؟

### Chrome DevTools

1. `F12` (یا `Cmd + Option + I`).
2. تب **Network**.
3. Hard Refresh: `Cmd + Shift + R`.
4. فیلتر: `font`.
5. باید فایل‌های `.woff2` را ببینی (Status 200).

### Elements

1. تب **Elements**.
2. روی یک متن کلیک کن.
3. تب **Computed**.
4. `font-family` را ببین.

**باید ببینی:** `Shabnam, Tahoma, sans-serif`.

## 🎓 وزن‌های فونت

| وزن | کاربرد |
|---|---|
| **Light (300)** | کپشن، متن فرعی |
| **Regular (400)** | متن بدنه |
| **Medium (500)** | عنوان‌های کوچک |
| **Bold (700)** | عنوان‌های اصلی |

**استفاده:**

```css
.caption { font-weight: 300; }
.body { font-weight: 400; }
.subtitle { font-weight: 500; }
.title { font-weight: 700; }
```

## 🎓 فونت Shabnam FD (ارقام فارسی)

Shabnam **FD (Farsi Digits)** نسخه‌ای است که اعداد را **فارسی** نشان می‌دهد.

**مثال:**

| Shabnam معمولی | Shabnam FD |
|---|---|
| 11000 | ۱۱۰۰۰ |

**توصیه:** ما از **Shabnam معمولی** استفاده می‌کنیم و اعداد فارسی را با `toLocaleString("fa-IR")` می‌سازیم.

**مزیت:** کنترل کامل روی هر عدد.

## 🎓 Fallback Fonts

```css
font-family: 'Shabnam', Tahoma, Arial, sans-serif;
```

**ترتیب:**

1. **Shabnam** — اگر موجود.
2. **Tahoma** — اگر Shabnam نبود.
3. **Arial** — اگر Tahoma نبود.
4. **sans-serif** — پیش‌فرض سیستم.

## 🎓 ویژگی‌های CSS مرتبط

### `font-display`

| مقدار | توضیح |
|---|---|
| `auto` | پیش‌فرض مرورگر |
| `block` | تا لود، هیچ چیز نشان نده |
| `swap` ✅ | موقتاً فونت پیش‌فرض، بعد عوض کن |
| `fallback` | کمی صبر، بعد swap |
| `optional` | اگر سریع نبود، هیچ |

**ما `swap` استفاده می‌کنیم.**

### `font-smoothing`

```css
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**مزیت:** متن روی صفحه‌های Retina نرم‌تر می‌شود.

## 🛑 عیب‌یابی

### مشکل ۱: فونت لود نمی‌شود

**علت‌ها:**
- مسیر اشتباه.
- نام فایل اشتباه.
- Cache.

**راه‌حل:**
- `ls public/fonts/` را بررسی کن.
- Hard Refresh.
- Cache مرورگر را پاک کن.

### مشکل ۲: فونت لود می‌شود ولی اعمال نمی‌شود

**علت:** `font-family` تنظیم نشده.

**راه‌حل:**

```css
body {
  font-family: 'Shabnam', Tahoma, sans-serif;
}
```

### مشکل ۳: `@font-face` کار نمی‌کند

**علت:** مسیر از `/` شروع نشده.

**راه‌حل:**

```css
/* درست */
src: url('/fonts/Shabnam.woff2');

/* اشتباه */
src: url('../fonts/Shabnam.woff2');
```

### مشکل ۴: فونت خیلی بزرگ است

**علت:** فرمت `ttf` یا `otf`.

**راه‌حل:** به `woff2` تبدیل کن.

**ابزار:** [cloudconvert.com](https://cloudconvert.com/ttf-to-woff2).

### مشکل ۵: FOUT (Flash of Unstyled Text)

**علت:** فونت دیر لود می‌شود.

**راه‌حل:** `font-display: swap` (که داریم).

**یا:** Preload:

```html
<link
  rel="preload"
  href="/fonts/Shabnam.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

## 🎓 بهترین تمرین‌ها

### ۱. فقط وزن‌های لازم

اگر وزن‌های اضافه لود کنی، سایت سنگین می‌شود.

**ما ۴ وزن داریم:** Light, Regular, Medium, Bold.

### ۲. Preload

```html
<link rel="preload" href="/fonts/Shabnam.woff2" as="font" crossorigin />
```

**مزیت:** فونت زودتر لود می‌شود.

### ۳. Fallback مناسب

همیشه Fallback بگذار:

```css
font-family: 'Shabnam', Tahoma, sans-serif;
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| فایل | `Shabnam.woff2` |
| محل | `public/fonts/` |
| تعریف | `@font-face` |
| اعمال | `font-family` |
| وزن‌ها | 300, 400, 500, 700 |
| Fallback | `Tahoma, sans-serif` |
| font-display | `swap` |

## آماده‌ای؟ برو به `05-responsive-design.md`.