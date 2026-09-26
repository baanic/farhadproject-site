# اولین اسکریپت Python

## 🎓 مفهوم

هر اسکریپت Python، فایلی با پسوند `.py` است که کد در آن نوشته می‌شود.

## 🛠 گام ۱: ساخت اولین فایل

```bash
cd ~/Documents/Projects/farhadproject/python-scripts
source venv/bin/activate
code hello.py
```

**کد:**

```python
# این یک کامنت است. Python آن را اجرا نمی‌کند.

# چاپ متن
print("سلام دنیا")

# یک متغیر
name = "فرهاد"
print(f"سلام {name}")

# محاسبه
a = 10
b = 20
print(f"جمع: {a + b}")
```

**ذخیره کن.**

## 🛠 گام ۲: اجرا

```bash
python3 hello.py
```

**خروجی:**

```
سلام دنیا
سلام فرهاد
جمع: 30
```

## 🎓 مفاهیم کد بالا

### ۱. کامنت

```python
# این یک کامنت است
```

Python هر چیزی بعد از `#` را نادیده می‌گیرد. برای توضیح کد.

### ۲. `print()`

```python
print("سلام")
```

یک تابع است که چیزی چاپ می‌کند.

### ۳. متغیر

```python
name = "فرهاد"
```

`name` یک **متغیر** است. مقدار `"فرهاد"` را در خود نگه می‌دارد.

### ۴. f-string

```python
print(f"سلام {name}")
```

`f` قبل از رشته یعنی «این یک f-string است». داخل `{}` می‌توانی متغیر بگذاری.

**بدون f-string:**

```python
print("سلام " + name)
```

**با f-string:** کد تمیزتر.

### ۵. عملگرهای ریاضی

| عملگر | کار |
|---|---|
| `+` | جمع |
| `-` | تفریق |
| `*` | ضرب |
| `/` | تقسیم |
| `**` | توان |
| `%` | باقیمانده |

## 🛠 گام ۳: کار با لیست

**List (لیست)** مجموعه‌ای مرتب از آیتم‌ها.

```python
# ساخت لیست
fruits = ["سیب", "موز", "پرتقال"]

# چاپ لیست
print(fruits)

# چاپ اولین آیتم
print(fruits[0])  # سیب

# چاپ آخرین آیتم
print(fruits[-1])  # پرتقال

# تعداد آیتم‌ها
print(len(fruits))  # 3

# اضافه کردن
fruits.append("انگور")
print(fruits)
```

## 🛠 گام ۴: کار با دیکشنری

**Dictionary (دیکشنری)** مجموعه‌ای از **کلید-مقدار**.

```python
# ساخت دیکشنری
person = {
    "name": "فرهاد",
    "age": 30,
    "city": "زاهدان"
}

# دسترسی به مقدار
print(person["name"])  # فرهاد

# اضافه کردن
person["job"] = "مهندس"
print(person)

# حذف
del person["city"]
print(person)
```

## 🛠 گام ۵: حلقه

**for loop:** تکرار روی آیتم‌ها.

```python
fruits = ["سیب", "موز", "پرتقال"]

for fruit in fruits:
    print(fruit)
```

**خروجی:**

```
سیب
موز
پرتقال
```

**روی دیکشنری:**

```python
person = {"name": "فرهاد", "age": 30}

for key, value in person.items():
    print(f"{key}: {value}")
```

**خروجی:**

```
name: فرهاد
age: 30
```

## 🛠 گام ۶: شرط

```python
age = 25

if age >= 18:
    print("بالغ")
else:
    print("کودک")
```

## 🛠 گام ۷: تابع

**تابع** یک بلوک کد قابل استفاده مجدد.

```python
def greet(name):
    return f"سلام {name}"

# استفاده
message = greet("فرهاد")
print(message)  # سلام فرهاد

# استفاده دوباره
print(greet("علی"))  # سلام علی
```

**تابع با مقدار پیش‌فرض:**

```python
def greet(name, greeting="سلام"):
    return f"{greeting} {name}"

print(greet("فرهاد"))               # سلام فرهاد
print(greet("فرهاد", "درود"))       # درود فرهاد
```

## 🛠 گام ۸: کار با فایل

### نوشتن

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("سلام دنیا\n")
    f.write("خط دوم\n")
```

### خواندن

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**نکته:** `encoding="utf-8"` برای پشتیبانی فارسی.

**`with` چیست؟**

یک **Context Manager** است. به‌طور خودکار فایل را می‌بندد. حتی اگر خطایی رخ دهد.

## 🎓 تمرین: یک اسکریپت کامل

```python
# projects.py
projects = [
    {"name": "پروژه A", "area": 5000, "year": 1403},
    {"name": "پروژه B", "area": 3000, "year": 1404},
    {"name": "پروژه C", "area": 8000, "year": 1404},
]

def print_project(project):
    print(f"نام: {project['name']}")
    print(f"مساحت: {project['area']} مترمربع")
    print(f"سال: {project['year']}")
    print("-" * 30)

# چاپ همه پروژه‌ها
for project in projects:
    print_project(project)

# جمع مساحت‌ها
total_area = sum(p["area"] for p in projects)
print(f"جمع مساحت: {total_area} مترمربع")

# فیلتر
recent = [p for p in projects if p["year"] == 1404]
print(f"پروژه‌های جدید: {len(recent)}")
```

## 🎁 خلاصه

| مفهوم | مثال |
|---|---|
| کامنت | `# متن` |
| چاپ | `print("متن")` |
| متغیر | `name = "فرهاد"` |
| f-string | `f"سلام {name}"` |
| لیست | `[1, 2, 3]` |
| دیکشنری | `{"key": "value"}` |
| حلقه | `for x in items:` |
| شرط | `if x > 0:` |
| تابع | `def name():` |
| فایل | `with open(...)` |

## آماده‌ای؟ برو به `04-data-structure.md`.