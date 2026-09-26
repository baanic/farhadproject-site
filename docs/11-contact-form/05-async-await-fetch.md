# Async/Await/Fetch

## 🎓 مفهوم

**Async/Await** و **Fetch** سه مفهوم مدرن JavaScript برای کار با شبکه.

## 🎓 چرا Async؟

عملیات‌های شبکه **کند** هستند (۱۰۰ms تا ۵ ثانیه).

بدون Async:

```javascript
const data = fetch("https://api.example.com");  // ❌ بلاک می‌شود
console.log(data);
```

**مشکل:** صفحه تا وقتی پاسخ بیاید، بلاک می‌شود.

## 🎓 Callback (روش قدیمی)

```javascript
fetch("https://api.example.com")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

**عیب:** کد تودرتو، سخت خواندن.

## 🎓 Promise

**Promise** = یک Object که **قرار است** آینده یک مقدار داشته باشد.

```javascript
const promise = fetch("https://api.example.com");
// Promise { <pending> }
```

**سه حالت:**

| حالت | معنی |
|---|---|
| **pending** | در انتظار |
| **fulfilled** | موفق |
| **rejected** | خطا |

## 🎓 Async/Await (روش مدرن)

```javascript
async function getData() {
  const response = await fetch("https://api.example.com");
  const data = await response.json();
  console.log(data);
}
```

**نکته:**
- `async` = «این تابع، Promise برمی‌گرداند.»
- `await` = «صبر کن تا این تمام شود.»
- کد **ساده‌تر** از Callback.

## 🎓 تفاوت

### با Promise

```javascript
fetch("https://api.example.com")
  .then(r => r.json())
  .then(data => console.log(data));
```

### با Async/Await

```javascript
const response = await fetch("https://api.example.com");
const data = await response.json();
console.log(data);
```

**دومی واضح‌تر است.**

## 🎓 Fetch API

**Fetch** یک تابع داخلی JavaScript برای ارسال HTTP Request.

### GET (پیش‌فرض)

```javascript
const response = await fetch("https://api.example.com/data");
```

### POST

```javascript
const response = await fetch("https://api.example.com/submit", {
  method: "POST",
  body: formData,
});
```

### با Headers

```javascript
const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ name: "فرهاد" }),
});
```

## 🎓 response چیست؟

`response` یک Object است که اطلاعات پاسخ HTTP را دارد.

| Property | مقدار |
|---|---|
| `response.ok` | `true` اگر Status 200-299 |
| `response.status` | 200, 404, 500 |
| `response.headers` | Headers |

### متدها

| متد | کاربرد |
|---|---|
| `response.json()` | تبدیل به JSON |
| `response.text()` | تبدیل به متن |
| `response.blob()` | تبدیل به Binary |

**نکته:** هر متد، یک Promise برمی‌گرداند. باید `await` بزنی.

## 🎓 Try/Catch

```javascript
try {
  const response = await fetch(url);
  const data = await response.json();
  // ...
} catch (error) {
  // اگر خطایی رخ داد
  console.error(error);
}
```

**نکته:** `try` کد خطرناک، `catch` خطا.

## 🎓 Finally

```javascript
try {
  // ...
} catch (error) {
  // ...
} finally {
  // در هر صورت اجرا می‌شود
}
```

**کاربرد:** بستن لودر، فعال کردن دکمه و ...

## 🎓 در فرم تماس

```javascript
form.addEventListener("submit", async function (e) {
  e.preventDefault();

  // ۱. غیرفعال کردن دکمه
  submitButton.disabled = true;

  // ۲. جمع داده‌ها
  const formData = new FormData(form);

  try {
    // ۳. ارسال
    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      body: formData,
    });

    // ۴. پردازش پاسخ
    const data = await response.json();

    if (data.success) {
      status.textContent = "✓ ارسال شد";
    } else {
      status.textContent = "✗ خطا";
    }
  } catch (error) {
    status.textContent = "✗ خطای شبکه";
  } finally {
    // ۵. بازگرداندن دکمه
    submitButton.disabled = false;
  }
});
```

## 🎓 آناتومی `addEventListener`

```javascript
form.addEventListener("submit", async function (e) { ... });
```

| بخش | معنی |
|---|---|
| `form` | عنصر |
| `addEventListener` | گوش دادن به رویداد |
| `"submit"` | رویداد ارسال فرم |
| `async function (e)` | تابع اجرا |
| `e` | Event Object |

## 🎓 Event Object

```javascript
function (e) {
  e.preventDefault();  // جلوگیری از رفتار پیش‌فرض
  console.log(e.target);  // عنصر
}
```

### متدهای مهم

| متد | کار |
|---|---|
| `e.preventDefault()` | جلوگیری از پیش‌فرض |
| `e.stopPropagation()` | جلوگیری از پخش |

## 🎓 انواع خطا

### ۱. خطای شبکه

اگر اینترنت قطع باشد:

```javascript
try {
  const response = await fetch(url);
} catch (error) {
  // Network error
}
```

### ۲. خطای HTTP

اگر سرور خطا برگرداند:

```javascript
const response = await fetch(url);
if (!response.ok) {
  // 4xx یا 5xx
}
```

### ۳. خطای JSON

اگر پاسخ JSON نامعتبر باشد:

```javascript
try {
  const data = await response.json();
} catch (error) {
  // JSON parse error
}
```

## 🎓 Async در Astro

### در Frontmatter

```astro
---
const response = await fetch("https://api.example.com");
const data = await response.json();
---

