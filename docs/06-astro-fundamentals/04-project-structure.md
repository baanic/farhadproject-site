# ساختار پروژه Astro

## 🎓 مفهوم

Astro یک **ساختار پوشه مشخص** دارد. فهم این ساختار، کلید کار با Astro است.

## 🛠 ساختار کامل

```
astro-site/
├── .vscode/                  ← تنظیمات VS Code
├── node_modules/             ← پکیج‌ها (به Git نمی‌رود)
├── public/                   ← فایل‌های استاتیک
│   ├── favicon/
│   ├── fonts/
│   ├── images/
│   └── robots.txt
├── src/                      ← کد اصلی
│   ├── assets/              ← تصاویر پردازش‌شده
│   ├── components/          ← Componentها
│   ├── content/             ← Content Collections
│   ├── data/                ← JSON
│   ├── layouts/             ← Layoutها
│   ├── pages/               ← صفحات
│   └── styles/              ← CSS
├── .gitignore
├── astro.config.mjs          ← تنظیمات Astro
├── package.json              ← لیست پکیج‌ها
├── tsconfig.json             ← تنظیمات TypeScript
└── README.md
```

## 🎓 توضیح پوشه‌ها

### `public/` — فایل‌های استاتیک

فایل‌هایی که **بدون پردازش** به مرورگر می‌روند:

- تصاویر (لوگو، favicon)
- فونت‌ها
- فایل‌های PDF
- `robots.txt`

**مسیر در Build نهایی:**

`public/images/logo.png` → `site.com/images/logo.png`

**نکته:** از `public/` با `/` شروع می‌کنی:

```html
<img src="/images/logo.png" />
```

### `src/` — کد اصلی

همه چیزهایی که Astro پردازش می‌کند:

#### `src/pages/` — صفحات

**مهم‌ترین پوشه!** هر فایل، یک صفحه سایت:

| فایل | مسیر |
|---|---|
| `pages/index.astro` | `/` |
| `pages/about.astro` | `/about` |
| `pages/contact.astro` | `/contact` |
| `pages/portfolio/index.astro` | `/portfolio` |
| `pages/portfolio/[slug].astro` | `/portfolio/anything` |

#### `src/components/` — Componentها

قطعه‌های قابل استفاده مجدد:

```
components/
├── Navbar.astro
├── Footer.astro
├── StatCard.astro
└── portfolio/
    ├── Hero.astro
    └── Zoning.astro
```

#### `src/layouts/` — قالب‌ها

ساختار مشترک صفحات:

```
layouts/
└── BaseLayout.astro
```

#### `src/data/` — داده‌های JSON

```
data/
└── master_data.json
```

#### `src/styles/` — CSS

```
styles/
└── global.css
```

#### `src/content/` — Content Collections

برای Markdown یا JSON با Schema.

## 🎓 فایل‌های ریشه

### `astro.config.mjs`

تنظیمات اصلی Astro:

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://farhadproject.ir',
  integrations: [sitemap()],
});
```

### `package.json`

لیست پکیج‌ها و اسکریپت‌ها:

```json
{
  "name": "astro-site",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.0.0"
  }
}
```

### `tsconfig.json`

تنظیمات TypeScript:

```json
{
  "extends": "astro/tsconfigs/strict"
}
```

### `.gitignore`

فایل‌هایی که به Git نمی‌روند:

```
node_modules/
dist/
.astro/
.DS_Store
```

## 🎓 تفاوت `public/` و `src/assets/`

| پوشه | کاربرد |
|---|---|
| `public/` | فایل‌هایی که Astro پردازش نمی‌کند |
| `src/assets/` | تصاویری که Astro بهینه می‌کند |

**مثال:**

`public/images/hero.jpg` → فقط کپی می‌شود.

`src/assets/hero.jpg` → Astro آن را فشرده، WebP و بهینه می‌کند.

**برای ما:** اکثر تصاویر در `public/` هستند چون حجم زیاد و Astro آن‌ها را بهینه نمی‌کند.

## 🎓 جریان فایل‌ها در Build

```
[src/pages/index.astro]
        │
        ├── Import داده از [src/data/master_data.json]
        ├── Import Component از [src/components/Hero.astro]
        ├── Import Layout از [src/layouts/BaseLayout.astro]
        ├── Import CSS از [src/styles/global.css]
        │
        ↓
[Astro Build]
        │
        ├── ترکیب همه با هم
        ├── تبدیل به HTML/CSS/JS
        ├── کپی [public/]
        │
        ↓
[dist/]
        ├── index.html
        ├── portfolio/index.html
        ├── _astro/*.css
        ├── _astro/*.js
        └── images/logo.png
```

## 🎓 ساختار پروژه ما

پروژه واقعی ما:

```
astro-site/
├── public/
│   ├── favicon/
│   ├── fonts/             ← Shabnam
│   └── images/portfolio/  ← ۱۷ تصویر
├── src/
│   ├── components/
│   │   ├── Navbar.astro
│   │   ├── Footer.astro
│   │   ├── Hero.astro
│   │   ├── StatCard.astro
│   │   ├── ServiceCard.astro
│   │   ├── ProjectCard.astro
│   │   └── portfolio/    ← ۱۵ بخش پرتفولیو
│   ├── data/
│   │   └── master_data.json
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── services.astro
│   │   ├── contact.astro
│   │   └── portfolio/
│   │       ├── index.astro
│   │       └── [slug].astro
│   └── styles/
│       └── global.css
└── (files)
```

## 🎓 نام‌گذاری فایل‌ها

### Astro

- `PascalCase.astro` برای Component: `Navbar.astro`, `Hero.astro`
- `kebab-case.astro` برای صفحه: `about.astro`, `contact.astro`

### CSS

- `kebab-case.css`: `global.css`, `dark-mode.css`

### JSON

- `snake_case.json` یا `kebab-case.json`: `master_data.json`

### TypeScript/JavaScript

- `kebab-case.ts` یا `PascalCase.tsx` (برای React Component)

## 🎓 ساختار پوشه‌ها در Component

برای پروژه‌های بزرگ، زیرپوشه بساز:

```
components/
├── common/
│   ├── Navbar.astro
│   └── Footer.astro
├── portfolio/
│   ├── Hero.astro
│   └── Zoning.astro
└── blog/
    ├── PostCard.astro
    └── PostList.astro
```

**مزیت:** پروژه بزرگ، مرتب می‌ماند.

## 🎁 خلاصه

| پوشه | کاربرد |
|---|---|
| `public/` | فایل‌های استاتیک |
| `src/pages/` | صفحات |
| `src/components/` | Componentها |
| `src/layouts/` | قالب‌ها |
| `src/data/` | داده‌ها |
| `src/styles/` | CSS |
| `node_modules/` | پکیج‌ها |
| `dist/` | خروجی Build |

## آماده‌ای؟ برو به `05-astro-file-format.md`.