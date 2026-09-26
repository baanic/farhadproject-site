# نصب کتابخانه‌های Python

## 🎓 مفهوم

Python به‌طور پیش‌فرض فقط **کتابخانه‌های استاندارد** دارد. برای کار با Excel، JSON، و داده، باید **کتابخانه‌های خارجی** نصب کنی.

## 🎓 pip چیست؟

**pip** = **P**ip **I**nstalls **P**ackages

مدیر پکیج Python. مشابه npm برای Node.js.

### بررسی نصب pip

```bash
pip3 --version
```

خروجی: `pip 23.x.x`.

اگر نصب نیست، Python را دوباره نصب کن.

## 🎓 چرا macOS و pip؟

در macOS، به‌طور پیش‌فرض Python 3 نصب است. اما:

- `python` ممکن است به Python 2 اشاره کند.
- `pip` ممکن است به pip قدیمی اشاره کند.

**همیشه از `python3` و `pip3` استفاده کن.**

## 🛠 گام ۱: بررسی Python

```bash
python3 --version
```

خروجی: `Python 3.11.x` یا بالاتر.

**اگر خطا داد:** Python نصب نیست. از [python.org](https://www.python.org/downloads/) نصب کن.

## 🛠 گام ۲: ساخت پوشه پروژه Python

```bash
cd ~/Documents/Projects/farhadproject
mkdir -p python-scripts
cd python-scripts
```

## 🛠 گام ۳: ساخت Virtual Environment

**چرا Virtual Environment؟**

هر پروژه Python باید **محیط مجزا** داشته باشد. چرا؟

- پروژه A کتابخانه‌های قدیمی می‌خواهد.
- پروژه B کتابخانه‌های جدید.
- بدون مجزاسازی، تناقض پیش می‌آید.

**ساخت:**

```bash
python3 -m venv venv
```

**فعال‌سازی:**

```bash
source venv/bin/activate
```

**نشانه فعال بودن:** در ابتدای prompt، `(venv)` می‌بینی:

```
(venv) macuser@macusers-MacBook-Pro python-scripts %
```

**غیرفعال‌سازی:**

```bash
deactivate
```

## 🎓 ساختار Virtual Environment

```
python-scripts/
├── venv/                    ← محیط مجازی (به Git نمی‌رود)
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
├── master_data_builder.py
└── requirements.txt
```

**نکته:** `venv/` باید در `.gitignore` باشد.

**بررسی `.gitignore`:**

```bash
grep venv ../.gitignore
```

باید ببینی: `venv/`.

## 🛠 گام ۴: نصب کتابخانه‌ها

با Virtual Environment فعال:

```bash
pip install pandas openpyxl
```

**توضیح:**

| کتابخانه | کاربرد |
|---|---|
| **pandas** | پردازش داده (جدولی) |
| **openpyxl** | ساخت Excel |

**زمان:** ۳۰ ثانیه تا ۱ دقیقه.

**خروجی:**

```
Successfully installed pandas-2.1.0 openpyxl-3.1.2 et-xmlfile-1.1.0 ...
```

## 🛠 گام ۵: بررسی نصب

```bash
pip list
```

باید در لیست ببینی:

```
pandas          2.1.0
openpyxl        3.1.2
```

## 🛠 گام ۶: ساخت `requirements.txt`

فایل `requirements.txt` **لیست کتابخانه‌های پروژه** است.

```bash
pip freeze > requirements.txt
```

فایل را با `code requirements.txt` باز کن. باید ببینی:

```
pandas==2.1.0
openpyxl==3.1.2
...
```

**چرا این فایل؟**

هر کس پروژه را Clone کند، با این دستور همه کتابخانه‌ها را نصب می‌کند:

```bash
pip install -r requirements.txt
```

## 🎓 روزهای بعد

هر بار می‌خواهی روی پروژه Python کار کنی:

```bash
cd ~/Documents/Projects/farhadproject/python-scripts
source venv/bin/activate
# کار کن
```

هر بار تمام شد:

```bash
deactivate
```

## 🎓 در VS Code

اگر Virtual Environment فعال باشد و VS Code باز کنی:

1. VS Code خودکار تشخیص می‌دهد.
2. پایین چپ، نام `venv` را می‌بینی.
3. اگر نبود: `Cmd + Shift + P` → `Python: Select Interpreter` → `venv`.

## 🛑 عیب‌یابی

### مشکل ۱: `pip: command not found`

**راه‌حل:** از `pip3` استفاده کن:

```bash
pip3 install pandas openpyxl
```

### مشکل ۲: `error: externally-managed-environment`

**علت:** Python سیستم مک.

**راه‌حل:** Virtual Environment فعال کن:

```bash
source venv/bin/activate
```

### مشکل ۳: نصب pandas کند است

**علت:** pandas حجم زیادی دارد (حدود ۳۰ MB).

**راه‌حل:** صبر کن.

### مشکل ۴: خطای permission

**راه‌حل:** از `sudo` **استفاده نکن**. Virtual Environment فعال کن.

## 🎓 چرا Virtual Environment مهم است؟

اگر در سیستم اصلی (بدون venv) نصب کنی:

- به روزرسانی Python → همه چیز می‌شکند.
- نصب کتابخانه جدید → ممکن است با قدیمی تناقض داشته باشد.
- پروژه دیگر → کتابخانه‌های متفاوت می‌خواهد.

**با venv:** هر پروژه جزیره خودش است.

## 🎁 خلاصه

| دستور | کار |
|---|---|
| `python3 --version` | بررسی Python |
| `python3 -m venv venv` | ساخت محیط |
| `source venv/bin/activate` | فعال‌سازی |
| `pip install X` | نصب کتابخانه |
| `pip list` | لیست نصب‌شده |
| `pip freeze > requirements.txt` | ذخیره لیست |
| `deactivate` | غیرفعال‌سازی |

## آماده‌ای؟ برو به `03-first-script.md`.