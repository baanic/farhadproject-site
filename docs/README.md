

## 📚 ساختار کامل مستندات

```
docs/
├── README.md                          ← فهرست کل
│
├── 00-introduction.md                 ← خوش‌آمدگویی و فلسفه
│
├── 01-terminal-basics/                ← مبانی ترمینال
│   ├── README.md
│   ├── 01-what-is-terminal.md
│   ├── 02-navigation.md               ← cd, ls, pwd
│   ├── 03-file-operations.md          ← mkdir, cp, rm
│   └── 04-command-cheatsheet.md       ← مرجع کامل
│
├── 02-dev-environment/                ← محیط توسعه
│   ├── README.md
│   ├── 01-what-is-nodejs.md
│   ├── 02-what-is-npm.md
│   ├── 03-install-nvm.md
│   ├── 04-install-node.md
│   ├── 05-install-vscode.md
│   └── 06-why-not-homebrew.md         ← چرا Homebrew را نصب نکردیم
│
├── 03-git-fundamentals/               ← مبانی Git
│   ├── README.md
│   ├── 01-what-is-git.md
│   ├── 02-git-vs-github.md
│   ├── 03-git-config.md               ← تنظیم نام و ایمیل
│   ├── 04-three-areas.md              ← Working / Staging / Repository
│   ├── 05-commit-workflow.md
│   ├── 06-branch-and-merge.md
│   └── 07-personal-access-token.md
│
├── 04-github-workflow/                ← کار با GitHub
│   ├── README.md
│   ├── 01-create-repo.md
│   ├── 02-connect-local-remote.md
│   ├── 03-first-push.md
│   ├── 04-readme-and-markdown.md
│   ├── 05-gitignore.md
│   └── 06-daily-workflow.md
│
├── 05-python-master-data/             ← Master Data با Python
│   ├── README.md
│   ├── 01-why-python.md
│   ├── 02-install-pandas.md
│   ├── 03-first-script.md
│   ├── 04-data-structure.md
│   └── 05-build-master-data.md
│
├── 06-astro-fundamentals/             ← مبانی Astro
│   ├── README.md
│   ├── 01-what-is-astro.md
│   ├── 02-static-vs-ssr.md
│   ├── 03-install-astro.md
│   ├── 04-project-structure.md
│   ├── 05-astro-file-format.md        ← --- و HTML و <style>
│   ├── 06-first-page.md
│   └── 07-dev-server.md               ← npm run dev و Hot Reload
│
├── 07-astro-components/               ← کامپوننت‌ها
│   ├── README.md
│   ├── 01-what-is-component.md
│   ├── 02-props.md
│   ├── 03-destructuring.md
│   ├── 04-compose-components.md
│   ├── 05-layouts.md
│   └── 06-slots.md
│
├── 08-astro-routing/                  ← مسیریابی
│   ├── README.md
│   ├── 01-file-based-routing.md
│   ├── 02-dynamic-routes.md           ← [slug].astro
│   ├── 03-get-static-paths.md
│   └── 04-nested-routes.md
│
├── 09-data-binding/                   ← اتصال داده
│   ├── README.md
│   ├── 01-import-json.md
│   ├── 02-map-iteration.md
│   ├── 03-conditional-rendering.md
│   └── 04-to-locale-string.md         ← اعداد فارسی
│
├── 10-styling/                        ← طراحی و استایل
│   ├── README.md
│   ├── 01-css-basics.md
│   ├── 02-inline-vs-scoped.md
│   ├── 03-color-system.md
│   ├── 04-font-shabnam.md
│   ├── 05-responsive-design.md
│   └── 06-media-queries.md
│
├── 11-contact-form/                   ← فرم تماس
│   ├── README.md
│   ├── 01-why-backend-needed.md
│   ├── 02-web3forms-intro.md
│   ├── 03-get-access-key.md
│   ├── 04-form-submission.md
│   └── 05-async-await-fetch.md
│
├── 12-seo/                            ← SEO
│   ├── README.md
│   ├── 01-meta-tags.md
│   ├── 02-open-graph.md
│   ├── 03-favicon.md
│   ├── 04-sitemap.md
│   └── 05-robots-txt.md
│
├── 13-portfolio-page/                 ← صفحه پرتفولیو
│   ├── README.md
│   ├── 01-narrative-structure.md
│   ├── 02-section-components.md
│   └── 03-reusable-patterns.md
│
├── 14-deployment/                     ← استقرار
│   ├── README.md
│   ├── 01-what-is-deploy.md
│   ├── 02-what-is-liara.md
│   ├── 03-install-liara-cli.md
│   ├── 04-first-deploy.md
│   ├── 05-domain-setup.md
│   └── 06-auto-deploy.md
│
├── 15-maintenance/                    ← نگهداری
│   ├── README.md
│   ├── 01-add-new-project.md
│   ├── 02-add-new-section.md
│   ├── 03-update-content.md
│   └── 04-troubleshooting.md
│
└── 16-glossary/                       ← واژه‌نامه
    └── README.md
```

**جمع:** حدود ۷۰ فایل مستند آموزشی. یک کتاب کامل برنامه‌نویسی وب.

