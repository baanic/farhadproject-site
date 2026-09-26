# اتصال دامنه

## 🎓 مفهوم

بعد از Deploy، سایت روی `*.liara.run` است. اما دامنه اصلی `farhadproject.ir` باید **وصل** شود.

## 🎓 پیش‌نیاز

- Deploy موفق
- دامنه `farhadproject.ir`
- دسترسی به DNS دامنه

## 🎓 مرحله ۱: بررسی محل DNS

**قبل از هر کاری، باید بدانی DNS دامنه‌ات کجاست.**

### روش ۱: مراجعه به ایرنیک

1. برو به [nic.ir](https://nic.ir).
2. وارد شو.
3. **دامنه‌های من**.
4. `farhadproject.ir` را پیدا کن.
5. **Name Server** را ببین.

**چند حالت:**

| Name Server | محل مدیریت |
|---|---|
| `ns*.iran-server.com` | cPanel |
| `ns*.parspack.com` | پنل Parspack |
| `ns*.cloudflare.com` | Cloudflare |
| `ns*.liara.ir` | Liara |

### روش ۲: `dig`

```bash
dig farhadproject.ir NS
```

**خروجی:** Name Serverهای دامنه.

## 🛠 مرحله ۲: اتصال دامنه در Liara

### در پنل Liara

1. برو به [console.liara.ir](https://console.liara.ir).
2. اپ `farhadproject` را باز کن.
3. تب **Domains**.
4. **Add Domain** را بزن.
5. دامنه را وارد کن:

```
farhadproject.ir
```

### Liara اطلاعات DNS می‌دهد

دو حالت:

#### حالت ۱: CNAME

```
Type: CNAME
Name: @
Value: farhadproject.liara.run
```

#### حالت ۲: A Record

```
Type: A
Name: @
Value: 185.xxx.xxx.xxx
```

**کدام را استفاده کنم؟**

- **CNAME:** توصیه‌شده.
- **A Record:** اگر CNAME در ریشه دامنه اجازه نداشت.

**نکته:** Liara به تو می‌گوید کدام را استفاده کن.

## 🛠 مرحله ۳: اضافه کردن رکورد DNS

### اگر DNS در cPanel است

1. cPanel → **Zone Editor**.
2. `farhadproject.ir` را انتخاب کن.
3. **Add Record**.
4. نوع: CNAME یا A.
5. مقادیر از Liara.
6. **Save**.

### اگر DNS در Cloudflare است

1. Cloudflare Dashboard.
2. دامنه را انتخاب کن.
3. **DNS** → **Records**.
4. **Add record**.
5. نوع: CNAME.
6. Name: `@`.
7. Target: `farhadproject.liara.run`.
8. **Proxy status:** اول DNS only (برای تست).
9. **Save**.

### اگر DNS در ایرنیک است

1. [nic.ir](https://nic.ir).
2. **دامنه‌های من** → `farhadproject.ir`.
3. **مدیریت DNS**.
4. رکورد جدید.
5. مقادیر از Liara.
6. **ثبت**.

## 🛠 مرحله ۴: زیردامنه www

معمولاً `www.farhadproject.ir` هم می‌خواهی:

### در Liara

Add Domain: `www.farhadproject.ir`.

### در DNS

```
Type: CNAME
Name: www
Value: farhadproject.liara.run
```

## 🛠 مرحله ۵: انتظار برای Propagate

DNS Propagate = پخش تغییرات در سراسر اینترنت.

**زمان:**

| مدت | توضیح |
|---|---|
| ۵ دقیقه | حداقل |
| ۳۰ دقیقه | معمول |
| ۲–۲۴ ساعت | حداکثر |
| ۴۸ ساعت | نادر |

### بررسی Propagate

```bash
dig farhadproject.ir
```

**خروجی موفق:**

```
farhadproject.ir.  300  IN  CNAME  farhadproject.liara.run.
```

**ابزار آنلاین:** [whatsmydns.net](https://www.whatsmydns.net).

## 🛠 مرحله ۶: SSL خودکار

بعد از Propagate، Liara خودکار SSL (Let's Encrypt) را فعال می‌کند.

**زمان:** ۵–۱۵ دقیقه.

**بررسی:**

آدرس `https://farhadproject.ir`.

**باید ببینی:** قفل سبز در نوار مرورگر.

**اگر SSL فعال نشد:**

1. در پنل Liara → Domains.
2. دامنه را انتخاب کن.
3. **Issue SSL Certificate**.

## 🎓 مرحله ۷: تست نهایی

- [ ] `http://farhadproject.ir` → Redirect به HTTPS
- [ ] `https://farhadproject.ir` → سایت بارگذاری می‌شود
- [ ] `https://www.farhadproject.ir` → همان سایت
- [ ] SSL قفل سبز
- [ ] همه صفحات کار می‌کنند

## 🎓 مفهوم: DNS Records

| نوع | کاربرد |
|---|---|
| **A** | IP مستقیم |
| **CNAME** | نام دیگر |
| **MX** | ایمیل |
| **TXT** | تأیید |
| **NS** | Name Server |

**ما از CNAME استفاده می‌کنیم.**

## 🎓 تفاوت A و CNAME

### A Record

```
farhadproject.ir → 185.xxx.xxx.xxx (IP)
```

**مزیت:** سریع‌تر.
**عیب:** اگر IP عوض شود، باید دستی.

### CNAME

```
farhadproject.ir → farhadproject.liara.run
```

**مزیت:** اگر IP عوض شود، خودکار.
**عیب:** کمی کندتر (نیاز به Resolve اضافه).

**Liara CNAME توصیه می‌کند.**

## 🛑 عیب‌یابی

### مشکل ۱: سایت هنوز روی IP قدیمی است

**علت:** DNS Propagate.

**راه‌حل:** صبر کن.

**بررسی:** `dig farhadproject.ir`.

### مشکل ۲: SSL فعال نمی‌شود

**علت:** DNS Propagate هنوز کامل نشده.

**راه‌حل:** صبر کن، یا در پنل Liara دوباره تلاش کن.

### مشکل ۳: `www` کار نمی‌کند

**علت:** رکورد `www` اضافه نشده.

**راه‌حل:** رکورد جدید در DNS.

### مشکل ۴: ریدایرکت HTTP → HTTPS نیست

**علت:** Liara باید خودکار کند.

**راه‌حل:** در پنل Liara تنظیمات SSL را بررسی کن.

### مشکل ۵: `CNAME at apex` خطا

**علت:** بعضی DNS‌ها CNAME روی ریشه دامنه را اجازه نمی‌دهند.

**راه‌حل:** از A Record استفاده کن.

## 🎓 تنظیمات اضافی

### HSTS

**HSTS** = HTTP Strict Transport Security.

مرورگر فقط از HTTPS استفاده می‌کند.

در Liara فعال کن.

### Redirect www → non-www

یا برعکس. در Liara تنظیم کن.

## 🎓 در پروژه ما

مراحل:

1. دامنه `farhadproject.ir` در Liara.
2. CNAME به `farhadproject.liara.run`.
3. Propagate (۳۰ دقیقه).
4. SSL خودکار.
5. تست.

## 🎁 خلاصه

| گام | کار |
|---|---|
| ۱ | بررسی محل DNS |
| ۲ | Add Domain در Liara |
| ۳ | Add DNS Record |
| ۴ | www |
| ۵ | انتظار Propagate |
| ۶ | SSL |
| ۷ | تست |

| رکورد | مقدار |
|---|---|
| Type | CNAME |
| Name | @ |
| Value | farhadproject.liara.run |

## آماده‌ای؟ برو به `06-auto-deploy.md`.