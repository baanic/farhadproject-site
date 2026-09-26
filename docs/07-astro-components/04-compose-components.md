# ترکیب Componentها

## 🎓 مفهوم

Componentها می‌توانند **Componentهای دیگر** را در خود داشته باشند.

### قیاس

مثل **لگو**:
- هر قطعه، خودش یک چیز است.
- اما با ترکیب، می‌توانی یک خانه بسازی.

## 🎓 چرا ترکیب؟

### ۱. تفکیک مسئولیت

هر Component، یک کار انجام می‌دهد.

### ۲. خوانایی

Componentهای بزرگ، به Componentهای کوچک می‌شکنند.

### ۳. استفاده مجدد

Component کوچک، در چند جا استفاده می‌شود.

## 🛠 مثال: Card و CardHeader

### Component کوچک

```astro
---
// components/CardHeader.astro
const { title, subtitle } = Astro.props;
---

<div style="padding: 16px; border-bottom: 1px solid #eee;">
  <h3 style="margin: 0; color: #1B2A4A;">
    {title}
  </h3>
  {subtitle && (
    <p style="margin: 4px 0 0; color: #666; font-size: 14px;">
      {subtitle}
    </p>
  )}
</div>
```

### Component بزرگ که از کوچک استفاده می‌کند

```astro
---
// components/Card.astro
import CardHeader from "./CardHeader.astro";

const { title, subtitle } = Astro.props;
---

<div style="
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
">
  <CardHeader title={title} subtitle={subtitle} />
  <div style="padding: 16px;">
    <slot />
  </div>
</div>
```

### استفاده

```astro
<Card title="پروژه A" subtitle="بخش فنی">
  <p>این توضیحات پروژه است.</p>
</Card>
```

## 🎓 مثال واقعی: Hero از StatCard

در پروژه ما، `Hero.astro` از `StatCard.astro` استفاده می‌کند:

### `StatCard.astro`

```astro
---
const { label, value } = Astro.props;
---

<div style="background: #F5F0E6; padding: 20px; border-radius: 8px;">
  <div style="color: #4A5568; font-size: 14px;">{label}</div>
  <div style="color: #1B2A4A; font-size: 20px; font-weight: 700;">
    {value}
  </div>
</div>
```

### `Hero.astro`

```astro
---
import StatCard from "./StatCard.astro";

const { title, subtitle, stats } = Astro.props;
---

<section style="max-width: 1100px; margin: 0 auto; padding: 60px 24px;">
  <h1>{title}</h1>
  <p>{subtitle}</p>

  <h2>آمار کلیدی</h2>
  <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;">
    {stats.map((stat) => (
      <StatCard label={stat.label} value={stat.value} />
    ))}
  </div>
</section>
```

**نکته:** `Hero` ۴ بار از `StatCard` استفاده می‌کند.

## 🎓 ساختار درختی Componentها

در پروژه ما، Componentها ساختار درختی دارند:

```
BaseLayout
├── Navbar
├── Slot (محتوای صفحه)
│   ├── PortfolioIntro
│   ├── AboutMini
│   ├── ServicesMini
│   ├── ProjectHero
│   ├── Zoning
│   ├── RoleTimeline
│   ├── TechnicalOfficeSection
│   ├── ProjectControlsSection
│   ├── QSSection
│   ├── AcousticDesignSection
│   ├── AcousticExecutionSection
│   ├── ResultsSection
│   ├── DeliveriesSection
│   ├── LessonsSection
│   └── ContactSection
└── Footer
```

**نکته:** هر Component، خودش می‌تواند زیر-Component داشته باشد.

## 🛠 مثال: Component با زیر-Component

### `ProjectHero.astro` (ما)

```astro
---
const { project } = Astro.props;

const stats = [
  { value: "۱۱,۰۰۰", unit: "مترمربع", label: "زیربنا", color: "#5C7A5C" },
  { value: "۱۸", unit: "ماه", label: "مدت اجرا", color: "#2D5C8A" },
];
---

<section>
  <h2>پروژه شاخص</h2>
  <h3>{project.title_fa}</h3>

  <div class="stats-grid">
    {stats.map((stat) => (
      <div style={`background: ${stat.color};`}>
        <div>{stat.value}</div>
        <div>{stat.unit}</div>
        <div>{stat.label}</div>
      </div>
    ))}
  </div>
</section>
```

**اینجا:** به‌جای `StatCard` جداگانه، **Inline** نوشتیم. چرا؟

- چون استایل متفاوتی داشت.
- اما در `Hero.astro` که StatCard ساده‌تری داشتیم، از Component استفاده کردیم.

**قاعده:**

- اگر استایل **مشترک** است → Component.
- اگر استایل **خاص** است → Inline.

## 🎓 Nested Components

Componentها می‌توانند چندین سطح تودرتو داشته باشند:

```astro
---
// Level1.astro
import Level2 from "./Level2.astro";
---

<Level2 />
```

```astro
---
// Level2.astro
import Level3 from "./Level3.astro";
---

<Level3 />
```

```astro
---
// Level3.astro
---
<p>من پایین‌ترین سطح هستم</p>
```

**نکته:** هر سطح، Props را به سطح بعدی می‌فرستد.

## 🎓 Props از Parent به Child

### Parent

```astro
---
// Parent.astro
import Child from "./Child.astro";

const user = { name: "فرهاد", age: 30 };
---

<Child user={user} showAge={true} />
```

### Child

```astro
---
// Child.astro
const { user, showAge } = Astro.props;
---

<div>
  <h3>{user.name}</h3>
  {showAge && <p>سن: {user.age}</p>}
</div>
```

## 🎓 Conditional Rendering

### شرط ساده

```astro
---
const isVisible = true;
---
{isVisible && <p>این نمایش داده می‌شود</p>}
```

### شرط سه‌گانه

```astro
{isLoggedIn ? <Dashboard /> : <LoginForm />}
```

### If-Else

```astro
---
if (status === "loading") {
  // ...
}
---

{status === "loading" && <Spinner />}
{status === "success" && <Content />}
{status === "error" && <ErrorBox />}
```

## 🎓 Fragment

اگر می‌خواهی چند چیز را برگردانی بدون Wrapper:

```astro
<>
  <h1>عنوان</h1>
  <p>متن</p>
</>
```

**نکته:** `<>` یک Fragment است. معادل `<Fragment>`.

## 🛑 عیب‌یابی

### مشکل ۱: `Cannot find module`

**علت:** مسیر Import اشتباه.

**راه‌حل:** از مسیر نسبی درست استفاده کن:

```astro
import Component from "./Component.astro";      // همان پوشه
import Component from "../Component.astro";     // یک بالا
import Component from "../../Component.astro";  // دو بالا
```

### مشکل ۲: Props به Child نمی‌رسد

**علت:** Props را در Child فرستادی اما نام اشتباه.

**راه‌حل:**

```astro
<!-- Parent -->
<Child title="سلام" />

<!-- Child -->
const { title } = Astro.props;  // نام باید یکی باشد
```

### مشکل ۳: Style Child روی Parent اثر می‌گذارد

**علت:** Style محلی در Astro اعمال می‌شود.

**راه‌حل:** Style را در Component خودش نگه‌دار.

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Import | `import X from "./X.astro"` |
| استفاده | `<X />` |
| Nested | Component در Component |
| Conditional | `{condition && ...}` |
| Ternary | `{cond ? <A /> : <B />}` |
| Fragment | `<><A /><B /></>` |

## آماده‌ای؟ برو به `05-layouts-and-slots.md`.