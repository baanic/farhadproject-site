# Dynamic Routes

## 🎓 مفهوم

**Dynamic Routes** یعنی: «یک فایل، چندین صفحه می‌سازد.»

## 🎓 مشکل: صفحه برای هر پروژه

فرض کن ۱۰ پروژه داری. می‌خواهی هر کدام یک صفحه داشته باشد:

- `/portfolio/project-1`
- `/portfolio/project-2`
- ...
- `/portfolio/project-10`

**راه ۱:** ۱۰ فایل بساز. (`project-1.astro`, `project-2.astro` و ...)

**مشکل:** اگر ۱۰۰ پروژه داشتی؟ ۱۰۰ فایل.

**راه ۲:** از **Dynamic Route** استفاده کن.

## 🎓 Syntax Dynamic Route

نام فایل را در **براکت** بگذار:

```
src/pages/portfolio/[slug].astro
```

**علامت `[]`** یعنی: این بخش، **متغیر** است.

**نتیجه:**

- `/portfolio/anything-1` → همین فایل
- `/portfolio/anything-2` → همین فایل
- `/portfolio/میخواهم-هرچه-بگویم` → همین فایل

## 🛠 ساختار

### فایل: `src/pages/portfolio/[slug].astro`

```astro
---
export async function getStaticPaths() {
  return [
    { params: { slug: "project-1" } },
    { params: { slug: "project-2" } },
    { params: { slug: "project-3" } },
  ];
}

const { slug } = Astro.params;
---

<html>
  <body>
    <h1>پروژه: {slug}</h1>
  </body>
</html>
```

### چه اتفاقی می‌افتد؟

Astro در Build، سه فایل HTML می‌سازد:

- `dist/portfolio/project-1/index.html`
- `dist/portfolio/project-2/index.html`
- `dist/portfolio/project-3/index.html`

**در هر فایل، مقدار `slug` متفاوت است.**

## 🎓 دو بخش مهم

### ۱. `getStaticPaths()`

تابع مخصوص Astro که می‌گوید: «چه URLهایی بساز؟»

### ۲. `Astro.params`

دسترسی به پارامترها (مثل `slug`).

## 🛠 مثال با داده واقعی

### فایل: `src/pages/portfolio/[slug].astro`

```astro
---
import masterData from "../../data/master_data.json";

export async function getStaticPaths() {
  return masterData.projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },   // ← پاس دادن داده به صفحه
  }));
}

const { project } = Astro.props;
---

<html>
  <body>
    <h1>{project.title_fa}</h1>
    <p>{project.subtitle_fa}</p>
    <p>مساحت: {project.area_m2} مترمربع</p>
  </body>
</html>
```

**چه اتفاقی می‌افتد؟**

1. Astro تابع `getStaticPaths` را صدا می‌زند.
2. تابع، لیست پروژه‌ها را برمی‌گرداند.
3. برای هر پروژه، یک صفحه HTML می‌سازد.
4. `project` را به هر صفحه پاس می‌دهد.

## 🎓 مفهوم: Params و Props

### Params

**Params** = پارامترهای URL.

```javascript
{ params: { slug: "media-building-phase1" } }
```

یعنی: این صفحه در URL `/portfolio/media-building-phase1` باشد.

### Props

**Props** = داده‌ای که به صفحه پاس داده می‌شود.

```javascript
{ props: { project: {...} } }
```

یعنی: کل Object پروژه را به صفحه بده.

## 🎓 تفاوت Params و Props

| Params | Props |
|---|---|
| در URL نمایش داده می‌شود | مخفی، فقط در کد |
| از نوع `string` | هر نوعی |
| در `Astro.params` | در `Astro.props` |

**مثال:**

```javascript
{
  params: { slug: "project-1" },        // URL: /portfolio/project-1
  props: { project: { full: "data" } }  // فقط در کد
}
```

## 🎓 چند پارامتر داینامیک

می‌توانی چند پارامتر داشته باشی:

### فایل: `src/pages/blog/[category]/[id].astro`

```astro
---
export async function getStaticPaths() {
  return [
    { params: { category: "tech", id: "1" } },
    { params: { category: "tech", id: "2" } },
    { params: { category: "design", id: "1" } },
  ];
}

const { category, id } = Astro.params;
---

<h1>دسته: {category}</h1>
<h2>شناسه: {id}</h2>
```

