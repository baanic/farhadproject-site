# npm چیست؟

## 🎓 مفهوم

**npm** مخفف **Node Package Manager** است — ابزار مدیریت پکیج‌های Node.js.

### کار npm چیست؟

| کار | مثال |
|---|---|
| نصب پکیج | `npm install astro` |
| حذف پکیج | `npm uninstall lodash` |
| بروزرسانی پکیج | `npm update` |
| اجرای اسکریپت | `npm run dev` |
| انتشار پکیج خودت | `npm publish` |

## 🎓 مفهوم: Package چیست؟

**Package (پکیج)** یک **بسته کد آماده** است که دیگران نوشته‌اند و ما استفاده می‌کنیم.

### مثال

فرض کن می‌خواهی تاریخ را به فارسی نمایش دهی. نیازی نیست خودت کد بنویسی. یک پکیج هست به نام `jalaali-js` که این کار را می‌کند:

```bash
npm install jalaali-js
```

حالا در کد:
```javascript
import jalaali from 'jalaali-js';
console.log(jalaali.toJalaali(2024, 9, 15));
```

## 🎓 مفهوم: Registry

**npm Registry** یک مخزن آنلاین است که همه پکیج‌های npm را نگه می‌دارد.

- آدرس: [npmjs.com](https://www.npmjs.com)
- تعداد پکیج: **بیش از ۳ میلیون**
- دانلود روزانه: **بیش از ۵۰ میلیارد**

هر پکیج، **نسخه‌بندی معنایی** دارد: `1.2.3`

| بخش | معنی | افزایش می‌یابد وقتی... |
|---|---|---|
| `1` (Major) | تغییرات ناسازگار | API کاملاً عوض شود |
| `2` (Minor) | ویژگی جدید | قابلیت جدید اضافه شود |
| `3` (Patch) | رفع باگ | باگ برطرف شود |

## 🎓 مفهوم: `package.json`

وقتی پروژه‌ای با npm می‌سازی، یک فایل `package.json` ساخته می‌شود. این **شناسنامه پروژه** است:

```json
{
  "name": "farhadproject",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build"
  },
  "dependencies": {
    "astro": "^5.0.0"
  }
}
```

| بخش | معنی |
|---|---|
| `name` | نام پروژه |
| `version` | نسخه |
| `scripts` | دستورات میانبر |
| `dependencies` | پکیج‌های موردنیاز |

## 🎓 مفهوم: `node_modules`

وقتی `npm install` می‌زنی، npm پکیج‌ها را از Registry دانلود و در پوشه `node_modules` ذخیره می‌کند.

**نکته مهم:** این پوشه **هرگز به GitHub نمی‌رود**. چرا؟

- حجمش زیاد است (ممکن است ۲۰۰–۵۰۰ مگابایت باشد).
- `package.json` و `package-lock.json` لیست پکیج‌ها را دارند.
- هر کس پروژه را Clone کند، با `npm install` همه چیز را می‌گیرد.

**به همین دلیل، در `.gitignore` خط `node_modules/` را گذاشتیم.**

## 🛠 دستورهای مهم npm

### نصب پکیج (به‌عنوان dependency)

```bash
npm install astro
```

پکیج در `package.json` (بخش dependencies) ثبت می‌شود.

### نصب پکیج فقط برای توسعه (devDependency)

```bash
npm install --save-dev typescript
```

پکیج‌هایی که فقط در زمان توسعه لازم هستند.

### نصب همه پکیج‌های `package.json`

```bash
npm install
```

اگر پروژه‌ای را Clone کردی و `node_modules` نداشت، این دستور همه را نصب می‌کند.

### حذف پکیج

```bash
npm uninstall astro
```

### بروزرسانی

```bash
npm update
```

### اجرای اسکریپت

اگر در `package.json` نوشتی:

```json
"scripts": {
  "dev": "astro dev"
}
```

با این دستور اجرا می‌کنی:

```bash
npm run dev
```

## 🛠 مقایسه npm با گزینه‌های دیگر

| ابزار | مزیت | عیب |
|---|---|---|
| **npm** | پیش‌فرض Node، ساده | کمی کندتر |
| **yarn** | سریع‌تر، Lockfile قوی‌تر | پیچیده‌تر |
| **pnpm** | فوق‌العاده سریع، صرفه‌جویی دیسک | نیاز به نصب جداگانه |
| **bun** | بسیار سریع | خیلی جدید، ممکن است باگ داشته باشد |

**ما npm استفاده می‌کنیم** چون:
- پیش‌فرض Node است.
- ساده‌ترین است.
- برای پروژه ما کافی است.

## 🎓 npm در پروژه ما

در این پروژه، دستورهای npm که استفاده کردیم:

| دستور | کاربرد |
|---|---|
| `npm create astro@latest .` | ساخت پروژه Astro |
| `npm install` | نصب پکیج‌ها |
| `npm run dev` | اجرای سرور توسعه |
| `npm run build` | ساخت خروجی نهایی |
| `npm run preview` | پیش‌نمایش خروجی build |

## 💡 چرا npm برای ما حیاتی است؟

بدون npm:

- نمی‌توانستی Astro را نصب کنی.
- نمی‌توانستی پکیج‌های جانبی (Sitemap، Tailwind و ...) اضافه کنی.
- نمی‌توانستی پروژه را Build کنی.

**پس npm، ستون فقرات توسعه Node.js است.**

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| npm | مدیر پکیج Node.js |
| Registry | مخزن آنلاین پکیج‌ها |
| Package | بسته کد آماده |
| `package.json` | شناسنامه پروژه |
| `node_modules` | پوشه پکیج‌ها (به Git نمی‌رود) |

## آماده‌ای؟ برو به `03-install-nvm.md`.
