# 📚 مستندات پروژه Farhad Project

راهنمای کامل ساخت یک پرتفولیوی حرفه‌ای با Astro.

---

## 👋 خوش آمدید

این مستندات، دفتر خاطرات یادگیری من در ساخت سایت پرتفولیوی شخصی است.

من **مهندس عمران** هستم، نه برنامه‌نویس. اما تصمیم گرفتم سایت خودم را **از صفر** بسازم تا برنامه‌نویسی وب را یاد بگیرم.

این مستندات، **همه چیز** را ثبت کرده:
- هر مفهوم
- هر دستور
- هر کد
- هر خطا و حل آن

---

## 🎯 برای چه کسی؟

### اگر تازه‌کار هستی

مستندات را **به ترتیب شماره** بخوان. هر بخش پیش‌نیاز بخش بعدی است.

### اگر می‌دانی چی می‌خواهی

از فهرست زیر، مستقیم به آن بخش برو.

### اگر در پروژه گیر کرده‌ای

**`15-maintenance/04-troubleshooting.md`** را ببین.

---

## 📚 فهرست کامل

### 🏗️ مبانی

| # | بخش | موضوع |
|---|---|---|
| 00 | [مقدمه](./00-introduction.md) | معرفی و فلسفه |
| 01 | [مبانی ترمینال](./01-terminal-basics/README.md) | cd, ls, mkdir, ... |

### 🔧 ابزارهای توسعه

| # | بخش | موضوع |
|---|---|---|
| 02 | [محیط توسعه](./02-dev-environment/README.md) | Node, npm, nvm, VS Code |
| 03 | [مبانی Git](./03-git-fundamentals/README.md) | Git چیست، سه ناحیه |
| 04 | [کار با GitHub](./04-github-workflow/README.md) | Repo, Push, Pull |
| 05 | [Master Data با Python](./05-python-master-data/README.md) | pandas، اسکریپت |

### 🚀 Astro

| # | بخش | موضوع |
|---|---|---|
| 06 | [مبانی Astro](./06-astro-fundamentals/README.md) | Astro چیست، ساختار |
| 07 | [کامپوننت‌ها](./07-astro-components/README.md) | Component، Props، Slot |
| 08 | [مسیریابی](./08-astro-routing/README.md) | Pages، Dynamic Routes |
| 09 | [اتصال داده](./09-data-binding/README.md) | Import JSON، Map |

### 🎨 طراحی

| # | بخش | موضوع |
|---|---|---|
| 10 | [استایل و طراحی](./10-styling/README.md) | CSS، رنگ، فونت، Responsive |

### ⚙️ امکانات پیشرفته

| # | بخش | موضوع |
|---|---|---|
| 11 | [فرم تماس](./11-contact-form/README.md) | Web3Forms، Fetch |
| 12 | [SEO](./12-seo/README.md) | Meta Tags، Sitemap |
| 13 | [صفحه پرتفولیو](./13-portfolio-page/README.md) | معماری ۱۵ بخش |

### 🚢 استقرار و نگهداری

| # | بخش | موضوع |
|---|---|---|
| 14 | [Deploy](./14-deployment/README.md) | Liara، دامنه، SSL |
| 15 | [نگهداری](./15-maintenance/README.md) | پروژه جدید، عیب‌یابی |
| 16 | [واژه‌نامه](./16-glossary/README.md) | همه اصطلاحات |

---

## 🗂️ ساختار پروژه

```
farhadproject/
├── docs/                        ← 📚 مستندات (همین)
│   ├── 00-introduction.md
│   ├── 01-terminal-basics/
│   ├── 02-dev-environment/
│   ├── 03-git-fundamentals/
│   ├── 04-github-workflow/
│   ├── 05-python-master-data/
│   ├── 06-astro-fundamentals/
│   ├── 07-astro-components/
│   ├── 08-astro-routing/
│   ├── 09-data-binding/
│   ├── 10-styling/
│   ├── 11-contact-form/
│   ├── 12-seo/
│   ├── 13-portfolio-page/
│   ├── 14-deployment/
│   ├── 15-maintenance/
│   └── 16-glossary/
│
├── python-scripts/              ← 🐍 اسکریپت Master Data
│   ├── master_data_builder.py
│   ├── requirements.txt
│   ├── Master_Data.xlsx
│   └── master_data.json
│
├── astro-site/                  ← 🚀 کد Astro
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── data/
│   │   └── styles/
│   ├── public/
│   │   ├── fonts/
│   │   ├── favicon/
│   │   └── images/
│   └── package.json
│
└── data/                        ← 📊 داده‌ها
    └── master_data.json
```

---

## 🛠️ ابزارهای استفاده‌شده

