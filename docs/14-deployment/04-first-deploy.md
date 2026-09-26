# اولین Deploy

## 🎓 مفهوم

**اولین Deploy** = کد را برای اولین بار به Liara می‌فرستی.

## 🎓 پیش‌نیاز

| مورد | وضعیت |
|---|---|
| اکانت Liara | ✅ |
| CLI نصب | ✅ |
| `liara login` | ✅ |
| `liara.json` | ✅ |

## 🛠 گام ۱: Build تست

قبل از Deploy، مطمئن شو Build محلی کار می‌کند:

```bash
cd ~/Documents/Projects/farhadproject/astro-site
npm run build
```

**خروجی موفق:**

```
 generating static routes
 ▶ src/pages/index.astro
   └─ /index.html (+17ms)
 ▶ src/pages/about.astro
   └─ /about/index.html (+5ms)
 ...
✓ Completed in 2.45s.
```

**پوشه `dist/` ساخته می‌شود.**

**بررسی:**

```bash
ls dist/
```

باید ببینی:
```
index.html
about/
portfolio/
_astro/
images/
fonts/
...
```

## 🛠 گام ۲: Deploy

```bash
liara deploy
```

### سؤالات Liara

اگر اولین بار است، ممکن است بپرسد:

```
? Choose a platform: static
? App name: farhadproject
? Do you want to create a new app? Yes
```

پاسخ:

| سؤال | پاسخ |
|---|---|
| Platform | `static` |
| App name | `farhadproject` |
| Create new app? | `Yes` |
| Build location | `.` |
| Static location | `dist` |

### فرآیند Deploy

```
✓ Building app...
✓ Uploading files...
✓ Deploying...
✓ App URL: https://farhadproject.liara.run
```

**زمان:** ۲–۵ دقیقه.

## 🛠 گام ۳: تست

آدرس `https://farhadproject.liara.run` را در مرورگر باز کن.

**باید ببینی:** سایت کامل، روی دامنه Liara.

### تست‌ها

- [ ] صفحه اصلی
- [ ] صفحه About
- [ ] صفحه Services
- [ ] صفحه Contact
- [ ] لیست پروژه‌ها
- [ ] صفحه پروژه شاخص
- [ ] فونت Shabnam
- [ ] تصاویر
- [ ] فرم تماس (ارسال تست)
- [ ] Responsive در موبایل

## 🎓 چه اتفاقی افتاد؟

```
[کامپیوتر تو]
    │
    │ ۱. Build محلی
    │ ۲. npm run build
    │ ۳. تولید dist/
    │
    ▼ liara deploy
[Liara]
    │
    │ ۴. آپلود فایل‌ها
    │ ۵. ذخیره روی سرور
    │ ۶. تخصیص URL
    │
    ▼
[farhadproject.liara.run]
    │
    │ ۷. کاربر دسترسی دارد
    ▼
[کاربر]
```

## 🎓 Deploy‌های بعدی

بعد از اولین Deploy، هر بار تغییری دادی:

```bash
git add .
git commit -m "..."
git push

cd astro-site
liara deploy
```

**نکته:** `liara deploy` خودش Build می‌گیرد.

## 🎓 دستورهای مرتبط

### لیست اپ‌ها

```bash
liara app list
```

### لیست Deployها

```bash
liara deploy list
```

### لاگ‌ها

```bash
liara logs
```

### حذف اپ

```bash
liara app delete
```

⚠️ **هشدار:** برگشت‌ناپذیر.

## 🎓 پنل Liara

برو به [console.liara.ir](https://console.liara.ir):

- اپ `farhadproject` را می‌بینی
- وضعیت: Running
- URL: `farhadproject.liara.run`
- لاگ‌ها
- تنظیمات
- دامنه‌ها

## 🎓 Deploy چقدر طول می‌کشد؟

| اندازه سایت | زمان |
|---|---|
| کوچک (< ۱۰۰ فایل) | ۱–۲ دقیقه |
| متوسط (۱۰۰–۵۰۰ فایل) | ۲–۵ دقیقه |
| بزرگ (> ۵۰۰ فایل) | ۵–۱۰ دقیقه |

**سایت ما:** کوچک/متوسط.

## 🎓 فرآیند Build روی Liara

Liara خودش Build می‌گیرد:

```
1. کد را می‌گیرد
2. npm install اجرا می‌کند
3. npm run build اجرا می‌کند
4. dist/ را می‌گیرد
5. dist/ را روی سرور می‌گذارد
```

**مزیت:** نیازی نیست محلی Build کنی.

## 🛑 عیب‌یابی

### مشکل ۱: خطای `app name already exists`

**علت:** نام `farhadproject` قبلاً گرفته شده.

**راه‌حل ۱:** نام دیگری انتخاب کن:

```json
{
  "app": "farhadproject-site"
}
```

**راه‌حل ۲:** از پنل Liara چک کن.

### مشکل ۲: `Build failed`

**علت:** خطای در npm run build.

**راه‌حل:** اول محلی تست کن:

```bash
npm run build
```

اگر محلی کار کرد، روی Liara هم کار می‌کند.

### مشکل ۳: `dist not found`

**علت:** `astro.config.mjs` یا مسیر اشتباه.

**راه‌حل:** مطمئن شو `liara.json` دارد:

```json
{
  "static": { "location": "dist" }
}
```

### مشکل ۴: سایت سفید

**علت‌ها:**
- فایل‌ها آپلود نشده.
- Cache مرورگر.

**راه‌حل:**
- Hard Refresh.
- حالت Incognito.
- لاگ‌های Liara را ببین.

### مشکل ۵: Deploy کند است

**علت‌ها:**
- `node_modules/` هم آپلود می‌شود.
- فایل‌های بزرگ.

**راه‌حل:** در `.gitignore` مطمئن شو:

```
node_modules/
dist/
.astro/
```

**نکته:** Liara خودش `node_modules` را نادیده می‌گیرد.

## 🎓 بررسی نهایی

پس از Deploy، چک کن:

- [ ] سایت بارگذاری می‌شود
- [ ] تمام صفحات کار می‌کنند
- [ ] فونت Shabnam لود شده
- [ ] تصاویر نمایش داده می‌شوند
- [ ] فرم تماس کار می‌کند
- [ ] Responsive در موبایل

## 🎁 خلاصه

| گام | دستور |
|---|---|
| ۱ | `npm run build` (تست محلی) |
| ۲ | `liara deploy` |
| ۳ | تست URL |
| ۴ | بررسی در پنل |

| دستور | کار |
|---|---|
| `liara deploy` | Deploy |
| `liara app list` | لیست اپ‌ها |
| `liara logs` | لاگ‌ها |

## آماده‌ای؟ برو به `05-domain-setup.md`.