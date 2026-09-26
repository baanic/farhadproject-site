# Nested Routes

## 🎓 مفهوم

**Nested Routes** یعنی: مسیرهایی که در **پوشه‌های تودرتو** هستند.

## 🎓 ساختار

```
src/pages/
├── portfolio/
│   ├── index.astro              → /portfolio
│   └── [slug].astro             → /portfolio/:slug
├── blog/
│   ├── index.astro              → /blog
│   ├── [category]/
│   │   ├── index.astro          → /blog/:category
│   │   └── [post].astro         → /blog/:category/:post
```

## 🛠 مثال واقعی

### فایل: `src/pages/portfolio/index.astro`

```astro
---
import masterData from "../../data/master_data.json";
import BaseLayout from "../../layouts/BaseLayout.astro";
import Navbar from "../../components/Navbar.astro";
import ProjectCard from "../../components/ProjectCard.astro";

const projects = masterData.projects;
---

<BaseLayout title="پروژه‌ها">
  <Navbar />
  <main>
    <h1>پروژه‌ها</h1>
    <div class="grid">
      {projects.map((project) => (
        <ProjectCard project={project} />
      ))}
    </div>
  </main>
</BaseLayout>
```

**URL:** `/portfolio`.

### فایل: `src/pages/portfolio/[slug].astro`

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
  <!-- ۱۵ بخش پرتفولیو -->
</BaseLayout>
```

**URL:** `/portfolio/media-building-phase1`.

## 🎓 مسیر Import

در فایل‌های تودرتو، تعداد `../` بیشتر می‌شود:

| فایل | Import |
|---|---|
| `src/pages/index.astro` | `../components/X.astro` |
| `src/pages/about.astro` | `../components/X.astro` |
| `src/pages/portfolio/index.astro` | `../../components/X.astro` |
| `src/pages/portfolio/[slug].astro` | `../../components/X.astro` |
| `src/pages/blog/[cat]/[post].astro` | `../../../components/X.astro` |

**قاعده:**

- یک `../` برای هر سطح پوشه.
- `src/pages/blog/[cat]/[post].astro` = ۳ سطح بالا تا `src/`.

## 🎓 ساختار URL

| فایل | URL |
|---|---|
| `pages/index.astro` | `/` |
| `pages/about.astro` | `/about` |
| `pages/portfolio/index.astro` | `/portfolio` |
| `pages/portfolio/[slug].astro` | `/portfolio/:slug` |
| `pages/blog/index.astro` | `/blog` |
| `pages/blog/[category]/index.astro` | `/blog/:category` |
| `pages/blog/[category]/[post].astro` | `/blog/:category/:post` |

## 🎓 Layout مشترک برای یک بخش

می‌توانی برای همه صفحات یک بخش، یک Layout مشترک بسازی:

### `src/pages/portfolio/_Layout.astro`

**نکته:** فایل‌های با `_` در ابتدای نام، **صفحه نمی‌شوند**.

```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
import Navbar from "../../components/Navbar.astro";
---

<BaseLayout title="پروژه‌ها">
  <Navbar />
  <main style="max-width: 1100px; margin: 0 auto; padding: 60px 24px;">
    <slot />
  </main>
</BaseLayout>
```

### استفاده در `index.astro`

```astro
---
import Layout from "./_Layout.astro";
---
<Layout>
  <h1>لیست پروژه‌ها</h1>
</Layout>
```

## 🎓 Partial Routes

اگر بخواهی یک فایل را برای **Fragment** استفاده کنی:

### `src/pages/portfolio/_partial.astro`

**نکته:** فایل با `_` = صفحه نمی‌شود.

**اما می‌توانی Import کنی:**

```astro
---
import Partial from "./_partial.astro";
---
<Partial />
```

## 🎓 ریدایرکت

اگر URL قدیمی داشتی:

### `src/pages/old-page.astro`

```astro
---
return Astro.redirect("/new-page");
---
```

**یا با Redirect در Config:**

```javascript
// astro.config.mjs
export default defineConfig({
  redirects: {
    "/old-page": "/new-page",
  },
});
```

## 🎓 Navigation فعال

برای هایلایت کردن لینک فعال:

```astro
---
const currentPath = Astro.url.pathname;
const menu = [
  { label: "خانه", href: "/" },
  { label: "پروژه‌ها", href: "/portfolio" },
  { label: "تماس", href: "/contact" },
];
---

