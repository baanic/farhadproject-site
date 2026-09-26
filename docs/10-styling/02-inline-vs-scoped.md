# Inline vs Scoped Style در Astro

## 🎓 مفهوم

در Astro، سه راه برای استایل‌دهی وجود دارد:

| روش | نحو | Scope |
|---|---|---|
| **Inline** | `style="..."` | فقط همان عنصر |
| **Scoped** | `<style>` در فایل `.astro` | فقط همان فایل |
| **Global** | `<style is:global>` یا فایل `.css` | همه‌جا |

## 🎓 روش ۱: Inline Style

### ساختار

```astro
<div style="background: red; padding: 20px;">
  محتوا
</div>
```

### مزیت

- سریع برای استایل کوچک.
- می‌توانی از متغیر استفاده کنی.
- Override قوی.

### عیب

- بدون Pseudo-class (`:hover`, `:focus`).
- بدون Media Query.
- بدون Keyframe Animation.

### با متغیر

```astro
---
const color = "#B8763E";
const size = "20px";
---

<div style={`
  background: ${color};
  padding: ${size};
`}>
```

**نکته:** از Backtick (`) استفاده کن، نه گیومه.

## 🎓 روش ۲: Scoped Style (توصیه‌شده)

### ساختار

```astro
<div class="card">
  <h3>عنوان</h3>
</div>

<style>
  .card {
    background: white;
    padding: 20px;
    border-radius: 8px;
  }

  .card h3 {
    color: #1B2A4A;
  }
</style>
```

### مزیت

- **Scoped:** فقط این فایل.
- Pseudo-class کار می‌کند.
- Media Query کار می‌کند.
- Animation کار می‌کند.
- خوانایی بالا.

### چه کار می‌کند؟

Astro استایل را **محدود** به همان Component می‌کند:

```html
<!-- خروجی HTML -->
<div class="card astro-abc123">
  ...
</div>

<style>
  .card.astro-abc123 {
    background: white;
  }
</style>
```

**نکته:** Astro یک شناسه یکتا (مثل `astro-abc123`) به Class اضافه می‌کند تا از تداخل جلوگیری شود.

## 🎓 روش ۳: Global Style

### ساختار

```astro
<style is:global>
  body {
    font-family: 'Shabnam';
  }
</style>
```

**نکته:** `is:global` یعنی «همه‌جا اعمال شود».

### فایل CSS جداگانه

```css
/* src/styles/global.css */
body {
  font-family: 'Shabnam';
}
```

**Import در Layout:**

```astro
---
import "../styles/global.css";
---
```

## 🎓 کدام کدام؟

| مورد | روش |
|---|---|
| رنگ داینامیک | Inline |
| استایل کامپوننت | Scoped |
| Reset کلی | Global |
| فونت | Global |
| Pseudo-class | Scoped |
| Media Query | Scoped |
| Keyframe | Scoped |

## 🛠 در پروژه ما

### `global.css` — Global

```css
* { box-sizing: border-box; }

html {
  font-family: 'Shabnam', Tahoma, sans-serif;
  direction: rtl;
}
```

### `Navbar.astro` — Inline

```astro
<a
  href={item.href}
  style={`
    color: ${currentPath === item.href ? "#B8763E" : "#F5F0E6"};
    font-size: 15px;
    padding: 8px 0;
  `}
>
  {item.label}
</a>
```

**چرا Inline؟** چون رنگ بر اساس مسیر فعلی داینامیک است.

### `Hero.astro` — ترکیبی

```astro
<section style="max-width: 1100px; margin: 0 auto; padding: 60px 24px;">
  <h1 style="color: #1B2A4A; font-size: 42px;">
    {title}
  </h1>
</section>

<style>
  @media (max-width: 768px) {
    section {
      padding: 40px 16px !important;
    }
    h1 {
      font-size: 28px !important;
    }
  }
</style>
```

**چرا ترکیبی؟** Inline برای استایل پایه، `<style>` برای Media Query.

## 🎓 ترفند: متغیرهای CSS

در `<style>`:

```css
.card {
  --card-color: #1B2A4A;
  --card-padding: 20px;

  background: var(--card-color);
  padding: var(--card-padding);
}
```

**مزیت:** یک بار تعریف، چند بار استفاده.

### در Media Query

```css
.card {
  --card-padding: 20px;
  padding: var(--card-padding);
}

@media (max-width: 768px) {
  .card {
    --card-padding: 12px;
  }
}
```

**نکته:** مقدار متغیر عوض می‌شود، ولی قاعده یکی است.

## 🎓 ترفند: `<style>` در Layout

اگر می‌خواهی استایل‌ها را در Layout مشترک بگذاری:

```astro
---
// BaseLayout.astro
---
<html>
  <head>
    <style is:global>
      body { margin: 0; }
    </style>
  </head>
  <body>
    <slot />
  </body>
</html>
```

## 🛑 عیب‌یابی

### مشکل ۱: استایل Scoped اعمال نمی‌شود

**علت:** Selector اشتباه.

**راه‌حل:** Class یا Element موجود در فایل را چک کن.

### مشکل ۲: استایل Scoped روی Child اثر نمی‌گذارد

**علت:** Astro استایل را محدود می‌کند.

**راه‌حل:** از `is:global` استفاده کن، یا استایل را در Child بگذار.

### مشکل ۳: Inline Style با Media Query

**علت:** Inline، Media Query ندارد.

**راه‌حل:** Media Query را در `<style>` بنویس:

```astro
<div class="hero">...</div>

<style>
  .hero {
    padding: 60px 24px;
  }

  @media (max-width: 768px) {
    .hero {
      padding: 40px 16px;
    }
  }
</style>
```

### مشکل ۴: `!important` استفاده می‌کنم ولی کار نمی‌کند

**علت:** شاید `!important` دیگری وجود دارد.

**راه‌حل:**

```css
.element {
  color: red !important !important;  /* ❌ کار نمی‌کند */
}
```

فقط یک `!important`.

## 🎓 بهترین تمرین‌ها

### ۱. اولویت به `<style>`

اگر استایل **ثابت** است، در `<style>`.

### ۲. Inline فقط برای داینامیک

اگر رنگ از داده می‌آید، Inline.

### ۳. Global برای Reset

فونت، direction، box-sizing → Global.

### ۴. از Class استفاده کن، نه ID

```css
.card { }       /* ✅ */
#card { }       /* ❌ */
```

### ۵. نام‌گذاری معنادار

```css
.hero-title { }       /* ✅ */
.title-1 { }          /* ❌ */
```

## 🎁 خلاصه

| روش | مزیت | عیب |
|---|---|---|
| Inline | سریع، داینامیک | بدون Pseudo، Media |
| Scoped | قدرتمند، امن | کمی پیچیده‌تر |
| Global | سراسری | ممکن است تداخل |

**قاعده:** 
- Reset → Global
- Component → Scoped
- داینامیک → Inline

## آماده‌ای؟ برو به `03-color-system.md`.
```

---

## 📄 فایل ۴: `docs/10-styling/03-color-system.md`