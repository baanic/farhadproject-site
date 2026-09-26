# Import JSON در Astro

## 🎓 مفهوم

Astro به‌طور **بومی** از Import فایل‌های JSON پشتیبانی می‌کند.

## 🎓 چرا JSON؟

| فرمت | مزیت |
|---|---|
| **JSON** | استاندارد، سریع، قابل خواندن در هر زبان |
| XML | قدیمی، حجیم |
| YAML | خوانا، اما پیچیده‌تر |
| CSV | فقط جدول ساده |

**JSON بهترین گزینه برای داده‌های ساختاریافته است.**

## 🛠 گام ۱: قرار دادن فایل JSON

فایل `master_data.json` را در `src/data/` بگذار:

```
astro-site/
└── src/
    └── data/
        └── master_data.json
```

**چرا `src/data/`؟**
- Astro از `src/` پردازش می‌کند.
- Import راحت‌تر.
- Git فقط فایل نهایی را می‌بیند.

## 🛠 گام ۲: Import در Astro

```astro
---
import masterData from "../data/master_data.json";
---
```

**نکته:** مسیر نسبی از فایل صفحه.

**از `src/pages/index.astro`:**

```astro
import masterData from "../data/master_data.json";
// یک `../` به src/ برمی‌گردد
```

**از `src/pages/portfolio/[slug].astro`:**

```astro
import masterData from "../../data/master_data.json";
// دو `../` به src/ برمی‌گردد
```

## 🛠 گام ۳: استفاده از داده

```astro
---
import masterData from "../data/master_data.json";

const project = masterData.projects[0];
---

<h1>{project.title_fa}</h1>
<p>{project.subtitle_fa}</p>
<p>مساحت: {project.area_m2}</p>
```

## 🎓 آناتومی داده

### ساختار کلی

```json
{
  "version": "1.0.0",
  "build_date": "2026-09-26",
  "projects": [ ... ],
  "spaces": [ ... ],
  "acoustic_layers": [ ... ]
}
```

### دسترسی

| کد | خروجی |
|---|---|
| `masterData.version` | `"1.0.0"` |
| `masterData.projects` | آرایه پروژه‌ها |
| `masterData.projects[0]` | اولین پروژه |
| `masterData.projects[0].title_fa` | عنوان اولین پروژه |
| `masterData.projects.length` | تعداد پروژه‌ها |

## 🎓 دسترسی تودرتو

```json
{
  "projects": [
    {
      "project_id": "P-001",
      "contract": {
        "amount": 1337036052238,
        "duration": 18
      }
    }
  ]
}
```

**دسترسی:**

```javascript
masterData.projects[0].contract.amount    // 1337036052238
masterData.projects[0].contract.duration  // 18
```

## 🛠 مثال کامل از پروژه ما

### در `src/pages/index.astro`

```astro
---
import masterData from "../data/master_data.json";
import BaseLayout from "../layouts/BaseLayout.astro";
import Navbar from "../components/Navbar.astro";
import Hero from "../components/Hero.astro";

const project = masterData.projects[0];

const stats = [
  {
    label: "زیربنا",
    value: `${project.area_m2.toLocaleString("fa-IR")} مترمربع`,
  },
  {
    label: "مدت اجرا",
    value: `${project.total_duration_months} ماه`,
  },
  {
    label: "مبلغ قرارداد",
    value: project.contract_amount_display_fa,
  },
  {
    label: "وضعیت",
    value: project.status_fa,
  },
];
---

<BaseLayout title="خانه">
  <Navbar />
  <Hero
    title={project.title_fa}
    subtitle={project.subtitle_fa}
    stats={stats}
  />
</BaseLayout>
```

**تحلیل:**

| خط | کار |
|---|---|
| `import masterData` | خواندن JSON |
| `masterData.projects[0]` | اولین پروژه |
| `project.area_m2` | دسترسی به فیلد |
| `stats = [...]` | ساخت آرایه برای Hero |

## 🎓 داده در `getStaticPaths`

در فایل‌های داینامیک، داده از `getStaticPaths` می‌آید:

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

**نکته:** در این حالت، داده از `Astro.props` می‌آید، نه مستقیم از `masterData`.

## 🎓 TypeScript

Astro از TypeScript پشتیبانی می‌کند. می‌توانی Type تعریف کنی:

```typescript
interface Project {
  project_id: string;
  slug: string;
  title_fa: string;
  area_m2: number;
}

const project: Project = masterData.projects[0];
```

**مزیت:** Autocomplete و بررسی نوع.

**نکته:** در `tsconfig.json` Astro، Type را تعریف کن.

## 🎓 داده در Component

همان‌طور که در صفحه، در Component هم می‌توانی Import کنی:

```astro
---
// src/components/Hero.astro
import masterData from "../data/master_data.json";

const project = masterData.projects[0];
---

<h1>{project.title_fa}</h1>
```

**نکته:** مسیر نسبی از پوشه Component.

## 🎓 بهترین تمرین‌ها

### ۱. یک بار Import کن

```astro
---
// در ابتدای فایل
import masterData from "../data/master_data.json";
const project = masterData.projects[0];
---
```

### ۲. Props را از والد بگیر

اگر Component در جای مختلف استفاده می‌شود، Props بگیر:

```astro
---
// Hero.astro
const { project } = Astro.props;
---
```

**والد:**

```astro
<Hero project={masterData.projects[0]} />
```

**مزیت:** Component قابل استفاده مجدد.

### ۳. داده را در Frontmatter پردازش کن

```astro
---
import masterData from "../data/master_data.json";

const projects = masterData.projects;
const featured = projects.filter(p => p.is_featured);
const totalArea = projects.reduce((sum, p) => sum + p.area_m2, 0);
---
```

**نکته:** محاسبات در سرور انجام می‌شود، نه مرورگر.

## 🛑 عیب‌یابی

### مشکل ۱: `Cannot find module`

**علت:** مسیر اشتباه.

**راه‌حل:**

- از `pages/index.astro`: `../data/master_data.json`
- از `pages/portfolio/[slug].astro`: `../../data/master_data.json`

### مشکل ۲: `JSON.parse error`

**علت:** JSON نامعتبر (مثلاً کاما اضافه).

**راه‌حل:** JSON را در [jsonlint.com](https://jsonlint.com) بررسی کن.

### مشکل ۳: `undefined` نمایش داده می‌شود

**علت:** فیلد وجود ندارد یا نام اشتباه.

**راه‌حل:**

```astro
---
console.log(masterData.projects[0]);  // در ترمینال چاپ می‌شود
---
```

### مشکل ۴: فارسی نمایش داده نمی‌شود

**علت:** JSON با `ensure_ascii=True` ذخیره شده.

**راه‌حل:** در اسکریپت Python:

```python
json.dump(data, f, ensure_ascii=False, indent=2)
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Import | `import data from "../data/x.json"` |
| دسترسی | `data.projects[0].title_fa` |
| آرایه | `data.projects` |
| تعداد | `data.projects.length` |
| فیلتر | `data.projects.filter(...)` |
| Map | `data.projects.map(...)` |

## آماده‌ای؟ برو به `02-map-iteration.md`.