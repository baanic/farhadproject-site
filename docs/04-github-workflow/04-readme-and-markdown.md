# README و Markdown

## 🎓 مفهوم

**README** یک فایل استاندارد در هر پروژه GitHub است. **اولین چیزی که بازدیدکننده می‌بیند.**

## 🎓 چرا README مهم است؟

### ۱. اولین برداشت

وقتی کسی وارد مخزن تو می‌شود، **README در صفحه اصلی نمایش داده می‌شود**.

### ۲. توضیح پروژه

README می‌گوید:
- پروژه چیست.
- چطور نصب شود.
- چطور استفاده شود.

### ۳. SEO

Google، محتوای README را ایندکس می‌کند.

### ۴. پرتفولیو

کارفرمای آینده، README را می‌خواند.

## 🎓 مفهوم: Markdown

**Markdown** یک **زبان نشانه‌گذاری سبک** است که با `.md` ذخیره می‌شود.

**چرا؟**
- ساده‌تر از HTML.
- تبدیل به HTML می‌شود.
- در GitHub، StackOverflow، Notion و ... استفاده می‌شود.

## 🎓 ساختار پایه Markdown

### عنوان‌ها

```markdown
# H1 (عنوان اصلی)
## H2 (زیرعنوان)
### H3 (زیرزیرعنوان)
#### H4
##### H5
###### H6
```

**نکته:** فقط **یک H1** در هر سند. مثل کتاب.

### متن

```markdown
**متن بولد**
*متن ایتالیک*
~~متن خط‌خورده~~
`کد درون‌خطی`
```

**خروجی:**

**متن بولد**، *متن ایتالیک*، ~~متن خط‌خورده~~، `کد درون‌خطی`

### لیست‌ها

**لیست نشانه‌دار:**

```markdown
- آیتم ۱
- آیتم ۲
  - زیرآیتم ۲.۱
  - زیرآیتم ۲.۲
- آیتم ۳
```

**لیست شماره‌دار:**

```markdown
1. مرحله اول
2. مرحله دوم
3. مرحله سوم
```

### لینک‌ها

```markdown
[متن لینک](https://example.com)
[لینک داخلی](./other-file.md)
```

### تصاویر

```markdown
![توضیح تصویر](./image.png)
![لوگو](https://example.com/logo.png)
```

### کد بلوکی

```markdown
```javascript
const greeting = "سلام";
console.log(greeting);
```
```

**با تعیین زبان، رنگ‌آمیزی می‌شود.**

### جدول

```markdown
| ستون ۱ | ستون ۲ | ستون ۳ |
|---|---|---|
| مقدار ۱ | مقدار ۲ | مقدار ۳ |
| مقدار ۴ | مقدار ۵ | مقدار ۶ |
```

**خروجی:**

| ستون ۱ | ستون ۲ | ستون ۳ |
|---|---|---|
| مقدار ۱ | مقدار ۲ | مقدار ۳ |
| مقدار ۴ | مقدار ۵ | مقدار ۶ |

### نقل قول

```markdown
> این یک نقل قول است.
> 
> با چند خط.
```

**خروجی:**

> این یک نقل قول است.
> 
> با چند خط.

### خط افقی

```markdown
---
```

**خروجی:**

---

## 🛠 ساختار پیشنهادی README

### برای پروژه‌های عمومی

```markdown
# نام پروژه

> توضیح کوتاه (یک خط).

## درباره پروژه

توضیح کامل‌تر (دو تا سه پاراگراف).

## ویژگی‌ها

- ویژگی ۱
- ویژگی ۲
- ویژگی ۳

## نصب

```bash
git clone https://github.com/user/repo.git
cd repo
npm install
```

## استفاده

```bash
npm run dev
```

## تکنولوژی‌ها

- Astro
- Tailwind CSS
- TypeScript

## لایسنس

MIT
```

### برای پروژه‌های شخصی

