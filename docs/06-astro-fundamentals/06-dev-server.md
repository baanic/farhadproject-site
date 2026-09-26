# Dev Server و Hot Reload

## 🎓 مفهوم

**Dev Server** یک سرور محلی است که سایت را در حین توسعه روی کامپیوتر تو اجرا می‌کند.

## 🎓 چرا Dev Server؟

### ۱. بدون نیاز به Deploy

هر تغییر کوچکی، نیازی به آپلود روی سرور ندارد.

### ۲. Hot Reload

بعد از ذخیره فایل، صفحه **خودکار** بروز می‌شود.

### ۳. پیام‌های خطا

خطاها را در ترمینال و مرورگر می‌بینی.

## 🛠 اجرای Dev Server

### گام ۱: رفتن به پوشه سایت

```bash
cd ~/Documents/Projects/farhadproject/astro-site
```

### گام ۲: اجرای دستور

```bash
npm run dev
```

### خروجی

```
> astro-site@0.0.1 dev
> astro dev

  🚀  astro  v5.x.x started in 250 ms

  ┃ Local    http://localhost:4321/
  ┃ Network  use --host to expose

  ┃ watching for file changes...
```

### گام ۳: باز کردن مرورگر

آدرس `http://localhost:4321` را در مرورگر باز کن.

## 🎓 مفهوم: `localhost`

**localhost** یعنی «این کامپیوتر».

- `localhost:4321` = سرور روی کامپیوتر خودت، پورت ۴۳۲۱.

**نکته:** `localhost` فقط روی کامپیوتر خودت کار می‌کند. کسی دیگری نمی‌بیندش.

## 🎓 مفهوم: Port 4321

**Port** یک شماره است که هر برنامه از آن استفاده می‌کند.

| Port | برنامه |
|---|---|
| 80 | HTTP |
| 443 | HTTPS |
| 3000 | Next.js (پیش‌فرض) |
| 4321 | Astro (پیش‌فرض) |
| 5173 | Vite (پیش‌فرض) |
| 8000 | Python |

**4321** = پورت پیش‌فرض Astro. می‌توانی عوضش کنی:

```bash
npm run dev -- --port 3000
```

## 🎓 Hot Reload (بارگذاری فوری)

**Hot Reload** یعنی: «صفحه را رفرش نکن، خودش بروز می‌شود.»

### تست

1. سایت را در مرورگر باز کن.
2. در VS Code، فایل `src/pages/index.astro` را باز کن.
3. یک کلمه را عوض کن.
4. ذخیره کن (`Cmd + S`).
5. **بدون رفرش**، مرورگر را نگاه کن.

**باید ببینی:** صفحه خودکار بروز شده.

## 🎓 چطور Hot Reload کار می‌کند؟

```
[VS Code]                    [Dev Server]              [مرورگر]
    │                              │                       │
    │  ۱. فایل را ذخیره می‌کنی       │                       │
    │  ─────────────────────────►  │                       │
    │                              │                       │
    │                        ۲. تغییر را تشخیص می‌دهد     │
    │                              │                       │
    │                        ۳. با WebSocket پیام می‌فرستد
    │                              │  ───────────────────► │
    │                              │                       │
    │                              │                  ۴. صفحه بروز می‌شود
    │                              │                       │
```

**WebSocket:** یک اتصال دائم بین Dev Server و مرورگر. از این طریق، تغییرات فوری می‌رسند.

## 🎓 متوقف کردن Dev Server

برای متوقف کردن:

```
Ctrl + C
```

## 🎓 دیدن تغییرات سریع

### تغییر CSS

Hot Reload فوری اعمال می‌کند.

### تغییر JavaScript/Frontmatter

Hot Reload صفحه را دوباره بارگذاری می‌کند.

### تغییر فایل جدید

فایل جدید ساخته شده. به مسیر مربوطه برو.

**مثال:** `src/pages/about.astro` ساختی → `http://localhost:4321/about`.

## 🎓 ترفند: چند ترمینال

می‌توانی **همزمان** چند دستور اجرا کنی:

