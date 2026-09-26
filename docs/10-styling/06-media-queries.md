# Media Queries

## 🎓 مفهوم

**Media Query** یک قاعده CSS است که استایل را **مشروط** می‌کند.

## 🎓 Syntax

```css
@media (شرط) {
  /* استایل */
}
```

## 🎓 انواع شرط

### ۱. عرض صفحه

```css
/* کمتر از ۷۶۸ */
@media (max-width: 768px) { }

/* بیشتر از ۷۶۸ */
@media (min-width: 768px) { }

/* بین ۷۶۸ و ۱۰۲۴ */
@media (min-width: 768px) and (max-width: 1024px) { }
```

### ۲. جهت صفحه

```css
@media (orientation: portrait) { }   /* عمودی */
@media (orientation: landscape) { }  /* افقی */
```

### ۳. Dark Mode

```css
@media (prefers-color-scheme: dark) { }
@media (prefers-color-scheme: light) { }
```

### ۴. رزولوشن

```css
@media (min-resolution: 2dppx) { }  /* Retina */
```

### ۵. Print

```css
@media print {
  /* فقط در چاپ */
}
```

### ۶. Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* برای کاربرانی که انیمیشن نمی‌خواهند */
}
```

## 🎓 Breakpoints

| نام | اندازه | دستگاه |
|---|---|---|
| **xs** | < 480px | موبایل کوچک |
| **sm** | 480 – 640px | موبایل |
| **md** | 640 – 768px | موبایل بزرگ |
| **lg** | 768 – 1024px | تبلت |
| **xl** | 1024 – 1280px | دسکتاپ |
| **2xl** | > 1280px | دسکتاپ بزرگ |

**ما از یک Breakpoint استفاده می‌کنیم: 768px.**

## 🎓 Mobile First vs Desktop First

### Mobile First (توصیه‌شده)

```css
/* پایه: موبایل */
.card { padding: 16px; }

/* دسکتاپ */
@media (min-width: 768px) {
  .card { padding: 24px; }
}
```

**مزیت:** برای موبایل بهینه، کم‌هزینه‌تر.

### Desktop First

```css
/* پایه: دسکتاپ */
.card { padding: 24px; }

/* موبایل */
@media (max-width: 768px) {
  .card { padding: 16px; }
}
```

**مزیت:** برای پروژه‌های قدیمی.

## 🎓 در پروژه ما

از رویکرد **Desktop First** استفاده کردیم، چون سایت از قبل ساخته شده بود.

```css
/* استایل پایه (دسکتاپ) */
.card { padding: 24px; }

/* موبایل */
@media (max-width: 768px) {
  .card { padding: 16px; }
}
```

## 🛠 مثال ۱: متن

```astro
<p class="text">متن</p>

<style>
  .text {
    font-size: 16px;
    line-height: 1.7;
  }

  @media (max-width: 768px) {
    .text {
      font-size: 15px;
      line-height: 1.8;
    }
  }
</style>
```

## 🛠 مثال ۲: Grid

```astro
<div class="grid">
  <!-- آیتم‌ها -->
</div>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }

  @media (max-width: 1024px) {
    .grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 640px) {
    .grid {
      grid-template-columns: 1fr;
      gap: 16px;
    }
  }
</style>
```

**نتیجه:**

- دسکتاپ: ۳ ستون
- تبلت: ۲ ستون
- موبایل: ۱ ستون

## 🛠 مثال ۳: Navbar

```astro
<header class="navbar">
  <a href="/" class="logo">فرهاد</a>
  <ul class="menu">
    ...
  </ul>
</header>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    padding: 16px 24px;
  }

  .menu {
    display: flex;
    gap: 24px;
  }

  @media (max-width: 768px) {
    .navbar {
      padding: 12px 16px;
    }

    .menu {
      display: none;  /* در موبایل مخفی */
    }
  }
</style>
```

## 🎓 Override کردن

اگر استایل پایه `inline` است، از `!important` استفاده کن:

```astro
<h1 style="font-size: 42px;">عنوان</h1>

<style>
  @media (max-width: 768px) {
    h1 {
      font-size: 28px !important;
    }
  }
</style>
```

**چرا؟** Inline Style بر `<style>` اولویت دارد. `!important` آن را override می‌کند.

## 🎓 Media Query در `<style>` Astro

```astro
<style>
  .card {
    padding: 24px;
  }

  @media (max-width: 768px) {
    .card {
      padding: 16px;
    }
  }
</style>
```

**نکته:** Astro آن را Scoped می‌کند. یعنی فقط این Component.

## 🎓 Media Query برای Print

```css
@media print {
  .no-print {
    display: none;
  }

  .page {
    page-break-after: always;
  }
}
```

**کاربرد:** وقتی کاربر `Cmd + P` می‌زند.

## 🎓 Media Query برای Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**کاربرد:** کاربرانی که به دلایل پزشکی، انیمیشن نمی‌خواهند.

## 🎓 تست Media Query

### Chrome DevTools

1. `F12`.
2. `Cmd + Shift + M`.
3. دستگاه انتخاب کن.
4. صفحه را resize کن.

### نشانگر

Chrome نشان می‌دهد در چه Breakpoint هستی:

```
768px × 1024px  |  Responsive
```

## 🎓 ابزارهای مفید

- [mediaqueri.es](https://mediaqueri.es) — نمونه‌های واقعی
- [mydevice.io](https://mydevice.io) — اندازه دستگاه‌ها

## 🛑 عیب‌یابی

### مشکل ۱: Media Query اعمال نمی‌شود

**علت‌ها:**
- Inline Style.
- Cache.
- Breakpoint اشتباه.

**راه‌حل:**
- `!important`.
- Hard Refresh.
- DevTools نشانگر را ببین.

### مشکل ۲: برای یک Component، Media Query کار نمی‌کند

**علت:** Style Scoped است.

**راه‌حل:** Media Query را در همان Component بنویس.

### مشکل ۳: Override خودم را Override می‌کند

**علت:** دو Media Query متضاد.

**راه‌حل:** ترتیب مهم است. آخرین برنده.

```css
@media (max-width: 1024px) { .x { color: red; } }
@media (max-width: 768px) { .x { color: blue; } }
/* در ۷۰۰px: blue */
```

## 🎓 در پروژه ما

### `global.css`

```css
@media (max-width: 768px) {
  h1 {
    font-size: 28px !important;
    line-height: 1.3 !important;
  }

  h2 {
    font-size: 20px !important;
  }

  h3 {
    font-size: 17px !important;
  }

  body {
    font-size: 15px;
  }

  section,
  main {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
}
```

### کامپوننت‌های Portfolio

```astro
<style>
  @media (max-width: 900px) {
    .stats-grid {
      grid-template-columns: repeat(2, 1fr) !important;
    }
  }

  @media (max-width: 500px) {
    .stats-grid {
      grid-template-columns: 1fr !important;
    }
  }
</style>
```

## 🎁 خلاصه

| Media Query | کاربرد |
|---|---|
| `max-width: 768px` | موبایل |
| `min-width: 768px` | دسکتاپ |
| `orientation: portrait` | عمودی |
| `prefers-color-scheme` | Dark Mode |
| `print` | چاپ |
| `prefers-reduced-motion` | بدون انیمیشن |

| مفهوم | توضیح |
|---|---|
| Mobile First | `min-width` |
| Desktop First | `max-width` |
| `!important` | Override |
| Breakpoint | 768px |