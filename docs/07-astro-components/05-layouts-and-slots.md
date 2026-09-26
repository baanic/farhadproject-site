# Layout و Slot

## 🎓 مفهوم

**Layout** یک Component است که **ساختار مشترک** صفحات را نگه می‌دارد.

## 🎓 چرا Layout؟

### مشکل: تکرار

بدون Layout، هر صفحه باید این ساختار را تکرار کند:

```astro
<html>
  <head>
    <meta charset="UTF-8" />
    <title>{title}</title>
  </head>
  <body>
    <Navbar />
    <main>...</main>
    <Footer />
  </body>
</html>
```

اگر ۱۰ صفحه داشته باشیم، ۱۰ بار این تکرار می‌شود.

### راه‌حل: Layout

یک بار می‌نویسی، در همه صفحات استفاده می‌کنی.

## 🎓 مفهوم: Slot

**Slot** یک **جای خالی** در Layout است که هر صفحه، محتوای خودش را در آن می‌گذارد.

### قیاس

Layout = قالب کاغذ نامه (سرصفحه، پاصفحه چاپی)
Slot = جای متن نامه

## 🛠 ساخت Layout

### `src/layouts/BaseLayout.astro`

```astro
---
import "../styles/global.css";
import Navbar from "../components/Navbar.astro";
import Footer from "../components/Footer.astro";

const { title, description } = Astro.props;
---

<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <title>{title}</title>
  </head>
  <body>
    <Navbar />
    <main>
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

**نکته:** `<slot />` جای محتوای صفحات است.

## 🛠 استفاده از Layout

### صفحه `index.astro`

```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
---

<BaseLayout title="خانه | پرتفولیو">
  <h1>صفحه اصلی</h1>
  <p>محتوای صفحه اینجاست.</p>
</BaseLayout>
```

### صفحه `about.astro`

```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
---

<BaseLayout title="درباره من">
  <h1>درباره من</h1>
  <p>متن درباره من.</p>
</BaseLayout>
```

**نکته:** محتوای هر صفحه، در Slot قرار می‌گیرد.

## 🎓 چه اتفاقی می‌افتد؟

### صفحه `about.astro`

```astro
<BaseLayout title="درباره من">
  <h1>درباره من</h1>
</BaseLayout>
```

### HTML نهایی

```html
<html lang="fa" dir="rtl">
  <head>
    <title>درباره من</title>
    ...
  </head>
  <body>
    <nav>...</nav>              <!-- از Navbar -->
    <main>
      <h1>درباره من</h1>        <!-- در Slot قرار گرفت -->
    </main>
    <footer>...</footer>        <!-- از Footer -->
  </body>
</html>
```

## 🎓 Named Slots (Slot با نام)

اگر Layout چند جای خالی داشته باشد:

### Layout

```astro
---
const { title } = Astro.props;
---

<html>
  <head>
    <title>{title}</title>
    <slot name="head" />
  </head>
  <body>
    <header>
      <slot name="header">پیش‌فرض هدر</slot>
    </header>
    <main>
      <slot />  <!-- slot پیش‌فرض -->
    </main>
    <footer>
      <slot name="footer">پیش‌فرض فوتر</slot>
    </footer>
  </body>
</html>
```

### استفاده

```astro
<BaseLayout title="خانه">
  <meta slot="head" name="keywords" content="..." />
  <h1 slot="header">عنوان</h1>
  <p>محتوای اصلی</p>
</BaseLayout>
```

**نکته:** با `slot="نام"` مشخص می‌کنی کدام محتوا در کدام Slot قرار گیرد.

## 🎓 Slot با Fallback

اگر محتوایی در Slot نباشد، مقدار پیش‌فرض نمایش داده می‌شود:

```astro
<slot>
  <p>محتوای پیش‌فرض</p>
</slot>
```

**مثال در Layout:**

```astro
<header>
  <slot name="header">
    <h1>سایت من</h1>
  </slot>
</header>
```

اگر صفحه محتوایی برای `header` نفرستد، `سایت من` نمایش داده می‌شود.

## 🛠 Layout در پروژه ما

### `BaseLayout.astro`

```astro
---
import "../styles/global.css";
import Footer from "../components/Footer.astro";

