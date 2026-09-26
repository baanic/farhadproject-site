# اعداد فارسی با toLocaleString

## 🎓 مفهوم

**`toLocaleString()`** یک متد JavaScript است که اعداد را با **قالب‌بندی محلی** نمایش می‌دهد.

## 🎓 چرا؟

اعداد در زبان‌های مختلف متفاوت نمایش داده می‌شوند:

| عدد | انگلیسی | فارسی |
|---|---|---|
| 1000 | `1,000` | `۱,۰۰۰` |
| 1000000 | `1,000,000` | `۱,۰۰۰,۰۰۰` |
| 3.14 | `3.14` | `۳.۱۴` |

## 🛠 استفاده پایه

### انگلیسی

```javascript
const num = 11000;
console.log(num.toLocaleString("en-US"));
// "11,000"
```

### فارسی

```javascript
const num = 11000;
console.log(num.toLocaleString("fa-IR"));
// "۱۱,۰۰۰"
```

## 🛠 در Astro

```astro
---
const area = 11000;
---

<p>مساحت: {area.toLocaleString("fa-IR")} مترمربع</p>
```

**خروجی:** `مساحت: ۱۱,۰۰۰ مترمربع`

## 🎓 قالب‌های پشتیبانی‌شده

| Locale | خروجی |
|---|---|
| `"fa-IR"` | `۱۱,۰۰۰` |
| `"en-US"` | `11,000` |
| `"de-DE"` | `11.000` |
| `"fr-FR"` | `11 000` |
| `"ar-SA"` | `١١٬٠٠٠` |

**توجه:** `fa-IR` یعنی **f**arsi-**IR**an.

## 🛠 گزینه‌ها

### با تنظیمات

```javascript
const num = 1234.5678;

num.toLocaleString("fa-IR", {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});
// "۱,۲۳۴.۵۷"
```

### به‌عنوان ارز

```javascript
const price = 1337036052238;

price.toLocaleString("fa-IR", {
  style: "currency",
  currency: "IRR",
});
// "۱,۳۳۷,۰۳۶,۰۵۲,۲۳۸ ریال ایران"
```

### به‌عنوان درصد

```javascript
const percent = 0.85;

percent.toLocaleString("fa-IR", {
  style: "percent",
});
// "۸۵٪"
```

## 🎓 در پروژه ما

### در `index.astro`

```astro
---
const project = masterData.projects[0];

const stats = [
  {
    label: "زیربنا",
    value: `${project.area_m2.toLocaleString("fa-IR")} مترمربع`,
  },
  // ...
];
---
```

**نکته:** `area_m2` یک عدد است. `toLocaleString` آن را به فارسی تبدیل می‌کند.

### در `ProjectHero.astro`

```astro
---
const stats = [
  {
    value: project.area_m2.toLocaleString("fa-IR"),  // "۱۱,۰۰۰"
    unit: "مترمربع",
    label: "زیربنا",
  },
  {
    value: "۱۸",       // دستی (کوتاه)
    unit: "ماه",
    label: "مدت اجرا",
  },
];
---
```

**نکته:** بعضی مقادیر را دستی نوشتیم (چون فارسی هستند).

## 🎓 مفهوم: عدد در برابر رشته

```javascript
const a = 11000;              // Number
const b = "11000";            // String
const c = "۱۱,۰۰۰";           // String فارسی
```

**`toLocaleString`** فقط روی **Number** کار می‌کند:

```javascript
11000.toLocaleString("fa-IR");   // ✅ "۱۱,۰۰۰"
"11000".toLocaleString("fa-IR"); // ❌ "11000" (بدون تغییر)
```

**نکته:** اگر مقدار از JSON به‌عنوان String بیاید، اول به Number تبدیل کن:

```javascript
const num = Number("11000");
num.toLocaleString("fa-IR");
```

## 🎓 ارقام فارسی در Font

اگر فونت تو **Shabnam** باشد و اعداد را می‌خواهی **فارسی** ببینی، `toLocaleString("fa-IR")` بهترین راه است.

**راه‌های دیگر:**

