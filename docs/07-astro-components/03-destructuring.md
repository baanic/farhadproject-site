# Destructuring در Astro

## 🎓 مفهوم

**Destructuring** = استخراج مقادیر از Object یا Array به متغیرهای جداگانه.

### قیاس

تصور کن یک جعبه داری با سه چیز:
- یک سیب
- یک موز
- یک پرتقال

**بدون Destructuring:**

```javascript
const box = { apple: "سیب", banana: "موز", orange: "پرتقال" };
const apple = box.apple;
const banana = box.banana;
const orange = box.orange;
```

**با Destructuring:**

```javascript
const { apple, banana, orange } = box;
```

## 🎓 چرا Destructuring؟

### ۱. کد کمتر

سه خط → یک خط.

### ۲. خوانایی

می‌دانی از همان اول چه فیلدهایی لازم داری.

### ۳. الگو استاندارد

در React، Vue، Astro و ... استفاده می‌شود.

## 🛠 Destructuring Object

### پایه

```javascript
const user = { name: "فرهاد", age: 30, city: "زاهدان" };

const { name, age, city } = user;
// name = "فرهاد"
// age = 30
// city = "زاهدان"
```

### با نام متفاوت

```javascript
const { name: userName, age: userAge } = user;
// userName = "فرهاد"
// userAge = 30
```

**چرا؟** اگر `name` قبلاً در Scope باشد، تعارض پیش می‌آید.

### با مقدار پیش‌فرض

```javascript
const { name, country = "ایران" } = user;
// name = "فرهاد"
// country = "ایران"
```

### تودرتو

```javascript
const user = {
  name: "فرهاد",
  address: { city: "زاهدان", country: "ایران" },
};

const { name, address: { city } } = user;
// name = "فرهاد"
// city = "زاهدان"
```

### در پارامتر تابع

```javascript
function greet({ name, age }) {
  return `سلام ${name}، سن: ${age}`;
}

greet({ name: "فرهاد", age: 30 });
```

## 🛠 Destructuring Array

### پایه

```javascript
const fruits = ["سیب", "موز", "پرتقال"];

const [first, second, third] = fruits;
// first = "سیب"
// second = "موز"
// third = "پرتقال"
```

### با Skip

```javascript
const [first, , third] = fruits;
// first = "سیب"
// third = "پرتقال"
```

### با Rest

```javascript
const [first, ...rest] = fruits;
// first = "سیب"
// rest = ["موز", "پرتقال"]
```

## 🎓 Destructuring در Astro

### الگوی استاندارد

```astro
---
const { title, subtitle, stats } = Astro.props;
---
```

**یعنی:** از Props، سه فیلد بردار.

### چرا این الگو؟

```astro
---
// ❌ بد: طولانی و تکراری
const title = Astro.props.title;
const subtitle = Astro.props.subtitle;
const stats = Astro.props.stats;
---
```

```astro
---
// ✅ خوب: یک خط
const { title, subtitle, stats } = Astro.props;
---
```

## 🛠 مثال کامل

### `Hero.astro`

```astro
---
const { title, subtitle, stats } = Astro.props;
---

<section>
  <h1>{title}</h1>
  <p>{subtitle}</p>
  <div>
    {stats.map(stat => <div>{stat.label}: {stat.value}</div>)}
  </div>
</section>
```

### استفاده

```astro
<Hero
  title="پروژه شاخص"
  subtitle="بخش فنی"
  stats={[
    { label: "مساحت", value: "۱۱,۰۰۰" },
    { label: "مدت", value: "۱۸ ماه" },
  ]}
/>
```

## 🎓 Destructuring در حلقه

### آرایه‌ای از آبجکت

```astro
---
const projects = [
  { title: "پروژه A", area: 5000 },
  { title: "پروژه B", area: 3000 },
];
---

{projects.map(({ title, area }) => (
  <div>
    <h3>{title}</h3>
    <p>{area}</p>
  </div>
))}
```

**به‌جای:**

```astro
{projects.map((project) => (
  <div>
    <h3>{project.title}</h3>
    <p>{project.area}</p>
  </div>
))}
```

## 🎓 مثال واقعی از پروژه ما

### `ProjectHero.astro`

```astro
---
const { project } = Astro.props;

const stats = [
  {
    value: project.area_m2.toLocaleString("fa-IR"),
    unit: "مترمربع",
    label: "زیربنا",
    color: "#5C7A5C",
  },
  {
    value: "۱۸",
    unit: "ماه",
    label: "مدت اجرا",
    color: "#2D5C8A",
  },
  // ...
];
---

<section>
  <h2>پروژه شاخص</h2>
  <h3>{project.title_fa}</h3>
  <!-- ... -->
</section>
```

### `QSSection.astro`

```astro
---
const disciplines = [
  {
    name: "ابنیه",
    count: "۴۷",
    unit: "قلم",
    color: "#8B6F47",
  },
  // ...
];
---

{disciplines.map(({ name, count, unit, color }) => (
  <div style={`background: ${color};`}>
    <h3>{name}</h3>
    <div>{count} {unit}</div>
  </div>
))}
```

**توجه:** در `map`، از `{ name, count, unit, color }` استفاده کردیم.

## 🎓 Destructuring با Rest

اگر می‌خواهی بعضی فیلدها را جدا کنی و بقیه را در یک Object بگذاری:

```javascript
const user = {
  name: "فرهاد",
  age: 30,
  city: "زاهدان",
  country: "ایران",
};

const { name, ...rest } = user;
// name = "فرهاد"
// rest = { age: 30, city: "زاهدان", country: "ایران" }
```

**کاربرد در Astro:**

```astro
---
const { label, ...otherProps } = Astro.props;
---

<div {...otherProps}>
  {label}
</div>
```

## 🎓 Destructuring با Alias

اگر نام فیلد با متغیر محلی تعارض دارد:

```javascript
const props = { name: "فرهاد" };
const name = "متغیر محلی";

const { name: propName } = props;
// propName = "فرهاد"
// name = "متغیر محلی"
```

## 🎓 در VS Code

VS Code خودکار Destructuring پیشنهاد می‌دهد:

```astro
---
const props = Astro.props;
// روی props برو، Cmd + . بزن
// "Extract to variable" را انتخاب کن
---
```

## 🛑 عیب‌یابی

### مشکل ۱: `undefined` می‌شود

**علت:** فیلد در Props نیست.

**راه‌حل:** مقدار پیش‌فرض بگذار:

```astro
const { name = "ناشناس" } = Astro.props;
```

### مشکل ۲: `Cannot destructure property of undefined`

**علت:** `Astro.props` خالی است.

**راه‌حل:**

```astro
const { name } = Astro.props || {};
```

### مشکل ۳: نام تکراری

**علت:** دو بار `name` داری.

**راه‌حل:** Alias:

```astro
const { name: userName } = Astro.props;
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Object | `const { a, b } = obj;` |
| Array | `const [x, y] = arr;` |
| پیش‌فرض | `const { a = 5 } = obj;` |
| Alias | `const { a: x } = obj;` |
| تودرتو | `const { a: { b } } = obj;` |
| Rest | `const { a, ...rest } = obj;` |
| در پارامتر | `function f({ a }) {}` |

## آماده‌ای؟ برو به `04-compose-components.md`.