| ابزار | کاربرد | چرا |
|---|---|---|
| **Node.js** | اجرای JavaScript خارج مرورگر | پیش‌نیاز Astro |
| **nvm** | مدیریت نسخه‌های Node | انعطاف |
| **npm** | مدیریت پکیج | استاندارد |
| **Git** | کنترل نسخه | تاریخچه |
| **GitHub** | میزبانی کد | بکاپ، همکاری |
| **VS Code** | ویرایشگر کد | رایگان، قدرتمند |
| **Astro** | فریمورک سایت | سریع، Static |
| **Python** | پردازش داده | Master Data |
| **Liara** | میزبانی | PaaS ایرانی |

---

## 🎨 پالت رنگی پروژه

| نقش | رنگ | HEX |
|---|---|---|
| اصلی | سرمه‌ای | `#1B2A4A` |
| تأکیدی | مسی | `#B8763E` |
| پس‌زمینه | کرم | `#F5F0E6` |
| متن | ذغالی | `#1C1C1C` |
| ثانویه | خاکستری | `#4A5568` |

---

## 📖 چطور از مستندات استفاده کنم؟

### ۱. ترتیب

مستندات از **ساده به پیچیده** ساخته شده:

```
ترمینال → نصب ابزار → Git → GitHub → Python → Astro
   ↓
Components → Routing → Data → Styling
   ↓
Form → SEO → Portfolio → Deploy → Maintenance
```

### ۲. سه لایه هر مستند

هر فایل، سه بخش دارد:

- **🎓 مفهوم** — این چیز چیست؟
- **🛠 اجرا** — چطور انجام دهم؟
- **💡 چرا** — دلیل انتخاب

### ۳. کد واقعی

همه کدها از **پروژه واقعی** ما هستند. هیچ مثال ساختگی نیست.

### ۴. تکرار نکن

هر مفهوم را یک بار توضیح دادم. اگر جای دیگری استفاده شده، **لینک** می‌دهم.

---

## 🚀 شروع سریع

### اگر ۵ دقیقه وقت داری

1. [مقدمه](./00-introduction.md) را بخوان.
2. [ساختار پروژه](./06-astro-fundamentals/04-project-structure.md) را ببین.

### اگر ۱ ساعت وقت داری

1. بخش‌های ۰۰ تا ۰۲ را بخوان.
2. اگر Node نصب نداری، نصب کن.

### اگر ۱ روز وقت داری

بخش‌های ۰۰ تا ۰۶ را بخوان و پروژه را Clone کن.

### اگر ۱ هفته وقت داری

همه مستندات را بخوان و پروژه را از صفر بساز.

---

## 🎯 آنچه یاد می‌گیری

بعد از خواندن کامل مستندات:

- ✅ ترمینال را راحت استفاده می‌کنی
- ✅ Git و GitHub را می‌فهمی
- ✅ Python برای پردازش داده می‌نویسی
- ✅ Astro را از صفر می‌سازی
- ✅ Component و Props را می‌فهمی
- ✅ Routing را پیاده می‌کنی
- ✅ داده را به سایت وصل می‌کنی
- ✅ CSS و Responsive را می‌دانی
- ✅ فرم تماس می‌سازی
- ✅ SEO را پیاده می‌کنی
- ✅ سایت را Deploy می‌کنی
- ✅ سایت را نگهداری می‌کنی

---

## 🌟 نکات مهم

### ۱. خواندن کافی نیست

هر دستور را **اجرا کن**. هر کد را **بنویس**.

### ۲. اشتباه، بخشی از یادگیری است

اگر خطا دیدی، **طبیعی است**. راه‌حل در [15-maintenance/04-troubleshooting.md](./15-maintenance/04-troubleshooting.md).

### ۳. این مستندات، نقطه شروع است

برای حرفه‌ای شدن، بعد از این باید سراغ:
- [MDN Web Docs](https://developer.mozilla.org)
- [Astro Docs](https://docs.astro.build)
- [Git Docs](https://git-scm.com/doc)

---

## 🤝 مشارکت

اگر خطایی دیدی یا می‌خواهی بخشی اضافه کنی:

1. Fork کن.
2. تغییر بده.
3. Pull Request بده.

---

## 📅 نسخه

- **نسخه:** 1.0.0
- **تاریخ:** آذر ۱۴۰۴
- **وضعیت:** کامل
- **زبان:** فارسی

---

## 📞 تماس

- **ایمیل:** farhadrezaei.eng@gmail.com
- **لینکدین:** [linkedin.com/in/farhadproject](https://linkedin.com/in/farhadproject)
- **وب‌سایت:** [farhadproject.ir](https://farhadproject.ir)
- **GitHub:** [@baanic](https://github.com/baanic)

---

## 🙏 تشکر

از همه کسانی که در این مسیر کمکم کردند.

**مخصوصاً خودم که تسلیم نشدم.** 🌟