| راه | توضیح |
|---|---|
| `toLocaleString("fa-IR")` ✅ | توصیه‌شده |
| فونت مخصوص اعداد | نیاز به فایل جداگانه |
| دستی تبدیل | `"۱۱۰۰۰"` (خطاپذیر) |

## 🛠 تابع کمکی

اگر زیاد استفاده می‌کنی، یک Helper بساز:

```typescript
// src/utils/format.ts

export function toFa(num: number): string {
  if (typeof num !== "number") return "—";
  return num.toLocaleString("fa-IR");
}

export function toFaDecimal(num: number, digits = 2): string {
  return num.toLocaleString("fa-IR", {
    minimumFractionDigits: digits,
    maximumFractionDigits: digits,
  });
}
```

**استفاده:**

```astro
---
import { toFa } from "../utils/format";
---

<p>{toFa(project.area_m2)} مترمربع</p>
<p>{toFaDecimal(project.percentage, 1)}٪</p>
```

## 🎓 در JSON

**توجه:** در `master_data.json`، اعداد را **Number** نگه‌دار، نه String:

```json
{
  "area_m2": 11000,        // ✅ Number
  "area_m2": "11000"       // ❌ String
}
```

**چرا؟**

- Number قابل محاسبه است.
- در Astro، به‌راحتی `toLocaleString` می‌شود.
- کم کردن، جمع کردن، و ... کار می‌کند.

## 🎓 مقایسه با Intl.NumberFormat

**دو راه** برای قالب‌بندی عدد:

### ۱. `toLocaleString()` — ساده

```javascript
num.toLocaleString("fa-IR");
```

### ۲. `Intl.NumberFormat` — قابل استفاده مجدد

```javascript
const formatter = new Intl.NumberFormat("fa-IR");
formatter.format(num);
```

**مزیت:** اگر بخواهی هزار عدد را قالب‌بندی کنی، یک بار `formatter` می‌سازی.

**در Astro:** `toLocaleString` ساده‌تر است.

## 🎓 اعداد انگلیسی در کنار فارسی

گاهی اوقات می‌خواهی عدد **انگلیسی** باشد (مثلاً در URL یا کد):

```astro
<div>
  <span>مساحت: {project.area_m2.toLocaleString("fa-IR")} مترمربع</span>
  <span class="ltr">({project.area_m2} m²)</span>
</div>
```

**خروجی:**

```
مساحت: ۱۱,۰۰۰ مترمربع (11000 m²)
```

## 🛑 عیب‌یابی

### مشکل ۱: اعداد انگلیسی نمایش داده می‌شوند

**علت:** `toLocaleString("fa-IR")` را صدا نزدی.

**راه‌حل:** به هر عدد اضافه کن.

### مشکل ۲: اعداد فارسی در Font مخصوص نمایش داده نمی‌شوند

**علت:** فونت Shabnam معمولی، اعداد را انگلیسی نشان می‌دهد.

**راه‌حل ۱:** از `toLocaleString("fa-IR")` استفاده کن.

**راه‌حل ۲:** فونت Shabnam FD را نصب کن (نسخه‌ای که اعداد را فارسی نشان می‌دهد).

### مشکل ۳: `toLocaleString is not a function`

**علت:** مقدار String است، نه Number.

**راه‌حل:**

```astro
const num = Number(value);
num.toLocaleString("fa-IR");
```

### مشکل ۴: `,` به‌جای `٬` نمایش داده می‌شود

**علت:** مرورگر از `,` انگلیسی استفاده می‌کند.

**راه‌حل:** این رفتار طبیعی است. برای `٬` خاص، از پکیج‌های تخصصی مثل `persian-tools` استفاده کن.

## 🎓 مراجع

- [MDN: toLocaleString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString)
- [MDN: Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| فارسی | `num.toLocaleString("fa-IR")` |
| انگلیسی | `num.toLocaleString("en-US")` |
| با اعشار | `{ minimumFractionDigits: 2 }` |
| ارز | `{ style: "currency", currency: "IRR" }` |
| درصد | `{ style: "percent" }` |
| Helper | تابع `toFa()` |
