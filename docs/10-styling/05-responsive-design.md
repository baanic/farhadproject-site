# Responsive Design

## 🎓 مفهوم

**Responsive Design** یعنی: سایت روی **همه اندازه صفحه‌ها** (موبایل، تبلت، دسکتاپ) خوب نمایش داده شود.

## 🎓 چرا Responsive؟

### آمار واقعی

- بیش از ۶۰٪ کاربران با **موبایل** می‌آیند.
- اگر سایت روی موبایل خراب باشد، کاربر می‌رود.
- Google، سایت‌های موبایل-فرندلی را در نتایج جستجو **بالاتر** می‌آورد.

## 🎓 چالش ما

سایت تو روی **دسکتاپ** عالی است. اما روی موبایل:

- Navbar با ۵ آیتم افقی → به‌هم می‌ریزد.
- Hero با فونت ۴۲px → بزرگ.
- Grid با ستون ثابت → از صفحه بیرون می‌زند.

## 🎓 راه‌حل: Media Query

```css
/* استایل پایه (موبایل) */
body {
  font-size: 14px;
}

/* استایل دسکتاپ */
@media (min-width: 768px) {
  body {
    font-size: 16px;
  }
}
```

## 🎓 رویکرد: Mobile First

**Mobile First** = اول موبایل، بعد دسکتاپ.

### چرا؟

- بیشتر کاربران موبایل.
- موبایل، محدودیت‌های سخت‌تری دارد.
- از ساده به پیچیده.

### دو رویکرد

| Mobile First | Desktop First |
|---|---|
| `min-width` | `max-width` |
| 320px → 768px → 1200px | 1200px → 768px → 320px |
| استاندارد مدرن ✅ | قدیمی |

**ما Mobile First را توصیه می‌کنیم.**

## 🎓 Breakpoints

**Breakpoints** نقاطی هستند که چیدمان عوض می‌شود.

| نام | اندازه | دستگاه |
|---|---|---|
| Mobile | < 640px | موبایل |
| Tablet | 640 – 1024px | تبلت |
| Desktop | > 1024px | دسکتاپ |

**ما از ۷۶۸px استفاده می‌کنیم.**

## 🛠 مثال ۱: Navbar

### مشکل

۵ آیتم افقی در موبایل جا نمی‌شوند.

### راه‌حل

در موبایل: منوی همبرگری.
در دسکتاپ: منوی افقی.

```astro
<button id="menu-toggle" style="display: none;">
  ☰
</button>

<ul id="desktop-menu" style="display: flex;">
  ...
</ul>

<ul id="mobile-menu" style="display: none;">
  ...
</ul>

<script is:inline>
  function updateLayout() {
    if (window.innerWidth <= 768) {
      toggle.style.display = "block";
      desktopMenu.style.display = "none";
    } else {
      toggle.style.display = "none";
      desktopMenu.style.display = "flex";
    }
  }

  updateLayout();
  window.addEventListener("resize", updateLayout);
</script>
```

## 🛠 مثال ۲: Grid

### مشکل

```astro
<div style="display: grid; grid-template-columns: repeat(4, 1fr);">
```

۴ ستون در موبایل خیلی تنگ است.

### راه‌حل

```astro
<div style="
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
">
```

**معنی:** «تا هر تعداد ستون که فضا اجازه دهد، حداقل ۲۲۰px.»

- موبایل: ۱ ستون
- تبلت: ۲ ستون
- دسکتاپ: ۴ ستون

## 🛠 مثال ۳: Font Size

### مشکل

```astro
<h1 style="font-size: 42px;">عنوان</h1>
```

۴۲px در موبایل خیلی بزرگ است.

### راه‌حل

```astro
<h1 style="font-size: 42px;" class="title">عنوان</h1>

<style>
  @media (max-width: 768px) {
    .title {
      font-size: 28px !important;
    }
  }
</style>
```

## 🎓 Media Query

### Syntax

```css
@media (شرط) {
  /* استایل */
}
```

### شرط‌ها

| شرط | معنی |
|---|---|
| `max-width: 768px` | کمتر از ۷۶۸ |
| `min-width: 768px` | بیشتر از ۷۶۸ |
| `(min-width: 768px) and (max-width: 1024px)` | بین ۷۶۸ و ۱۰۲۴ |
| `(orientation: portrait)` | حالت عمودی |
| `(orientation: landscape)` | حالت افقی |
| `(prefers-color-scheme: dark)` | Dark Mode |

