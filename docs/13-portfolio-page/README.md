# 🎯 صفحه پرتفولیو

## این بخش چیست؟

در این بخش، معماری **صفحه پرتفولیو** (۱۵ بخش) را توضیح می‌دهیم.

## چرا این بخش مهم است؟

**صفحه پرتفولیو، قلب سایت توست.**

- آینه‌ای از PDF پرتفولیو.
- روایت یکپارچه از پروژه.
- نمایش تمام مهارت‌ها.

## چالش اصلی

**چطور یک صفحه طولانی با ۱۵ بخش را سازمان‌دهی کنیم؟**

### بدون Component

یک فایل غول‌آسا با ۲۰۰۰ خط کد. غیرقابل نگهداری.

### با Component

۱۵ Component مستقل، هرکدام یک فایل. قابل نگهداری و توسعه.

## ساختار صفحه

```
/portfolio/media-building-phase1
├── PortfolioIntro           → عنوان اصلی
├── AboutMini                → معرفی کوتاه
├── ServicesMini             → ۴ خدمت
├── ProjectHero              → آمار پروژه
├── Zoning                   → ۴ بلوک
├── RoleTimeline             → نقش من
├── TechnicalOfficeSection   → دفتر فنی
├── ProjectControlsSection   → کنترل پروژه
├── QSSection                → متره
├── AcousticDesignSection    → طراحی آکوستیک
├── AcousticExecutionSection → اجرای آکوستیک
├── ResultsSection           → نتایج
├── DeliveriesSection        → تحویل‌ها
├── LessonsSection           → آموخته‌ها
└── ContactSection           → تماس
```

## چه چیزی یاد می‌گیری؟

| فایل | موضوع |
|---|---|
| [01 - ساختار روایت](./01-narrative-structure.md) | چرا این ترتیب |
| [02 - Componentهای بخش](./02-section-components.md) | هر بخش چیست |
| [03 - الگوهای قابل استفاده](./03-reusable-patterns.md) | الگوهای تکرارشونده |

## اصول طراحی

1. **تفکیک کامل:** هر بخش یک Component.
2. **Props ساده:** فقط `project` و داده‌های ثابت.
3. **استایل یکنواخت:** رنگ‌ها، فاصله‌ها، فونت.
4. **روایت منسجم:** هر بخش، ادامه بخش قبل.
5. **Responsive:** همه بخش‌ها در موبایل.

## آماده‌ای؟ برو به `01-narrative-structure.md`.