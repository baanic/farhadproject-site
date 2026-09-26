# Componentهای هر بخش

## 🎓 مفهوم

هر بخش صفحه پرتفولیو، یک **Component مستقل** است.

## 🎓 چرا Component جدا؟

### ۱. تفکیک مسئولیت

هر Component، یک کار انجام می‌دهد.

### ۲. قابل تست

هر بخش را می‌توانی جدا تست کنی.

### ۳. قابل توسعه

اگر بخشی را عوض کنی، بقیه دست‌نخورده می‌مانند.

## 🎓 ساختار پوشه

```
src/components/portfolio/
├── PortfolioIntro.astro
├── AboutMini.astro
├── ServicesMini.astro
├── ProjectHero.astro
├── Zoning.astro
├── RoleTimeline.astro
├── TechnicalOfficeSection.astro
├── ProjectControlsSection.astro
├── QSSection.astro
├── AcousticDesignSection.astro
├── AcousticExecutionSection.astro
├── ResultsSection.astro
├── DeliveriesSection.astro
├── LessonsSection.astro
└── ContactSection.astro
```

## 🎓 Component ۱: PortfolioIntro

**نقش:** جلد صفحه.

**Props:**
- `projectName: string`
- `year: string`

**محتوا:**
- عنوان بزرگ «پرتفولیو فنی»
- زیرعنوان خدمات
- نام پروژه
- گرادیانت سرمه‌ای

**استفاده:**

```astro
<PortfolioIntro projectName={project.title_fa} year="۱۴۰۴" />
```

## 🎓 Component ۲: AboutMini

**نقش:** معرفی کوتاه.

**Props:** ندارد.

**محتوا:**
- عکس پروفایل
- نام + تخصص
- بیوگرافی کوتاه
- Tagهای تخصصی
- اطلاعات تماس

**استفاده:**

```astro
<AboutMini />
```

## 🎓 Component ۳: ServicesMini

**نقش:** ۴ خدمت.

**Props:** ندارد.

**محتوا:**
- ۴ کارت خدمت
- رنگ اختصاصی هر خدمت

**استفاده:**

```astro
<ServicesMini />
```

## 🎓 Component ۴: ProjectHero

**نقش:** آمار پروژه.

**Props:**
- `project: Project`

**محتوا:**
- تصویر پروژه
- عنوان و توضیح
- ۴ کارت آمار بزرگ

**استفاده:**

```astro
<ProjectHero project={project} />
```

## 🎓 Component ۵: Zoning

**نقش:** ۴ بلوک.

**Props:** ندارد.

**محتوا:**
- ۴ کارت بلوک
- ویژگی‌های هر بلوک

**استفاده:**

```astro
<Zoning />
```

## 🎓 Component ۶: RoleTimeline

**نقش:** نقش من در ۴ مرحله.

**Props:** ندارد.

**محتوا:**
- تایم‌لاین افقی
- ۴ دایره رنگی
- توضیح هر مرحله

**استفاده:**

```astro
<RoleTimeline />
```

## 🎓 Component ۷: TechnicalOfficeSection

**نقش:** دفتر فنی.

**Props:** ندارد.

**محتوا:**
- متن توضیحی
- کارت آمار در کنار (۴۰+ صورت‌جلسه، ۱۰۰٪ مستندسازی، ۴ رشته)
- ۳ کارت ویژگی

**استفاده:**

```astro
<TechnicalOfficeSection />
```

## 🎓 Component ۸: ProjectControlsSection

**نقش:** کنترل پروژه.

**Props:** ندارد.

**محتوا:**
- WBS چهار فاز
- تصویر S-Curve
- آمار: ۸۸ فعالیت، ۱۲ نقطه عطف، ۱۸ ماه

**استفاده:**

```astro
<ProjectControlsSection />
```

## 🎓 Component ۹: QSSection

**نقش:** متره.

**Props:** ندارد.

**محتوا:**
- ۳ کارت متره (ابنیه، مکانیک، برق)
- نوار درصد
- فصل‌ها
- ۳ کارت شاخص

**استفاده:**

```astro
<QSSection />
```

## 🎓 Component ۱۰: AcousticDesignSection

**نقش:** طراحی آکوستیک.

**Props:** ندارد.

**محتوا:**
- مقطع دیوار (SVG)
- مقطع سقف (SVG)
- ۵ لایه دیوار
- ۴ لایه سقف
- ۳ کارت جزئیات (درب، ویزور، تهویه)

**استفاده:**

```astro
<AcousticDesignSection />
```

## 🎓 Component ۱۱: AcousticExecutionSection

**نقش:** اجرای آکوستیک.

