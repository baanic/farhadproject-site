# Favicon

## 🎓 مفهوم

**Favicon** = **Fav**orite **Icon**.

آیکون کوچکی که در **تب مرورگر**، **بوکمارک‌ها**، و **نتایج جستجو** نمایش داده می‌شود.

## 🎓 چرا Favicon مهم است؟

### ۱. تب مرورگر

کاربر بین ۱۰ تب، سایت تو را **سریع‌تر پیدا می‌کند**.

### ۲. بوکمارک

وقتی کاربر سایت را ذخیره می‌کند، آیکون را می‌بیند.

### ۳. حرفه‌ای بودن

سایت بدون favicon، **ناتمام** به نظر می‌رسد.

### ۴. SEO کوچک

Google در نتایج موبایل، آیکون را نشان می‌دهد.

## 🎓 اندازه‌های مختلف

| اندازه | کاربرد |
|---|---|
| **16×16** | تب مرورگر |
| **32×32** | بوکمارک |
| **180×180** | اپل تاچ (Home Screen) |
| **192×192** | اندروید |
| **512×512** | PWA و اشتراک‌گذاری |
| **favicon.ico** | فایل قدیمی (16, 32, 48 یکجا) |

## 🛠 گام ۱: طراحی Favicon

### گزینه ۱: با Figma

1. یک Frame با اندازه **۵۱۲×۵۱۲** بساز.
2. طراحی ساده:
   - **پس‌زمینه:** سرمه‌ای `#1B2A4A`
   - **متن:** حرف اول نامت (ف) به رنگ کرم `#F5F0E6`
   - **فونت:** Shabnam Bold
3. Export به PNG.

### گزینه ۲: با سایت آنلاین

