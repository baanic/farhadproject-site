# فرمت فایل Astro

## 🎓 مفهوم

هر فایل Astro (`.astro`) سه بخش دارد:

```
---
// Frontmatter (JavaScript)
---

<!-- Template (HTML) -->

<style>
/* CSS */
</style>
```

## 🎓 ساختار کامل

```astro
---
// ۱. Frontmatter
// کد JavaScript که در سرور اجرا می‌شود
const title = "سلام";
const items = ["a", "b", "c"];
---

<!-- ۲. Template -->
<!-- HTML که به کاربر می‌رسد -->
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <ul>
      {items.map(item => <li>{item}</li>)}
    </ul>
  </body>
</html>

<!-- ۳. Style (اختیاری) -->
<style>
  h1 { color: red; }
</style>
```

## 🎓 بخش ۱: Frontmatter

بین `---` و `---` قرار دارد. **فقط JavaScript**.

### چرا Frontmatter؟

کدی که اینجا می‌نویسی، **در سرور** اجرا می‌شود. سپس فقط **نتیجه** به HTML می‌رود.

**مثال:**

```astro
---
const number = 42;
const doubled = number * 2;
---
<p>عدد: {doubled}</p>
```

**HTML نهایی:**

```html
<p>عدد: 84</p>
```

**توجه:** کاربر `number = 42` را نمی‌بیند. فقط نتیجه.

### نکته: این کد در مرورگر نیست

برخلاف React/Vue که کد در مرورگر اجرا می‌شود، در Astro کد **فقط در Build Time** اجرا می‌شود.

**نتیجه:** اطلاعات حساس، امن می‌مانند.

### مثال‌های Frontmatter

**متغیر:**

```astro
---
const name = "فرهاد";
const age = 30;
---
```

**آرایه:**

```astro
---
const items = [
  { name: "A", value: 1 },
  { name: "B", value: 2 },
];
---
```

**Import:**

```astro
---
import Header from "../components/Header.astro";
import data from "../data/master_data.json";
---
```

**تابع:**

```astro
---
function formatPrice(price) {
  return `$${price.toFixed(2)}`;
}

const price = formatPrice(99.99);
---
```

## 🎓 بخش ۲: Template

HTML است با **قدرت JavaScript**.

### تفاوت با HTML معمولی

| HTML | Astro Template |
|---|---|
| متن ثابت | می‌توانی متغیر بگذاری |
| بدون منطق | حلقه، شرط |

### متغیر در Template

```astro
---
const name = "فرهاد";
---
<p>سلام {name}</p>
```

**نتیجه:** `سلام فرهاد`.

### حلقه

```astro
---
const fruits = ["سیب", "موز", "پرتقال"];
---
<ul>
  {fruits.map(fruit => <li>{fruit}</li>)}
</ul>
```

**نتیجه:**

```html
<ul>
  <li>سیب</li>
  <li>موز</li>
  <li>پرتقال</li>
</ul>
```

### شرط

```astro
---
const isLoggedIn = true;
---
{isLoggedIn ? <p>خوش آمدی</p> : <p>لطفاً وارد شو</p>}
```

**نتیجه:** `خوش آمدی`.

### Component

```astro
---
import Header from "../components/Header.astro";
---
<Header />

<div>
  <h1>سلام</h1>
</div>
```

## 🎓 بخش ۳: Style

CSS محلی که فقط برای این فایل اعمال می‌شود.

### Style محلی (پیش‌فرض)

```astro
<style>
  h1 { color: red; }
</style>
```

**نکته:** Astro این استایل را **scoped** می‌کند. یعنی فقط این فایل را تحت تأثیر قرار می‌دهد.

**مثال:** اگر دو فایل `h1 { color: red }` داشته باشند، هیچ تداخلی نیست.

### Style سراسری

```astro
<style is:global>
  h1 { color: red; }
</style>
```

**نکته:** این استایل، همه فایل‌ها را تحت تأثیر قرار می‌دهد.

### Style با متغیر

```astro
---
const primaryColor = "#1B2A4A";
---
<div style={`color: ${primaryColor};`}>
  متن
</div>
```

## 🎓 تفاوت `style` و `class`

### استفاده از `<style>`

```astro
<style>
  .card {
    background: red;
  }
</style>

<div class="card">محتوا</div>
```

**مزیت:**
- CSS در یک جا.
- خوانایی بهتر.
- Pseudo-classes و Media Query.

### Inline Style

```astro
<div style="background: red;">محتوا</div>
```

**مزیت:**
- سریع‌تر برای استایل کوچک.
- می‌توانی متغیر بگذاری.

**مثال ما:**

```astro
<div style={`
  background: ${color};
  color: ${textColor};
`}>
```

**در پروژه ما:** برای رنگ‌های داینامیک، از Inline استفاده کردیم. برای استایل‌های ثابت، از `<style>`.

## 🎓 مثال کامل از پروژه ما

فایل `Hero.astro`:

```astro
---
import StatCard from "./StatCard.astro";

const { title, subtitle, stats } = Astro.props;
---

<section style="max-width: 1100px; margin: 0 auto; padding: 60px 24px;">
  <h1 style="color: #1B2A4A; font-size: 42px; margin-bottom: 12px;">
    {title}
  </h1>
  <p style="color: #B8763E; font-size: 20px; margin-bottom: 48px;">
    {subtitle}
  </p>

  <h2 style="color: #1B2A4A; font-size: 24px; margin-bottom: 20px;">
    آمار کلیدی
  </h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px;">
    {stats.map((stat) => (
      <StatCard label={stat.label} value={stat.value} />
    ))}
  </div>
</section>

<style>
  @media (max-width: 768px) {
    section {
      padding: 40px 16px !important;
    }
  }
</style>
```

**تحلیل:**

| خط | کار |
|---|---|
| `import StatCard` | Import Component |
| `const { title, subtitle, stats } = Astro.props` | دریافت Props |
| `<h1>{title}</h1>` | نمایش متغیر |
| `{stats.map(...)}` | حلقه روی آرایه |
| `<StatCard ... />` | استفاده از Component |
| `<style>@media ...</style>` | Media Query |

## 🎓 بهترین تمرین‌ها

### ۱. Frontmatter فقط برای منطق

```astro
---
// ✅ خوب: منطق
const items = [...];
const count = items.length;
---
```

### ۲. Template فقط برای نمایش

```astro
<!-- ✅ خوب: نمایش -->
<ul>
  {items.map(i => <li>{i.name}</li>)}
</ul>
```

### ۳. Style در `<style>` برای پیچیدگی

```astro
<!-- ✅ خوب -->
<style>
  .card:hover {
    transform: scale(1.05);
  }
</style>
```

### ۴. Inline Style برای داینامیک

```astro
<!-- ✅ خوب -->
<div style={`color: ${color};`}>متن</div>
```

## 🎁 خلاصه

| بخش | نقش |
|---|---|
| Frontmatter (`---`) | JavaScript در سرور |
| Template | HTML + منطق نمایش |
| `<style>` | CSS محلی |

| مفهوم | مثال |
|---|---|
| متغیر | `{name}` |
| حلقه | `{items.map(...)}` |
| شرط | `{condition ? ... : ...}` |
| Import | `import X from "..."` |
| Style محلی | `<style>` |
| Style سراسری | `<style is:global>` |

## آماده‌ای؟ برو به `06-dev-server.md`.