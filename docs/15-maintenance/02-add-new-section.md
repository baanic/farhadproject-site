# افزودن بخش جدید به پرتفولیو

## 🎓 مفهوم

**افزودن بخش جدید** = ساختن یک Component جدید و اضافه کردن آن به صفحه پرتفولیو.

## 🎓 چرا؟

شاید بخواهی بخش جدیدی مثل «Certifications» یا «Client Testimonials» یا «Awards» اضافه کنی.

## 🛠 گام ۱: ساخت Component جدید

```bash
cd ~/Documents/Projects/farhadproject/astro-site
code src/components/portfolio/NewSection.astro
```

**الگوی استاندارد:**

```astro
---
const items = [
  { title: "عنوان ۱", description: "توضیح ۱" },
  { title: "عنوان ۲", description: "توضیح ۲" },
  { title: "عنوان ۳", description: "توضیح ۳" },
];
---

<section style="padding: 80px 24px; background: #FFFFFF;">
  <div style="max-width: 1100px; margin: 0 auto;">
    <!-- Section Header -->
    <div style="display: flex; gap: 16px; margin-bottom: 48px;">
      <div style="width: 8px; height: 48px; background: #B8763E; border-radius: 4px;"></div>
      <div>
        <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px; margin: 0 0 4px;">
          NEW SECTION
        </p>
        <h2 style="color: #1B2A4A; font-size: 32px; margin: 0;">
          بخش جدید
        </h2>
      </div>
    </div>

    <!-- محتوا -->
    <div style="
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    ">
      {items.map(item => (
        <div style="
          background: #F5F0E6;
          padding: 24px;
          border-radius: 12px;
        ">
          <h3 style="color: #1B2A4A; font-size: 17px; margin-bottom: 12px;">
            {item.title}
          </h3>
          <p style="color: #4A5568; font-size: 14px; line-height: 1.8; margin: 0;">
            {item.description}
          </p>
        </div>
      ))}
    </div>
  </div>
</section>
```

## 🛠 گام ۲: Import در `[slug].astro`

```bash
code "src/pages/portfolio/[slug].astro"
```

**اضافه کن:**

```astro
---
// ... Importهای قبلی
import NewSection from "../../components/portfolio/NewSection.astro";
---

<BaseLayout>
  <Navbar />
  <!-- ... ۱۵ بخش قبلی -->
  <NewSection />
</BaseLayout>
```

## 🛠 گام ۳: تصمیم محل قرارگیری

**کجای ۱۵ بخش قبلی؟**

| نوع بخش | محل پیشنهادی |
|---|---|
| معرفی | بعد از AboutMini |
| نتیجه | قبل از ResultsSection |
| تماس | قبل از ContactSection |
| آموخته | بعد از LessonsSection |

**نکته:** برای حفظ روایت، بخش جدید را **منطقی** جای‌گذاری کن.

## 🛠 گام ۴: رنگ پس‌زمینه

**الگوی متناوب:**

| بخش قبلی | بخش جدید |
|---|---|
| سفید | کرم |
| کرم | سفید |

**بررسی:**

```astro
<LessonsSection />      {/* سفید */}
<NewSection />          {/* کرم */}
<ContactSection />      {/* گرادیانت */}
```

## 🛠 گام ۵: تست

```bash
npm run dev
```

برو به `/portfolio/media-building-phase1`.

**باید ببینی:** بخش جدید بین دو بخش دیگر.

## 🛠 گام ۶: Commit و Push

```bash
git add .
git commit -m "Add new section: Awards"
git push
```

## 🎓 مثال واقعی: افزودن بخش «Certifications»

### Component

```astro
---
const certs = [
  {
    name: "مدیریت پروژه حرفه‌ای",
    issuer: "PMI",
    year: "۱۴۰۳",
    color: "#5C7A5C",
  },
  {
    name: "کنترل پروژه پیشرفته",
    issuer: "PMI",
    year: "۱۴۰۲",
    color: "#2D5C8A",
  },
];
---

<section style="padding: 80px 24px; background: #F5F0E6;">
  <div style="max-width: 1100px; margin: 0 auto;">
    <!-- Header -->
    <div style="display: flex; gap: 16px; margin-bottom: 48px;">
      <div style="width: 8px; height: 48px; background: #B8763E; border-radius: 4px;"></div>
      <div>
        <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px;">
          CERTIFICATIONS
        </p>
        <h2 style="color: #1B2A4A; font-size: 32px; margin: 0;">
          مدارک و گواهینامه‌ها
        </h2>
      </div>
    </div>

    <!-- کارت‌ها -->
    <div style="
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    ">
      {certs.map(cert => (
        <div style={`background: ${cert.color}; color: #F5F0E6; padding: 32px; border-radius: 12px;`}>
          <div style="font-size: 28px; font-weight: 700; line-height: 1; margin-bottom: 12px;">
            {cert.year}
          </div>
          <h3 style="font-size: 18px; margin-bottom: 8px;">
            {cert.name}
          </h3>
          <p style="font-size: 14px; opacity: 0.85; margin: 0;">
            {cert.issuer}
          </p>
        </div>
      ))}
    </div>
  </div>
</section>
```

## 🎓 چک‌لیست افزودن بخش

- [ ] ساخت Component در `src/components/portfolio/`
- [ ] الگوی Section Header
- [ ] گرید Responsive
- [ ] رنگ پس‌زمینه متناسب
- [ ] Import در `[slug].astro`
- [ ] جای‌گذاری منطقی
- [ ] تست محلی
- [ ] Commit + Push

## 🛑 عیب‌یابی

### مشکل ۱: بخش جدید نمایش داده نمی‌شود

**علت:** Import فراموش شده.

**راه‌حل:** در `[slug].astro` Import کن.

### مشکل ۲: بخش جدید خیلی نزدیک به بخش قبلی

**علت:** Padding ندارد.

**راه‌حل:** `padding: 80px 24px;`.

### مشکل ۳: رنگ پس‌زمینه با بخش قبلی یکسان

**علت:** تناوب رعایت نشده.

**راه‌حل:** برعکس بخش قبلی.

## 🎓 در پروژه ما

**۱۵ بخش داریم.** برای بخش‌های بعدی، همین الگو.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | ساخت Component |
| ۲ | Import |
| ۳ | جای‌گذاری |
| ۴ | تست |
| ۵ | Commit |

## آماده‌ای؟ برو به `03-update-content.md`.