<h1>{data.title}</h1>
```

**نکته:** Astro از Top-level await پشتیبانی می‌کند.

### در `<script>`

```astro
<script is:inline>
  async function loadData() {
    const response = await fetch(url);
    // ...
  }
</script>
```

**نکته:** در مرورگر، Async باید داخل تابع باشد (مگر با ماژول).

## 🎓 Async/Await در پروژه ما

فقط در **فرم تماس** استفاده شده، در `<script is:inline>`.

```javascript
const response = await fetch("https://api.web3forms.com/submit", {
  method: "POST",
  body: formData,
});
```

## 🛑 عیب‌یابی

### مشکل ۱: `await is only valid in async function`

**علت:** از `await` در تابع غیر `async` استفاده کردی.

**راه‌حل:**

```javascript
async function myFunc() {
  await fetch(url);
}
```

### مشکل ۲: `fetch is not defined`

**علت:** در Node.js با نسخه قدیمی.

**راه‌حل:** Node 18+ دارد.

### مشکل ۳: `CORS error`

**علت:** سرور مقصد اجازه نمی‌دهد.

**راه‌حل:** Web3Forms اجازه می‌دهد. اگر خطای دیگر داری، بررسی کن.

### مشکل ۴: `response.json is not a function`

**علت:** `response` یک Promise است، نه Object.

**راه‌حل:** `await` فراموش شده:

```javascript
const response = await fetch(url);  // ✅
const response = fetch(url);        // ❌
```

### مشکل ۵: خطا در `try` گرفته نمی‌شود

**علت:** خطای Asynchronous در `try` بدون `await`.

**راه‌حل:** حتماً `await` بگذار.

## 🎓 بهترین تمرین‌ها

### ۱. همیشه `try/catch`

```javascript
try {
  // ...
} catch (error) {
  // ...
}
```

### ۲. `finally` برای پاکسازی

```javascript
try {
  submitButton.disabled = true;
} finally {
  submitButton.disabled = false;
}
```

### ۳. بررسی `response.ok`

```javascript
if (!response.ok) {
  throw new Error("Network error");
}
```

### ۴. پیام‌های خطای واضح

```javascript
catch (error) {
  status.textContent = "خطا: " + error.message;
}
```

## 🎁 خلاصه

| مفهوم | توضیح |
|---|---|
| Promise | وعده آینده |
| async | تابع Async |
| await | صبر |
| fetch | درخواست HTTP |
| try/catch | مدیریت خطا |
| finally | در هر صورت |
| response.json() | تبدیل به JSON |
