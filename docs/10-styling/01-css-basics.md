# مبانی CSS

## 🎓 مفهوم

**CSS** مخفف **C**ascading **S**tyle **S**heets.

زبان استایل‌دهی برای HTML. مشخص می‌کند HTML **چطور دیده شود**.

### قیاس

- **HTML** = اسکلت ساختمان.
- **CSS** = رنگ، کاغذ دیواری، دکوراسیون.
- **JavaScript** = برق، آسانسور، حرکت.

## 🎓 ساختار CSS

```css
selector {
  property: value;
  property: value;
}
```

### مثال

```css
h1 {
  color: #1B2A4A;
  font-size: 32px;
}
```

**ترجمه:** «همه `h1`ها رنگ سرمه‌ای و اندازه ۳۲ پیکسل داشته باشند.»

## 🎓 انواع Selector

### ۱. Element

```css
h1 { color: red; }
p { color: blue; }
```

همه تگ‌های مشخص.

### ۲. Class

```css
.card { padding: 20px; }
.button { background: blue; }
```

**در HTML:**

```html
<div class="card">...</div>
<button class="button">...</button>
```

**قاعده:** با `.` شروع می‌شود.

### ۳. ID

```css
#header { background: black; }
```

**در HTML:**

```html
<header id="header">...</header>
```

**نکته:** IDها **یکتا** هستند. در یک صفحه، فقط یک `#header`.

**توصیه:** کمتر از ID استفاده کن. Class بهتر است.

### ۴. Universal

```css
* { box-sizing: border-box; }
```

همه عناصر.

### ۵. ترکیبی

```css
.card p { color: gray; }
```

همه `p`های داخل `.card`.

## 🎓 Propertyهای رایج

### رنگ

```css
color: #1B2A4A;               /* رنگ متن */
background-color: #F5F0E6;    /* رنگ پس‌زمینه */
border-color: #B8763E;        /* رنگ حاشیه */
```

### اندازه

```css
width: 100px;
height: 200px;
max-width: 800px;
min-height: 100vh;
```

### فاصله

```css
/* فاصله داخلی */
padding: 20px;
padding: 10px 20px;           /* بالا/پایین، چپ/راست */
padding: 10px 20px 15px 25px; /* بالا، راست، پایین، چپ */

/* فاصله خارجی */
margin: 20px;
margin: 0 auto;               /* وسط‌چین افقی */
```

### فونت

```css
font-family: 'Shabnam', sans-serif;
font-size: 16px;
font-weight: 700;
line-height: 1.7;
text-align: right;
```

### Layout

```css
display: flex;
display: grid;
display: block;
display: inline-block;
```

### موقعیت

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

## 🎓 Box Model

هر عنصر HTML یک **جعبه** است:

```
┌─────────────────────────────┐
│        Margin               │
│  ┌─────────────────────┐    │
│  │      Border         │    │
│  │  ┌─────────────┐    │    │
│  │  │   Padding   │    │    │
│  │  │  ┌───────┐  │    │    │
│  │  │  │Content│  │    │    │
│  │  │  └───────┘  │    │    │
│  │  └─────────────┘    │    │
│  └─────────────────────┘    │
└─────────────────────────────┘
```

| لایه | توضیح |
|---|---|
| **Content** | محتوا |
| **Padding** | فاصله داخلی |
| **Border** | حاشیه |
| **Margin** | فاصله خارجی |

## 🎓 Box Sizing

### حالت پیش‌فرض

`width: 100px` = فقط محتوا ۱۰۰px. Padding و border روی آن **اضافه** می‌شود.

### حالت `border-box`

`width: 100px` = کل جعبه ۱۰۰px (شامل padding و border).

**تنظیم در Global CSS:**

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

**ما این را در `global.css` داریم.**

## 🎓 Flexbox

**Flexbox** برای چیدمان یک‌بعدی (ردیف یا ستون).

```css
.container {
  display: flex;
  justify-content: space-between;  /* افقی */
  align-items: center;             /* عمودی */
  gap: 16px;
}
```

### مقادیر `justify-content`

| مقدار | کار |
|---|---|
| `flex-start` | چپ (راست در RTL) |
| `flex-end` | راست (چپ در RTL) |
| `center` | وسط |
| `space-between` | فاصله بین |
| `space-around` | فاصله دور |
| `space-evenly` | فاصله مساوی |

### مقادیر `align-items`

| مقدار | کار |
|---|---|
| `flex-start` | بالا |
| `flex-end` | پایین |
| `center` | وسط |
| `stretch` | کشیده |

## 🎓 CSS Grid

**Grid** برای چیدمان دوبعدی (سطر و ستون).

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

**3 ستون مساوی.**

### Grid تطبیقی

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
```

**معنی:** «ستون‌هایی حداقل ۲۸۰px، تا هر تعداد که فضا اجازه دهد.»

**این الگو در سایت ما همه‌جا استفاده می‌شود.**

## 🎓 واحدها

| واحد | توضیح | مثال |
|---|---|---|
| `px` | پیکسل (ثابت) | `16px` |
| `%` | درصد از والد | `50%` |
| `em` | نسبت به اندازه فونت والد | `1.5em` |
| `rem` | نسبت به فونت ریشه | `1.5rem` |
| `vh` | درصد ارتفاع viewport | `100vh` |
| `vw` | درصد عرض viewport | `50vw` |

**توصیه:**
- `px` برای border و font.
- `rem` برای فاصله.
- `%` برای عرض.
- `vh` برای ارتفاع صفحه.

## 🎓 رنگ‌ها

### نام‌ها

```css
color: red;
color: blue;
```

محدود.

### HEX

```css
color: #1B2A4A;
color: #FFFFFF;
```

**رایج‌ترین.**

### RGB / RGBA

```css
color: rgb(27, 42, 74);
color: rgba(27, 42, 74, 0.5);  /* 50% شفاف */
```

### HSL

```css
color: hsl(220, 47%, 20%);
```

**نکته:** در پروژه ما از **HEX** استفاده می‌کنیم.

## 🎓 Cascade و Specificity

**Cascade** یعنی: اگر چند قاعده برای یک عنصر باشد، کدام اعمال شود؟

### ترتیب

```css
p { color: red; }
p { color: blue; }
```

`blue` اعمال می‌شود (آخرین).

### Specificity

```css
p { color: red; }       /* 1 */
.text { color: blue; }  /* 10 */
#header { color: green; } /* 100 */
```

`#header` برنده می‌شود.

## 🎓 `!important`

```css
p { color: red !important; }
```

**معنی:** «این را حتی اگر Specificity کمتر است، اعمال کن.»

**استفاده:**
- در Media Query برای override کردن inline style.
- **با احتیاط.** خیلی استفاده نکن.

## 🎓 در پروژه ما

```css
/* global.css */
* {
  box-sizing: border-box;
}

html {
  font-family: 'Shabnam', Tahoma, sans-serif;
  direction: rtl;
}

body {
  margin: 0;
  line-height: 1.7;
  color: #1C1C1C;
  background: #FFFFFF;
}

h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  margin: 0;
}
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| Selector | `h1`, `.class`, `#id` |
| Color | `#1B2A4A` |
| Padding | `padding: 20px` |
| Margin | `margin: 0 auto` |
| Flexbox | `display: flex` |
| Grid | `display: grid` |
| Box Model | content + padding + border + margin |

## آماده‌ای؟ برو به `02-inline-vs-scoped.md`.