<nav>
  {menu.map(item => (
    <a
      href={item.href}
      style={`color: ${currentPath === item.href ? "#B8763E" : "#F5F0E6"};`}
    >
      {item.label}
    </a>
  ))}
</nav>
```

**`Astro.url.pathname`** = مسیر فعلی.

## 🎓 مسیرهای دینامیک تودرتو

### فایل: `src/pages/blog/[category]/[post].astro`

```astro
---
const posts = [
  { category: "tech", slug: "javascript-intro", title: "مقدمه JavaScript" },
  { category: "tech", slug: "css-grid", title: "CSS Grid" },
  { category: "design", slug: "color-theory", title: "تئوری رنگ" },
];

export async function getStaticPaths() {
  return posts.map((post) => ({
    params: {
      category: post.category,
      post: post.slug,
    },
    props: { post },
  }));
}

const { post } = Astro.props;
---

<article>
  <h1>{post.title}</h1>
  <p>دسته: {post.category}</p>
  <p>شناسه: {post.slug}</p>
</article>
```

**URLها:**

- `/blog/tech/javascript-intro`
- `/blog/tech/css-grid`
- `/blog/design/color-theory`

## 🎓 ساختار پروژه ما

```
src/pages/
├── index.astro                  → /
├── about.astro                  → /about
├── services.astro               → /services
├── contact.astro                → /contact
├── 404.astro                    → 404
└── portfolio/
    ├── index.astro              → /portfolio
    └── [slug].astro             → /portfolio/:slug
```

**جمع:** ۵ صفحه + ۱ داینامیک.

## 🎓 قرارداد نام‌گذاری

### فایل‌های عادی (صفحه)

- `about.astro`
- `contact.astro`
- `index.astro`

### فایل‌های داینامیک

- `[slug].astro`
- `[id].astro`
- `[...path].astro`

### فایل‌های غیرصفحه‌ای (Partial، Layout)

- `_Layout.astro`
- `_partial.astro`
- `_utils.astro`

**نکته:** هر فایل با `_` = صفحه نمی‌شود.

## 🛑 عیب‌یابی

### مشکل ۱: URL اشتباه

**علت:** ساختار پوشه اشتباه.

**راه‌حل:** پوشه‌ها را با URL مقایسه کن.

### مشکل ۲: Import کار نمی‌کند

**علت:** تعداد `../` اشتباه.

**راه‌حل:** برای فایل در `src/pages/portfolio/`:

- `../components/X.astro` ← غلط
- `../../components/X.astro` ← درست

### مشکل ۳: صفحه 404 در subfolder

**علت:** فایل `index.astro` را در پوشه نداری.

**راه‌حل:** `src/pages/portfolio/index.astro` بساز.

### مشکل ۴: `_partial.astro` صفحه شده

**علت:** فایل با `_` را در `pages/` گذاشتی و Astro صفحه‌اش کرده.

**راه‌حل:** مطمئن شو خط underscore در ابتدای نام است:

- `_partial.astro` ✅
- `partial.astro` ❌ (صفحه می‌شود)
- `partial_.astro` ❌ (صفحه می‌شود)

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Nested Route | `portfolio/[slug].astro` |
| Import Path | `../../components/` |
| Partial File | `_Layout.astro` |
| Active Link | `Astro.url.pathname` |
| Multi-level | `blog/[cat]/[post].astro` |
| Redirect | `Astro.redirect("/new")` |