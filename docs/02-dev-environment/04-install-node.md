# نصب Node.js

## 🎓 پیش‌نیاز

قبل از نصب Node، باید nvm نصب باشد. اگر نیست، به فایل قبلی برگرد.

## 🛠 گام ۱: نصب آخرین LTS

```bash
nvm install --lts
```

**خروجی نمونه:**

```
Downloading and installing node v24.21.0...
Downloading https://nodejs.org/dist/v24.21.0/node-v24.21.0-darwin-arm64.tar.gz...
#################################################################### 100.0%
Computing checksum with shasum -a 256
Checksums matched!
Now using node v24.21.0 (npm v11.19.0)
Creating default alias: default -> lts/* (-> v24.21.0)
```

**چه اتفاقی افتاد؟**

1. nvm آخرین نسخه LTS را پیدا کرد.
2. دانلود کرد (حدود ۳۰–۵۰ مگابایت).
3. در `~/.nvm/versions/node/` نصب کرد.
4. `npm` را همراهش نصب کرد.
5. نسخه را فعال کرد.

**زمان:** ۳۰ ثانیه تا ۲ دقیقه (بسته به سرعت اینترنت).

## 🛠 گام ۲: تنظیم Node پیش‌فرض

برای اینکه هر بار ترمینال جدید باز می‌کنی، این نسخه فعال باشد:

```bash
nvm alias default node
```

خروجی: `default -> node (-> v24.21.0)`.

## 🛠 گام ۳: بررسی نصب

سه دستور زیر را بزن:

```bash
node --version
npm --version
nvm --version
```

**خروجی مورد انتظار:**

```
v24.21.0
11.19.0
0.40.4
```

اگر این سه را دیدی، **Node.js با موفقیت نصب شده.** ✅

## 🎓 مفهوم: سه لایه Node.js

Node.js سه لایه دارد:

| لایه | توضیح |
|---|---|
| **Runtime** | موتور اجرای JavaScript (V8) |
| **Standard Library** | کتابخانه‌های داخلی (fs, http, path) |
| **Package Ecosystem** | پکیج‌های npm |

**ما همه این سه لایه را با هم نصب کردیم.**

## 🎓 مفهوم: Global vs Local

### Global Packages

پکیج‌هایی که در **سراسر سیستم** قابل استفاده‌اند:

```bash
npm install -g typescript
```

می‌توانی در هر پوشه‌ای از `tsc` استفاده کنی.

**محل نصب:** `~/.nvm/versions/node/v24.21.0/lib/node_modules/`

### Local Packages

پکیج‌هایی که فقط در **یک پروژه**:

```bash
cd my-project
npm install astro
```

فقط در `my-project/node_modules`.

**توصیه:** تا حد امکان از Local استفاده کن. Global را فقط برای ابزارهای CLI که همیشه لازم داری (مثل `liara` یا `typescript`).

## 🛠 دستورات مهم پس از نصب

### بررسی نسخه‌های نصب‌شده

```bash
nvm ls
```

خروجی نمونه:

```
→       v24.21.0
        v20.11.0
        system
default → node (-> v24.21.0)
```

- `→` = نسخه فعال
- `system` = نسخه نصب‌شده سیستم (اگر داشته باشی)
- `default` = نسخه پیش‌فرض

### سوئیچ به نسخه دیگر

```bash
nvm install 20
nvm use 20
node --version   # v20.11.0
```

### بررسی اینکه واقعاً کدام Node استفاده می‌شود

```bash
which node
```

خروجی باید در پوشه `~/.nvm` باشد:

```
/Users/macuser/.nvm/versions/node/v24.21.0/bin/node
```

اگر مسیر دیگری بود (مثل `/usr/local/bin/node`)، یعنی نسخه‌ای از Node در سیستم قدیمی مانده.

## 🛑 عیب‌یابی

### مشکل ۱: `nvm install --lts` کند است

**علت:** سرورهای nodejs.org در ایران کند هستند.

**راه‌حل:**
- صبر کن.
- اگر خیلی طول کشید، از VPN استفاده کن.

### مشکل ۲: `npm: command not found`

**علت:** nvm نصب است، اما Node نصب نیست.

**راه‌حل:**

```bash
nvm install --lts
nvm use --lts
```

### مشکل ۳: نصب شد، ولی نسخه جدید نیست

**علت:** ممکن است نسخه قدیمی Node هنوز در PATH باشد.

**راه‌حل:**

```bash
nvm use --lts
which node    # بررسی مسیر
```

اگر مسیر `/usr/local/bin/node` بود، باید PATH تنظیم شود. یا Node قدیمی را حذف کن.

### مشکل ۴: `nvm: command not found` (بعد از Reboot)

**علت:** خطوط nvm در `~/.zshrc` نبوده.

**راه‌حل:**

```bash
cat ~/.zshrc
```

باید این خطوط را ببینی:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

اگر نبودند، دوباره نصب کن.

## 🎓 نکته: کدام نسخه LTS استفاده کنیم؟

**آخرین LTS** همیشه بهترین انتخاب است. LTS فعلی (زمان نصب): `v24.21.0`.

اگر در آینده بخواهی Node را آپدیت کنی:

```bash
nvm install --lts --reinstall-packages-from=current
```

این دستور Node جدید را نصب می‌کند و پکیج‌های global قبلی را منتقل می‌کند.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `nvm install --lts` | نصب آخرین LTS |
| `nvm use --lts` | فعال‌سازی |
| `nvm alias default node` | تنظیم پیش‌فرض |
| `nvm ls` | لیست نصب‌شده‌ها |
| `which node` | مسیر Node فعال |
| `node --version` | نسخه Node |
| `npm --version` | نسخه npm |

## آماده‌ای؟ برو به `05-install-vscode.md`.
