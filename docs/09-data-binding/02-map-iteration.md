# حلقه Map در Astro

## 🎓 مفهوم

**`map()`** یک تابع JavaScript است که روی هر آیتم آرایه، یک تابع اجرا می‌کند و آرایه جدید برمی‌گرداند.

## 🎓 چرا Map در Astro؟

در Astro، برای **تکرار Componentها روی آرایه** از `map` استفاده می‌کنیم.

## 🛠 مثال ساده

### JavaScript خالص

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);
// doubled = [2, 4, 6]
```

### در Astro

```astro
---
const fruits = ["سیب", "موز", "پرتقال"];
---

<ul>
  {fruits.map(fruit => <li>{fruit}</li>)}
</ul>
```

**خروجی:**

```html
<ul>
  <li>سیب</li>
  <li>موز</li>
  <li>پرتقال</li>
</ul>
```

## 🎓 آناتومی Map

```javascript
{items.map(item => <Component prop={item} />)}
    ↑      ↑      ↑
    |      |      └── خروجی
    |      └── هر آیتم
    └── آرایه
```

## 🛠 مثال با Object

```astro
---
const users = [
  { name: "فرهاد", age: 30 },
  { name: "علی", age: 25 },
  { name: "مریم", age: 28 },
];
---

{users.map(user => (
  <div>
    <h3>{user.name}</h3>
    <p>سن: {user.age}</p>
  </div>
))}
```

## 🎓 تفاوت `map` و `for`

### `for` (در Frontmatter)

```astro
---
const items = ["A", "B", "C"];
const output = [];

for (const item of items) {
  output.push(`<li>${item}</li>`);
}
---

<ul>
  {output.map(o => <li>{o}</li>)}
</ul>
```

**نکته:** در Astro، `for` مستقیم در Template نمی‌شود. باید از `map` استفاده کنی.

### `map` (توصیه‌شده)

```astro
<ul>
  {items.map(item => <li>{item}</li>)}
</ul>
```

## 🎓 Map با Index

```astro
{items.map((item, index) => (
  <div>
    <span>{index + 1}.</span>
    <span>{item}</span>
  </div>
))}
```

**نکته:** `index` از ۰ شروع می‌شود.

## 🎓 Map با Destructuring

```astro
{users.map(({ name, age }) => (
  <div>
    <h3>{name}</h3>
    <p>{age}</p>
  </div>
))}
```

**نکته:** به‌جای `user.name`، مستقیم `name` استفاده می‌شود.

## 🛠 مثال واقعی از پروژه ما

### در `QSSection.astro`

```astro
---
const disciplines = [
  { name: "ابنیه", count: "۴۷", color: "#8B6F47" },
  { name: "مکانیک", count: "۱۵", color: "#5A4A7A" },
  { name: "برق", count: "۱۵", color: "#2D5C8A" },
];
---

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
  {disciplines.map((disc) => (
    <div style={`background: ${disc.color}; color: white; padding: 24px;`}>
      <h3>{disc.name}</h3>
      <div>{disc.count} قلم</div>
    </div>
  ))}
</div>
```

### در `ProjectCard.astro` (لیست پروژه‌ها)

```astro
---
const { projects } = Astro.props;
---

<div class="projects-grid">
  {projects.map((project) => (
    <ProjectCard project={project} />
  ))}
</div>
```

### در `Navbar.astro`

```astro
---
const menuItems = [
  { label: "خانه", href: "/" },
  { label: "پروژه‌ها", href: "/portfolio" },
  { label: "خدمات", href: "/services" },
  { label: "درباره من", href: "/about" },
  { label: "تماس", href: "/contact" },
];
---

<nav>
  <ul>
    {menuItems.map((item) => (
      <li>
        <a href={item.href}>{item.label}</a>
      </li>
    ))}
  </ul>
</nav>
```

## 🎓 Map تودرتو

```astro
---
const categories = [
  {
    name: "ابنیه",
    items: ["تخریب", "بتن", "آجرکاری"],
  },
  {
    name: "برق",
    items: ["کابل", "تابلو", "روشنایی"],
  },
];
---

{categories.map((cat) => (
  <div>
    <h2>{cat.name}</h2>
    <ul>
      {cat.items.map((item) => (
        <li>{item}</li>
      ))}
    </ul>
  </div>
))}
```

## 🎓 Map و Key

در React، برای `map` باید `key` بدهی. **در Astro لازم نیست**، چون Astro HTML تولید می‌کند، نه Virtual DOM.

**اما اگر** از Component تعاملی (React) در Astro استفاده کنی، آن Component خودش `key` می‌خواهد.

## 🎓 فیلتر + Map

```astro
---
const projects = masterData.projects;
const featured = projects.filter(p => p.is_featured);
---

{featured.map((project) => (
  <ProjectCard project={project} />
))}
```

**نکته:** `filter` اول، بعد `map`.

## 🎓 Sort + Map

```astro
---
const projects = masterData.projects
  .sort((a, b) => b.area_m2 - a.area_m2);
---

{projects.map((project) => (
  <ProjectCard project={project} />
))}
```

**نتیجه:** پروژه‌ها از بزرگ به کوچک.

## 🎓 Reduce

اگر می‌خواهی یک مقدار تجمیعی:

```astro
---
const projects = masterData.projects;
const totalArea = projects.reduce((sum, p) => sum + p.area_m2, 0);
---

<p>جمع مساحت: {totalArea.toLocaleString("fa-IR")} مترمربع</p>
```

## 🎓 Slice

فقط ۳ مورد اول:

```astro
{projects.slice(0, 3).map((project) => (
  <ProjectCard project={project} />
))}
```

## 🛑 عیب‌یابی

### مشکل ۱: Map نمایش داده نمی‌شود

**علت:** آرایه خالی است.

**راه‌حل:**

```astro
---
console.log(items);  // بررسی کن
---
```

### مشکل ۲: HTML اشتباه تولید می‌شود

**علت:** `{}` را در جای اشتباه گذاشتی.

**راه‌حل:**

```astro
<!-- درست -->
{items.map(i => <li>{i}</li>)}

<!-- اشتباه -->
{items.map(i => { return <li>{i}</li> })}
```

**نکته:** در Arrow Function، اگر `{}` استفاده کنی، باید `return` بزنی.

### مشکل ۳: `items is not defined`

**علت:** متغیر تعریف نشده.

**راه‌حل:** در Frontmatter تعریف کن.

### مشکل ۴: `items.map is not a function`

**علت:** `items` آرایه نیست.

**راه‌حل:**

```astro
---
console.log(Array.isArray(items));  // باید true باشد
---
```

## 🎁 خلاصه

| عملیات | مثال |
|---|---|
| Map | `items.map(i => ...)` |
| Map با Index | `items.map((i, idx) => ...)` |
| Destructuring | `items.map(({ a, b }) => ...)` |
| Filter | `items.filter(i => i.active)` |
| Sort | `items.sort((a, b) => a - b)` |
| Slice | `items.slice(0, 5)` |
| Reduce | `items.reduce((sum, i) => sum + i.n, 0)` |

## آماده‌ای؟ برو به `03-conditional-rendering.md`.