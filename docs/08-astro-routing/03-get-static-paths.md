# getStaticPaths

## 🎓 مفهوم

**`getStaticPaths`** یک **تابع مخصوص Astro** است که فقط در فایل‌های Dynamic Route (`[param].astro`) استفاده می‌شود.

## 🎓 کار آن

**این تابع به Astro می‌گوید:**
> «چه URLهایی باید در Build ساخته شوند؟»

**Astro این تابع را در Build Time صدا می‌زند.**

## 🎓 بدون getStaticPaths

اگر در یک فایل `[slug].astro` این تابع نباشد:

```
Error: getStaticPaths() is required for dynamic routes
```

**دلیل:** Astro نمی‌داند چه صفحاتی بسازد.

## 🛠 ساختار تابع

```astro
---
export async function getStaticPaths() {
  return [
    { params: { slug: "page-1" } },
    { params: { slug: "page-2" } },
    { params: { slug: "page-3" } },
  ];
}
---
```

**خروجی:** یک آرایه از Objectها.

## 🎓 ساختار Object

هر Object دو بخش **اختیاری** دارد:

```javascript
{
  params: { ... },   // اجباری برای URL
  props: { ... }     // اختیاری، برای داده
}
```

### params

```javascript
{ params: { slug: "my-slug" } }
```

**معنی:** صفحه در URL `/portfolio/my-slug` باشد.

### props

```javascript
{ props: { project: { ... } } }
```

**معنی:** داده `project` را به صفحه پاس بده.

## 🛠 مثال کامل

### فایل: `src/pages/blog/[slug].astro`

```astro
---
export async function getStaticPaths() {
  return [
    {
      params: { slug: "first-post" },
      props: { title: "اولین پست", date: "1404-01-01" },
    },
    {
      params: { slug: "second-post" },
      props: { title: "دومین پست", date: "1404-01-15" },
    },
    {
      params: { slug: "third-post" },
      props: { title: "سومین پست", date: "1404-02-01" },
    },
  ];
}

const { title, date } = Astro.props;
const { slug } = Astro.params;
---

<article>
  <h1>{title}</h1>
  <time>{date}</time>
  <p>Slug: {slug}</p>
</article>
```

### در Build

Astro سه فایل HTML می‌سازد:

- `/blog/first-post/index.html`
- `/blog/second-post/index.html`
- `/blog/third-post/index.html`

## 🎓 استفاده از داده JSON

### معمول‌ترین حالت

```astro
---
import masterData from "../../data/master_data.json";

export async function getStaticPaths() {
  return masterData.projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },
  }));
}

const { project } = Astro.props;
---
```

**توضیح:**

| خط | کار |
|---|---|
| `import masterData` | خواندن JSON |
| `masterData.projects.map(...)` | تبدیل هر پروژه به Object |
| `params: { slug }` | URL از slug |
| `props: { project }` | داده کامل پاس داده می‌شود |

## 🎓 چند پارامتر

### فایل: `src/pages/blog/[category]/[id].astro`

```astro
---
const posts = [
  { category: "tech", id: "1", title: "پست تکنولوژی ۱" },
  { category: "tech", id: "2", title: "پست تکنولوژی ۲" },
  { category: "design", id: "1", title: "پست طراحی ۱" },
];

export async function getStaticPaths() {
  return posts.map((post) => ({
    params: {
      category: post.category,
      id: post.id,
    },
    props: { post },
  }));
}

const { post } = Astro.props;
---

<h1>{post.title}</h1>
```

**URLها:**

- `/blog/tech/1`
- `/blog/tech/2`
- `/blog/design/1`

## 🎓 Rest Parameters

### فایل: `src/pages/docs/[...path].astro`

```astro
---
const pages = [
  { path: "intro" },
  { path: "guide/install" },
  { path: "guide/usage/advanced" },
];

export async function getStaticPaths() {
  return pages.map((page) => ({
    params: { path: page.path },
  }));
}

const { path } = Astro.params;
---

<h1>مسیر: {path}</h1>
```