## 🛠 استفاده در Astro

### در `<style>`

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

### نه در Inline

**Inline Style از Media Query پشتیبانی نمی‌کند.**

```astro
<!-- ❌ کار نمی‌کند -->
<div style="
  padding: 24px;
  @media (max-width: 768px) { padding: 16px; }
">
```

**باید در `<style>` باشد.**

## 🎓 مثال کامل: Hero

```astro
<section class="hero">
  <h1 class="hero-title">{title}</h1>
  <p class="hero-subtitle">{subtitle}</p>
</section>

<style>
  .hero {
    max-width: 1100px;
    margin: 0 auto;
    padding: 60px 24px;
  }

  .hero-title {
    font-size: 42px;
    color: #1B2A4A;
  }

  .hero-subtitle {
    font-size: 20px;
    color: #B8763E;
  }

  @media (max-width: 768px) {
    .hero {
      padding: 40px 16px;
    }

    .hero-title {
      font-size: 28px;
    }

    .hero-subtitle {
      font-size: 16px;
    }
  }
</style>
```

## 🎓 Grid تطبیقی

### `grid-template-columns`

```css
/* ۴ ستون ثابت */
grid-template-columns: repeat(4, 1fr);

/* ۴ ستون، اما ریسپانسیو */
grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
```

**`auto-fit`** = «تا هر تعداد که جا شود.»

**`minmax(220px, 1fr)`** = «حداقل ۲۲۰px، حداکثر فضای موجود.»

### مثال

```css
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}
```

**نتیجه:**

| عرض | تعداد ستون |
|---|---|
| 375px | ۱ |
| 768px | ۲ یا ۳ |
| 1200px | ۴ |

## 🎓 Flex تطبیقی

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
```

**`flex-wrap: wrap`** = «اگر جا نبود، به خط بعد برو.»

## 🎓 تصاویر Responsive

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

**معنی:** تصویر هیچ‌وقت از container بزرگ‌تر نمی‌شود.

## 🎓 تست Responsive

### در Chrome DevTools

1. `F12` (یا `Cmd + Option + I`).
2. آیکون **Toggle Device Toolbar** (یا `Cmd + Shift + M`).
3. انتخاب دستگاه:
   - iPhone SE (375px)
   - iPhone 14 (390px)
   - iPad Mini (768px)
   - Desktop (1440px)

### ابزار آنلاین

- [responsivedesignchecker.com](https://responsivedesignchecker.com)
- [am-i-responsive.com](https://am-i-responsive.com)

## 🎓 در پروژه ما

### `global.css`

```css
@media (max-width: 768px) {
  h1 {
    font-size: 28px !important;
  }

  h2 {
    font-size: 20px !important;
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

### کامپوننت‌های کلیدی

- **Navbar:** منوی همبرگری
- **Hero:** فونت کوچک‌تر
- **Zoning:** Grid یک‌ستونه
- **Deliveries:** Grid یک‌ستونه
- **Contact:** Grid یک‌ستونه

## 🛑 عیب‌یابی

### مشکل ۱: Media Query اعمال نمی‌شود

**علت:** Inline Style است.

**راه‌حل:** به `<style>` منتقل کن.

### مشکل ۲: `!important` لازم است ولی جواب نمی‌دهد

**علت:** شاید Specificity بالاتر باشد.

**راه‌حل:** Selector را خاص‌تر کن.

### مشکل ۳: Grid در موبایل یک‌ستونه نمی‌شود

**علت:** `grid-template-columns` سخت‌گیر.

**راه‌حل:** از `auto-fit` استفاده کن.

### مشکل ۴: Navbar در موبایل به‌هم می‌ریزد

**علت:** Media Query ننوشتی.

**راه‌حل:** منوی همبرگری بساز.

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Media Query | `@media (max-width: 768px)` |
| Mobile First | `min-width` |
| Breakpoint | 768px |
| Grid تطبیقی | `repeat(auto-fit, minmax(...))` |
| Flex Wrap | `flex-wrap: wrap` |
| تصویر | `max-width: 100%` |

## آماده‌ای؟ برو به `06-media-queries.md`.