---

## 🎯 چطور این مستندات را بنویسیم؟

هر فایل، سه بخش دارد:

| بخش | توضیح |
|---|---|
| **مفهوم (Concept)** | این چیز چیست و چرا وجود دارد |
| **دستور/کد (How-to)** | دقیقاً چه بنویس، با مثال از پروژه ما |
| **چرا (Why)** | چرا این تصمیم را گرفتیم |

**مثال از ساختار درونی یک فایل:**

```markdown
# Git Commit چیست؟

## مفهوم
Commit یعنی...

## نحوه استفاده
دستور:
git commit -m "پیام"

## مثال از پروژه ما
در پروژه ما، اولین Commit این بود:
git commit -m "Initial commit: project structure and README"

## چرا "Initial commit"؟
چون...
```

---

## 🚦 پیشنهاد من برای امشب

تو گفتی خسته‌ای. پس بگذار **فقط فونداسیون را امشب بگذارم** و بقیه را در پیام‌های بعدی:

### امشب (همین پیام):
1. **`docs/README.md`** — فهرست کل + راهنمای استفاده
2. **`docs/00-introduction.md`** — خوش‌آمدگویی و فلسفه پروژه

### پیام بعدی:
3. **`docs/01-terminal-basics/`** — کل پوشه (۴ فایل)

### پیام سوم:
4. **`docs/02-dev-environment/`** — کل پوشه (۶ فایل)

### الی آخر...

این روش، **خوانا و قابل هضم** است. اگر همه را در یک پیام بدهم، ۳۰ هزار کلمه می‌شود و غیرقابل مطالعه.

---

## 🎁 حالا شروع کنیم: `docs/README.md`

# 📚 مستندات پروژه Farhad Project

خوش آمدید به مستندات آموزشی پروژه پرتفولیوی شخصی.

## این مستندات برای چه کسی است؟

برای **فرهاد رضائی** — که در طول ساخت این سایت، تصمیم گرفت برنامه‌نویسی وب را از صفر یاد بگیرد.

## فلسفه این مستندات

این مستندات، سه لایه دارند:

1. **لایه Concept (مفهوم):** توضیح «این چیز چیست و چرا وجود دارد».
2. **لایه How-to (اجرا):** دستور یا کد دقیق، با مثال از پروژه واقعی.
3. **لایه Why (چرا):** دلیل انتخاب این روش، در مقابل گزینه‌های دیگر.

هدف این نیست که فقط «سایت ساخته شود». هدف این است که **بعد از خواندن این مستندات، بتوانی خودت سایت را توسعه دهی**.

## چطور از این مستندات استفاده کنم؟

### اگر تازه شروع کرده‌ای:
مستندات را به ترتیب شماره (01، 02، 03...) بخوان. هر بخش پیش‌نیاز بخش بعدی است.

### اگر می‌خواهی چیزی را سریع پیدا کنی:
از فهرست زیر استفاده کن. هر فایل، مستقل است.

### اگر در پروژه گیر کرده‌ای:
سراغ `15-maintenance/04-troubleshooting.md` برو.

## فهرست

### مبانی (Foundations)
- [00 - مقدمه](./00-introduction.md)
- [01 - مبانی ترمینال](./01-terminal-basics/README.md)

### ابزارهای توسعه (Development Tools)
- [02 - محیط توسعه](./02-dev-environment/README.md)
- [03 - Git](./03-git-fundamentals/README.md)
- [04 - GitHub](./04-github-workflow/README.md)
- [05 - Python و Master Data](./05-python-master-data/README.md)

### Astro
- [06 - مبانی Astro](./06-astro-fundamentals/README.md)
- [07 - کامپوننت‌ها](./07-astro-components/README.md)
- [08 - مسیریابی](./08-astro-routing/README.md)
- [09 - اتصال داده](./09-data-binding/README.md)

### طراحی
- [10 - استایل و طراحی](./10-styling/README.md)

### امکانات پیشرفته
- [11 - فرم تماس](./11-contact-form/README.md)
- [12 - SEO](./12-seo/README.md)
- [13 - صفحه پرتفولیو](./13-portfolio-page/README.md)

### استقرار و نگهداری
- [14 - Deploy](./14-deployment/README.md)
- [15 - نگهداری](./15-maintenance/README.md)
- [16 - واژه‌نامه](./16-glossary/README.md)

## ساختار پروژه

```
farhadproject/
├── docs/                    ← 📚 همین مستندات
├── python-scripts/          ← 🐍 اسکریپت Master Data
├── astro-site/              ← 🚀 سایت Astro
└── data/                    ← 📊 داده‌های خام
```

## پیش‌نیازها

برای شروع، نیاز داری به:
- macOS یا Windows
- VS Code (ویرایشگر کد)
- اتصال اینترنت
- صبر و علاقه به یادگیری

## نسخه و وضعیت

- **نسخه:** 1.0.0
- **آخرین بروزرسانی:** آذر ۱۴۰۴
- **وضعیت:** در حال تکمیل

## لایسنس

این مستندات، بخشی از پروژه شخصی فرهاد رضائی است.


---

