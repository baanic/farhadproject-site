# نصب Liara CLI

## 🎓 مفهوم

**Liara CLI** ابزار خط فرمان برای Deploy.

## 🛠 گام ۱: ساخت اکانت

1. برو به [liara.ir](https://liara.ir).
2. **ثبت‌نام**.
3. ایمیل: `farhadrezaei.eng@gmail.com`.
4. رمز عبور قوی.
5. کد تأیید به ایمیل می‌آید.
6. تأیید کن.
7. شماره موبایل را وارد کن.
8. کد پیامکی را تأیید کن.

## 🛠 گام ۲: نصب CLI

### با npm

```bash
npm install -g @liara/cli
```

**توضیح:**
- `-g`: Global
- `@liara/cli`: پکیج

### بررسی

```bash
liara --version
```

**خروجی:** `7.x.x`.

## 🛠 گام ۳: ورود

```bash
liara login
```

**چه اتفاقی می‌افتد؟**

1. یک URL در ترمینال ظاهر می‌شود.
2. مرورگر باز می‌شود.
3. **Authorize** را کلیک کن.
4. ترمینال می‌گوید: `✓ You are logged in`.

**اگر مرورگر باز نشد:** URL را دستی کپی و باز کن.

## 🛠 گام ۴: بررسی ورود

```bash
liara whoami
```

**خروجی:** ایمیل تو.

```
farhadrezaei.eng@gmail.com
```

## 🎓 دستورهای مهم Liara CLI

| دستور | کار |
|---|---|
| `liara login` | ورود |
| `liara logout` | خروج |
| `liara whoami` | کاربر فعلی |
| `liara deploy` | Deploy |
| `liara app list` | لیست اپ‌ها |
| `liara app create` | ساخت اپ |
| `liara app delete` | حذف اپ |
| `liara env list` | متغیرهای محیطی |
| `liara logs` | لاگ‌ها |
| `liara domain add` | اتصال دامنه |

## 🎓 فایل `liara.json`

قبل از اولین Deploy، فایل `liara.json` را در `astro-site/` بساز:

```bash
cd ~/Documents/Projects/farhadproject/astro-site
code liara.json
```

**محتوا:**

```json
{
  "platform": "static",
  "app": "farhadproject",
  "build": {
    "location": ".",
    "scripts": []
  },
  "static": {
    "location": "dist"
  }
}
```

### توضیح

| کلید | معنی |
|---|---|
| `platform: "static"` | نوع اپ |
| `app: "farhadproject"` | نام اپ (یکتا) |
| `build.location: "."` | پوشه پروژه |
| `static.location: "dist"` | خروجی Astro |

**نکته:** `app` در همه Liara یکتا است. اگر قبلاً گرفته شده، نام دیگری بگذار.

## 🎓 در VS Code

Extension Liara برای VS Code وجود دارد (اختیاری). اما ما از CLI استفاده می‌کنیم.

## 🛑 عیب‌یابی

### مشکل ۱: `command not found: liara`

**راه‌حل:** نصب را چک کن:

```bash
npm install -g @liara/cli
```

**یا:** با `sudo`:

```bash
sudo npm install -g @liara/cli
```

### مشکل ۲: خطای login

**علت:** Cache یا مرورگر.

**راه‌حل:**

```bash
liara logout
liara login
```

### مشکل ۳: `Unauthorized`

**علت:** Session منقضی.

**راه‌حل:** دوباره login کن.

### مشکل ۴: ورژن CLI قدیمی

**راه‌حل:** آپدیت:

```bash
npm update -g @liara/cli
```

## 🎓 در پروژه ما

نصب کردیم:

```bash
npm install -g @liara/cli
```

ورود:

```bash
liara login
```

---

## 🎯 حالا فایل `liara.json` را بساز

```bash
cd ~/Documents/Projects/farhadproject/astro-site
code liara.json
```

محتوا را پیست کن.

**نکته:** در `.gitignore` باید `liara.json` باشد یا نه؟

**نه** — `liara.json` اطلاعات حساس ندارد. می‌توانی در Git نگه‌داری.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | ساخت اکانت |
| ۲ | `npm install -g @liara/cli` |
| ۳ | `liara login` |
| ۴ | ساخت `liara.json` |

| دستور | کار |
|---|---|
| `liara --version` | نسخه |
| `liara login` | ورود |
| `liara whoami` | کاربر |

## آماده‌ای؟ برو به `04-first-deploy.md`.