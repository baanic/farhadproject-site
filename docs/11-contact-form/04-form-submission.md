# ارسال فرم

## 🎓 مفهوم

پس از گرفتن Access Key، حالا فرم HTML + JavaScript را می‌سازیم.

## 🛠 گام ۱: ساختار فرم

### `src/pages/contact.astro`

```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
import Navbar from "../components/Navbar.astro";
---

<BaseLayout title="تماس">
  <Navbar />

  <main style="max-width: 700px; margin: 0 auto; padding: 60px 24px;">
    <h1>تماس با من</h1>
    <p>اگر به دنبال یک متخصص هستید، با من تماس بگیرید.</p>

    <form id="contact-form">
      <input
        type="hidden"
        name="access_key"
        value="YOUR-ACCESS-KEY-HERE"
      />

      <input
        type="checkbox"
        name="botcheck"
        style="display: none;"
      />

      <div>
        <label for="name">نام و نام خانوادگی</label>
        <input type="text" id="name" name="name" required />
      </div>

      <div>
        <label for="email">ایمیل</label>
        <input type="email" id="email" name="email" required />
      </div>

      <div>
        <label for="subject">موضوع</label>
        <input type="text" id="subject" name="subject" required />
      </div>

      <div>
        <label for="message">پیام</label>
        <textarea id="message" name="message" required></textarea>
      </div>

      <button type="submit" id="submit-button">
        ارسال پیام
      </button>

      <p id="form-status"></p>
    </form>
  </main>
</BaseLayout>
```

## 🎓 آناتومی فرم

### ۱. `access_key`

```astro
<input type="hidden" name="access_key" value="..." />
```

**نکته:** `type="hidden"` یعنی «نامرئی، اما در ارسال می‌رود.»

### ۲. `botcheck`

```astro
<input type="checkbox" name="botcheck" style="display: none;" />
```

**نکته:** کاربر نمی‌بیند، اما ربات‌ها آن را تیک می‌زنند → Web3Forms می‌فهمد.

### ۳. فیلدهای اصلی

هر فیلد `name` دارد. Web3Forms از `name` برای ساخت ایمیل استفاده می‌کند:

| `name` | محتوای ایمیل |
|---|---|
| `name` | «نام: فرهاد» |
| `email` | «ایمیل: user@example.com» |
| `subject` | موضوع ایمیل |
| `message` | متن پیام |

**نکته:** فیلد `subject` به‌طور خودکار **موضوع ایمیل** می‌شود.

### ۴. دکمه ارسال

```astro
<button type="submit">ارسال پیام</button>
```

**نکته:** `type="submit"` یعنی «این دکمه فرم را ارسال می‌کند.»

## 🛠 گام ۲: استایل فرم

```astro
<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  label {
    display: block;
    color: #1B2A4A;
    font-size: 14px;
    margin-bottom: 8px;
  }

  input,
  textarea {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #D9D4C8;
    border-radius: 8px;
    font-family: inherit;
    font-size: 15px;
  }

  button {
    background: #1B2A4A;
    color: #F5F0E6;
    padding: 14px 32px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
  }

  button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  #form-status {
    text-align: center;
    font-size: 14px;
    min-height: 20px;
  }
</style>
```

## 🛠 گام ۳: JavaScript ارسال

```astro
<script is:inline>
  const form = document.getElementById("contact-form");
  const status = document.getElementById("form-status");
  const submitButton = document.getElementById("submit-button");

  form.addEventListener("submit", async function (e) {
    // جلوگیری از رفتار پیش‌فرض
    e.preventDefault();

    // تغییر ظاهر دکمه
    submitButton.disabled = true;
    submitButton.textContent = "در حال ارسال...";
    status.textContent = "";

    // جمع‌آوری داده فرم
    const formData = new FormData(form);

    try {
      // ارسال به Web3Forms
      const response = await fetch(
        "https://api.web3forms.com/submit",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (data.success) {
        status.style.color = "#5C7A5C";
        status.textContent = "✓ پیام شما با موفقیت ارسال شد.";
        form.reset();
      } else {
        status.style.color = "#A33";
        status.textContent = "✗ خطا در ارسال. دوباره تلاش کنید.";
      }
    } catch (error) {
      status.style.color = "#A33";
      status.textContent = "✗ خطای شبکه. دوباره تلاش کنید.";
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "ارسال پیام";
    }
  });
</script>
```

## 🎓 توضیح خط به خط

### `e.preventDefault()`

