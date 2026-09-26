# الگوهای قابل استفاده مجدد

## 🎓 مفهوم

در ۱۵ Component، بسیاری از ساختارها **تکرار** می‌شوند. به این‌ها **Pattern (الگو)** می‌گوییم.

## 🎓 چرا Pattern؟

- **یکنواختی:** همه بخش‌ها شبیه هم.
- **سرعت:** یک بار می‌سازی، بارها استفاده.
- **کیفیت:** یک الگوی خوب، همه‌جا خوب.

## 🎓 الگو ۱: Section Header (Eyebrow)

**در همه ۱۵ بخش استفاده می‌شود.**

### ساختار

```astro
<div style="display: flex; gap: 16px; margin-bottom: 48px;">
  <div style="width: 8px; height: 48px; background: #B8763E; border-radius: 4px;"></div>
  <div>
    <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px; margin: 0 0 4px;">
      {eyebrow}
    </p>
    <h2 style="color: #1B2A4A; font-size: 32px; margin: 0;">
      {title}
    </h2>
  </div>
</div>
```

### می‌توانی Component بسازی

```astro
---
// components/portfolio/SectionHeader.astro
const { eyebrow, title } = Astro.props;
---

<div style="display: flex; gap: 16px; margin-bottom: 48px;">
  <div style="width: 8px; height: 48px; background: #B8763E; border-radius: 4px;"></div>
  <div>
    <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px; margin: 0 0 4px;">
      {eyebrow}
    </p>
    <h2 style="color: #1B2A4A; font-size: 32px; margin: 0;">
      {title}
    </h2>
  </div>
</div>
```

**استفاده:**

```astro
<SectionHeader eyebrow="ZONING" title="زون‌بندی پروژه" />
```

**نکته:** ما این کار را **نکردیم** و در هر Component تکرار کردیم. می‌توانی در آینده به Component تبدیل کنی.

## 🎓 الگو ۲: Card Grid

**در بخش‌های ۳، ۵، ۹، ۱۳ استفاده می‌شود.**

### ساختار

```astro
<div style="
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
">
  {items.map(item => (
    <div style="
      background: #FFFFFF;
      border-radius: 12px;
      padding: 24px;
    ">
      ...
    </div>
  ))}
</div>
```

### دو نوع Grid

| نوع | کاربرد |
|---|---|
| `repeat(2, 1fr)` | دو ستون ثابت |
| `repeat(auto-fit, minmax(280px, 1fr))` | Responsive |

**در موبایل:**
- `repeat(2, 1fr)` → یک‌ستونه با Media Query.
- `auto-fit` → خودکار یک‌ستونه.

## 🎓 الگو ۳: Stat Card

**در بخش‌های ۴، ۷، ۱۲ استفاده می‌شود.**

### ساختار

```astro
<div style={`
  background: ${color};
  color: #F5F0E6;
  padding: 32px 24px;
  border-radius: 12px;
  text-align: center;
`}>
  <div style="font-size: 40px; font-weight: 700; line-height: 1; margin-bottom: 8px;">
    {value}
  </div>
  <div style="font-size: 13px; opacity: 0.85; margin-bottom: 16px;">
    {unit}
  </div>
  <div style="font-size: 14px; padding-top: 12px; border-top: 1px solid rgba(245, 240, 230, 0.2);">
    {label}
  </div>
</div>
```

**Component آماده:**

```astro
---
// components/portfolio/StatCard.astro
const { value, unit, label, color } = Astro.props;
---

<div style={`background: ${color}; color: #F5F0E6; padding: 32px 24px; border-radius: 12px; text-align: center;`}>
  <!-- محتوا -->
</div>
```

## 🎓 الگو ۴: Section Container

**در همه بخش‌ها.**

```astro
<section style="padding: 80px 24px; background: {BG_COLOR};">
  <div style="max-width: 1100px; margin: 0 auto;">
    <!-- محتوا -->
  </div>
