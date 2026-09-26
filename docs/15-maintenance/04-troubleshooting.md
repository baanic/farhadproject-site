# عیب‌یابی

## 🎓 مفهوم

این فایل، **راهنمای حل مشکلات** رایج است.

## 🎓 دسته‌بندی مشکلات

1. **نصب و راه‌اندازی**
2. **Dev Server**
3. **Build**
4. **Deploy**
5. **بعد از Deploy**

## 🛠 مشکلات نصب

### `command not found: node`

**علت:** Node نصب نیست.

**راه‌حل:**

```bash
nvm install --lts
nvm use --lts
```

### `command not found: npm`

**علت:** npm همراه Node نیست.

**راه‌حل:**

```bash
nvm reinstall-packages
```

### `command not found: nvm`

**علت:** `.zshrc` تنظیم نشده.

**راه‌حل:**

```bash
cat ~/.zshrc
```

باید خطوط nvm را ببینی.

### `command not found: git`

**علت:** Git نصب نیست.

**راه‌حل:**

```bash
xcode-select --install
```

## 🛠 مشکلات Dev Server

### `npm run dev` خطا می‌دهد

**علت‌ها:**
- `node_modules` ناقص.
- خطای Import.

**راه‌حل:**

```bash
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### `Port 4321 already in use`

**علت:** Dev Server قبلی هنوز اجرا می‌شود.

**راه‌حل:**

```bash
lsof -ti:4321 | xargs kill -9
```

**یا:** پورت دیگری:

```bash
npm run dev -- --port 3000
```

### Hot Reload کار نمی‌کند

**علت:** Cache یا چند Dev Server.

**راه‌حل:**
- Dev Server را ببند و باز کن.
- Hard Refresh در مرورگر.

### صفحه سفید در Dev

**علت:** خطای JavaScript یا Import.

**راه‌حل:** ترمینال Dev Server را نگاه کن. خطا آنجاست.

## 🛠 مشکلات Build

### `npm run build` خطا می‌دهد

**علت‌ها:**
- خطای Syntax.
- Import اشتباه.
- فایل نبود.

**راه‌حل:**

```bash
npm run build 2>&1 | head -50
```

۵۰ خط اول خطا را ببین.

### `Cannot find module`

**علت:** مسیر Import اشتباه.

**راه‌حل:**

```astro
<!-- اشتباه -->
import X from "./X.astro";

