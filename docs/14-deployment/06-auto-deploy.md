# Deploy خودکار

## 🎓 مفهوم

**Auto Deploy** = هر بار به GitHub Push می‌کنی، Liara خودش Deploy می‌کند.

## 🎓 چرا Auto Deploy؟

### بدون Auto

```
git push
cd astro-site
liara deploy
```

هر بار دستی.

### با Auto

```
git push
```

خودش Deploy می‌کند.

## 🎓 پیش‌نیاز

- اکانت GitHub
- مخزن `farhadproject-site`
- اپ Liara فعال

## 🛠 گام ۱: اتصال GitHub به Liara

### در پنل Liara

1. برو به [console.liara.ir](https://console.liara.ir).
2. اپ `farhadproject` را باز کن.
3. تب **Source** یا **Deployments**.
4. **Connect to GitHub**.
5. **Authorize** کن.
6. مخزن `baanic/farhadproject-site` را انتخاب کن.
7. **Branch:** `main`.
8. **Root Directory:** `astro-site` (چون مونوریپو است).

## 🛠 گام ۲: تنظیم Build

Liara خودکار Astro را تشخیص می‌دهد. اما اگر لازم بود:

| فیلد | مقدار |
|---|---|
| **Build Command** | `npm run build` |
| **Output Directory** | `dist` |
| **Root Directory** | `astro-site` |
| **Node Version** | `20` |

## 🛠 گام ۳: ذخیره

**Save** را بزن.

از این پس:

```
git push → GitHub → Liara → Deploy
```

## 🎓 چطور تست کنم؟

### ۱. یک تغییر کوچک بده

```bash
cd ~/Documents/Projects/farhadproject
code README.md
# یک خط اضافه کن
git add .
git commit -m "Test auto-deploy"
git push
```

### ۲. در پنل Liara نگاه کن

1. تب **Deployments**.
2. یک Deploy جدید در حال اجرا.
3. وضعیت: `Building` → `Deploying` → `Success`.

**زمان:** ۲–۵ دقیقه.

### ۳. سایت را ببین

Hard Refresh: `Cmd + Shift + R`.

## 🎓 مفهوم: CI/CD

**CI/CD** = Continuous Integration / Continuous Deployment.

- **CI:** کد خودکار تست می‌شود.
- **CD:** کد خودکار Deploy می‌شود.

**ما فقط CD داریم** (بدون تست).

### افزودن تست (آینده)

می‌توانی GitHub Actions اضافه کنی که قبل از Deploy، تست بگیرد.

## 🎓 GitHub Actions (اختیاری)

اگر نخواستی از Liara Auto استفاده کنی:

**`.github/workflows/deploy.yml`:**

```yaml
name: Deploy to Liara

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install Liara CLI
        run: npm install -g @liara/cli

      - name: Deploy
        run: |
          cd astro-site
          liara deploy --api-token=${{ secrets.LIARA_TOKEN }}
```

**نکته:** نیاز به ذخیره Token در GitHub Secrets.

**مزیت:** کنترل بیشتر، تست.

**عیب:** پیچیدگی.

**ما از Liara Auto استفاده می‌کنیم** چون ساده‌تر است.

## 🎓 فلو روزمره جدید

### صبح

```bash
cd ~/Documents/Projects/farhadproject
git pull
```

### در روز

```bash
# ویرایش
git add .
git commit -m "..."
git push
```

### خودکار

Liara خودش Deploy می‌کند.

### نتیجه

سایت پس از ۲–۵ دقیقه آپدیت می‌شود.

## 🎓 Rollback

اگر Deploy خطا داد:

### در پنل Liara

1. تب **Deployments**.
2. Deploy قبلی موفق را انتخاب کن.
3. **Rollback**.

**نتیجه:** سایت به نسخه قبلی برمی‌گردد.

## 🎓 مشاهده لاگ‌ها

### CLI

```bash
liara logs
```

### پنل

اپ → **Logs**.

**کاربرد:** دیدن خطاها.

## 🎓 محدودیت‌ها

| مورد | مقدار |
|---|---|
| Deploy در روز | محدود (پلن رایگان) |
| مدت Build | محدود |
| منابع | محدود |

**برای ما کافی است.**

## 🛑 عیب‌یابی

### مشکل ۱: Auto Deploy اجرا نمی‌شود

**علت‌ها:**
- GitHub متصل نیست.
- Branch اشتباه.
- Root Directory اشتباه.

**راه‌حل:**
- در پنل Liara → Source → بررسی.
- Branch: `main`.
- Root Directory: `astro-site`.

### مشکل ۲: Build خطا می‌دهد

**علت:** خطای محلی.

**راه‌حل:** اول محلی تست کن:

```bash
cd astro-site
npm run build
```

### مشکل ۳: سایت آپدیت نمی‌شود

**علت:** Cache.

**راه‌حل:** Hard Refresh.

### مشکل ۴: Root Directory اشتباه

**علت:** در مونوریپو، Liara نمی‌داند کجا Build کند.

**راه‌حل:** `astro-site` را در پنل تنظیم کن.

## 🎓 بهترین تمرین‌ها

### ۱. Commit‌های منطقی

هر Commit، یک تغییر منطقی.

### ۲. پیام واضح

```
✅ Add new section
✅ Fix typo
✅ Update README
❌ changes
❌ fix
```

### ۳. تست محلی قبل از Push

```bash
npm run build
```

### ۴. Push به main فقط

Auto Deploy فقط روی `main` است. برای Branch‌های دیگر، دستی Deploy.

### ۵. Backup

GitHub همیشه بکاپ است.

## 🎓 در پروژه ما

تنظیمات:

| فیلد | مقدار |
|---|---|
| GitHub Repo | `baanic/farhadproject-site` |
| Branch | `main` |
| Root Directory | `astro-site` |
| Build Command | `npm run build` |
| Output | `dist` |

**نتیجه:** هر `git push`، Deploy خودکار.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | اتصال GitHub در Liara |
| ۲ | تنظیم Build |
| ۳ | تست |

| مفهوم | توضیح |
|---|---|
| Auto Deploy | خودکار از GitHub |
| CI/CD | تست + Deploy |
| Rollback | برگشت |
| Logs | لاگ |