**URLها:**

- `/blog/tech/1`
- `/blog/tech/2`
- `/blog/design/1`

## 🎓 پارامتر Rest

می‌توانی همه بخش‌ها را بگیر:

### فایل: `src/pages/docs/[...path].astro`

```astro
---
export async function getStaticPaths() {
  return [
    { params: { path: "intro" } },
    { params: { path: "guide/install" } },
    { params: { path: "guide/usage/advanced" } },
  ];
}

const { path } = Astro.params;
---

<h1>مسیر: {path}</h1>
```

**URLها:**

- `/docs/intro`
- `/docs/guide/install`
- `/docs/guide/usage/advanced`

**نکته:** `[...path]` یعنی «هر چیزی در این سطح و پایین‌تر».

## 🎓 Fallback

اگر URL وجود نداشت چه اتفاقی می‌افتد؟

**پیش‌فرض:** صفحه 404.

می‌توانی **Fallback** تعریف کنی:

```astro
---
export const prerender = false;  // فعال‌سازی SSR

export async function getStaticPaths() {
  return [];  // لیست خالی
}

const { slug } = Astro.params;
---

<!-- در SSR، اینجا منطق داینامیک -->
{slug ? <h1>پروژه: {slug}</h1> : <h1>صفحه پیدا نشد</h1>}
```

**اما ما Static هستیم، از Fallback استفاده نمی‌کنیم.**

## 🛠 مثال کامل از پروژه ما

### `src/pages/portfolio/[slug].astro`

```astro
---
import masterData from "../../data/master_data.json";
import BaseLayout from "../../layouts/BaseLayout.astro";
import Navbar from "../../components/Navbar.astro";
import PortfolioIntro from "../../components/portfolio/PortfolioIntro.astro";
import AboutMini from "../../components/portfolio/AboutMini.astro";
// ... بقیه Importها

export async function getStaticPaths() {
  return masterData.projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },
  }));
}

const { project } = Astro.props;
---

<BaseLayout title={project.title_fa} description={project.subtitle_fa}>
  <Navbar />
  <PortfolioIntro projectName={project.title_fa} year="۱۴۰۴" />
  <AboutMini />
  <!-- ... ۱۵ بخش دیگر -->
</BaseLayout>
```

**این فایل، ۱ صفحه HTML در Build تولید می‌کند** (چون فعلاً یک پروژه داریم).

## 🎓 لینک به صفحه داینامیک

### از `ProjectCard.astro`

```astro
---
const { project } = Astro.props;
---

<a href={`/portfolio/${project.slug}`}>
  <h3>{project.title_fa}</h3>
</a>
```

**توجه:** `project.slug` در URL قرار می‌گیرد.

## 🎓 Validation Slug

می‌توانی در `getStaticPaths` فقط Slugهای معتبر را برگردانی:

```astro
export async function getStaticPaths() {
  return masterData.projects
    .filter((project) => project.is_public === true)
    .map((project) => ({
      params: { slug: project.slug },
      props: { project },
    }));
}
```

**نتیجه:** فقط پروژه‌های عمومی صفحه دارند.

## 🛑 عیب‌یابی

### مشکل ۱: `getStaticPaths is required`

**علت:** در یک فایل `[param].astro`، تابع `getStaticPaths` ننوشتی.

**راه‌حل:** تابع را اضافه کن.

### مشکل ۲: صفحه 404 می‌دهد

**علت:** URL در `getStaticPaths` نبوده.

**راه‌حل:** مقادیر `params` را بررسی کن.

### مشکل ۳: `slug` در `Astro.params` نیست

**علت:** نام اشتباه.

**راه‌حل:** نام فایل `[slug].astro` را با کلید Object هماهنگ کن.

### مشکل ۴: Build خطا می‌دهد

**علت:** داده در `getStaticPaths` خالی است.

**راه‌حل:** `master_data.json` را بررسی کن.

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Dynamic Route | `[slug].astro` |
| `getStaticPaths` | تابع اجباری |
| `Astro.params` | دسترسی به URL |
| `Astro.props` | دسترسی به داده |
| `props` | پاس داده به صفحه |
| چند پارامتر | `[category]/[id].astro` |
| Rest | `[...path].astro` |

## آماده‌ای؟ برو به `03-get-static-paths.md`.