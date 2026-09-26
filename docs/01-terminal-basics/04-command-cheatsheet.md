# مرجع کامل دستورات ترمینال

این یک **مرجع سریع** است. برای توضیح کامل هر دستور، به فایل مربوطه برگرد.

## 📂 ناوبری (Navigation)

| دستور | کار | مثال |
|---|---|---|
| `pwd` | مسیر فعلی | `pwd` |
| `ls` | لیست محتوا | `ls` |
| `ls -l` | لیست با جزئیات | `ls -l` |
| `ls -la` | لیست کامل + مخفی | `ls -la` |
| `ls -lah` | لیست خوانا با حجم | `ls -lah` |
| `cd X` | رفتن به پوشه X | `cd Documents` |
| `cd` | رفتن به Home | `cd` |
| `cd ~` | همان بالا | `cd ~` |
| `cd ..` | یک مرحله بالا | `cd ..` |
| `cd ../..` | دو مرحله بالا | `cd ../..` |
| `cd -` | بازگشت به پوشه قبلی | `cd -` |

## 📁 ساخت (Creation)

| دستور | کار | مثال |
|---|---|---|
| `mkdir name` | ساخت پوشه | `mkdir new-folder` |
| `mkdir -p a/b/c` | ساخت تو در تو | `mkdir -p src/components` |
| `touch file.txt` | ساخت فایل خالی | `touch README.md` |

## 📋 کپی و جابه‌جایی (Copy & Move)

| دستور | کار | مثال |
|---|---|---|
| `cp src dst` | کپی فایل | `cp a.txt b.txt` |
| `cp -r src dst` | کپی پوشه | `cp -r docs/ docs-backup/` |
| `mv src dst` | جابه‌جایی یا تغییر نام | `mv old.txt new.txt` |

## 🗑️ حذف (Delete)

| دستور | کار | هشدار |
|---|---|---|
| `rm file.txt` | حذف فایل | ⚠️ بدون بازگشت |
| `rm -i file.txt` | حذف با تأیید | ایمن‌تر |
| `rm -r folder` | حذف پوشه | ⚠️ خطرناک |
| `rm -rf folder` | حذف بدون تأیید | 🚨 بسیار خطرناک |

## 📄 خواندن (Read)

| دستور | کار | مثال |
|---|---|---|
| `cat file.txt` | نمایش محتوا | `cat package.json` |
| `less file.txt` | نمایش با اسکرول | `less README.md` |
| `head file.txt` | ۱۰ خط اول | `head log.txt` |
| `tail file.txt` | ۱۰ خط آخر | `tail log.txt` |
| `wc file.txt` | شمارش خط/کلمه/کاراکتر | `wc README.md` |

## ✏️ ویرایش (Edit)

| دستور | کار | مثال |
|---|---|---|
| `code file.txt` | باز کردن در VS Code | `code README.md` |
| `code .` | باز کردن پوشه فعلی | `code .` |
| `nano file.txt` | ویرایشگر ساده ترمینال | `nano config.txt` |
| `vim file.txt` | ویرایشگر حرفه‌ای | `vim script.sh` |

## 🔍 جستجو (Search)

| دستور | کار | مثال |
|---|---|---|
| `grep "text" file` | جستجوی متن در فایل | `grep "error" log.txt` |
| `grep -r "text" folder` | جستجوی بازگشتی | `grep -r "TODO" src/` |
| `find . -name "*.md"` | پیدا کردن فایل | `find . -name "*.json"` |
| `which command` | محل نصب دستور | `which node` |

## 💡 اطلاعات سیستم (System Info)

| دستور | کار | مثال |
|---|---|---|
| `date` | تاریخ و ساعت | `date` |
| `whoami` | کاربر فعلی | `whoami` |
| `hostname` | نام کامپیوتر | `hostname` |
| `uname -a` | اطلاعات سیستم | `uname -a` |
| `df -h` | فضای دیسک | `df -h` |
| `du -sh folder` | حجم پوشه | `du -sh node_modules` |
| `top` | فعالیت‌های سیستم | `top` |
| `ps aux` | پروسه‌های فعال | `ps aux` |

## 📡 شبکه (Network)

| دستور | کار | مثال |
|---|---|---|
| `ping host` | تست اتصال | `ping google.com` |
| `curl url` | درخواست HTTP | `curl https://api.example.com` |
| `dig domain` | بررسی DNS | `dig farhadproject.ir` |
| `ifconfig` | اطلاعات شبکه | `ifconfig` |

## 🔧 ابزارهای توسعه (Dev Tools)

| دستور | کار |
|---|---|
| `node --version` | نسخه Node.js |
| `npm --version` | نسخه npm |
| `git --version` | نسخه Git |
| `python3 --version` | نسخه Python |
| `brew --version` | نسخه Homebrew |

## ⚙️ مدیریت پروسه (Process)

| دستور | کار |
|---|---|
| `Ctrl + C` | متوقف کردن دستور فعال |
| `Ctrl + Z` | متوقف کردن موقت |
| `Ctrl + D` | بستن Shell |
| `Ctrl + L` | پاک کردن صفحه |
| `Ctrl + A` | رفتن به ابتدای خط |
| `Ctrl + E` | رفتن به انتهای خط |
| `Ctrl + U` | پاک کردن تا ابتدا |
| `Ctrl + K` | پاک کردن تا انتها |
| `Ctrl + R` | جستجو در تاریخچه |
| `Tab` | تکمیل خودکار |
| `↑ / ↓` | پیمایش تاریخچه |

## 📝 مسیرها (Paths)

| علامت | معنی |
|---|---|
| `/` | ریشه فایل‌سیستم |
| `~` | پوشه Home |
| `.` | پوشه فعلی |
| `..` | پوشه والد |
| `-` | پوشه قبلی |
| `*` | هر چیزی |

## 🎯 الگوهای رایج (Wildcards)

| الگو | معنی | مثال |
|---|---|---|
| `*.txt` | هر فایل `.txt` | `rm *.txt` (احتیاط!) |
| `**/*.js` | هر `.js` در هر عمقی | `find . -name "**/*.js"` |
| `file?.txt` | یک کاراکتر | `file1.txt`, `file2.txt` |

## 🔗 ترکیب دستورات (Pipes & Redirects)

| علامت | کار | مثال |
|---|---|---|
| `|` | خروجی به ورودی بعدی | `ls \| grep ".md"` |
| `>` | ذخیره در فایل (جایگزین) | `ls > files.txt` |
| `>>` | اضافه به فایل | `echo "line" >> log.txt` |
| `&&` | اجرا اگر موفق بود | `cd X && ls` |
| `\|\|` | اجرا اگر ناموفق بود | `ls \| \|\| echo "not found"` |

## 🚀 دستورات ویژه این پروژه

| دستور | کاربرد |
|---|---|
| `nvm install --lts` | نصب Node.js LTS |
| `nvm use 20` | استفاده از Node 20 |
| `npm install` | نصب پکیج‌ها |
| `npm run dev` | اجرای سرور Astro |
| `npm run build` | Build نهایی |
| `npm create astro@latest .` | ساخت پروژه Astro |
| `git init` | راه‌اندازی Git |
| `git add .` | افزودن همه تغییرات |
| `git commit -m "msg"` | Commit |
| `git push` | فرستادن به GitHub |
| `git log --oneline` | تاریخچه Commit‌ها |
| `liara deploy` | Deploy روی Liara |
