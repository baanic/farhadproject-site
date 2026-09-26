# گرفتن Access Key

## 🎓 چرا Access Key؟

Web3Forms باید بداند ایمیل تو **کدام** است تا پیام‌ها را به آن بفرستد. Access Key این اطلاعات را نگه می‌دارد.

## 🛠 گام ۱: رفتن به سایت

آدرس: [web3forms.com](https://web3forms.com)

## 🛠 گام ۲: کلیک روی Create Access Key

در صفحه اصلی، دکمه **Create Access Key** را می‌بینی.

## 🛠 گام ۳: وارد کردن ایمیل

ایمیل خودت را وارد کن:

```
farhadrezaei.eng@gmail.com
```

**نکته:** این ایمیل، **مقصد پیام‌ها** است.

## 🛠 گام ۴: تأیید ایمیل

پس از ثبت، به ایمیلت می‌رود. لینک تأیید را کلیک کن.

**نکته:** ایمیل ممکن است در **Spam** باشد. پوشه Spam را بررسی کن.

## 🛠 گام ۵: دریافت Access Key

یک رشته طولانی به تو می‌دهد:

```
a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**این کلید را کپی کن.**

## 🎓 چطور Access Key را ذخیره کنم؟

### گزینه ۱: در پروژه

```astro
---
// contact.astro
---

<form>
  <input type="hidden" name="access_key" value="a1b2c3d4-..." />
</form>
```

### گزینه ۲: در فایل Environment

اگر نمی‌خواهی در کد باشد:

**.env**

```
PUBLIC_WEB3FORMS_KEY=a1b2c3d4-...
```

**در Astro:**

```astro
---
const web3formsKey = import.meta.env.PUBLIC_WEB3FORMS_KEY;
---

<input type="hidden" name="access_key" value={web3formsKey} />
```

**نکته:** `PUBLIC_` یعنی «این متغیر در مرورگر قابل دسترسی است.»

## 🎓 Access Key در پروژه ما

ما آن را **مستقیم در کد** گذاشتیم:

```astro
<input
  type="hidden"
  name="access_key"
  value="a1b2c3d4-..."
/>
```

**چرا؟**

- **محرمانه نیست.**
- هر کسی می‌بیند، فقط می‌تواند به **ایمیل ما** پیام بفرستد.
- استفاده از Env برای این کار، پیچیدگی بی‌دلیل.

## 🎓 اگر Access Key لو رفت

- **کسی نمی‌تواند به ایمیل تو دسترسی پیدا کند.**
- فقط می‌تواند پیام بفرستد.
- اگر آزاردهنده شد:
  1. در پنل Web3Forms، Key قدیمی را حذف کن.
  2. Key جدید بساز.
  3. در کد عوض کن.

## 🎓 تنظیمات اضافی در پنل

### ۱. Domain Restriction

اگر فقط روی دامنه `farhadproject.ir` کار کند:

```
Allowed Domains:
  farhadproject.ir
  www.farhadproject.ir
  localhost
```

**توجه:** در حالت `localhost` هم باید مجاز باشد.

### ۲. Auto-Response

به کاربر ایمیل خودکار بفرست:

```
Subject: پیام شما دریافت شد
From: farhadrezaei.eng@gmail.com
To: {email}
```

### ۳. Email Notifications

Web3Forms به ایمیل تو نوتیفیکیشن می‌فرستد.

### ۴. Custom Subject

موضوع ایمیل‌ها را تنظیم کن:

```
📬 پیام جدید از farhadproject.ir
```

## 🎓 بررسی Access Key

برای تست:

1. فرم را در سایت پر کن.
2. ارسال کن.
3. ایمیل خودت را چک کن.
4. اگر پیام رسید، کلید کار می‌کند.

## 🛑 عیب‌یابی

### مشکل ۱: ایمیل تأیید نمی‌رسد

**علت:** Spam.

**راه‌حل:**
- پوشه Spam.
- اگر پیدا نکردی، دوباره ثبت‌نام کن.

### مشکل ۲: Access Key کار نمی‌کند

**علت‌ها:**
- کپی ناقص.
- فاصله اضافه.
- کلید اشتباه.

**راه‌حل:**
- کلید را کامل کپی کن.
- در پنل Web3Forms کلید را چک کن.

### مشکل ۳: محدودیت پیام

**علت:** بیش از ۲۵۰ پیام در ماه.

**راه‌حل:**
- صبر کن تا ماه بعد.
- یا پلن حرفه‌ای.

### مشکل ۴: پیام‌ها به Spam می‌روند

**علت:** فیلتر ایمیل.

**راه‌حل:**
- در ایمیل، پیام Web3Forms را **Not Spam** کن.
- از ایمیل شخصی استفاده کن، نه شرکتی.

## 🎓 امنیت Access Key

### چه کار نکنی

- ❌ در GitHub Commit نکن.
- ❌ در جای عمومی نگذار.
- ❌ در Postman یا cURL با URL عمومی نگذار.

### چه کار کنی

- ✅ در `.env` بگذار (اگر حساس است).
- ✅ در HTML مستقیم (اگر public است).
- ✅ برای هر پروژه، یک Key جدا.

## 🎓 در پروژه ما

Access Key ما:

```astro
<input
  type="hidden"
  name="access_key"
  value="a1b2c3d4-..."
/>
```

در فایل `src/pages/contact.astro`.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | رفتن به web3forms.com |
| ۲ | Create Access Key |
| ۳ | وارد کردن ایمیل |
| ۴ | تأیید ایمیل |
| ۵ | کپی کلید |
| ۶ | استفاده در فرم |

| تنظیم | کاربرد |
|---|---|
| Domain Restriction | محدود به دامنه |
| Auto-Response | ایمیل خودکار به کاربر |
| Custom Subject | موضوع ایمیل |

## آماده‌ای؟ برو به `04-form-submission.md`.