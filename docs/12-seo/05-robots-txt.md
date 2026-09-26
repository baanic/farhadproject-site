# robots.txt

## 🎓 مفهوم

**`robots.txt`** یک فایل متنی است که به **ربات‌های موتور جستجو** می‌گوید کدام صفحات را بخوانند و کدام را نه.

## 🎓 چرا robots.txt؟

### ۱. راهنمایی ربات‌ها

به Googlebot بگو چه صفحاتی مجاز هستند.

### ۲. جلوگیری از ایندکس ناخواسته

صفحات اداری، API، یا محتوای حساس را بلاک کن.

### ۳. اشاره به Sitemap

به Google بگو Sitemap کجاست.

## 🎓 ساختار فایل

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/

Sitemap: https://farhadproject.ir/sitemap-index.xml
```

## 🎓 Directiveها

### `User-agent`

| مقدار | معنی |
|---|---|
| `*` | همه ربات‌ها |
| `Googlebot` | فقط Google |
| `Bingbot` | فقط Bing |

**ما `*` استفاده می‌کنیم.**

### `Allow`

اجازه دسترسی.

```
Allow: /
```

همه صفحات.

### `Disallow`

ممنوعیت.

```
Disallow: /admin/
Disallow: /private/
Disallow: /api/
```

### `Sitemap`

آدرس Sitemap.

```
Sitemap: https://farhadproject.ir/sitemap-index.xml
```

## 🛠 ساخت فایل

### گام ۱: ساخت فایل

```bash
cd ~/Documents/Projects/farhadproject/astro-site
code public/robots.txt
```

**نکته:** فایل در `public/` می‌رود، نه `src/`.

### گام ۲: محتوا

```
User-agent: *
Allow: /

Sitemap: https://farhadproject.ir/sitemap-index.xml
```

**ذخیره کن.**

## 🎓 الگوهای Disallow

### یک پوشه

```
Disallow: /admin/
```

### یک فایل

```
Disallow: /secret.html
```

### با Wildcard

```
Disallow: /*.pdf$
```

همه فایل‌های PDF.

### چند پوشه

```
Disallow: /admin/
Disallow: /private/
Disallow: /tmp/
```

## 🎓 Allow و Disallow با هم

```txt
User-agent: *
Disallow: /
Allow: /public/
```

**ترجمه:** «همه چیز ممنوع، جز `/public/`.»

**نکته:** Google از **طولانی‌ترین** match استفاده می‌کند.

## 🎓 User-agent خاص

```txt
# همه
User-agent: *
Disallow: /admin/

# فقط Google
User-agent: Googlebot
Disallow: /no-google/
```

## 🎓 ربات‌های مختلف

| ربات | کاربرد |
|---|---|
| `Googlebot` | Google Search |
| `Bingbot` | Bing |
| `Baiduspider` | Baidu |
| `YandexBot` | Yandex |
| `DuckDuckBot` | DuckDuckGo |
| `Twitterbot` | Twitter |
| `facebookexternalhit` | Facebook |

## 🎓 سایت ما

**همه صفحات عمومی هستند.** پس:

```
User-agent: *
Allow: /

Sitemap: https://farhadproject.ir/sitemap-index.xml
```

**هیچ `Disallow` نداریم.**

**چرا؟**

- صفحه اداری نداریم.
- API نداریم.
- همه صفحات عمومی هستند.
- پس همه مجاز.

## 🎓 سایت‌هایی که نیاز به Disallow دارند

| نوع سایت | Disallow |
|---|---|
| **فروشگاه** | `/checkout/`, `/cart/` |
| **پنل کاربری** | `/dashboard/`, `/account/` |
| **API** | `/api/v1/` |
| **ادمین** | `/admin/`, `/wp-admin/` |
| **جستجو** | `/search?` |

**ما هیچ‌کدام را نداریم.**

## 🎓 تست robots.txt

### ۱. آدرس

```
https://farhadproject.ir/robots.txt
```

### ۲. Google Search Console

- **robots.txt Tester** در قدیم (حذف شده)
- **URL Inspection** → `robots.txt`

### ۳. ابزارهای آنلاین

- [Technical SEO Robots.txt Tester](https://technicalseo.com/tools/robots-txt/)

## 🎓 robots.txt vs Meta Robots

### `robots.txt`

- **فایل** در ریشه سایت.
- برای **کل سایت** یا **پوشه‌ها**.
- توسط **خزنده** خوانده می‌شود.

### Meta Robots

- **تگ HTML** در `head` صفحه.
- برای **یک صفحه**.
- توسط **خزنده** خوانده می‌شود.

**تفاوت مهم:**

- `robots.txt`: «این صفحه را **Crawl نکن**.»
- `<meta robots="noindex">`: «این صفحه را **Index نکن** (اما Crawl کن).»

**نکته:** برای حذف صفحه از نتایج جستجو، **بهتر است** از `noindex` استفاده کنی. `Disallow` گاهی اوقات برعکس عمل می‌کند (Google نمی‌تواند `noindex` را ببیند اگر صفحه Crawl نشود).

## 🛑 عیب‌یابی

### مشکل ۱: `robots.txt` ۴۰۴ می‌دهد

**علت:** فایل در `public/` نیست.

**راه‌حل:** `ls public/robots.txt`.

### مشکل ۲: صفحه‌ای که نباید، ایندکس شده

**علت:** Cache Google.

**راه‌حل:**
- Google Search Console → **Remove URLs**.
- یا صبر کن (۱–۷ روز).

### مشکل ۳: `Sitemap` خطا می‌دهد

**علت:** URL اشتباه.

**راه‌حل:** از `sitemap-index.xml` استفاده کن (نه `sitemap-0.xml`).

### مشکل ۴: Google صفحات را Crawl نمی‌کند

**علت‌ها:**
- `Disallow: /`.
- سایت در Search Console ثبت نشده.
- Sitemap ثبت نشده.

**راه‌حل:** همه را چک کن.

## 🎓 بهترین تمرین‌ها

### ۱. همیشه Sitemap بده

```
Sitemap: https://farhadproject.ir/sitemap-index.xml
```

### ۲. از `Disallow` کمتر استفاده کن

**توصیه:** فقط برای پوشه‌های واقعاً حساس.

### ۳. کامنت بگذار

```
# Block admin panel
Disallow: /admin/

# Sitemap location
Sitemap: https://farhadproject.ir/sitemap-index.xml
```

### ۴. Google Search Console

سایت را ثبت کن تا خطاها را ببینی.

## 🎓 robots.txt در پروژه ما

```
User-agent: *
Allow: /

Sitemap: https://farhadproject.ir/sitemap-index.xml
```

**سه خط، کار تمام.**

## 🎁 خلاصه

| Directive | کاربرد |
|---|---|
| `User-agent: *` | همه ربات‌ها |
| `Allow: /` | اجازه همه |
| `Disallow: /path/` | ممنوعیت |
| `Sitemap: URL` | اشاره به Sitemap |

| ابزار | کاربرد |
|---|---|
| Google Search Console | تست و ثبت |
| robots.txt Tester | تست |