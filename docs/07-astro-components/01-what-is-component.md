# Component چیست؟

## 🎓 مفهوم

**Component** یک **فایل مستقل** است که بخشی از UI را می‌سازد.

### قیاس روزمره

مثل **آجر** در ساختمان‌سازی:
- یک آجر، کوچک است.
- اما با ترکیب آجرها، یک ساختمان می‌سازی.
- هر آجر، قابل استفاده مجدد است.

**Component هم همین است:**
- یک بلوک کوچک.
- با ترکیب، صفحه کامل.
- قابل استفاده مجدد.

## 🎓 چرا Component؟

### ۱. DRY Principle

**DRY = Don't Repeat Yourself**

اگر کدی را دو بار نوشتی، جای Component است.

### ۲. Maintainability

تغییر در یک جا، همه‌جا اعمال می‌شود.

**مثال:** بخواهی رنگ دکمه‌ها را عوض کنی:

| بدون Component | با Component |
|---|---|
| ۵۰ فایل را دست بزن | فقط `Button.astro` را |

### ۳. تست‌پذیری

هر Component را می‌توانی جدا تست کنی.

### ۴. تیم‌کاری

هر نفر روی یک Component کار می‌کند.

## 🛠 ساخت اولین Component

### گام ۱: ساخت فایل

```bash
cd ~/Documents/Projects/farhadproject/astro-site
mkdir -p src/components
code src/components/Greeting.astro
```

### گام ۲: نوشتن کد

```astro
---
// Props
const { name } = Astro.props;
---

<div style="
  padding: 20px;
  background: #F5F0E6;
  border-radius: 8px;
  text-align: center;
">
  <h2 style="color: #1B2A4A;">
    سلام {name}!
  </h2>
  <p style="color: #4A5568;">
    به سایت من خوش آمدی.
  </p>
</div>
```

**ذخیره کن.**

### گام ۳: استفاده در صفحه

```bash
code src/pages/index.astro
```

```astro
---
import Greeting from "../components/Greeting.astro";
---

<html lang="fa" dir="rtl">
  <body>
    <Greeting name="فرهاد" />
    <Greeting name="علی" />
    <Greeting name="مریم" />
  </body>
</html>
```

**نتیجه:** سه کارت Greeting، با نام‌های مختلف.

## 🎓 آناتومی یک Component

```astro
---
// Frontmatter
// - Props
// - منطق
const { name } = Astro.props;
---

<!-- Template -->
<!-- - HTML -->
<div>{name}</div>

<!-- Style (اختیاری) -->
<style>
  div { color: red; }
</style>
```

## 🎓 قواعد نام‌گذاری

| قاعده | مثال |
|---|---|
| **PascalCase** | `Navbar.astro`, `Hero.astro` |
| توصیفی | `ProjectCard.astro`، نه `Card.astro` |
| تک کلمه یا ترکیبی | `Header.astro`, `UserProfile.astro` |

**چرا PascalCase؟**

- استاندارد صنعت.
- تمایز از فایل‌های عادی.
- هماهنگ با React و Vue.

## 🎓 انواع Component

### ۱. Presentational (نمایشی)

فقط نمایش. منطق کم.

```astro
---
const { title } = Astro.props;
---
<h2>{title}</h2>
```

### ۲. Layout

ساختار مشترک صفحات:

```astro
---
const { title } = Astro.props;
---
<html>
  <head><title>{title}</title></head>
  <body>
    <slot />
  </body>
</html>
```

### ۳. Container

مدیریت داده و منطق:

```astro
---
import ProjectCard from "./ProjectCard.astro";
import data from "../data/master_data.json";
---
{data.projects.map(p => <ProjectCard project={p} />)}
```

## 🎓 در پروژه ما

### مثال ۱: `StatCard.astro`

**نقش:** نمایش یک کارت آمار (مثل «۱۱,۰۰۰ مترمربع»).

**استفاده:**

```astro
<StatCard label="زیربنا" value="۱۱,۰۰۰ مترمربع" />
```

### مثال ۲: `Navbar.astro`

**نقش:** نوار ناوبری در بالای همه صفحات.

**استفاده:**

```astro
<Navbar />
```

**در همه صفحات:**
- `/` (index)
- `/portfolio`
- `/about`
- `/services`
- `/contact`

### مثال ۳: `ProjectCard.astro`

**نقش:** نمایش یک پروژه در لیست.

**استفاده:**

```astro
{projects.map(project => (
  <ProjectCard project={project} />
))}
```

## 🎓 ساختار پروژه ما

```
src/components/
├── Navbar.astro           ← نوار بالا
├── Footer.astro           ← پاورقی
├── Hero.astro             ← صفحه اصلی
├── StatCard.astro         ← کارت آمار
├── ServiceCard.astro      ← کارت خدمات
├── ProjectCard.astro      ← کارت پروژه
└── portfolio/
    ├── PortfolioIntro.astro
    ├── AboutMini.astro
    ├── ServicesMini.astro
    ├── ProjectHero.astro
    ├── Zoning.astro
    ├── RoleTimeline.astro
    ├── TechnicalOfficeSection.astro
    ├── ProjectControlsSection.astro
    ├── QSSection.astro
    ├── AcousticDesignSection.astro
    ├── AcousticExecutionSection.astro
    ├── ResultsSection.astro
    ├── DeliveriesSection.astro
    ├── LessonsSection.astro
    └── ContactSection.astro
```

**جمع:** حدود ۲۰ Component.

## 🎓 تفاوت با React

| | Astro | React |
|---|---|---|
| پسوند | `.astro` | `.jsx`, `.tsx` |
| اجرا در مرورگر | ❌ (فقط در سرور) | ✅ |
| حجم خروجی | HTML خالص | HTML + JS |
| سرعت | ⚡ | 🐌 |

**Astro:** HTML اول، JS در صورت نیاز.

**React:** JS اول، بعد HTML می‌سازد.

## 🛑 عیب‌یابی

### مشکل ۱: `Cannot find module`

**علت:** مسیر Import اشتباه.

**راه‌حل:** مسیر را بررسی کن. از `./` یا `../` استفاده کن.

### مشکل ۲: Props نمایش داده نمی‌شوند

**علت:** `Astro.props` را import نکردی.

**راه‌حل:**

```astro
---
const { name } = Astro.props;
---
```

### مشکل ۳: Style اعمال نمی‌شود

**علت:** Style محلی است.

**راه‌حل:** اگر می‌خواهی سراسری باشد:

```astro
<style is:global>
  ...
</style>
```

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| Component | قطعه کد قابل استفاده مجدد |
| پسوند | `.astro` |
| نام‌گذاری | PascalCase |
| ساخت | در `src/components/` |
| اجرا | در سرور (نه مرورگر) |

## آماده‌ای؟ برو به `02-props.md`.