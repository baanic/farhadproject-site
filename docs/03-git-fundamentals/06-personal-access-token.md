# Personal Access Token

## 🎓 مفهوم

وقتی می‌خواهی کد را به GitHub بفرستی، GitHub از تو **احراز هویت** می‌خواهد.

**قبل از سال ۲۰۲۱:**

```
Username: baanic
Password: my-password
```

**از سال ۲۰۲۱:**

```
Username: baanic
Password: ghp_xxxxxxxxxxxxxxxxxx
```

GitHub رمز عبور معمولی را **قبول نمی‌کند**. باید **Personal Access Token** بسازی.

## 🎓 چرا GitHub این تصمیم را گرفت؟

### دلیل ۱: امنیت

- رمز عبور را می‌توانی جایی ذخیره کنی که امن نیست.
- Token محدودیت دارد (فقط Scope مشخص).
- Token را می‌توانی هر وقت باطل کنی.

### دلیل ۲: انعطاف

- می‌توانی Token‌های مختلف برای کارهای مختلف بسازی.
- هر Token فقط دسترسی‌های مشخص دارد.

### دلیل ۳: ردیابی

- GitHub می‌داند چه Token‌ای، از کجا، چه کارهایی انجام داده.

## 🛠 گام ۱: ساخت Token

### ۱. رفتن به تنظیمات