```javascript
e.preventDefault();
```

جلوگیری از رفتار پیش‌فرض فرم (رفرش صفحه).

**بدون آن:** صفحه رفرش می‌شود و داده از دست می‌رود.

### `submitButton.disabled = true`

دکمه را غیرفعال می‌کند تا کاربر دوباره کلیک نکند.

### `new FormData(form)`

همه فیلدهای فرم را به‌صورت Object جمع می‌کند.

### `fetch(...)`

درخواست HTTP به Web3Forms.

### `await response.json()`

پاسخ را به JSON تبدیل می‌کند.

### `data.success`

اگر `true`، ارسال موفق بوده.

### `form.reset()`

فرم را خالی می‌کند.

### `finally`

در هر صورت (موفق یا ناموفق)، دکمه را به حالت اولیه برمی‌گرداند.

## 🎓 چرا `is:inline`؟

```astro
<script is:inline>
```

**بدون `is:inline`:** Astro فایل را پردازش و Minify می‌کند.

**با `is:inline`:** Astro آن را مستقیماً در HTML می‌گذارد.

**چرا `is:inline` در این مورد؟**
- کد به DOM نیاز دارد.
- Astro اسکریپت‌های Scoped را به ماژول تبدیل می‌کند که دسترسی به `document` را محدود می‌کند.
- `is:inline` کد را در محل خودش می‌گذارد.

## 🎓 امنیت

### چرا فرم امن است؟

1. **HTTPS:** همه داده رمزنگاری می‌شود.
2. **Access Key:** فقط برای ایمیل تو.
3. **Botcheck:** ضد ربات.
4. **Rate Limiting:** Web3Forms جلوی ارسال زیاد را می‌گیرد.

### نکات امنیتی

- **Access Key در HTML:** مشکلی نیست.
- **فیلدهای اضافی:** نگذار.
- **Validate در سمت کاربر:** کافی نیست، اما کمک می‌کند.

## 🛠 تست

### ۱. اجرای Dev Server

```bash
npm run dev
```

### ۲. باز کردن صفحه

`http://localhost:4321/contact`

### ۳. پر کردن فرم

- نام: تست
- ایمیل: هر ایمیل
- موضوع: تست فرم
- پیام: این یک تست است.

### ۴. ارسال

روی **ارسال پیام** کلیک کن.

### ۵. بررسی

- **در مرورگر:** پیغام سبز موفقیت.
- **در ایمیل:** پیام دریافت می‌شود.

## 🎓 در پروژه ما

فایل: `src/pages/contact.astro`.

ساختار:
- فرم با ۴ فیلد.
- Access Key مخفی.
- Botcheck.
- JavaScript برای ارسال.
- پیغام وضعیت.

## 🛑 عیب‌یابی

### مشکل ۱: پیغام خطا

**علت:** Access Key اشتباه.

**راه‌حل:** کلید را بررسی کن.

### مشکل ۲: صفحه رفرش می‌شود

**علت:** `e.preventDefault()` نبوده.

**راه‌حل:** اضافه کن.

### مشکل ۳: ایمیل نمی‌رسد

**علت:** Spam.

**راه‌حل:** پوشه Spam را چک کن.

### مشکل ۴: ۴۰۳ Forbidden

**علت:** Domain Restriction.

**راه‌حل:** در پنل Web3Forms، دامنه را اضافه کن.

### مشکل ۵: ۴۲۹ Too Many Requests

**علت:** Rate Limit.

**راه‌حل:** صبر کن یا پلن حرفه‌ای.

## 🎓 پیشرفت‌های ممکن

### ۱. Validation

```javascript
if (!formData.get("name")) {
  status.textContent = "نام را وارد کنید";
  return;
}
```

### ۲. Loading Spinner

```astro
<button disabled>
  <span class="spinner"></span>
  در حال ارسال...
</button>
```

### ۳. Redirect به صفحه تشکر

```javascript
if (data.success) {
  window.location.href = "/thank-you";
}
```

### ۴. reCAPTCHA

در پنل Web3Forms فعال کن.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | ساخت فرم |
| ۲ | استایل |
| ۳ | JavaScript |
| ۴ | تست |
| ۵ | بررسی |

| مفهوم | توضیح |
|---|---|
| `FormData` | جمع داده‌ها |
| `fetch` | ارسال درخواست |
| `preventDefault` | جلوگیری از رفرش |
| `is:inline` | Script بدون پردازش |

## آماده‌ای؟ برو به `05-async-await-fetch.md`.