<!-- درست (بر اساس محل) -->
import X from "../components/X.astro";
import X from "../../components/X.astro";
```

**قاعده:**
- `pages/index.astro` → `../`
- `pages/portfolio/[slug].astro` → `../../`

### `Expected "}"`

**علت:** خطای Syntax در CSS یا JS.

**راه‌حل:** خط را بررسی کن.

### `dist` ساخته نمی‌شود

**علت:** خطای Build.

**راه‌حل:** خطای Build را بخوان و اصلاح کن.

## 🛠 مشکلات Deploy

### `liara: command not found`

**علت:** CLI نصب نیست.

**راه‌حل:**

```bash
npm install -g @liara/cli
```

### `Unauthorized`

**علت:** Session منقضی.

**راه‌حل:**

```bash
liara logout
liara login
```

### `App name already exists`

**علت:** نام اپ گرفته شده.

**راه‌حل:** در `liara.json`:

```json
{
  "app": "farhadproject-site"
}
```

### `Build failed on Liara`

**علت:** خطای Build.

**راه‌حل:** اول محلی Build کن:

```bash
cd astro-site
npm run build
```

### Deploy کند است

**علت:** فایل‌های بزرگ.

**راه‌حل:**
- `node_modules/` نباید در Git باشد.
- در `.gitignore` چک کن.

## 🛠 مشکلات بعد از Deploy

### سایت سفید است

**علت‌ها:**
- فایل‌ها آپلود نشده.
- `dist` اشتباه.
- خطای Build.

**راه‌حل:**
- لاگ‌های Liara: `liara logs`.
- در پنل Liara → Deployments → آخرین Build.

### فونت Shabnam لود نمی‌شود

**علت:** مسیر فونت.

**راه‌حل:**
- در `global.css`: `url('/fonts/Shabnam.woff2')`.
- فایل در `public/fonts/`.

### تصاویر نمایش داده نمی‌شوند

**علت:** مسیر تصویر.

**راه‌حل:**
- در Astro: `/images/...`.
- فایل در `public/images/...`.

### فرم تماس کار نمی‌کند

**علت‌ها:**
- Access Key اشتباه.
- Domain Restriction.

**راه‌حل:**
- در پنل Web3Forms → Allowed Domains.
- `farhadproject.ir` و `www.farhadproject.ir` و `localhost`.
- DevTools → Network → Submit را ببین.

### DNS Propagate نمی‌شود

**علت:** صبر.

**راه‌حل:**

```bash
dig farhadproject.ir
```

- اگر جواب صحیح است، صبر کن.
- اگر جواب اشتباه، رکورد DNS.

### SSL فعال نمی‌شود

**علت:** DNS Propagate کامل نشده.

**راه‌حل:** صبر کن (۱–۲ ساعت).

## 🛠 مشکلات Git

### `remote origin already exists`

**راه‌حل:**

```bash
git remote set-url origin https://github.com/baanic/new.git
```

### `Authentication failed`

**علت:** Token اشتباه.

**راه‌حل:**

```bash
git credential-osxkeychain erase
host=github.com
protocol=https
[Enter]
```

سپس `git push` و Token جدید.

### `rejected — non-fast-forward`

**علت:** مخزن ریموت Commit دارد.

**راه‌حل:**

```bash
git pull --rebase
git push
```

### `fatal: not a git repository`

**علت:** در پوشه اشتباه.

**راه‌حل:**

```bash
cd ~/Documents/Projects/farhadproject
```

## 🛠 مشکلات Python

### `pip: command not found`

**راه‌حل:**

```bash
pip3 install pandas openpyxl
```

### Virtual Environment فعال نمی‌شود

**راه‌حل:**

```bash
source venv/bin/activate
```

### `ModuleNotFoundError: No module named 'pandas'`

**علت:** venv فعال نیست.

**راه‌حل:**

```bash
source venv/bin/activate
pip install pandas
```

### `JSON decode error`

**علت:** JSON نامعتبر.

**راه‌حل:** در [jsonlint.com](https://jsonlint.com) چک کن.

## 🎓 اورژانس: بازگشت به نسخه قبلی

### اگر Commit اشتباه زدی

```bash
git log --oneline  # پیدا کردن Commit قبلی
git revert abc1234
git push
```

### اگر سایت خراب شد

**در پنل Liara:**

1. Deployments.
2. Deploy قبلی موفق.
3. **Rollback**.

### اگر همه چیز خراب شد

```bash
cd ~/Documents/Projects/farhadproject
git reset --hard HEAD~1
git push --force
```

⚠️ **هشدار:** `--force` خطرناک.

## 🎓 ابزارهای مفید

### بررسی Node

```bash
node --version
npm --version
nvm --version
```

### بررسی Git

```bash
git --version
git status
git log --oneline | head -10
```

### بررسی Liara

```bash
liara whoami
liara app list
liara logs
```

### بررسی DNS

```bash
dig farhadproject.ir
nslookup farhadproject.ir
```

## 🎓 منابع کمک

### مستندات رسمی

- [Astro Docs](https://docs.astro.build)
- [Liara Docs](https://docs.liara.ir)
- [Git Docs](https://git-scm.com/doc)
- [MDN Web Docs](https://developer.mozilla.org)

### انجمن‌ها

- [GitHub Discussions](https://github.com/orgs/withastro/discussions)
- [Stack Overflow](https://stackoverflow.com)
- [Liara Support](https://liara.ir/support)

### ابزارهای آنلاین

- [Google Search Console](https://search.google.com/search-console)
- [Metatags.io](https://metatags.io)
- [Whatsmydns.net](https://www.whatsmydns.net)

## 🎓 پروتکل عیب‌یابی

اگر مشکل داری:

1. **آرام باش.** هر مشکل، راه‌حل دارد.
2. **خطا را کامل بخوان.**
3. **پیام خطا را در Google جستجو کن.**
4. **این فایل را مرور کن.**
5. **مستندات رسمی را ببین.**
6. **اگر حل نشد، از یک توسعه‌دهنده کمک بگیر.**

## 🎁 خلاصه

| دسته | بررسی |
|---|---|
| نصب | Node, npm, git |
| Dev | پورت، Cache |
| Build | خطای Syntax |
| Deploy | liara logs |
| بعد Deploy | DNS، SSL |
| Git | Token، Branch |
| Python | venv، pip |