1. وارد [github.com](https://github.com) شو.
2. روی آواتار (بالا راست) کلیک کن.
3. **Settings**.
4. در سایدبار، **Developer settings** (پایین).
5. **Personal access tokens**.
6. **Tokens (classic)**.

**آدرس مستقیم:**
[github.com/settings/tokens](https://github.com/settings/tokens)

### ۲. ساخت Token جدید

1. **Generate new token**.
2. **Generate new token (classic)**.

**چرا Classic؟**

- ساده‌تر.
- برای پروژه‌های شخصی کافی است.
- Fine-grained برای سازمان‌های بزرگ طراحی شده.

### ۳. تنظیمات

| فیلد | مقدار |
|---|---|
| **Note** | `Mac Terminal — Farhad` |
| **Expiration** | `90 days` (یا `No expiration` با احتیاط) |

**نکته درباره Expiration:**
- ۳۰ روز، ۶۰ روز، ۹۰ روز، ۱ سال یا Custom.
- `No expiration` امنیت را کم می‌کند.
- پیشنهاد: `90 days`.

### ۴. انتخاب Scope

در بخش **Select scopes**:

**حداقل موردنیاز برای ما:**

| Scope | کاربرد |
|---|---|
| ✅ `repo` | کامل: خواندن و نوشتن مخزن‌های خصوصی و عمومی |
| ✅ `workflow` | برای GitHub Actions (اختیاری) |

**چرا `repo` کافی است؟**

- Push کردن.
- Pull کردن.
- مدیریت مخزن.

**Scope‌های اضافه نزن.** هر Scope، یک سطح دسترسی است.

### ۵. تولید Token

1. **Generate token** (پایین صفحه).
2. Token نمایش داده می‌شود:

```
ghp_abcdefghijklmnopqrstuvwxyz1234567890
```

⚠️ **هشدار مهم:** این Token **فقط یک بار** نمایش داده می‌شود. اگر گمش کنی، باید یکی جدید بسازی.

**راه‌حل:** فوراً کپی کن و در **جای امن** ذخیره کن.

## 🎓 کجا Token را ذخیره کنیم؟

### گزینه ۱: Password Manager

- **1Password** (پولی).
- **Bitwarden** (رایگان و Open Source).
- **KeePass** (رایگان).

### گزینه ۲: macOS Keychain

در ترمینال:

```bash
git config --global credential.helper osxkeychain
```

از این پس، مک Token را در Keychain ذخیره می‌کند. یک بار که وارد کنی، برای همیشه یادش می‌ماند.

### گزینه ۳: در یک فایل متنی محلی

⚠️ **خطرناک.** فقط اگر بقیه گزینه‌ها نیستند.

فایل در `~/Documents/private/tokens.txt` (بیرون از پروژه).

## 🛠 گام ۲: استفاده از Token در Git

### بار اول Push

```bash
git push -u origin main
```

خروجی:

```
Username for 'https://github.com': baanic
Password for 'https://baanic@github.com': 
```

**چی وارد کنم؟**

- **Username:** `baanic` (نام کاربری GitHub).
- **Password:** **Token را پیست کن** (نه رمز GitHub).

**نکته:** هنگام تایپ Password، هیچ کاراکتری نمایش داده نمی‌شود. طبیعی است.

### پس از موفقیت

اگر تنظیمات Credential Helper فعال باشد، Token ذخیره می‌شود. برای Push‌های بعدی، دیگر نمی‌پرسد.

## 🎓 مقایسه روش‌های احراز هویت

| روش | توضیح | مناسب برای |
|---|---|---|
| **HTTPS + Token** | ساده، همه جا کار می‌کند | مبتدی‌ها ✅ |
| **SSH Key** | امن‌تر، بدون رمز | حرفه‌ای‌ها |
| **GitHub CLI** | راحت‌ترین | کاربران حرفه‌ای |

**ما HTTPS + Token استفاده می‌کنیم** چون:
- ساده‌تر است.
- با Liara سازگار است.
- برای مبتدی کافی است.

## 🎓 اگر Token را گم کردی

1. برو به [github.com/settings/tokens](https://github.com/settings/tokens).
2. Token قدیمی را **Revoke** کن (حذف).
3. یکی جدید بساز.
4. Token جدید را در Git استفاده کن.

**پاک کردن Token ذخیره‌شده در مک:**

```bash
git credential-osxkeychain erase
host=github.com
protocol=https
[Enter]
```

## 🎓 ترفند: GitHub CLI

اگر می‌خواهی راحت‌تر باشد:

1. نصب GitHub CLI:

   ```bash
   brew install gh
   ```
   (یا از سایت GitHub دانلود کن)

2. ورود:

   ```bash
   gh auth login
   ```

3. تمام! `gh` خودش همه چیز را مدیریت می‌کند.

## 🎓 در پروژه ما

ما از **HTTPS + Token** استفاده کردیم.

**مراحل:**

1. Token در GitHub ساختیم.
2. در اولین Push، Username و Token را وارد کردیم.
3. macOS Keychain آن را ذخیره کرد.
4. Push‌های بعدی، بدون پرسیدن.

**بررسی Credential Helper:**

```bash
git config --global credential.helper
```

باید ببینی: `osxkeychain`.

اگر خالی است:

```bash
git config --global credential.helper osxkeychain
```

## 🛑 عیب‌یابی

### مشکل ۱: `Authentication failed`

**علت‌های احتمالی:**
- Token اشتباه.
- Token منقضی شده.
- Username اشتباه.

**راه‌حل:**
- Token جدید بساز.
- Username را بررسی کن.
- Token را از Keychain پاک کن و دوباره وارد کن.

### مشکل ۲: هر بار می‌پرسد

**علت:** Credential Helper تنظیم نشده.

**راه‌حل:**

```bash
git config --global credential.helper osxkeychain
```

### مشکل ۳: `remote: Support for password authentication was removed`

**علت:** از رمز عبور استفاده کردی، نه Token.

**راه‌حل:**
- Token جدید بساز.
- از Token استفاده کن.

## 🎓 امنیت Token

### قواعد طلایی

| قاعده | چرا |
|---|---|
| Token را در پروژه ذخیره نکن | به Git می‌رود، همه می‌بینند |
| Scope اضافی نده | اگر لو رفت، آسیب کمتر |
| Expiration کوتاه بگذار | Token‌های قدیمی خطرناک‌اند |
| دوره‌ای Token عوض کن | امنیت بیشتر |
| Revoke کن Token‌های قدیمی | پاکسازی |

### اگر Token لو رفت

1. **فوراً** Revoke کن.
2. Token جدید بساز.
3. تمام رمزهای مرتبط را عوض کن.

## 🎁 خلاصه

| کار | روش |
|---|---|
| ساخت Token | GitHub → Settings → Developer → Tokens |
| Scope موردنیاز | `repo` |
| ذخیره امن | macOS Keychain |
| استفاده در Git | Username + Token |
| تنظیم Credential | `git config --global credential.helper osxkeychain` |

## 🎉 پایان بخش ۰۳

تبریک! Git را یاد گرفتی. حالا می‌توانی:
- مخزن بسازی.
- Commit بزنی.
- Push کنی.
- با GitHub کار کنی.

## گام بعدی: `../04-github-workflow/`.