</section>
```

**ارزش‌ها:**

| بخش | مقدار |
|---|---|
| `padding` | `80px 24px` |
| `max-width` | `1100px` |
| `margin` | `0 auto` |

**نکته:** `max-width: 1100px` یعنی «در صفحه‌های بزرگ، محتوا وسط‌چین، حداکثر ۱۱۰۰px.»

## 🎓 الگو ۵: Feature Card

**در بخش ۷، ۸، ۹، ۱۴.**

### ساختار

```astro
<div style="
  background: #FFFFFF;
  border-radius: 12px;
  padding: 28px;
  border-top: 4px solid {color};
">
  <div style="color: {color}; font-size: 36px; font-weight: 700; opacity: 0.4; margin-bottom: 16px;">
    {number}
  </div>
  <h3 style="color: #1B2A4A; font-size: 17px; margin-bottom: 12px;">
    {title}
  </h3>
  <p style="color: #4A5568; font-size: 14px; line-height: 1.8;">
    {description}
  </p>
</div>
```

## 🎓 الگو ۶: Colored Bar (برای بخش‌ها)

**در بخش‌های ۹ (QS)، ۱۳ (Deliveries).**

```astro
<div style="background: #FFFFFF; border-radius: 12px; overflow: hidden;">
  <div style={`background: ${color}; color: #F5F0E6; padding: 24px;`}>
    <h3>{title}</h3>
    <div>{count}</div>
  </div>
  <div style="padding: 20px 24px;">
    <!-- محتوا -->
  </div>
</div>
```

## 🎓 الگو ۷: Percentage Bar

**در بخش ۹ (QS).**

```astro
<div style="background: #F5F0E6; height: 6px; border-radius: 3px; overflow: hidden;">
  <div style={`width: ${percent}%; height: 100%; background: ${color};`}></div>
</div>
<p>{percent}٪</p>
```

## 🎓 الگو ۸: Tag/Chip

**در AboutMini و بخش‌های دیگر.**

```astro
<span style="
  background: #1B2A4A;
  color: #F5F0E6;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 13px;
">
  {text}
</span>
```

## 🎓 الگو ۹: Gradient Section

**در بخش‌های ۱ و ۱۵.**

```astro
<section style="
  background: linear-gradient(135deg, #1B2A4A 0%, #2D5C8A 100%);
  color: #F5F0E6;
  padding: 100px 24px 80px;
  position: relative;
">
  <div style="position: absolute; top: 0; right: 0; left: 0; height: 4px; background: #B8763E;"></div>
  <!-- محتوا -->
</section>
```

## 🎓 الگو ۱۰: Responsive Grid

**الگوی طلایی ما.**

```astro
<div class="responsive-grid">
  {items.map(item => <Card {...item} />)}
</div>

<style>
  .responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
  }

  @media (max-width: 500px) {
    .responsive-grid {
      grid-template-columns: 1fr !important;
    }
  }
</style>
```

**نتیجه:**
- دسکتاپ: ۳–۴ ستون
- تبلت: ۲ ستون
- موبایل: ۱ ستون

## 🎓 الگو ۱۱: Two-Column Layout

**در بخش‌های ۲، ۷، ۱۰، ۱۴.**

```astro
<div style="
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 48px;
  align-items: center;
">
  <div>ستون ۱</div>
  <div>ستون ۲</div>
</div>

<style>
  @media (max-width: 768px) {
    /* تبدیل به یک‌ستونه */
  }
</style>
```

## 🎓 الگو ۱۲: Image Wrapper

**در همه بخش‌های دارای تصویر.**

```astro
<div style="
  border-radius: 16px;
  overflow: hidden;
  background: #F5F0E6;
">
  <img
    src="/images/..."
    alt="..."
    style="
      width: 100%;
      height: auto;
      display: block;
    "
  />
