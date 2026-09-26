# رندر شرطی در Astro

## 🎓 مفهوم

**رندر شرطی** یعنی: «فقط اگر شرطی برقرار بود، این بخش را نمایش بده.»

## 🎓 انواع شرط در Astro

| روش | کاربرد |
|---|---|
| `{condition && <A />}` | اگر درست، A را نشان بده |
| `{condition ? <A /> : <B />}` | اگر درست A، وگرنه B |
| `{condition ? <A /> : null}` | اگر درست A، وگرنه هیچ |
| `{condition || <B />}` | اگر غلط، B را نشان بده |

## 🛠 ۱. `&&` — شرط ساده

```astro
---
const isVisible = true;
---

{isVisible && <p>این نمایش داده می‌شود</p>}
```

**اگر `isVisible = false`:** هیچ چیز نمایش داده نمی‌شود.

### مثال واقعی

```astro
---
const project = masterData.projects[0];
---

{project.has_visor_window && (
  <div>
    <h3>پنجره ویزور</h3>
    <p>دارد</p>
  </div>
)}
```

## 🛠 ۲. سه‌گانه — `? :`

```astro
---
const isLoggedIn = true;
---

{isLoggedIn ? (
  <p>خوش آمدی</p>
) : (
  <p>لطفاً وارد شو</p>
)}
```

### مثال واقعی

```astro
---
const status = "delivered";
---

<span style={`
  color: ${status === "delivered" ? "#5C7A5C" : "#D89B5A"};
`}>
  {status === "delivered" ? "تحویل شده" : "در حال اجرا"}
</span>
```

## 🛠 ۳. `null` — هیچ چیز

اگر بخواهی فقط وقتی شرط برقرار بود چیزی نشان بدهی و اگر نبود **هیچ** (بدون else):

```astro
{condition ? <A /> : null}
```

**یا:**

```astro
{condition ? <A /> : ""}
```

## 🛠 ۴. `||` — مقدار پیش‌فرض

```astro
---
const name = "";
---

<p>{name || "ناشناس"}</p>
```

**خروجی:** `ناشناس` (چون `name` خالی است).

### مثال واقعی

```astro
---
const project = masterData.projects[0];
---

<p>{project.subtitle_fa || "بدون زیرعنوان"}</p>
```

## 🎓 شرط پیچیده

```astro
---
const user = { name: "فرهاد", isAdmin: true };
---

{user.isAdmin && (
  <button>پنل ادمین</button>
)}

{user.name && user.name.length > 0 && (
  <p>سلام {user.name}</p>
)}
```

## 🎓 شرط در Style

```astro
---
const status = "active";
---

<div style={`
  background: ${status === "active" ? "#5C7A5C" : "#D89B5A"};
  color: white;
  padding: 12px;
`}>
  وضعیت
</div>
```

## 🎓 شرط در Class

```astro
---
const isActive = true;
---

<a
  href="/"
  class={isActive ? "active" : ""}
>
  خانه
</a>
```

## 🎓 شرط چندگانه

```astro
---
const status = "loading";
---

{status === "loading" && <Spinner />}
{status === "success" && <Content />}
{status === "error" && <ErrorBox />}
```

**توجه:** اگر می‌خواهی فقط **یکی** نمایش داده شود، از `else if` استفاده کن:

```astro
---
if (status === "loading") {
  // ...
}
---

{status === "loading" ? (
  <Spinner />
) : status === "success" ? (
  <Content />
) : (
  <ErrorBox />
)}
```

## 🎓 رندر لیست خالی

```astro
---
const projects = [];
---

{projects.length > 0 ? (
  <div>
    {projects.map(p => <ProjectCard project={p} />)}
  </div>
) : (
  <p>هیچ پروژه‌ای موجود نیست.</p>
)}
```

**الگوی رایج:**

```astro
{items.length === 0 && <p>لیست خالی است.</p>}
{items.length > 0 && items.map(...)}
```

## 🛠 مثال واقعی از پروژه ما

### در `Navbar.astro`

```astro
---
const currentPath = Astro.url.pathname;
const menu = [
  { label: "خانه", href: "/" },
  { label: "پروژه‌ها", href: "/portfolio" },
];
---

{menu.map(item => (
  <a
    href={item.href}
    style={`
      color: ${currentPath === item.href ? "#B8763E" : "#F5F0E6"};
      border-bottom: 2px solid ${currentPath === item.href ? "#B8763E" : "transparent"};
    `}
  >
    {item.label}
  </a>
))}
```

### در `Hero.astro`

```astro
---
const { title, subtitle, stats } = Astro.props;
---

{subtitle && (
  <p style="color: #B8763E; font-size: 20px;">
    {subtitle}
  </p>
)}

{stats && stats.length > 0 && (
  <div class="stats-grid">
    {stats.map(stat => <StatCard {...stat} />)}
  </div>
)}
```

### در `ProjectCard.astro`

```astro
---
const { project } = Astro.props;
---

<div class="card">
  <h3>{project.title_fa}</h3>

  {project.subtitle_fa && (
    <p>{project.subtitle_fa}</p>
  )}

  {project.area_m2 && (
    <span>مساحت: {project.area_m2} مترمربع</span>
  )}

  <span class={project.executed ? "badge-success" : "badge-pending"}>
    {project.executed ? "اجرا شده" : "در حال اجرا"}
  </span>
</div>
```

## 🎓 مفهوم: Truthy و Falsy

در JavaScript، مقادیر زیر **Falsy** هستند (در شرط، غلط):

| مقدار | Falsy؟ |
|---|---|
| `false` | ✅ |
| `0` | ✅ |
| `""` (رشته خالی) | ✅ |
| `null` | ✅ |
| `undefined` | ✅ |
| `NaN` | ✅ |
| `[]` (آرایه خالی) | ❌ (truthy) |
| `{}` (آبجکت خالی) | ❌ (truthy) |
| `"0"` (رشته صفر) | ❌ (truthy) |

**نکته:** آرایه خالی **truthy** است. برای چک کردن خالی بودن:

```astro
{items.length > 0 && ...}
```

## 🛑 عیب‌یابی

### مشکل ۱: `0` نمایش داده می‌شود

**علت:**

```astro
{count && <p>تعداد: {count}</p>}
```

اگر `count = 0` باشد، `0` نمایش داده می‌شود (چون `0` falsy است، اما React/Astro آن را نشان می‌دهد).

**راه‌حل:**

```astro
{count > 0 && <p>تعداد: {count}</p>}
```

### مشکل ۲: شرط کار نمی‌کند

**علت:** مقدار `undefined` است.

**راه‌حل:**

```astro
---
console.log(value);  // بررسی کن
---
```

### مشکل ۳: `Cannot read property of undefined`

**علت:** دسترسی به فیلد Object که وجود ندارد.

**راه‌حل:** از Optional Chaining:

```astro
<p>{project?.contract?.amount}</p>
```

## 🎁 خلاصه

| الگو | کاربرد |
|---|---|
| `{a && <X />}` | اگر `a` درست |
| `{a ? <X /> : <Y />}` | اگر درست X، وگرنه Y |
| `{a ? <X /> : null}` | اگر درست X، وگرنه هیچ |
| `{a \|\| "پیش‌فرض"}` | مقدار پیش‌فرض |
| `{a?.b?.c}` | دسترسی امن |
| `{arr.length > 0 && ...}` | چک کردن آرایه |

## آماده‌ای؟ برو به `04-to-locale-string.md`.