## 🎁 و `docs/00-introduction.md`


# 🚀 مقدمه

## این پروژه چیست؟

این پروژه، یک **پرتفولیوی شخصی آنلاین** است که برای نمایش تخصص من در حوزه‌های زیر طراحی و ساخته شد:

- دفتر فنی و مستندسازی
- کنترل پروژه و زمان‌بندی
- متره، برآورد و صورت‌وضعیت
- طراحی و اجرای آکوستیک

## چرا این مستندات را نوشتم؟

من مهندس عمران هستم، نه برنامه‌نویس. اما تصمیم گرفتم این پروژه را **خودم بسازم** تا در حین ساخت، برنامه‌نویسی وب را یاد بگیرم.

این مستندات، **دفتر خاطرات یادگیری من** است. هر مفهوم، هر دستور، و هر کدی که در این مسیر یاد گرفتم، اینجا ثبت شده.

## چه چیزی یاد خواهی گرفت؟

### سطح ۱: مبانی (Foundations)
- کار با ترمینال
- نصب ابزارها با nvm
- مفاهیم Git

### سطح ۲: Astro (Framework)
- سایت استاتیک چطور کار می‌کند
- کامپوننت چیست
- مسیریابی چطور کار می‌کند

### سطح ۳: طراحی (Design)
- CSS و RTL
- فونت‌های فارسی
- Responsive Design

### سطح ۴: امکانات پیشرفته
- اتصال فرم به سرویس خارجی
- SEO و Open Graph

### سطح ۵: انتشار (Deploy)
- سایت را روی اینترنت ببر

## ساختار درسی

هر مستند، سه لایه دارد:

### 🎓 مفهوم (Concept)
توضیح ساده و شهودی. بدون اصطلاحات پیچیده.

### 🛠 اجرا (How-to)
دستور یا کد دقیق. با مثال واقعی از پروژه.

### 💡 چرا (Why)
دلیل انتخاب این روش. مقایسه با گزینه‌های دیگر.

## یک تذکر مهم

**این مستندات، قرار نیست همه چیز را در مورد برنامه‌نویسی وب یاد بدهد.** فقط چیزهایی که برای این پروژه لازم بود.

اگر می‌خواهی برنامه‌نویس حرفه‌ای وب شوی، این مستندات نقطه شروع خوبی است، اما کافی نیست. بعد از این، باید سراغ منابع دیگر بروی (MDN Web Docs، ویدیوهای آموزشی، کتاب‌های تخصصی).

## چطور شروع کنم؟

1. اگر تازه‌کار هستی: از `01-terminal-basics/` شروع کن.
2. اگر ترمینال می‌دانی: از `02-dev-environment/` شروع کن.
3. اگر Git می‌دانی: از `06-astro-fundamentals/` شروع کن.

## ساختار پروژه

```
farhadproject/
├── docs/                    ← 📚 مستندات
├── python-scripts/          ← 🐍 Master Data Builder
├── astro-site/              ← 🚀 سایت (کد اصلی)
└── data/                    ← 📊 داده‌های JSON
```

## ابزارهایی که استفاده کردیم

| ابزار | کاربرد | چرا |
|---|---|---|
| **Node.js** | اجرای JavaScript در سرور | پیش‌نیاز Astro |
| **nvm** | مدیریت نسخه‌های Node | انعطاف در پروژه‌های مختلف |
| **Git** | کنترل نسخه | تاریخچه تغییرات |
| **GitHub** | میزبانی آنلاین کد | بکاپ و اشتراک‌گذاری |
| **VS Code** | ویرایشگر کد | رایگان، محبوب، قوی |
| **Astro** | فریمورک سایت | سریع، استاتیک، SEO-friendly |
| **Python** | ساخت Master Data | قدرتمند برای پردازش داده |
| **Liara** | میزبانی سایت | CDN ایرانی، Deploy ساده |

## قواعد مستندات

### ۱. همه چیز شفاف
هیچ دستور یا کدی بدون توضیح نیست. اگر جایی مفهوم پیچیده است، با مثال توضیح داده شده.

### ۲. همه چیز واقعی
هر دستور، در پروژه واقعی ما اجرا شده. هیچ دستور فرضی نیست.

### ۳. همه چیز قابل بازتولید
اگر همین مستندات را دنبال کنی، می‌توانی از صفر، همین سایت را بسازی.

## منابع مکمل

در پایان هر مستند، منابعی برای مطالعه بیشتر پیشنهاد می‌شود.

## به‌روزرسانی مستندات

اگر پروژه توسعه پیدا کرد، مستندات هم به‌روز می‌شوند. نسخه‌بندی در GitHub انجام می‌شود.

---

آماده‌ای شروع کنیم؟ برو به `01-terminal-basics/`.


---

## 🎯 گام بعدی

امشب فقط همین دو فایل را در `docs/` پیست کن:

```bash
cd ~/Documents/Projects/farhadproject
code docs/README.md
```

و

```bash
code docs/00-introduction.md
```

محتوای بالا را در هر کدام پیست کن و ذخیره کن.

سپس Commit:

```bash
git add .
git commit -m "Add documentation index and introduction"
git push
```