**URLها:**

- `/docs/intro`
- `/docs/guide/install`
- `/docs/guide/usage/advanced`

**نکته:** Rest Parameters می‌تواند شامل `/` باشد.

## 🎓 Filter قبل از برگرداندن

```astro
export async function getStaticPaths() {
  return masterData.projects
    .filter((p) => p.is_public)
    .map((project) => ({
      params: { slug: project.slug },
      props: { project },
    }));
}
```

**نکته:** فقط پروژه‌های عمومی.

## 🎓 Sort قبل از برگرداندن

```astro
export async function getStaticPaths() {
  return masterData.projects
    .sort((a, b) => b.year - a.year)
    .map((project) => ({
      params: { slug: project.slug },
      props: { project },
    }));
}
```

**نتیجه:** ترتیب صفحات در Sitemap.

## 🎓 Async/Await

تابع `async` است، چون ممکن است داده از API بیاید:

```astro
export async function getStaticPaths() {
  const response = await fetch("https://api.example.com/projects");
  const projects = await response.json();

  return projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },
  }));
}
```

**نکته:** ما از JSON محلی استفاده می‌کنیم، اما اگر روزی API داشته باشی، همین ساختار کار می‌کند.

## 🎓 خروجی HTML

اگر ۳ پروژه داشته باشی، در Build:

```
dist/
├── portfolio/
│   ├── project-1/
│   │   └── index.html
│   ├── project-2/
│   │   └── index.html
│   └── project-3/
│       └── index.html
└── ...
```

**هر پروژه، یک صفحه کامل و مستقل.**

## 🎓 فایل‌های مرتبط در پروژه ما

### `src/pages/portfolio/[slug].astro`

```astro
---
import masterData from "../../data/master_data.json";
// ...

export async function getStaticPaths() {
  return masterData.projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },
  }));
}

const { project } = Astro.props;
---

<BaseLayout title={project.title_fa}>
  <Navbar />
  <!-- ۱۵ بخش -->
</BaseLayout>
```

## 🛑 عیب‌یابی

### مشکل ۱: `getStaticPaths is required`

**علت:** در فایل `[slug].astro` تابع ننوشتی.

**راه‌حل:** تابع را اضافه کن.

### مشکل ۲: `params.slug is required`

**علت:** Object `params` نداری.

**راه‌حل:**

```javascript
{ params: { slug: "..." } }   // ← باید params داشته باشد
```

### مشکل ۳: `Astro.props.project is undefined`

**علت:** در `getStaticPaths` `props` را نفرستادی.

**راه‌حل:**

```javascript
{
  params: { slug: "..." },
  props: { project: {...} },   // ← props هم لازم است
}
```

### مشکل ۴: صفحه 404 می‌دهد

**علت:** URL در `params` نیست.

**راه‌حل:** بررسی کن `slug` در `master_data.json` همان است که در URL می‌زنی.

### مشکل ۵: تعداد صفحات Build اشتباه است

**علت:** `master_data.json` تغییر نکرده یا Dev Server Cache دارد.

**راه‌حل:** Dev Server را Restart کن.

## 🎓 چرا Async؟

```javascript
export async function getStaticPaths() {
  // می‌توانی از await استفاده کنی
  const data = await fetchData();
  return data.map(...);
}
```

**اگر تمام داده محلی است:**

```javascript
export function getStaticPaths() {
  return masterData.projects.map(...);
}
```

**هر دو کار می‌کنند.** ما از `async` استفاده می‌کنیم که استاندارد است.

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| `getStaticPaths` | تابع مخصوص Dynamic Route |
| صدا زدن | در Build Time |
| خروجی | آرایه از Objects |
| `params` | URL |
| `props` | داده |
| `.map()` | تبدیل آرایه |
| `.filter()` | فیلتر کردن |

## آماده‌ای؟ برو به `04-nested-routes.md`.