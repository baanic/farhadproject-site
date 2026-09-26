# 🧩 کامپوننت‌های Astro

## این بخش چیست؟

در این بخش، **Component** را یاد می‌گیری — بلوک‌های سازنده هر سایت Astro.

## Component چیست؟

یک **قطعه کد قابل استفاده مجدد** که:
- یک بار نوشته می‌شود.
- در چندین جا استفاده می‌شود.
- Props دریافت می‌کند.

## چرا Component؟

### بدون Component

اگر ۱۰ کارت پروژه داری، باید ۱۰ بار HTML بنویسی:

```html
<div class="card">
  <h3>پروژه A</h3>
  <p>مساحت: 5000</p>
</div>
<div class="card">
  <h3>پروژه B</h3>
  <p>مساحت: 3000</p>
</div>
<!-- ۸ بار دیگر... -->
```

**مشکل:** اگر بخواهی رنگ کارت را عوض کنی، ۱۰ جا را دست می‌زنی.

### با Component

```astro
<ProjectCard title="پروژه A" area={5000} />
<ProjectCard title="پروژه B" area={3000} />
<!-- بقیه -->
```

**مزیت:** یک بار می‌نویسی، همه‌جا استفاده می‌کنی.

## چه چیزی یاد می‌گیری؟

| فایل | موضوع |
|---|---|
| [01 - Component چیست؟](./01-what-is-component.md) | مفاهیم، ساخت |
| [02 - Props](./02-props.md) | پاس دادن داده |
| [03 - Destructuring](./03-destructuring.md) | استخراج Props |
| [04 - ترکیب Componentها](./04-compose-components.md) | Component در Component |
| [05 - Layout و Slot](./05-layouts-and-slots.md) | ساختار مشترک |
| [06 - Slots پیشرفته](./06-advanced-slots.md) | Slot با نام |

## ساختار پوشه

در پروژه ما:

```
src/components/
├── Navbar.astro
├── Footer.astro
├── Hero.astro
├── StatCard.astro
├── ServiceCard.astro
├── ProjectCard.astro
└── portfolio/
    ├── PortfolioIntro.astro
    ├── AboutMini.astro
    ├── ServicesMini.astro
    └── ... (۱۲ Component دیگر)
```

## آماده‌ای؟ برو به `01-what-is-component.md`.