[**favicon.io**](https://favicon.io/favicon-generator/):

1. **Text** را بزن.
2. **Text** = `ف` یا `فر`.
3. **Background** = `#1B2A4A`.
4. **Text Color** = `#F5F0E6`.
5. **Font Family** = `Shabnam` یا `Arial`.
6. **Font Size** = `Auto`.
7. **Download** → ZIP می‌گیری.

## 🛠 گام ۲: قرار دادن در پروژه

```
astro-site/
└── public/
    └── favicon/
        ├── favicon.ico
        ├── favicon-16x16.png
        ├── favicon-32x32.png
        ├── apple-touch-icon.png
        ├── android-chrome-192x192.png
        ├── android-chrome-512x512.png
        └── site.webmanifest
```

**نکته:** ZIP را extract کن و همه فایل‌ها را در `public/favicon/` بگذار.

## 🛠 گام ۳: اضافه کردن به HTML

### در `BaseLayout.astro`

```astro
<head>
  <link rel="icon" type="image/x-icon" href="/favicon/favicon.ico" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png" />
  <link rel="manifest" href="/favicon/site.webmanifest" />
</head>
```

### توضیح

| تگ | کاربرد |
|---|---|
| `favicon.ico` | مرورگرهای قدیمی |
| `16x16`, `32x32` | تب مرورگر |
| `apple-touch-icon` | iOS Home Screen |
| `manifest` | PWA |

## 🎓 فایل `site.webmanifest`

این فایل، اطلاعات اپ را نگه می‌دارد:

```json
{
  "name": "پرتفولیو فرهاد",
  "short_name": "فرهاد",
  "icons": [
    {
      "src": "/favicon/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/favicon/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#1B2A4A",
  "background_color": "#1B2A4A",
  "display": "standalone"
}
```

## 🎓 فایل `favicon.ico`

فرمت `ico` یک فایل چند-اندازه‌ای است که همه مرورگرها می‌فهمند.

**ابزار ساخت:** [realfavicongenerator.net](https://realfavicongenerator.net).

**چطور ساخت؟**

1. برو به سایت.
2. یک PNG **۵۱۲×۵۱۲** آپلود کن.
3. تنظیمات را تنظیم کن.
4. **Generate** → ZIP می‌گیری.
5. Extract در `public/favicon/`.

## 🎓 Browser Support

| فایل | Chrome | Firefox | Safari | Edge |
|---|---|---|---|---|
| `.ico` | ✅ | ✅ | ✅ | ✅ |
| `16x16.png` | ✅ | ✅ | ✅ | ✅ |
| `32x32.png` | ✅ | ✅ | ✅ | ✅ |
| `apple-touch-icon.png` | ❌ | ❌ | ✅ | ❌ |
| `manifest.json` | ✅ | ✅ | ❌ | ✅ |

## 🎓 تست

### ۱. در تب مرورگر

سایت را باز کن. باید آیکون را در تب ببینی.

### ۲. Hard Refresh

`Cmd + Shift + R` بزن. Cache پاک می‌شود.

### ۳. حالت Incognito

مرورگر را در حالت **Incognito** باز کن. اگر آیکون نمایش داده شد، یعنی درست کار می‌کند.

## 🛑 عیب‌یابی

### مشکل ۱: Favicon نمایش داده نمی‌شود

**علت‌ها:**
- مسیر اشتباه.
- Cache مرورگر.
- فایل نامعتبر.

**راه‌حل:**
- مسیر: `/favicon/favicon.ico`.
- Hard Refresh.
- حالت Incognito.

### مشکل ۲: در Safari نمایش نمی‌شود

**علت:** Safari Cache قوی دارد.

**راه‌حل:**
- Safari → **Empty Caches**.
- یا از حالت Private استفاده کن.

### مشکل ۳: در Google نمایش داده نمی‌شود

**علت:** Google بعد از Index کردن، آیکون را نشان می‌دهد.

**راه‌حل:** صبر کن (۱–۷ روز).

### مشکل ۴: `favicon.ico` 404 می‌دهد

**علت:** فایل موجود نیست یا مسیر اشتباه.

**راه‌حل:** بررسی کن `public/favicon/favicon.ico` وجود دارد.

## 🎓 طراحی Favicon

### اصول

| اصل | توضیح |
|---|---|
| **سادگی** | در ۱۶×۱۶ خوانا |
| **تضاد** | رنگ‌های متمایز |
| **یادآور** | منحصر به برند |
| **بدون متن زیاد** | فقط حرف یا نماد |

### مثال‌های خوب

- **حرف اول نام:** «ف» سفید روی سرمه‌ای
- **نماد هندسی:** مربع با گوشه‌های گرد
- **آیکون مرتبط:** مثلث (مهندسی)

### مثال‌های بد

- عکس واقعی (در ۱۶×۱۶ خیلی ریز)
- متن زیاد (خوانا نیست)
- رنگ‌های ملایم (محو می‌شود)
- جزئیات زیاد (دیده نمی‌شود)

## 🎓 در پروژه ما

پروژه ما:

```
public/favicon/
├── favicon.ico
├── favicon-16x16.png
├── favicon-32x32.png
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
└── site.webmanifest
```

طراحی: **حرف «ف»** روی پس‌زمینه سرمه‌ای.

## 🎁 خلاصه

| فایل | اندازه | کاربرد |
|---|---|---|
| `favicon.ico` | 16/32/48 | همه مرورگرها |
| `favicon-16x16.png` | 16 | تب |
| `favicon-32x32.png` | 32 | Retina |
| `apple-touch-icon.png` | 180 | iOS |
| `android-chrome-192.png` | 192 | Android |
| `android-chrome-512.png` | 512 | PWA |
| `site.webmanifest` | — | اپ |

| ابزار | کاربرد |
|---|---|
| [favicon.io](https://favicon.io) | ساخت سریع |
| [realfavicongenerator.net](https://realfavicongenerator.net) | حرفه‌ای |

## آماده‌ای؟ برو به `04-sitemap.md`.