# اولین Push

## 🎓 مفهوم

**Push** یعنی «فرستادن». Commit‌های محلی را به GitHub می‌فرستد.

## 🎓 پیش‌نیاز

| مورد | وضعیت |
|---|---|
| مخزن محلی Git init شده | ✅ |
| Remote `origin` تنظیم شده | ✅ |
| حداقل یک Commit | ✅ |
| Personal Access Token | ✅ |

## 🛠 گام ۱: بررسی وضعیت

```bash
git status
```

خروجی موفق:

```
On branch main
nothing to commit, working tree clean
```

## 🛠 گام ۲: بررسی تاریخچه

```bash
git log --oneline
```

باید حداقل یک Commit ببینی. اگر خالی است، اول Commit بزن.

**اگر خالی بود:**

```bash
git add .
git commit -m "Initial commit"
```

## 🛠 گام ۳: اولین Push

```bash
git push -u origin main
```

**آناتومی:**

| بخش | معنی |
|---|---|
| `git push` | فرستادن |
| `-u` | Set Upstream (تنظیم رابطه) |
| `origin` | نام Remote |
| `main` | نام Branch |

**چرا `-u`؟**

`-u` = `--set-upstream`. به Git می‌گوید: «این Branch محلی به آن Branch ریموت وصل است.»

**پس از اولین Push، دیگر لازم نیست این را بزنی.** فقط `git push` کافی است.

## 🎓 چه اتفاقی می‌افتد؟

### مرحله ۱: احراز هویت

GitHub از تو می‌پرسد:

```
Username for 'https://github.com': 
```

نام کاربری GitHub خودت را وارد کن: `baanic`.

```
Password for 'https://baanic@github.com': 
```

**Token را پیست کن** (نه رمز GitHub).

⚠️ **نکته:** هنگام تایپ Token، هیچ کاراکتری نمایش داده نمی‌شود. طبیعی است.

### مرحله ۲: Push

پس از احراز هویت، Push شروع می‌شود:

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 1.2 KiB | 400.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To https://github.com/baanic/farhadproject-site.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**ترجمه:**

- ۵ object فرستاده شد.
- ۱.۲ KiB حجم کل.
- Branch جدید `main` ساخته شد.
- Branch محلی به Branch ریموت وصل شد.

## 🛠 گام ۴: بررسی موفقیت

### در ترمینال

```bash
git log --oneline
```

خط اول باید یک Commit جدید نشان دهد:

```
def5678 (HEAD -> main, origin/main) Initial commit
```

**توجه:** حالا `origin/main` هم در کنار `main` است. یعنی Commit هم محلی و هم ریموت است.

### در GitHub

1. برو به `https://github.com/baanic/farhadproject-site`.
2. باید فایل‌ها را ببینی.
3. تاریخچه Commit‌ها در بخش **Commits** موجود است.

## 🎓 Push‌های بعدی

بعد از اولین Push، فرآیند ساده‌تر است:

```bash
# تغییر بده
code file.txt

# Stage
git add .

# Commit
git commit -m "Update file"

# Push
git push
```

فقط `git push` کافی است. `-u` دیگر لازم نیست.

## 🎓 مفاهیم مرتبط

### Push بدون Set Upstream

اگر `-u` نزنی:

```bash
git push origin main
```

هر بار باید Branch را مشخص کنی.

**اگر `-u` بزنی:**

```bash
git push
```

Git خودش می‌داند کجا بفرستد.

### Push همه Branchها

```bash
git push --all origin
```

### Push با Force (خطرناک!)

```bash
git push --force origin main
```

⚠️ **هشدار:** این دستور تاریخچه ریموت را **بازنویسی می‌کند**. ممکن است Commit‌های دیگران را پاک کند. هرگز روی Branch مشترک استفاده نکن.

## 🎓 در پروژه ما

اولین Push در روز دوم انجام شد:

```bash
git push -u origin main
```

Token در macOS Keychain ذخیره شد. از آن پس، هر بار فقط:

```bash
git push
```

بدون پرسیدن رمز.

## 🛑 عیب‌یابی

### مشکل ۱: `Authentication failed`

**علت‌ها:**
- Token اشتباه.
- Token منقضی.
- رمز GitHub وارد شده به‌جای Token.

**راه‌حل:**
- Token جدید بساز.
- macOS Keychain را پاک کن:

  ```bash
  git credential-osxkeychain erase
  host=github.com
  protocol=https
  [Ctrl + D]
  ```

- دوباره `git push` بزن.

### مشکل ۲: `Repository not found`

**علت‌ها:**
- URL اشتباه.
- مخزن حذف شده.
- Token اجازه دسترسی ندارد.

**بررسی:**

```bash
git remote -v
```

URL را چک کن. اگر اشتباه است:

```bash
git remote set-url origin https://github.com/CORRECT.git
```

### مشکل ۳: `rejected — non-fast-forward`

**علت:** مخزن ریموت Commit‌هایی دارد که تو نداری. (معمولاً چون GitHub README اولیه ساخت).

**راه‌حل ۱: Pull و Merge**

```bash
git pull origin main --allow-unrelated-histories
git push
```

**راه‌حل ۲: Force Push (خطرناک!)**

فقط اگر مطمئنی کسی روی مخزن کار نمی‌کند:

```bash
git push --force origin main
```

### مشکل ۴: `src refspec main does not match any`

**علت:** Branch فعلی `main` نیست (شاید `master`).

**بررسی:**

```bash
git branch
```

**راه‌حل: تغییر نام Branch**

```bash
git branch -M main
git push -u origin main
```

### مشکل ۵: Push بسیار کند است

**علت:** سرعت آپلود یا فایل‌های بزرگ.

**راه‌حل:**
- صبر کن.
- بررسی کن فایل بزرگی در Commit نباشد:

  ```bash
  git ls-files | xargs ls -la | sort -k5 -n | tail -10
  ```

  (۱۰ فایل بزرگ را نشان می‌دهد)

## 🎓 Push چطور کار می‌کند؟

در پشت صحنه، Push یک فرآیند پیچیده است:

```
[مخزن محلی]                         [مخزن ریموت]
     │                                    │
     │  ۱. Git objects محلی را بسته‌بندی می‌کند
     │  ۲. با SSH/HTTPS متصل می‌شود
     │  ۳. احراز هویت
     │  ۴. objects را می‌فرستد
     │                                    │
     │  ─────────────────────────────►   │
     │                                    │
     │                            ۵. objects را ذخیره می‌کند
     │                            ۶. Branch را بروز می‌کند
     │                                    │
     │  ◄─────────────────────────────    │
     │  ۷. تأیید موفقیت
     │                                    │
```

**Git Objects** چیست؟ هر Commit، یک object است. Push، همه objectهای جدید را می‌فرستد.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `git push -u origin main` | اولین Push |
| `git push` | Push‌های بعدی |
| `git push origin branch` | Push به Branch خاص |
| `git push --all origin` | همه Branchها |

## آماده‌ای؟ برو به `04-readme-and-markdown.md`.