```markdown
# پروژه شخصی

## توضیح

...

## وضعیت

🚧 در حال توسعه

## تماس

- Email: ...
- LinkedIn: ...
```

## 🎓 در پروژه ما

فایل `README.md` در ریشه پروژه:

```markdown
# Farhad Project — Portfolio Website

پرتفولیو تخصصی در حوزه‌های دفتر فنی، کنترل پروژه، متره و برآورد و آکوستیک.

## بخش‌های پروژه

- `docs/` — مستندات آموزشی گام‌به‌گام
- `python-scripts/` — اسکریپت‌های Python برای Master Data
- `astro-site/` — کد سایت Astro
- `data/` — داده‌های خام و پردازش‌شده

## ابزارهای استفاده‌شده

- Astro (Static Site Generator)
- Tailwind CSS (Styling)
- Python (Master Data Builder)
- Liara (Hosting)

## وضعیت پروژه

🚧 در حال ساخت...
```

## 🎓 ترفند: Badge

می‌توانی **Badge** اضافه کنی. Badge آیکون‌های کوچکی هستند که اطلاعات سریع نشان می‌دهند:

```markdown
![Astro](https://img.shields.io/badge/Astro-5.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
```

**خروجی:**

![Astro](https://img.shields.io/badge/Astro-5.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**سرویس‌ها:**
- [shields.io](https://shields.io) — Badgeهای آماده
- [badgen.net](https://badgen.net) — مشابه

## 🎓 ترفند: Table of Contents

برای READMEهای بلند، فهرست مطالب اضافه کن:

```markdown
## فهرست

- [نصب](#نصب)
- [استفاده](#استفاده)
- [تکنولوژی‌ها](#تکنولوژیها)
- [لایسنس](#لایسنس)

## نصب
...

## استفاده
...
```

GitHub خودش لینک‌های `#عنوان` را می‌فهمد.

## 🎓 ترفند: Collapsible Sections

برای محتوای طولانی:

```markdown
<details>
<summary>کلیک کن تا ببینی</summary>

محتوای مخفی اینجا.

</details>
```

**خروجی:**

<details>
<summary>کلیک کن تا ببینی</summary>

محتوای مخفی اینجا.

</details>

## 🎓 ترفند: Checkbox

```markdown
- [x] کار انجام‌شده
- [ ] کار در انتظار
- [ ] کار دیگر
```

**خروجی:**

- [x] کار انجام‌شده
- [ ] کار در انتظار
- [ ] کار دیگر

## 🎓 ترفند: Emoji

GitHub از Emoji پشتیبانی می‌کند:

```markdown
:rocket: شروع
:bug: باگ
:books: مستندات
```

**خروجی:** 🚀، 🐛، 📚

**فهرست کامل:** [emoji-cheat-sheet.com](https://www.webfx.com/tools/emoji-cheat-sheet/)

## 🎓 در VS Code

### پیش‌نمایش

1. یک فایل `.md` باز کن.
2. `Cmd + K` و بعد `V` (یا `Cmd + Shift + V`).
3. پیش‌نمایش باز می‌شود.

### Extensions

**Markdown All in One:**
- Format خودکار.
- فهرست مطالب.
- Table of Contents.

**Markdown Preview GitHub Styling:**
- پیش‌نمایش شبیه GitHub.

## 🎁 خلاصه

| عنصر | Markdown |
|---|---|
| H1-H6 | `# H1` تا `###### H6` |
| بولد | `**متن**` |
| ایتالیک | `*متن*` |
| لیست | `- آیتم` |
| شماره | `1. آیتم` |
| لینک | `[متن](url)` |
| تصویر | `![alt](url)` |
| کد | `` `کد` `` |
| کد بلوکی | ` ```lang ... ``` ` |
| جدول | `| ستون | ستون |` |
| نقل قول | `> متن` |

## آماده‌ای؟ برو به `05-gitignore.md`.