const { title, description } = Astro.props;
---

<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description || "پرتفولیو مهندسی فرهاد"} />
    <title>{title ? `${title} | پرتفولیو فرهاد` : "پرتفولیو فرهاد"}</title>
  </head>
  <body style="display: flex; flex-direction: column; min-height: 100vh;">
    <div style="flex: 1;">
      <slot />
    </div>
    <Footer />
  </body>
</html>
```

**نکته:** در این Layout، Navbar در Slot قرار می‌گیرد، چون هر صفحه Navbar خودش را دارد.

### استفاده در `index.astro`

```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
import Navbar from "../components/Navbar.astro";
import Hero from "../components/Hero.astro";

const project = masterData.projects[0];
---

<BaseLayout title="خانه">
  <Navbar />
  <Hero title={project.title_fa} ... />
</BaseLayout>
```

## 🎓 چرا Navbar در Layout نیست؟

سؤال خوبی است. دو رویکرد وجود دارد:

### رویکرد ۱: Navbar در Layout

```astro
<body>
  <Navbar />     ← همیشه نمایش داده می‌شود
  <slot />
  <Footer />
</body>
```

**مزیت:** کد کمتر در صفحات.

**عیب:** اگر صفحه‌ای Navbar نخواهد، باید Layout دیگری بسازد.

### رویکرد ۲: Navbar در صفحات (ما)

```astro
<BaseLayout>
  <Navbar />     ← در هر صفحه دستی می‌گذاریم
  <Hero />
</BaseLayout>
```

**مزیت:** انعطاف. صفحه‌ای می‌تواند Navbar نداشته باشد.

**عیب:** تکرار در هر صفحه.

**ما رویکرد ۲ انتخاب کردیم** چون:
- پروژه کوچک است.
- انعطاف مهم است.
- اگر صفحات زیاد شد، رویکرد ۱ بهتر است.

## 🎓 Layout تودرتو

می‌توانی Layout داشته باشی که از Layout دیگر استفاده می‌کند:

### `BaseLayout.astro`

```astro
---
import Footer from "../components/Footer.astro";
---
<html>
  <head><slot name="head" /></head>
  <body>
    <slot />
    <Footer />
  </body>
</html>
```

### `DocsLayout.astro`

```astro
---
import BaseLayout from "./BaseLayout.astro";
import Sidebar from "../components/Sidebar.astro";
---
<BaseLayout>
  <div style="display: flex;">
    <Sidebar />
    <main>
      <slot />
    </main>
  </div>
</BaseLayout>
```

**نکته:** `DocsLayout` از `BaseLayout` استفاده می‌کند و یک Sidebar اضافه می‌کند.

## 🎓 Layout سراسری در Astro

Astro گاهی اوقات اگر فایل `src/layouts/BaseLayout.astro` وجود داشته باشد، خودکار تشخیص می‌دهد. اما ما **دستی** آن را در هر صفحه Import می‌کنیم.

## 🎓 Props در Layout

Layout هم Props می‌گیرد:

```astro
---
const { title, description = "...", lang = "fa" } = Astro.props;
---
<html lang={lang}>
  <head>
    <title>{title}</title>
    <meta name="description" content={description} />
  </head>
  <body>
    <slot />
  </body>
</html>
```

**استفاده:**

```astro
<BaseLayout title="درباره من" description="درباره فرهاد">
  ...
</BaseLayout>
```

## 🛑 عیب‌یابی

### مشکل ۱: Slot نمایش داده نمی‌شود

**علت:** `<slot />` فراموش شده.

**راه‌حل:** در Layout، دقیقاً `<slot />` بگذار.

### مشکل ۲: Named Slot کار نمی‌کند

**علت:** در صفحه، `slot="name"` نگذاشتی.

**راه‌حل:**

```astro
<div slot="header">...</div>
```

### مشکل ۳: چند Layout لازم است

**راه‌حل:** Layout تودرتو بساز.

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Layout | Component ساختار مشترک |
| Slot | `<slot />` |
| Named Slot | `<slot name="x" />` |
| استفاده | `<Layout>...</Layout>` |
| Named استفاده | `<div slot="x">...</div>` |
| Fallback | `<slot>پیش‌فرض</slot>` |