### ترمینال ۱: Dev Server

```bash
npm run dev
```

### ترمینال ۲: Git، نصب پکیج، ...

```bash
git status
```

**در VS Code:** `Cmd + Shift + ` (Backtick) → Terminal جدید.

## 🎓 ترفند: Network Access

اگر می‌خواهی از موبایل یا کامپیوتر دیگر به سایت دسترسی داشته باشی:

```bash
npm run dev -- --host
```

خروجی:

```
┃ Local    http://localhost:4321/
┃ Network  http://192.168.1.100:4321/
```

**آدرس Network:** از دستگاه‌های دیگر در همان WiFi کار می‌کند.

**مثال:** موبایل خودت را وصل کن، آدرس را در مرورگر بزن.

## 🎓 تفاوت `dev` و `build` و `preview`

| دستور | کاربرد | سرعت |
|---|---|---|
| `npm run dev` | توسعه | سریع |
| `npm run build` | ساخت خروجی | کند |
| `npm run preview` | پیش‌نمایش Build | سریع |

### `dev`

- سرور توسعه.
- Hot Reload.
- فقط برای تو.

### `build`

- خروجی `dist/`.
- بهینه‌سازی شده.
- برای Deploy.

### `preview`

- خروجی `dist/` را در سرور محلی.
- تست قبل از Deploy.

**مثال:**

```bash
npm run build
npm run preview
```

سپس `http://localhost:4321` را ببین. این دقیقاً همان چیزی است که روی Liara اجرا می‌شود.

## 🎓 پیام‌های Dev Server

### شروع موفق

```
🚀 astro v5.x.x started in 250 ms
```

### تغییر فایل

```
[vite] hmr update /src/pages/index.astro
```

`hmr` = Hot Module Replacement.

### خطا

```
✘ [ERROR] Cannot find module "./Hero.astro"
```

خطا را سریع ببین و اصلاح کن.

## 🛑 عیب‌یابی

### مشکل ۱: `Port 4321 already in use`

**علت:** یک Dev Server قبلاً در حال اجرا است.

**راه‌حل ۱:** سرور قدیمی را ببند:

```bash
lsof -ti:4321 | xargs kill -9
```

**راه‌حل ۲:** از پورت دیگری استفاده کن:

```bash
npm run dev -- --port 3000
```

### مشکل ۲: Hot Reload کار نمی‌کند

**علت‌ها:**
- Cache مرورگر.
- چند Dev Server.

**راه‌حل:**
- Hard Refresh: `Cmd + Shift + R`.
- Dev Server را ببند و دوباره اجرا کن.

### مشکل ۳: مرورگر صفحه سفید نشان می‌دهد

**علت:** خطای Build یا Import.

**راه‌حل:** ترمینال را ببین. خطا آنجاست.

### مشکل ۴: `npm run dev` بلافاصله متوقف می‌شود

**علت:** خطای Import یا Syntax.

**راه‌حل:** خطای ترمینال را بخوان و اصلاح کن.

### مشکل ۵: خیلی کند است

**علت:** پروژه بزرگ یا کامپیوتر کند.

**راه‌حل:**
- `node_modules` را دوباره نصب کن:
  ```bash
  rm -rf node_modules
  npm install
  ```

## 🎓 در پروژه ما

هر بار کار روی پروژه:

```bash
cd ~/Documents/Projects/farhadproject/astro-site
npm run dev
```

مرورگر: `http://localhost:4321`.

هر تغییر، فوری.

هر بار تمام شد:

```
Ctrl + C
```

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `npm run dev` | شروع Dev Server |
| `npm run build` | ساخت خروجی |
| `npm run preview` | پیش‌نمایش Build |
| `Ctrl + C` | توقف |
| `--host` | دسترسی از شبکه |

| مفهوم | توضیح |
|---|---|
| localhost | کامپیوتر خودت |
| Port 4321 | پورت پیش‌فرض |
| Hot Reload | بروزرسانی خودکار |
| HMR | جایگزینی فوری |