</div>
```

**نکته:** `overflow: hidden` برای اینکه گوشه‌های تصویر با border-radius هماهنگ باشند.

## 🎓 الگو ۱۳: Callout Box

**در بخش ۹ (QSSection).**

```astro
<div style="
  background: #F5F0E6;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 20px;
">
  <div style="color: #B8763E; font-size: 11px; letter-spacing: 2px;">
    LABEL
  </div>
  <div style="color: #1B2A4A; font-size: 14px; font-weight: 500;">
    Value
  </div>
</div>
```

## 🎓 الگو ۱۴: List Item with Dot

**در بخش‌های ۵، ۱۳، ۱۴.**

```astro
<div style="display: flex; gap: 8px; font-size: 13px;">
  <span style="color: #B8763E; font-weight: 700;">▪</span>
  <span>{text}</span>
</div>
```

## 🎓 الگو ۱۵: Stat Row (عمودی)

**در بخش ۷ (TechnicalOfficeSection).**

```astro
<div>
  <div style="color: #1B2A4A; font-size: 32px; font-weight: 700; line-height: 1;">
    {value}
  </div>
  <div style="color: #4A5568; font-size: 13px; margin-top: 4px;">
    {label}
  </div>
</div>
```

## 🎓 در پروژه ما

**پروژه ما ۱۵ Component دارد که این ۱۵ الگو را تکرار می‌کند.**

**آیا می‌شود Componentهای بیشتری ساخت؟**

**بله.** مثلاً:

- `SectionHeader.astro`
- `StatCard.astro`
- `FeatureCard.astro`
- `CardGrid.astro`

**چرا نساختیم؟**

- پروژه کوچک است.
- تکرار محدود است.
- **Over-engineering نکن.**

**قاعده:** اگر یک الگو **بیش از ۳ بار** تکرار شد، Component بساز.

## 🎓 مثال: تبدیل SectionHeader

### قبل

```astro
<!-- در ۱۵ Component -->
<div style="display: flex; gap: 16px; margin-bottom: 48px;">
  <div style="width: 8px; height: 48px; background: #B8763E;"></div>
  <div>
    <p style="color: #B8763E; font-size: 13px; letter-spacing: 3px;">
      ZONING
    </p>
    <h2 style="color: #1B2A4A; font-size: 32px;">
      زون‌بندی پروژه
    </h2>
  </div>
</div>
```

### بعد

```astro
<!-- در هر ۱۵ Component -->
<SectionHeader eyebrow="ZONING" title="زون‌بندی پروژه" />
```

**مزیت:**
- یک بار می‌نویسی.
- اگر بخواهی رنگ نوار را عوض کنی، فقط یک فایل.
- کد تمیزتر.

**عیب:**
- یک سطح پیچیدگی بیشتر.
- اگر تفاوت‌های جزئی وجود داشته باشد، باید Props بدهی.

**در پروژه ما:** تفاوت‌ها زیاد نبود، اما ترجیح دادیم **صریح** باشیم.

## 🎓 چه زمانی Component بساز؟

| تکرار | اقدام |
|---|---|
| ۱ بار | فقط Inline |
| ۲ بار | فکر کن |
| ۳ بار | **Component** ✅ |
| ۵+ بار | **الزامی** |

## 🎁 خلاصه

| الگو | بخش‌ها |
|---|---|
| Section Header | همه |
| Card Grid | ۳، ۵، ۹، ۱۳ |
| Stat Card | ۴، ۷، ۱۲ |
| Section Container | همه |
| Feature Card | ۷، ۸، ۹، ۱۴ |
| Colored Bar | ۹، ۱۳ |
| Percentage Bar | ۹ |
| Tag/Chip | ۲ |
| Gradient Section | ۱، ۱۵ |
| Responsive Grid | همه |
| Two-Column | ۲، ۷، ۱۰، ۱۴ |
| Image Wrapper | همه با تصویر |
| Callout Box | ۹ |
| List with Dot | ۵، ۱۳، ۱۴ |
| Stat Row | ۷ |