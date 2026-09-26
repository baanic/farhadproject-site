# Props در Astro

## 🎓 مفهوم

**Props** = **Properties**

داده‌ای که از **بیرون** به Component داده می‌شود.

### قیاس

مثل تابع در ریاضیات:

```
f(x) = x + 1
   ↑
   ورودی (Prop)
```

## 🎓 چرا Props؟

Component بدون Props، همیشه یکسان است. Props به آن **تنوع** می‌دهد.

**مثال:**

```astro
<StatCard label="زیربنا" value="۱۱,۰۰۰" />
<StatCard label="مدت" value="۱۸ ماه" />
<StatCard label="مبلغ" value="۱۳۳.۷" />
```

همان Component، سه محتوای مختلف.

## 🛠 پاس دادن Props

### گام ۱: تعریف در Component

```astro
---
// StatCard.astro
const { label, value } = Astro.props;
---

<div>
  <div>{label}</div>
  <div>{value}</div>
</div>
```

### گام ۲: استفاده

```astro
<StatCard label="زیربنا" value="۱۱,۰۰۰ مترمربع" />
```

### نتیجه

```html
<div>
  <div>زیربنا</div>
  <div>۱۱,۰۰۰ مترمربع</div>
</div>
```

## 🎓 آناتومی

```astro
<StatCard label="زیربنا" value="۱۱,۰۰۰" />
    ↑       ↑             ↑
    |       |             |
   نام    Prop ۱        Prop ۲
  Component
```

## 🎓 انواع Props

### ۱. String (متن)

```astro
<Greeting name="فرهاد" />
```

### ۲. Number (عدد)

```astro
<StatCard value={11000} />
```

**توجه:** `{}` برای اعداد و متغیرها.

### ۳. Boolean

```astro
<Button disabled={true} />
<Button disabled />        {/* کوتاه‌نویسی */}
```

### ۴. Object

```astro
---
const user = { name: "فرهاد", age: 30 };
---
<UserCard user={user} />
```

### ۵. Array

```astro
---
const items = ["A", "B", "C"];
---
<List items={items} />
```

### ۶. Function

```astro
---
const handleClick = () => console.log("کلیک");
---
<Button onClick={handleClick} />
```

**نکته:** توابع در Astro فقط در Frontmatter کار می‌کنند.

## 🎓 Props اختیاری

بعضی Props لازم نیستند همیشه مقدار داشته باشند.

### تعریف

```astro
---
const { title, subtitle = "زیرعنوان پیش‌فرض" } = Astro.props;
---
<h1>{title}</h1>
<p>{subtitle}</p>
```

### استفاده

```astro
<Card title="عنوان" />
<!-- subtitle: "زیرعنوان پیش‌فرض" -->

<Card title="عنوان" subtitle="زیرعنوان خاص" />
<!-- subtitle: "زیرعنوان خاص" -->
```

## 🎓 Props تودرتو

می‌توانی Object تودرتو پاس بدهی:

```astro
---
// components/UserCard.astro
const { user } = Astro.props;
---

<div>
  <h3>{user.name}</h3>
  <p>{user.email}</p>
  <p>{user.address.city}</p>
</div>
```

**استفاده:**

```astro
---
const user = {
  name: "فرهاد",
  email: "farhad@example.com",
  address: {
    city: "زاهدان",
    country: "ایران",
  },
};
---
<UserCard user={user} />
```

## 🎓 Spread Props

اگر Object داری و می‌خواهی همه فیلدها را پاس بدهی:

```astro
---
const props = {
  label: "زیربنا",
  value: "۱۱,۰۰۰",
  icon: "📐",
};
---
<StatCard {...props} />
```

معادل:

```astro
<StatCard label={props.label} value={props.value} icon={props.icon} />
```

## 🛠 مثال کامل: `StatCard.astro`

```astro
---
// src/components/StatCard.astro
const { label, value } = Astro.props;
---

<div style="
  background: #F5F0E6;
  padding: 20px;
  border-radius: 8px;
">
  <div style="
    color: #4A5568;
    font-size: 14px;
    margin-bottom: 8px;
  ">
    {label}
  </div>
  <div style="
    color: #1B2A4A;
    font-size: 20px;
    font-weight: bold;
  ">
    {value}
  </div>
</div>
```

**استفاده در `Hero.astro`:**

```astro
---
import StatCard from "./StatCard.astro";

const stats = [
  { label: "زیربنا", value: "۱۱,۰۰۰ مترمربع" },
  { label: "مدت اجرا", value: "۱۸ ماه" },
  { label: "مبلغ قرارداد", value: "۱۳۳.۷ میلیارد" },
  { label: "وضعیت", value: "تحویل شده" },
];
---

<section>
  <h2>آمار کلیدی</h2>
  <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;">
    {stats.map((stat) => (
      <StatCard label={stat.label} value={stat.value} />
    ))}
  </div>
</section>
```

## 🎓 Props با فایل JSON

در پروژه ما، Props از `master_data.json` می‌آید:

```astro
---
import masterData from "../data/master_data.json";
const project = masterData.projects[0];
---

<ProjectCard
  title={project.title_fa}
  area={project.area_m2}
  status={project.status_fa}
/>
```

## 🎓 Debug Props

اگر Props درست نمایش داده نمی‌شود:

```astro
---
const props = Astro.props;
console.log(props);  // در ترمینال چاپ می‌شود
---
```

**نکته:** `console.log` در Astro، در **ترمینال** نمایش داده می‌شود، نه مرورگر.

## 🎓 Props در Componentهای تودرتو

```astro
---
// Parent.astro
import Child from "./Child.astro";
const user = { name: "فرهاد" };
---

<Child user={user} />
```

```astro
---
// Child.astro
import GrandChild from "./GrandChild.astro";
const { user } = Astro.props;
---

<GrandChild name={user.name} />
```

**نکته:** Props از Parent به Child منتقل می‌شوند. از Child به Parent **نه**.

## 🛑 عیب‌یابی

### مشکل ۱: `undefined` نمایش داده می‌شود

**علت:** Prop پاس داده نشده یا نام اشتباه.

**راه‌حل:**

```astro
---
const { label } = Astro.props;
console.log("label:", label);
---
```

### مشکل ۲: Prop عددی به رشته تبدیل می‌شود

**علت:** اعداد را باید در `{}` بگذاری.

```astro
<!-- اشتباه -->
<StatCard value="11000" />

<!-- درست -->
<StatCard value={11000} />
```

### مشکل ۳: `Cannot read property of undefined`

**علت:** Prop وجود ندارد.

**راه‌حل:** مقدار پیش‌فرض بگذار:

```astro
const { value = 0 } = Astro.props;
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| String | `label="زیربنا"` |
| Number | `value={11000}` |
| Boolean | `disabled={true}` |
| Object | `user={userObject}` |
| Array | `items={[...]}` |
| پیش‌فرض | `subtitle = "..."` |
| Spread | `{...props}` |

## آماده‌ای؟ برو به `03-destructuring.md`.