**Props:** ندارد.

**محتوا:**
- متن توضیحی
- گالری ۶ تصویر

**استفاده:**

```astro
<AcousticExecutionSection />
```

## 🎓 Component ۱۲: ResultsSection

**نقش:** نتایج.

**Props:** ندارد.

**محتوا:**
- متن توضیحی
- ۴ کارت آمار (۱۲۲، ۴، ۱، ۱۲)
- تصویر

**استفاده:**

```astro
<ResultsSection />
```

## 🎓 Component ۱۳: DeliveriesSection

**نقش:** تحویل‌ها.

**Props:** ندارد.

**محتوا:**
- ۴ کارت بلوک
- اقلام تحویل
- رشته‌های تحویل

**استفاده:**

```astro
<DeliveriesSection />
```

## 🎓 Component ۱۴: LessonsSection

**نقش:** آموخته‌ها.

**Props:** ندارد.

**محتوا:**
- تصویر
- ۳ درس کلیدی

**استفاده:**

```astro
<LessonsSection />
```

## 🎓 Component ۱۵: ContactSection

**نقش:** تماس.

**Props:** ندارد.

**محتوا:**
- گرادیانت سرمه‌ای
- اطلاعات تماس
- QR Code

**استفاده:**

```astro
<ContactSection />
```

## 🎓 Props در برابر داده ثابت

| نوع داده | مثال | چرا |
|---|---|---|
| **Prop** | `project` | در چند صفحه استفاده می‌شود |
| **ثابت** | لیست خدمات | فقط اینجا |

**نکته:** اگر داده فقط در یک Component استفاده می‌شود، می‌توانی **داخل** آن تعریف کنی.

## 🎓 مثال کامل `ProjectHero`

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
  // ...
];
---

<section style="padding: 80px 24px; background: #FFFFFF;">
  <div style="max-width: 1100px; margin: 0 auto;">
    <!-- Eyebrow -->
    <div style="display: flex; gap: 16px; margin-bottom: 48px;">
      <div style="width: 8px; height: 48px; background: #B8763E;"></div>
      <div>
        <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px;">
          FEATURED PROJECT
        </p>
        <h2 style="color: #1B2A4A; font-size: 32px;">
          پروژه شاخص
        </h2>
      </div>
    </div>

    <!-- تصویر -->
    <img src="/images/portfolio/project-exterior.jpg" />

    <!-- عنوان -->
    <h3>{project.title_fa}</h3>
    <p>{project.subtitle_fa}</p>

    <!-- کارت‌های آمار -->
    <div class="stats-grid">
      {stats.map((stat) => (
        <div style={`background: ${stat.color};`}>
          <div>{stat.value}</div>
          <div>{stat.unit}</div>
          <div>{stat.label}</div>
        </div>
      ))}
    </div>
  </div>
</section>
```

## 🎓 چیدمان در `[slug].astro`

```astro
---
import masterData from "../../data/master_data.json";
// ... همه Importها

export async function getStaticPaths() {
  return masterData.projects.map((project) => ({
    params: { slug: project.slug },
    props: { project },
  }));
}

const { project } = Astro.props;
---

<BaseLayout title={project.title_fa} description={project.subtitle_fa}>
  <Navbar />

  <PortfolioIntro projectName={project.title_fa} year="۱۴۰۴" />
  <AboutMini />
  <ServicesMini />
  <ProjectHero project={project} />
  <Zoning />
  <RoleTimeline />
  <TechnicalOfficeSection />
  <ProjectControlsSection />
  <QSSection />
  <AcousticDesignSection />
  <AcousticExecutionSection />
  <ResultsSection />
  <DeliveriesSection />
  <LessonsSection />
  <ContactSection />
</BaseLayout>
```

**نکته:** ۱۵ خط، ۱۵ بخش. **تمیز و خوانا.**

## 🎁 خلاصه

| # | Component | Props |
|---|---|---|
| ۱ | PortfolioIntro | projectName, year |
| ۲ | AboutMini | — |
| ۳ | ServicesMini | — |
| ۴ | ProjectHero | project |
| ۵ | Zoning | — |
| ۶ | RoleTimeline | — |
| ۷ | TechnicalOfficeSection | — |
| ۸ | ProjectControlsSection | — |
| ۹ | QSSection | — |
| ۱۰ | AcousticDesignSection | — |
| ۱۱ | AcousticExecutionSection | — |
| ۱۲ | ResultsSection | — |
| ۱۳ | DeliveriesSection | — |
| ۱۴ | LessonsSection | — |
| ۱۵ | ContactSection | — |

## آماده‌ای؟ برو به `03-reusable-patterns.md`.