# -*- coding: utf-8 -*-
"""
Master Data Builder - Media Building Portfolio
نسخه: 0.1.0 (Projects + Spaces)
"""

import json
import pandas as pd
from datetime import datetime

VERSION = "0.1.0"
BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M")

# ============================================================
# شیت ۱: Projects
# ============================================================
PROJECTS = [
    {
        "project_id": "P-001",
        "slug": "media-building-phase1",
        "title_fa": "پروژه تکمیل فاز ۱ ساختمان فنی و اداری",
        "title_en": "Phase 1 Completion of Technical & Administrative Building",
        "subtitle_fa": "تکمیل، تجهیز و تحویل بخش فنی یک مجتمع رسانه‌ای",
        "client_fa": "کارفرمای دولتی / رسانه‌ای",
        "client_en": "Public / Media Client",
        "contractor_fa": "پیمانکار اصلی",
        "consultant_fa": "مشاور",
        "location_fa": "محرمانه",
        "location_en": "Restricted",
        "area_m2": 11000,
        "contract_amount_rial": 1337036052238,
        "contract_amount_display_fa": "حدود ۱۳۳.۷ میلیارد تومان",
        "duration_months": 12,
        "extension_months": 6,
        "total_duration_months": 18,
        "status_fa": "تحویل شده و در بهره‌برداری",
        "status_en": "Delivered & Operational",
        "year_start_fa": "سال اول پروژه",
        "year_end_fa": "سال دوم پروژه",
        "scope_fa": "ابنیه، تأسیسات برقی، تأسیسات مکانیکی، آکوستیک، دکوراسیون",
        "blocks": "A,B1,B2,B3",
        "total_floors": 2,
        "role_fa": "دفتر فنی، کنترل پروژه، متره و برآورد، طراحی و اجرای آکوستیک",
        "role_en": "Technical Office, Project Controls, QS, Acoustic Design & Execution",
        "key_achievements_fa": "تکمیل و تحویل زون‌های کلیدی؛ تولید ۴ استودیو رادیویی و ۱ استودیو تلویزیونی؛ تهیه ریزمتره و صورت‌وضعیت کامل؛ طراحی و اجرای آکوستیک استودیوها",
        "cover_image": "/assets/covers/P-001.jpg",
        "is_public": True,
        "is_featured": True,
    }
]

# ============================================================
# شیت ۲: Spaces (بخش ۲الف - استودیوها و اتاق‌های کنترل)
# ============================================================
SPACES_RAW = [
    # --- استودیوهای رادیویی ---
    {"space_id": "S-001", "name_fa": "استودیو رادیویی A", "name_en": "Radio Studio A", "name_internal": "استودیو رادیویی شماره ۱", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 10.31, "width_m": 6.83, "height_m": 5.40, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-002", "name_fa": "استودیو رادیویی B", "name_en": "Radio Studio B", "name_internal": "استودیو رادیویی شماره ۲", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.91, "width_m": 5.49, "height_m": 4.80, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-003", "name_fa": "استودیو رادیویی C", "name_en": "Radio Studio C", "name_internal": "استودیو رادیویی شماره ۳", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 5.19, "width_m": 3.74, "height_m": 5.40, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-004", "name_fa": "استودیو رادیویی D", "name_en": "Radio Studio D", "name_internal": "استودیو رادیویی شماره ۴", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.77, "width_m": 5.00, "height_m": 5.70, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": True},

    # --- اتاق‌های کنترل رادیویی ---
    {"space_id": "S-005", "name_fa": "اتاق کنترل رادیویی A", "name_en": "Radio Control Room A", "name_internal": "رژی استودیو رادیویی شماره ۱", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 7.95, "width_m": 5.10, "height_m": 5.40, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-006", "name_fa": "اتاق کنترل رادیویی B", "name_en": "Radio Control Room B", "name_internal": "رژی استودیو رادیویی شماره ۲", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.40, "width_m": 4.70, "height_m": 4.80, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-007", "name_fa": "اتاق کنترل رادیویی C", "name_en": "Radio Control Room C", "name_internal": "رژی استودیو رادیویی شماره ۳", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 5.25, "width_m": 3.70, "height_m": 5.40, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-008", "name_fa": "اتاق کنترل رادیویی D", "name_en": "Radio Control Room D", "name_internal": "رژی استودیو رادیویی شماره ۴", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 5.75, "width_m": 5.15, "height_m": 5.70, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": True},

    # --- استودیوهای تلویزیونی ---
    {"space_id": "S-009", "name_fa": "استودیو تلویزیونی A", "name_en": "TV Studio A", "name_internal": "استودیو تلویزیونی شماره ۱", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 20.80, "width_m": 13.70, "height_m": 12.90, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": False},
    {"space_id": "S-010", "name_fa": "استودیو تلویزیونی B", "name_en": "TV Studio B", "name_internal": "استودیو تلویزیونی شماره ۲", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 8.40, "width_m": 5.90, "height_m": 5.80, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-011", "name_fa": "استودیو تلویزیونی C", "name_en": "TV Studio C", "name_internal": "استودیو تلویزیونی شماره ۳", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 14.00, "width_m": 9.60, "height_m": 12.90, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": False},
    {"space_id": "S-012", "name_fa": "استودیو تلویزیونی D", "name_en": "TV Studio D", "name_internal": "استودیو تلویزیونی شماره ۴", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 7.70, "width_m": 5.00, "height_m": 5.70, "acoustic_class": "full", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": False},

    # --- اتاق‌های کنترل تلویزیونی ---
    {"space_id": "S-013", "name_fa": "اتاق کنترل تلویزیونی A", "name_en": "TV Control Room A", "name_internal": "رژی استودیو تلویزیونی شماره ۱", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 11.40, "width_m": 6.65, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": False},
    {"space_id": "S-014", "name_fa": "اتاق کنترل تلویزیونی B", "name_en": "TV Control Room B", "name_internal": "رژی استودیو تلویزیونی شماره ۲", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.00, "width_m": 6.80, "height_m": 5.80, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": True},
    {"space_id": "S-015", "name_fa": "اتاق کنترل تلویزیونی C", "name_en": "TV Control Room C", "name_internal": "رژی استودیو تلویزیونی شماره ۳", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 7.80, "width_m": 6.00, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": False},
    {"space_id": "S-016", "name_fa": "اتاق کنترل تلویزیونی D", "name_en": "TV Control Room D", "name_internal": "رژی استودیو تلویزیونی شماره ۴", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 7.65, "width_m": 4.60, "height_m": 5.70, "acoustic_class": "semi", "has_visor_window": True, "has_airlock": True, "has_silencer": True, "executed": False},

    # --- اتاق‌های پشتیبان ---
    {"space_id": "S-017", "name_fa": "اتاق تجهیزات A", "name_en": "Equipment Room A", "name_internal": "ماشین روم (رژی رادیویی ۱)", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 5.25, "width_m": 2.80, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-018", "name_fa": "اتاق تجهیزات B", "name_en": "Equipment Room B", "name_internal": "ماشین روم (رژی رادیویی ۲)", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.74, "width_m": 2.67, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-019", "name_fa": "اتاق تجهیزات C", "name_en": "Equipment Room C", "name_internal": "ماشین روم (رژی تلویزیونی ۲)", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.70, "width_m": 2.80, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-020", "name_fa": "اتاق ارتباط مایکروویو", "name_en": "Microwave Room", "name_internal": "ماکروویو", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.55, "width_m": 3.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-021", "name_fa": "اتاق دیمر", "name_en": "Dimmer Room", "name_internal": "دیمر", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 4.55, "width_m": 3.10, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": False},
    {"space_id": "S-022", "name_fa": "اتاق بازشنوایی", "name_en": "Listening Room", "name_internal": "اتاق بازشنوایی", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 4.00, "width_m": 3.50, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": False},

    # --- اتاق‌های ادیت ---
    {"space_id": "S-023", "name_fa": "اتاق ادیت A", "name_en": "Edit Room A", "name_internal": "تدوین و مونتاژ", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.60, "width_m": 3.00, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-024", "name_fa": "اتاق ادیت B", "name_en": "Edit Room B", "name_internal": "تدوین ۱", "block": "A", "floor": "همکف", "zone": "شمالی", "length_m": 3.00, "width_m": 3.35, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-025", "name_fa": "اتاق ادیت C", "name_en": "Edit Room C", "name_internal": "تدوین ۲", "block": "A", "floor": "همکف", "zone": "شمالی", "length_m": 3.00, "width_m": 3.35, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-026", "name_fa": "اتاق ادیت D", "name_en": "Edit Room D", "name_internal": "ادیت ۴", "block": "A", "floor": "همکف", "zone": "جنوبی", "length_m": 3.80, "width_m": 2.40, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-027", "name_fa": "اتاق ادیت E", "name_en": "Edit Room E", "name_internal": "ادیت ۲", "block": "A", "floor": "همکف", "zone": "جنوبی", "length_m": 3.90, "width_m": 2.95, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های فنی ویژه ---
    {"space_id": "S-028", "name_fa": "اتاق فنی ویژه ۱", "name_en": "Special Technical Room 1", "name_internal": "MCR", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 6.00, "width_m": 4.00, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": True, "has_silencer": True, "executed": False},
    {"space_id": "S-029", "name_fa": "اتاق فنی ویژه ۲", "name_en": "Special Technical Room 2", "name_internal": "STM-1", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 10.90, "width_m": 5.63, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": False},
    {"space_id": "S-030", "name_fa": "اتاق فنی سوئیچ", "name_en": "Technical Switch Room", "name_internal": "نودال", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.70, "width_m": 3.30, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-031", "name_fa": "اتاق پشتیبان سرور", "name_en": "Server Support Room", "name_internal": "سرور روم", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 11.50, "width_m": 5.30, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-032", "name_fa": "اتاق برق و اطفا", "name_en": "Power & Fire Room", "name_internal": "اتاق برق و اطفا", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.80, "width_m": 2.70, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

        # ============================================================
    # بخش ۲ب: اتاق‌های اداری، فنی و پشتیبان
    # ============================================================

    # --- اتاق‌های اداری فنی بلوک B2 - همکف (۱ تا ۱۶) ---
    {"space_id": "S-033", "name_fa": "اداری فنی ۱", "name_en": "Technical Office 1", "name_internal": "اداری فنی ۱ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.60, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-034", "name_fa": "اداری فنی ۲", "name_en": "Technical Office 2", "name_internal": "اداری فنی ۲ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.00, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-035", "name_fa": "اداری فنی ۳", "name_en": "Technical Office 3", "name_internal": "اداری فنی ۳ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.80, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-036", "name_fa": "اداری فنی ۴", "name_en": "Technical Office 4", "name_internal": "اداری فنی ۴ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.15, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-037", "name_fa": "اداری فنی ۵", "name_en": "Technical Office 5", "name_internal": "اداری فنی ۵ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.05, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-038", "name_fa": "اداری فنی ۶", "name_en": "Technical Office 6", "name_internal": "اداری فنی ۶ (سمت راست)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.80, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-039", "name_fa": "اداری فنی ۷", "name_en": "Technical Office 7", "name_internal": "اداری فنی ۷ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.08, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-040", "name_fa": "اداری فنی ۸", "name_en": "Technical Office 8", "name_internal": "اداری فنی ۸ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.80, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-041", "name_fa": "اداری فنی ۹", "name_en": "Technical Office 9", "name_internal": "اداری فنی ۹ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.05, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-042", "name_fa": "اداری فنی ۱۰", "name_en": "Technical Office 10", "name_internal": "اداری فنی ۱۰ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.60, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-043", "name_fa": "اداری فنی ۱۱", "name_en": "Technical Office 11", "name_internal": "اداری فنی ۱۱ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 4.78, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-044", "name_fa": "اداری فنی ۱۲", "name_en": "Technical Office 12", "name_internal": "اداری فنی ۱۲ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 4.65, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-045", "name_fa": "اداری فنی ۱۳", "name_en": "Technical Office 13", "name_internal": "اداری فنی ۱۳ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 4.15, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-046", "name_fa": "اداری فنی ۱۴", "name_en": "Technical Office 14", "name_internal": "اداری فنی ۱۴ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 3.80, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-047", "name_fa": "اداری فنی ۱۵", "name_en": "Technical Office 15", "name_internal": "اداری فنی ۱۵ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 5.08, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-048", "name_fa": "اداری فنی ۱۶", "name_en": "Technical Office 16", "name_internal": "اداری فنی ۱۶ (سمت چپ)", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 3.92, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های اداری بلوک B2 - طبقه اول - بال شمالی ---
    {"space_id": "S-049", "name_fa": "اداری ۱ بال شمالی", "name_en": "Office 1 - North Wing", "name_internal": "اداری ۱ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 3.83, "width_m": 3.18, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-051", "name_fa": "اداری ۳ بال شمالی", "name_en": "Office 3 - North Wing", "name_internal": "اداری ۳ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 3.80, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-052", "name_fa": "اداری ۴ بال شمالی", "name_en": "Office 4 - North Wing", "name_internal": "اداری ۴ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 4.05, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-053", "name_fa": "اداری ۵ بال شمالی", "name_en": "Office 5 - North Wing", "name_internal": "اداری ۵ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 4.65, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-054", "name_fa": "اداری ۶ بال شمالی", "name_en": "Office 6 - North Wing", "name_internal": "اداری ۶ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 4.60, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-055", "name_fa": "اداری ۷ بال شمالی", "name_en": "Office 7 - North Wing", "name_internal": "اداری ۱ - ضلع شمالی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.20, "width_m": 4.65, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-056", "name_fa": "اداری ۸ بال شمالی", "name_en": "Office 8 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 4.05, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-057", "name_fa": "اداری ۹ بال شمالی", "name_en": "Office 9 - North Wing", "name_internal": "اداری ۳ - ضلع شمالی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 3.80, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-058", "name_fa": "اداری ۱۰ بال شمالی", "name_en": "Office 10 - North Wing", "name_internal": "اداری ۴ - ضلع شمالی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-059", "name_fa": "اداری ۱۱ بال شمالی", "name_en": "Office 11 - North Wing", "name_internal": "اداری ۵ - ضلع شمالی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 3.90, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های اداری بلوک B2 - طبقه اول - بال جنوبی ---
    {"space_id": "S-060", "name_fa": "اداری ۱ بال جنوبی", "name_en": "Office 1 - South Wing", "name_internal": "اداری ۱ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 3.83, "width_m": 3.18, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-061", "name_fa": "اداری ۲ بال جنوبی", "name_en": "Office 2 - South Wing", "name_internal": "اداری ۲ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-062", "name_fa": "اداری ۳ بال جنوبی", "name_en": "Office 3 - South Wing", "name_internal": "اداری ۳ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 3.80, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-063", "name_fa": "اداری ۴ بال جنوبی", "name_en": "Office 4 - South Wing", "name_internal": "اداری ۴ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 4.05, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-064", "name_fa": "اداری ۵ بال جنوبی", "name_en": "Office 5 - South Wing", "name_internal": "اداری ۵ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 4.65, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-065", "name_fa": "اداری ۶ بال جنوبی", "name_en": "Office 6 - South Wing", "name_internal": "اداری ۶ - ضلع جنوبی - راست", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 4.60, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-066", "name_fa": "اداری ۷ بال جنوبی", "name_en": "Office 7 - South Wing", "name_internal": "اداری ۱ - ضلع جنوبی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 5.20, "width_m": 4.65, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-067", "name_fa": "اداری ۸ بال جنوبی", "name_en": "Office 8 - South Wing", "name_internal": "اداری ۲ - ضلع جنوبی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 4.05, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-068", "name_fa": "اداری ۹ بال جنوبی", "name_en": "Office 9 - South Wing", "name_internal": "اداری ۳ - ضلع جنوبی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 3.80, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-069", "name_fa": "اداری ۱۰ بال جنوبی", "name_en": "Office 10 - South Wing", "name_internal": "اداری ۴ - ضلع جنوبی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-070", "name_fa": "اداری ۱۱ بال جنوبی", "name_en": "Office 11 - South Wing", "name_internal": "اداری ۵ - ضلع جنوبی - چپ", "block": "B2", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 3.90, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True, "display_group": "offices-floor1-22"},    {"space_id": "S-050", "name_fa": "اداری ۲ بال شمالی", "name_en": "Office 2 - North Wing", "name_internal": "اداری ۲ - ضلع شمالی - راست", "block": "B2", "floor": "طبقه اول", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های تخصصی ---
    {"space_id": "S-071", "name_fa": "اتاق کامپیوتر", "name_en": "Computer Room", "name_internal": "کامپیوتر", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.70, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-072", "name_fa": "اتاق نرم‌افزار", "name_en": "Software Room", "name_internal": "نرم افزار", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.62, "width_m": 4.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-073", "name_fa": "اتاق سخت‌افزار", "name_en": "Hardware Room", "name_internal": "سخت افزار", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.95, "width_m": 2.73, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-074", "name_fa": "انبار کامپیوتر", "name_en": "IT Storage", "name_internal": "انبار کامپیوتر", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.30, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-075", "name_fa": "مرکز تلفن", "name_en": "Telephone Center", "name_internal": "مرکز تلفن", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.70, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-076", "name_fa": "اتاق کارشناسی", "name_en": "Expert Room", "name_internal": "کارشناسی STM1", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 5.18, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": False},
    {"space_id": "S-077", "name_fa": "تایپ و تلکس", "name_en": "Typing & Telex", "name_internal": "تایپ و تلکس", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.62, "width_m": 3.55, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-078", "name_fa": "اتاق ارتباطات رادیویی", "name_en": "Radio Communication Room", "name_internal": "اتاق بیسیم", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.65, "width_m": 2.50, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- تعمیرگاه‌های فنی ---
    {"space_id": "S-079", "name_fa": "تعمیرگاه فنی ۱", "name_en": "Technical Workshop 1", "name_internal": "تعمیرگاه فنی ۱", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.15, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-080", "name_fa": "تعمیرگاه فنی ۲", "name_en": "Technical Workshop 2", "name_internal": "تعمیرگاه فنی ۲", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.80, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-081", "name_fa": "تعمیرگاه فنی ۳", "name_en": "Technical Workshop 3", "name_internal": "تعمیرگاه فنی ۳", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 5.08, "width_m": 4.23, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- آرشیوها ---
    {"space_id": "S-082", "name_fa": "اتاق مدیر آرشیو", "name_en": "Archive Manager Room", "name_internal": "مدیر آرشیو", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 5.90, "width_m": 4.55, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-083", "name_fa": "اتاق مدیر آرشیو دوم", "name_en": "Archive Manager Room 2", "name_internal": "مدیر آرشیو (دوم)", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 4.35, "width_m": 3.30, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-084", "name_fa": "آرشیو ویژه ۱", "name_en": "Special Archive 1", "name_internal": "آرشیو محرمانه", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 7.83, "width_m": 2.18, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-085", "name_fa": "آرشیو تصویری A", "name_en": "Visual Archive A", "name_internal": "آرشیو تصویر ۱", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 5.10, "width_m": 8.40, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-086", "name_fa": "آرشیو تصویری B", "name_en": "Visual Archive B", "name_internal": "آرشیو تصویر ۲", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 2.90, "width_m": 3.73, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-087", "name_fa": "آرشیو صوتی", "name_en": "Audio Archive", "name_internal": "آرشیو رادیویی", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 7.45, "width_m": 6.08, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-088", "name_fa": "انبار ملزومات", "name_en": "Supplies Storage", "name_internal": "انبار ملزومات", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 9.60, "width_m": 3.75, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-089", "name_fa": "انبار", "name_en": "Storage", "name_internal": "انبار", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 8.23, "width_m": 7.70, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های گریم ---
    {"space_id": "S-090", "name_fa": "اتاق گریم بانوان", "name_en": "Female Makeup Room", "name_internal": "اتاق گریم زنانه", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 4.27, "width_m": 3.50, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-091", "name_fa": "اتاق گریم آقایان", "name_en": "Male Makeup Room", "name_internal": "اتاق گریم مردانه", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 4.27, "width_m": 3.50, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های تأسیسات ---
    {"space_id": "S-092", "name_fa": "اتاق مدیر تأسیسات", "name_en": "Facilities Manager Room", "name_internal": "مدیر تاسیسات", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 3.00, "width_m": 3.30, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-093", "name_fa": "اتاق پرسنل تأسیسات", "name_en": "Facilities Staff Room", "name_internal": "پرسنل تاسیسات", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 6.80, "width_m": 3.30, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- تحریریه خبر ---
    {"space_id": "S-094", "name_fa": "تحریریه خبر", "name_en": "Newsroom", "name_internal": "تحریریه خبر", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 7.15, "width_m": 5.63, "height_m": 4.60, "acoustic_class": "semi", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- کافه کتاب ---
    {"space_id": "S-095", "name_fa": "کافه کتاب", "name_en": "Book Cafe", "name_internal": "کافه کتاب", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 115.20, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- لابراتوار و انبار STM1 ---
    {"space_id": "S-096", "name_fa": "آزمایشگاه و انبار فنی", "name_en": "Technical Lab & Storage", "name_internal": "لابراتوار و انبار STM1", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 4.30, "width_m": 4.22, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": False},

    # --- اتاق برق B2 ---
    {"space_id": "S-097", "name_fa": "اتاق برق B2", "name_en": "Power Room B2", "name_internal": "اتاق برق B2", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 3.80, "width_m": 2.40, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
        # ============================================================
    # بخش ۲ج: راهروها، لابی، سرویس‌ها، تونل‌ها و محوطه
    # ============================================================

    # --- راهروهای بلوک A ---
    {"space_id": "S-098", "name_fa": "راهرو شمالی A", "name_en": "North Corridor A", "name_internal": "راهرو شمالی بلوک A", "block": "A", "floor": "همکف", "zone": "شمالی", "length_m": 35.00, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-099", "name_fa": "راهرو جنوبی A", "name_en": "South Corridor A", "name_internal": "راهرو جنوبی بلوک A", "block": "A", "floor": "همکف", "zone": "جنوبی", "length_m": 31.50, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-100", "name_fa": "راهرو شرقی A", "name_en": "East Corridor A", "name_internal": "راهرو شرقی بلوک A", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 32.85, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-101", "name_fa": "راهرو غربی A", "name_en": "West Corridor A", "name_internal": "راهرو غربی بلوک A", "block": "A", "floor": "همکف", "zone": "غربی", "length_m": 30.50, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-102", "name_fa": "راهرو جنوب شرقی A", "name_en": "Southeast Corridor A", "name_internal": "راهرو جنوب شرقی بلوک A", "block": "A", "floor": "همکف", "zone": "جنوب شرقی", "length_m": 10.64, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-103", "name_fa": "راهرو جنوب غربی A", "name_en": "Southwest Corridor A", "name_internal": "راهرو جنوب غربی بلوک A", "block": "A", "floor": "همکف", "zone": "جنوب غربی", "length_m": 27.27, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-104", "name_fa": "راهرو طبقه اول A", "name_en": "First Floor Corridor A", "name_internal": "راهرو طبقه اول بلوک A", "block": "A", "floor": "طبقه اول", "zone": "مرکزی", "length_m": 191.00, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- لابی و استراحت ---
    {"space_id": "S-105", "name_fa": "لابی استراحت فنی", "name_en": "Technical Lounge", "name_internal": "استراحت افراد فنی", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 17.20, "width_m": 5.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- ورودی بخش فنی ---
    {"space_id": "S-106", "name_fa": "ورودی بخش فنی", "name_en": "Technical Section Entrance", "name_internal": "ورودی بخش فنی", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 33.00, "width_m": 2.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق پایش امنیتی ---
    {"space_id": "S-107", "name_fa": "اتاق پایش امنیتی", "name_en": "Security Monitoring Room", "name_internal": "مونیتورینگ حراست", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 9.55, "width_m": 3.68, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- آبدارخانه‌ها ---
    {"space_id": "S-108", "name_fa": "آبدارخانه شمالی", "name_en": "North Pantry", "name_internal": "آبدارخانه شمالی", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 2.66, "width_m": 3.75, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-109", "name_fa": "آبدارخانه جنوبی", "name_en": "South Pantry", "name_internal": "آبدارخانه جنوبی", "block": "B2", "floor": "همکف", "zone": "جنوبی", "length_m": 2.66, "width_m": 3.75, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-110", "name_fa": "آبدارخانه B1", "name_en": "Pantry B1", "name_internal": "آبدارخانه بلوک B1", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 2.66, "width_m": 3.75, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- سرویس‌های بهداشتی ---
    {"space_id": "S-111", "name_fa": "سرویس بهداشتی A همکف", "name_en": "Restroom A - Ground Floor", "name_internal": "سرویس بلوک A طبقه همکف", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 3.35, "width_m": 3.10, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-112", "name_fa": "سرویس بهداشتی A طبقه اول", "name_en": "Restroom A - First Floor", "name_internal": "سرویس بلوک A طبقه اول", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 3.35, "width_m": 3.10, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-113", "name_fa": "سرویس عمومی B3", "name_en": "Public Restroom B3", "name_internal": "سرویس عمومی بلوک B3", "block": "B3", "floor": "همکف", "zone": "مرکزی", "length_m": 19.40, "width_m": 2.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- پله‌ها ---
    {"space_id": "S-114", "name_fa": "راه‌پله ورودی A", "name_en": "Entrance Staircase A", "name_internal": "راه پله بلوک A", "block": "A", "floor": "همکف", "zone": "شرقی", "length_m": 5.70, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-115", "name_fa": "ورودی پله طبقه اول A", "name_en": "First Floor Stair Entrance A", "name_internal": "ورودی پله طبقه اول بلوک A", "block": "A", "floor": "طبقه اول", "zone": "شرقی", "length_m": 7.60, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- تونل تأسیسات ---
    {"space_id": "S-116", "name_fa": "تونل تأسیسات شمالی", "name_en": "North MEP Tunnel", "name_internal": "تونل تأسیسات ضلع شمالی", "block": "A", "floor": "طبقه اول", "zone": "شمالی", "length_m": 25.60, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-117", "name_fa": "تونل تأسیسات جنوبی", "name_en": "South MEP Tunnel", "name_internal": "تونل تأسیسات ضلع جنوبی", "block": "A", "floor": "طبقه اول", "zone": "جنوبی", "length_m": 25.60, "width_m": 2.20, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- سالن گریم و اتاق‌های مرتبط ---
    {"space_id": "S-118", "name_fa": "سالن گریم", "name_en": "Makeup Hall", "name_internal": "سالن گریم", "block": "B2", "floor": "همکف", "zone": "شمالی", "length_m": 56.00, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- اتاق‌های کنار تحریریه ---
    {"space_id": "S-119", "name_fa": "اتاق‌های کنار تحریریه", "name_en": "Newsroom Side Rooms", "name_internal": "اتاقک های کنار تحریریه خبر", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 9.21, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-120", "name_fa": "ورودی تحریریه", "name_en": "Newsroom Entrance", "name_internal": "ورودی تحریریه خبر", "block": "B1", "floor": "همکف", "zone": "مرکزی", "length_m": 8.30, "width_m": 1.00, "height_m": 4.60, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},

    # --- محوطه B3 ---
    {"space_id": "S-121", "name_fa": "محوطه بلوک تحریریه", "name_en": "Newsroom Block Yard", "name_internal": "محوطه بلوک B3", "block": "B3", "floor": "همکف", "zone": "مرکزی", "length_m": 15.00, "width_m": 6.00, "height_m": 0.00, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    {"space_id": "S-122", "name_fa": "فضای سبز B3", "name_en": "B3 Green Space", "name_internal": "محوطه فضای سبز B3", "block": "B3", "floor": "همکف", "zone": "مرکزی", "length_m": 25.00, "width_m": 8.00, "height_m": 0.00, "acoustic_class": "none", "has_visor_window": False, "has_airlock": False, "has_silencer": False, "executed": True},
    
]
# ============================================================
# شیت ۳: Acoustic_Layers - لایه‌بندی دیوار و سقف استودیوها
# ============================================================
ACOUSTIC_LAYERS = [
    # --- لایه‌بندی دیوار استودیوهای رادیویی (نوع ۱) ---
    {"layer_id": "AL-001", "space_id": "S-001", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس دوجداره + پشم سنگ میانی", "spec_fa": "هبلکس ۲۰ سانتی + عایق ۱۰ سانتی + هبلکس ۲۰ سانتی", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون صوتی"},
    {"layer_id": "AL-002", "space_id": "S-001", "element": "دیوار", "layer_order": 1, "material_fa": "استخوان‌بندی فولادی", "spec_fa": "پروفیل فولادی ۳۰×۳۰ با شبکه ۱۲۵×۶۳", "thickness_cm": 3, "density_kg_m3": None, "function_fa": "شاسی‌کشی"},
    {"layer_id": "AL-003", "space_id": "S-001", "element": "دیوار", "layer_order": 2, "material_fa": "ایزولاسیون صوتی", "spec_fa": "پشم سنگ تخته‌ای دانسیته ۸۰، ضخامت ۱۰ سانتی‌متر", "thickness_cm": 10, "density_kg_m3": 80, "function_fa": "جذب و ایزولاسیون صدا"},
    {"layer_id": "AL-004", "space_id": "S-001", "element": "دیوار", "layer_order": 3, "material_fa": "زیرسازی چوبی", "spec_fa": "چوب روسی عمودی، عرض ۵ سانت، ضخامت ۲۲ میلی‌متر، فاصله ۶۰ سانت", "thickness_cm": 2.2, "density_kg_m3": None, "function_fa": "زیرسازی فینیشینگ"},
    {"layer_id": "AL-005", "space_id": "S-001", "element": "دیوار", "layer_order": 4, "material_fa": "تأسیسات پنهان", "spec_fa": "لوله ۴ اینچ S-Shape زیر ویزور، تراز +۱۵۰ برای اسپیکر", "thickness_cm": None, "density_kg_m3": None, "function_fa": "تأسیسات صوتی و برق"},
    {"layer_id": "AL-006", "space_id": "S-001", "element": "دیوار", "layer_order": 5, "material_fa": "ازاره MDF شیاردار", "spec_fa": "MDF ازاره تا ارتفاع ۱۲۰ سانتی با شیارهای عمودی ۵ سانتی، کد T107", "thickness_cm": 8, "density_kg_m3": None, "function_fa": "فینیشینگ و جذب"},
    {"layer_id": "AL-007", "space_id": "S-001", "element": "دیوار", "layer_order": 6, "material_fa": "پارچه دیواری فوقانی", "spec_fa": "نساج پایا کد ۲۱-۴۲۴ با اسفنج زیرین", "thickness_cm": 1, "density_kg_m3": None, "function_fa": "فینیشینگ و جذب صدا"},

    # --- لایه‌بندی سقف استودیوهای رادیویی ---
    {"layer_id": "AL-008", "space_id": "S-001", "element": "سقف", "layer_order": 0, "material_fa": "شاسی‌کشی فولادی", "spec_fa": "پروفیل‌های فولادی با شبکه ۶۰×۶۰ یا ۶۳×۱۲۳", "thickness_cm": 3, "density_kg_m3": None, "function_fa": "شاسی‌کشی"},
    {"layer_id": "AL-009", "space_id": "S-001", "element": "سقف", "layer_order": 1, "material_fa": "زیرسازی چوبی", "spec_fa": "چوب روسی عرض ۵، ضخامت ۲ سانت با فواصل ۶۰ سانت", "thickness_cm": 2, "density_kg_m3": None, "function_fa": "زیرسازی"},
    {"layer_id": "AL-010", "space_id": "S-001", "element": "سقف", "layer_order": 2, "material_fa": "MDF پانچ‌شده", "spec_fa": "MDF ضخامت ۸ میلی‌متر پانچ‌شده", "thickness_cm": 0.8, "density_kg_m3": None, "function_fa": "لایه واسط جذب صدا"},
    {"layer_id": "AL-011", "space_id": "S-001", "element": "سقف", "layer_order": 3, "material_fa": "وول‌پنل نورس‌پنل", "spec_fa": "وول‌پنل کد NP03 طوسی روشن در شبکه ۶۰×۱۲۰", "thickness_cm": 2, "density_kg_m3": None, "function_fa": "لایه نهایی جذب صدا"},
    {"layer_id": "AL-012", "space_id": "S-001", "element": "سقف", "layer_order": 4, "material_fa": "MDF دکوراتیو", "spec_fa": "MDF ۸ میلی‌متری هم‌رنگ T107 دور پنل‌های روشنایی و دریچه‌های هوا", "thickness_cm": 0.8, "density_kg_m3": None, "function_fa": "دکوراسیون"},

    # --- لایه‌بندی مشترک برای سایر استودیوها (نمونه فشرده) ---
    {"layer_id": "AL-013", "space_id": "S-002", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-014", "space_id": "S-003", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-015", "space_id": "S-004", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-016", "space_id": "S-009", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-017", "space_id": "S-010", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-018", "space_id": "S-011", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
    {"layer_id": "AL-019", "space_id": "S-012", "element": "دیوار", "layer_order": 0, "material_fa": "هبلکس + پشم سنگ", "spec_fa": "هبلکس ۲۰ + عایق ۱۰ + هبلکس ۲۰", "thickness_cm": 50, "density_kg_m3": 80, "function_fa": "سازه + ایزولاسیون"},
]
# ============================================================
# شیت ۴: Acoustic_Doors - درب‌های آکوستیک و نیمه‌آکوستیک
# ============================================================
ACOUSTIC_DOORS = [
    # --- درب‌های تمام آکوستیک استودیوهای رادیویی ---
    {"door_id": "AD-001", "space_id": "S-001", "name_fa": "درب ورودی استودیو رادیویی A", "door_type": "full_acoustic", "count": 3, "width_m": 1.35, "height_m": 2.13, "frame_material_fa": "چوب ماسیو روسی", "leaf_thickness_cm": 8, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "روکش چرمی با لبه‌های چوب طبیعی"},
    {"door_id": "AD-002", "space_id": "S-002", "name_fa": "درب ورودی استودیو رادیویی B", "door_type": "full_acoustic", "count": 2, "width_m": 1.20, "height_m": 2.13, "frame_material_fa": "چوب ماسیو روسی", "leaf_thickness_cm": 8, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "روکش چرمی با لبه‌های چوب طبیعی"},
    {"door_id": "AD-003", "space_id": "S-003", "name_fa": "درب ورودی استودیو رادیویی C", "door_type": "full_acoustic", "count": 2, "width_m": 1.20, "height_m": 2.13, "frame_material_fa": "چوب ماسیو روسی", "leaf_thickness_cm": 8, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "روکش چرمی با لبه‌های چوب طبیعی"},
    {"door_id": "AD-004", "space_id": "S-004", "name_fa": "درب ورودی استودیو رادیویی D", "door_type": "full_acoustic", "count": 2, "width_m": 1.20, "height_m": 2.13, "frame_material_fa": "چوب ماسیو روسی", "leaf_thickness_cm": 8, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "روکش چرمی با لبه‌های چوب طبیعی"},
    {"door_id": "AD-005", "space_id": "S-010", "name_fa": "درب ورودی استودیو تلویزیونی B", "door_type": "full_acoustic", "count": 1, "width_m": 1.20, "height_m": 2.13, "frame_material_fa": "چوب ماسیو روسی", "leaf_thickness_cm": 8, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "روکش چرمی با لبه‌های چوب طبیعی"},

    # --- درب‌های نیمه‌آکوستیک اتاق‌های کنترل ---
    {"door_id": "AD-006", "space_id": "S-005", "name_fa": "درب اتاق کنترل رادیویی A", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "چهارچوب فلزی با نوار درزگیر فشاری"},
    {"door_id": "AD-007", "space_id": "S-006", "name_fa": "درب اتاق کنترل رادیویی B", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "چهارچوب فلزی با نوار درزگیر فشاری"},
    {"door_id": "AD-008", "space_id": "S-007", "name_fa": "درب اتاق کنترل رادیویی C", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "چهارچوب فلزی با نوار درزگیر فشاری"},
    {"door_id": "AD-009", "space_id": "S-008", "name_fa": "درب اتاق کنترل رادیویی D", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "چهارچوب فلزی با نوار درزگیر فشاری"},
    {"door_id": "AD-010", "space_id": "S-014", "name_fa": "درب اتاق کنترل تلویزیونی B", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "چهارچوب فلزی با نوار درزگیر فشاری"},

    # --- درب‌های نیمه‌آکوستیک اتاق‌های ادیت و بازشنوایی ---
    {"door_id": "AD-011", "space_id": "S-023", "name_fa": "درب اتاق ادیت A", "door_type": "semi_acoustic", "count": 2, "width_m": 0.95, "height_m": 2.10, "frame_material_fa": "چهارچوب چوبی", "leaf_thickness_cm": 4, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "درب نیمه‌آکوستیک با بادخور"},
    {"door_id": "AD-012", "space_id": "S-022", "name_fa": "درب اتاق بازشنوایی", "door_type": "semi_acoustic", "count": 3, "width_m": 0.95, "height_m": 2.10, "frame_material_fa": "چهارچوب چوبی", "leaf_thickness_cm": 4, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "درب نیمه‌آکوستیک با بادخور"},

    # --- درب‌های نیمه‌آکوستیک اتاق‌های فنی ویژه ---
    {"door_id": "AD-013", "space_id": "S-028", "name_fa": "درب اتاق فنی ویژه ۱", "door_type": "semi_acoustic", "count": 1, "width_m": 0.88, "height_m": 2.13, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": True, "cover_fa": "درب فلزی با دستگیره پانیک بار"},

    # --- درب‌های اتاق پشتیبان سرور ---
    {"door_id": "AD-014", "space_id": "S-031", "name_fa": "درب اتاق پشتیبان سرور - مانیتورینگ", "door_type": "semi_acoustic", "count": 1, "width_m": 0.89, "height_m": 2.10, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "درب نیمه‌آکوستیک فلزی"},
    {"door_id": "AD-015", "space_id": "S-030", "name_fa": "درب اتاق فنی سوئیچ", "door_type": "semi_acoustic", "count": 1, "width_m": 0.89, "height_m": 2.10, "frame_material_fa": "فلزی", "leaf_thickness_cm": 5, "has_gasket": True, "has_threshold": True, "has_panic_bar": False, "cover_fa": "درب نیمه‌آکوستیک فلزی"},
]
# ============================================================
# شیت ۵: Acoustic_Details - جزئیات اجرایی آکوستیک
# ============================================================
ACOUSTIC_DETAILS = [
    {"detail_id": "ADT-001", "space_id": "S-001", "category": "پنجره ویزور", "name_fa": "پنجره ویزور بین استودیو و رژی", "spec_fa": "شیشه زاویه‌دار با تزریق گاز آرگون، قاب MDF گردویی T107", "dimensions_fa": "شروع از تراز ۱۲۰ سانتی‌متر (بالای ازاره)", "notes_fa": "لبه پنجره هم‌تراز با بالای ازاره"},
    {"detail_id": "ADT-002", "space_id": "S-001", "category": "تأسیسات صوتی", "name_fa": "سیستم صوت و مانیتورینگ", "spec_fa": "۴ خط لوله برق در دو طرف پنجره ویزور، تراز +۱۵۰ از زیر قرنیز", "dimensions_fa": "اسپیکرهای Yamaha HS8 سری سفید", "notes_fa": "برای مانیتورینگ صدای استودیو"},
    {"detail_id": "ADT-003", "space_id": "S-001", "category": "روشنایی سیگنال", "name_fa": "چراغ On Air", "spec_fa": "چراغ قرمز/سبز سردرب، ۱۰ سانتی‌متر بالاتر از تراز فوقانی پنجره ویزور", "dimensions_fa": "۱۰ سانتی‌متر", "notes_fa": "برای نمایش وضعیت پخش"},
    {"detail_id": "ADT-004", "space_id": "S-001", "category": "تهویه", "name_fa": "سایلنسر کانال هوا", "spec_fa": "نصب سایلنسر در مسیر کانال‌های هوا جهت جلوگیری از انتقال صدای فن", "dimensions_fa": None, "notes_fa": "برای کنترل صدای HVAC"},
    {"detail_id": "ADT-005", "space_id": "S-001", "category": "ترنچ و کابل‌کشی", "name_fa": "ترنچ S شکل", "spec_fa": "لوله سایز ۴ اینچ به شکل S در انتهای ترنچ", "dimensions_fa": "۴ اینچ", "notes_fa": "عبور کابل‌های صدا و شبکه"},
    {"detail_id": "ADT-006", "space_id": "S-001", "category": "ایرلاک صوتی", "name_fa": "سیستم ایرلاک", "spec_fa": "درب‌های دوجداره + فیلتر ورودی + لایه‌های سنگین دیوار", "dimensions_fa": None, "notes_fa": "نویز خارجی را به صفر می‌رساند"},
    {"detail_id": "ADT-007", "space_id": "S-001", "category": "روشنایی سقفی", "name_fa": "چراغ‌های ۶۰×۶۰ سقفی", "spec_fa": "مدل M521SLED2865-W مازی‌نور در شبکه سقف", "dimensions_fa": "۶۰×۶۰", "notes_fa": "روشنایی یکنواخت سقف"},
    {"detail_id": "ADT-008", "space_id": "S-005", "category": "پریز و کف‌خواب", "name_fa": "پریزهای توکار و کف‌خواب", "spec_fa": "پریزهای توکار برند لگراند روی ازاره + محفظه‌های خروج کابل Cat6 در کف", "dimensions_fa": "Floor Boxes", "notes_fa": "برای اتصالات صوتی و شبکه"},
    {"detail_id": "ADT-009", "space_id": "S-001", "category": "درز انقطاع", "name_fa": "درز انقطاع سازه", "spec_fa": "پروفیل آلومینیوم آنودایز شده و لاستیک، رنگ لاستیک طوسی و مشکی", "dimensions_fa": None, "notes_fa": "در کف، دیوار، نما و کنج"},
]
# ============================================================
# شیت ۶: Doors - درب‌های چوبی، فلزی و ABS
# ============================================================
DOORS = [
    # --- درب‌های چوبی اداری فنی B2 (ED-01 تا ED-16) ---
    {"door_id": "D-001", "space_id": "S-033", "door_code": "ED-01", "name_fa": "درب اداری فنی ۱", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-002", "space_id": "S-034", "door_code": "ED-02", "name_fa": "درب اداری فنی ۲", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-003", "space_id": "S-035", "door_code": "ED-03", "name_fa": "درب اداری فنی ۳", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-004", "space_id": "S-036", "door_code": "ED-04", "name_fa": "درب اداری فنی ۴", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-005", "space_id": "S-037", "door_code": "ED-05", "name_fa": "درب اداری فنی ۵", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-006", "space_id": "S-038", "door_code": "ED-06", "name_fa": "درب اداری فنی ۶", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.13, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-007", "space_id": "S-039", "door_code": "ED-07", "name_fa": "درب اداری فنی ۷", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-008", "space_id": "S-040", "door_code": "ED-08", "name_fa": "درب اداری فنی ۸", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-009", "space_id": "S-041", "door_code": "ED-09", "name_fa": "درب اداری فنی ۹", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-010", "space_id": "S-042", "door_code": "ED-10", "name_fa": "درب اداری فنی ۱۰", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-011", "space_id": "S-043", "door_code": "ED-11", "name_fa": "درب اداری فنی ۱۱", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-012", "space_id": "S-044", "door_code": "ED-12", "name_fa": "درب اداری فنی ۱۲", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.13, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-013", "space_id": "S-045", "door_code": "ED-13", "name_fa": "درب اداری فنی ۱۳", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-014", "space_id": "S-046", "door_code": "ED-14", "name_fa": "درب اداری فنی ۱۴", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-015", "space_id": "S-047", "door_code": "ED-15", "name_fa": "درب اداری فنی ۱۵", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-016", "space_id": "S-048", "door_code": "ED-16", "name_fa": "درب اداری فنی ۱۶", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های چوبی اداری طبقه اول (ED-17 تا ED-38) ---
    {"door_id": "D-017", "space_id": "S-049", "door_code": "ED-17", "name_fa": "درب اداری ۱ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.09, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-018", "space_id": "S-050", "door_code": "ED-18", "name_fa": "درب اداری ۲ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-019", "space_id": "S-051", "door_code": "ED-19", "name_fa": "درب اداری ۳ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-020", "space_id": "S-052", "door_code": "ED-20", "name_fa": "درب اداری ۴ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-021", "space_id": "S-053", "door_code": "ED-21", "name_fa": "درب اداری ۵ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-022", "space_id": "S-054", "door_code": "ED-22", "name_fa": "درب اداری ۶ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-023", "space_id": "S-055", "door_code": "ED-23", "name_fa": "درب اداری ۷ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-024", "space_id": "S-056", "door_code": "ED-24", "name_fa": "درب اداری ۸ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-025", "space_id": "S-057", "door_code": "ED-25", "name_fa": "درب اداری ۹ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-026", "space_id": "S-058", "door_code": "ED-26", "name_fa": "درب اداری ۱۰ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-027", "space_id": "S-059", "door_code": "ED-27", "name_fa": "درب اداری ۱۱ بال شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.09, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-028", "space_id": "S-060", "door_code": "ED-28", "name_fa": "درب اداری ۱ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-029", "space_id": "S-061", "door_code": "ED-29", "name_fa": "درب اداری ۲ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-030", "space_id": "S-062", "door_code": "ED-30", "name_fa": "درب اداری ۳ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.09, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-031", "space_id": "S-063", "door_code": "ED-31", "name_fa": "درب اداری ۴ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.09, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-032", "space_id": "S-064", "door_code": "ED-32", "name_fa": "درب اداری ۵ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-033", "space_id": "S-065", "door_code": "ED-33", "name_fa": "درب اداری ۶ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-034", "space_id": "S-066", "door_code": "ED-34", "name_fa": "درب اداری ۷ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-035", "space_id": "S-067", "door_code": "ED-35", "name_fa": "درب اداری ۸ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-036", "space_id": "S-068", "door_code": "ED-36", "name_fa": "درب اداری ۹ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-037", "space_id": "S-069", "door_code": "ED-37", "name_fa": "درب اداری ۱۰ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.09, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-038", "space_id": "S-070", "door_code": "ED-38", "name_fa": "درب اداری ۱۱ بال جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های اتاق‌های تخصصی B2 ---
    {"door_id": "D-039", "space_id": "S-071", "door_code": "CA-01", "name_fa": "درب اتاق کامپیوتر", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-040", "space_id": "S-074", "door_code": "CA-02", "name_fa": "درب انبار کامپیوتر", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-041", "space_id": "S-072", "door_code": "NA-01", "name_fa": "درب اتاق نرم‌افزار", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-042", "space_id": "S-073", "door_code": "NA-02", "name_fa": "درب اتاق سخت‌افزار", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-043", "space_id": "S-077", "door_code": "TT-01", "name_fa": "درب اتاق تایپ و تلکس", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-044", "space_id": "S-078", "door_code": "BI-01", "name_fa": "درب اتاق بیسیم", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-045", "space_id": "S-075", "door_code": "MT-01", "name_fa": "درب مرکز تلفن", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های تعمیرگاه فنی ---
    {"door_id": "D-046", "space_id": "S-079", "door_code": "TF-01", "name_fa": "درب تعمیرگاه فنی ۱", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-047", "space_id": "S-080", "door_code": "TF-02", "name_fa": "درب تعمیرگاه فنی ۲", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-048", "space_id": "S-081", "door_code": "TF-03", "name_fa": "درب تعمیرگاه فنی ۳", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های تحریریه و اداری B1 ---
    {"door_id": "D-049", "space_id": "S-094", "door_code": "TK-01", "name_fa": "درب تحریریه خبر ۱", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-050", "space_id": "S-094", "door_code": "TK-02", "name_fa": "درب تحریریه خبر ۲", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-051", "space_id": "S-095", "door_code": "VRB3-03", "name_fa": "درب مدور B3", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های گریم ---
    {"door_id": "D-052", "space_id": "S-090", "door_code": "OG-01", "name_fa": "درب اتاق گریم بانوان", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-053", "space_id": "S-091", "door_code": "OG-02", "name_fa": "درب اتاق گریم آقایان", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های آبدارخانه ---
    {"door_id": "D-054", "space_id": "S-108", "door_code": "AB-01", "name_fa": "درب آبدارخانه شمالی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-055", "space_id": "S-109", "door_code": "AB-02", "name_fa": "درب آبدارخانه جنوبی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های سرویس بهداشتی (ABS) ---
    {"door_id": "D-056", "space_id": "S-113", "door_code": "SRV-01", "name_fa": "درب سرویس بلوک B3 - بانوان", "door_type": "ABS", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "ABS", "has_glass": False, "executed": True},
    {"door_id": "D-057", "space_id": "S-113", "door_code": "SRV-02", "name_fa": "درب سرویس بلوک B3 - آقایان", "door_type": "ABS", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "ABS", "has_glass": False, "executed": True},
    {"door_id": "D-058", "space_id": "S-111", "door_code": "SRV-03", "name_fa": "درب سرویس بلوک A - همکف ۱", "door_type": "ABS", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "ABS", "has_glass": False, "executed": True},
    {"door_id": "D-059", "space_id": "S-111", "door_code": "SRV-04", "name_fa": "درب سرویس بلوک A - همکف ۲", "door_type": "ABS", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "ABS", "has_glass": False, "executed": True},
    {"door_id": "D-060", "space_id": "S-112", "door_code": "SRV-05", "name_fa": "درب سرویس بلوک A - طبقه اول ۱", "door_type": "ABS", "width_m": 0.88, "height_m": 2.13, "opening_direction": "چپ", "frame_material_fa": "ABS", "has_glass": False, "executed": True},
    {"door_id": "D-061", "space_id": "S-112", "door_code": "SRV-06", "name_fa": "درب سرویس بلوک A - طبقه اول ۲", "door_type": "ABS", "width_m": 0.88, "height_m": 2.13, "opening_direction": "راست", "frame_material_fa": "ABS", "has_glass": False, "executed": True},

    # --- درب‌های فنی ویژه ---
    {"door_id": "D-062", "space_id": "S-029", "door_code": "STM-01", "name_fa": "درب اول STM1", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": False},
    {"door_id": "D-063", "space_id": "S-029", "door_code": "STM-02", "name_fa": "درب شیفت و مانیتورینگ STM1", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": False},
    {"door_id": "D-064", "space_id": "S-096", "door_code": "STM-03", "name_fa": "درب لابراتوار و انبار STM1", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": False},
    {"door_id": "D-065", "space_id": "S-029", "door_code": "STM-04", "name_fa": "درب دوم STM1", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": False},
    {"door_id": "D-066", "space_id": "S-076", "door_code": "STM-05", "name_fa": "درب اتاق کارشناسی STM1", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": False},
    {"door_id": "D-067", "space_id": "S-030", "door_code": "NDL-01", "name_fa": "درب اتاق نودال", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-068", "space_id": "S-031", "door_code": "SRVR-02", "name_fa": "درب اتاق پشتیبان سرور - مانیتورینگ", "door_type": "فلزی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "فلزی", "has_glass": False, "executed": True},

    # --- درب‌های آرشیو ---
    {"door_id": "D-069", "space_id": "S-082", "door_code": "A-ARC-02", "name_fa": "درب اتاق مدیر آرشیو", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-070", "space_id": "S-084", "door_code": "A-ARC-01", "name_fa": "درب آرشیو ویژه ۱", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-071", "space_id": "S-087", "door_code": "R-ARC-03", "name_fa": "درب آرشیو صوتی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.13, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های انبار ---
    {"door_id": "D-072", "space_id": "S-088", "door_code": "ANBR-01", "name_fa": "درب انبار ملزومات", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-073", "space_id": "S-089", "door_code": "ANBR-02", "name_fa": "درب انبار", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.10, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های تأسیسات ---
    {"door_id": "D-074", "space_id": "S-092", "door_code": "TST-01", "name_fa": "درب اتاق پرسنل تأسیسات", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-075", "space_id": "S-093", "door_code": "TST-02", "name_fa": "درب اتاق مدیر تأسیسات", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "راست", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-076", "space_id": "S-083", "door_code": "TST-03", "name_fa": "درب اتاق مدیر آرشیو دوم", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},

    # --- درب‌های برق و مانیتورینگ ---
    {"door_id": "D-077", "space_id": "S-097", "door_code": "BR-01", "name_fa": "درب اتاق برق B2", "door_type": "فلزی", "width_m": 0.88, "height_m": 2.11, "opening_direction": "چپ", "frame_material_fa": "فلزی", "has_glass": False, "executed": True},
    {"door_id": "D-078", "space_id": "S-107", "door_code": "MNT-01", "name_fa": "درب اتاق پایش امنیتی", "door_type": "چوبی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "چپ", "frame_material_fa": "چهارچوب چوبی", "has_glass": False, "executed": True},
    {"door_id": "D-079", "space_id": "S-032", "door_code": "BR-02", "name_fa": "درب اتاق برق و اطفا", "door_type": "فلزی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "فلزی", "has_glass": False, "executed": True},
    {"door_id": "D-080", "space_id": None, "door_code": "BR-03", "name_fa": "درب اتاق برق سوم", "door_type": "فلزی", "width_m": 0.88, "height_m": 2.12, "opening_direction": "راست", "frame_material_fa": "فلزی", "has_glass": False, "executed": True},
]
# ============================================================
# شیت ۷: Windows_Visors - پنجره‌ها و ویزورها
# ============================================================
WINDOWS_VISORS = [
    # --- پنجره‌های ویزور آکوستیک (بین رژی و استودیو) ---
    {"window_id": "W-001", "space_id": "S-001", "name_fa": "ویزور بین استودیو رادیویی A و اتاق کنترل", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 2.00, "height_m": 1.60, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": "لبه پنجره هم‌تراز با بالای ازاره"},
    {"window_id": "W-002", "space_id": "S-002", "name_fa": "ویزور بین استودیو رادیویی B و اتاق کنترل", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 1.80, "height_m": 1.60, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
    {"window_id": "W-003", "space_id": "S-003", "name_fa": "ویزور بین استودیو رادیویی C و اتاق کنترل", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 1.60, "height_m": 1.60, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
    {"window_id": "W-004", "space_id": "S-004", "name_fa": "ویزور بین استودیو رادیویی D و اتاق کنترل", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 1.60, "height_m": 1.60, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
    {"window_id": "W-005", "space_id": "S-010", "name_fa": "ویزور بین استودیو تلویزیونی B و اتاق کنترل", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 2.00, "height_m": 1.80, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},

    # --- پنجره‌های آکوستیک اتاق‌های کنترل ---
    {"window_id": "W-006", "space_id": "S-013", "name_fa": "ویزور اتاق کنترل تلویزیونی A", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 2.20, "height_m": 1.80, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
    {"window_id": "W-007", "space_id": "S-015", "name_fa": "ویزور اتاق کنترل تلویزیونی C", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 2.00, "height_m": 1.80, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
    {"window_id": "W-008", "space_id": "S-016", "name_fa": "ویزور اتاق کنترل تلویزیونی D", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 1.80, "height_m": 1.80, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},

    # --- پنجره‌های آکوستیک اتاق‌های فنی ویژه ---
    {"window_id": "W-011", "space_id": "S-028", "name_fa": "ویزور اتاق فنی ویژه ۱", "window_type": "ویزور آکوستیک", "count": 1, "width_m": 1.60, "height_m": 1.60, "glass_type_fa": "شیشه زاویه‌دار با گاز آرگون", "frame_material_fa": "MDF گردویی T107", "has_gas": True, "gas_type": "Argon", "sill_height_cm": 120, "notes_fa": None},
]
# ============================================================
# شیت ۸: HVAC_Dampers - دریچه‌های هوای تأسیسات مکانیکی
# ============================================================
HVAC_DAMPERS = [
    # --- دریچه‌های دیواری (رفت) ---
    {"damper_id": "DM-001", "category": "دیواری", "flow_type": "رفت", "size_inch": "10x6", "size_fa": "۱۰×۶ اینچ", "count": 1, "install_location_fa": "اتاق اداری", "notes_fa": None},
    {"damper_id": "DM-002", "category": "دیواری", "flow_type": "رفت", "size_inch": "12x6", "size_fa": "۱۲×۶ اینچ", "count": 1, "install_location_fa": "اتاق اداری", "notes_fa": None},
    {"damper_id": "DM-003", "category": "دیواری", "flow_type": "رفت", "size_inch": "12x10", "size_fa": "۱۲×۱۰ اینچ", "count": 1, "install_location_fa": "اتاق اداری", "notes_fa": None},
    {"damper_id": "DM-004", "category": "دیواری", "flow_type": "رفت", "size_inch": "14x10", "size_fa": "۱۴×۱۰ اینچ", "count": 10, "install_location_fa": "اتاق‌های اداری طبقه اول", "notes_fa": None},
    {"damper_id": "DM-005", "category": "دیواری", "flow_type": "رفت", "size_inch": "16x8", "size_fa": "۱۶×۸ اینچ", "count": 28, "install_location_fa": "اتاق‌های اداری همکف و اول", "notes_fa": "پرکاربردترین دریچه دیواری"},
    {"damper_id": "DM-006", "category": "دیواری", "flow_type": "رفت", "size_inch": "16x10", "size_fa": "۱۶×۱۰ اینچ", "count": 7, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-007", "category": "دیواری", "flow_type": "رفت", "size_inch": "18x10", "size_fa": "۱۸×۱۰ اینچ", "count": 6, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-008", "category": "دیواری", "flow_type": "رفت", "size_inch": "20x10", "size_fa": "۲۰×۱۰ اینچ", "count": 5, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-009", "category": "دیواری", "flow_type": "رفت", "size_inch": "20x12", "size_fa": "۲۰×۱۲ اینچ", "count": 1, "install_location_fa": "اتاق اداری", "notes_fa": None},

    # --- دریچه‌های سقفی چهارجهت (رفت) ---
    {"damper_id": "DM-010", "category": "سقفی چهارجهت", "flow_type": "رفت", "size_inch": "12x12", "size_fa": "۱۲×۱۲ اینچ", "count": 4, "install_location_fa": "آبدارخانه و گریم", "notes_fa": None},
    {"damper_id": "DM-011", "category": "سقفی چهارجهت", "flow_type": "رفت", "size_inch": "60x60", "size_fa": "۶۰×۶۰ سانتی‌متر", "count": 124, "install_location_fa": "اتاق‌های فنی و اداری", "notes_fa": "استاندارد اصلی پروژه"},
    {"damper_id": "DM-012", "category": "سقفی چهارجهت (دکوراتیو)", "flow_type": "رفت", "size_inch": "60x60", "size_fa": "۶۰×۶۰ سانتی‌متر", "count": 32, "install_location_fa": "استودیوها و اتاق‌های کنترل", "notes_fa": "رنگ دکوراتیو هم‌رنگ سقف آکوستیک"},

    # --- دریچه‌های سقفی مشبک (برگشت) ---
    {"damper_id": "DM-013", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "8x8", "size_fa": "۸×۸ اینچ", "count": 3, "install_location_fa": "اتاق بازشنوایی", "notes_fa": None},
    {"damper_id": "DM-014", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "12x6", "size_fa": "۱۲×۶ اینچ", "count": 1, "install_location_fa": "اتاق‌های کوچک", "notes_fa": None},
    {"damper_id": "DM-015", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "12x8", "size_fa": "۱۲×۸ اینچ", "count": 5, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-016", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "12x12", "size_fa": "۱۲×۱۲ اینچ", "count": 7, "install_location_fa": "اتاق‌های تدوین", "notes_fa": None},
    {"damper_id": "DM-017", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "18x6", "size_fa": "۱۸×۶ اینچ", "count": 3, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-018", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "18x8", "size_fa": "۱۸×۸ اینچ", "count": 6, "install_location_fa": "اتاق‌های اداری طبقه اول", "notes_fa": None},
    {"damper_id": "DM-019", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "18x10", "size_fa": "۱۸×۱۰ اینچ", "count": 8, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-020", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "18x12", "size_fa": "۱۸×۱۲ اینچ", "count": 1, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-021", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "18x12", "size_fa": "۱۸×۱۲ اینچ", "count": 3, "install_location_fa": "اتاق‌های اداری", "notes_fa": None},
    {"damper_id": "DM-022", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "20x6", "size_fa": "۲۰×۶ اینچ", "count": 15, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-023", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "20x10", "size_fa": "۲۰×۱۰ اینچ", "count": 3, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-024", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "20x12", "size_fa": "۲۰×۱۲ اینچ", "count": 2, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-025", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "22x6", "size_fa": "۲۲×۶ اینچ", "count": 4, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-026", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "22x8", "size_fa": "۲۲×۸ اینچ", "count": 1, "install_location_fa": "اتاق فنی", "notes_fa": None},
    {"damper_id": "DM-027", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "22x12", "size_fa": "۲۲×۱۲ اینچ", "count": 2, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-028", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "22x12", "size_fa": "۲۲×۱۲ اینچ", "count": 5, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-029", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "24x6", "size_fa": "۲۴×۶ اینچ", "count": 9, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-030", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "24x12", "size_fa": "۲۴×۱۲ اینچ", "count": 2, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-031", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "24x12", "size_fa": "۲۴×۱۲ اینچ", "count": 4, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-032", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "24x14", "size_fa": "۲۴×۱۴ اینچ", "count": 1, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-033", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "24x18", "size_fa": "۲۴×۱۸ اینچ", "count": 4, "install_location_fa": "استودیوهای تلویزیونی", "notes_fa": None},
    {"damper_id": "DM-034", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "26x6", "size_fa": "۲۶×۶ اینچ", "count": 2, "install_location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"damper_id": "DM-035", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "30x12", "size_fa": "۳۰×۱۲ اینچ", "count": 1, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-036", "category": "سقفی مشبک (دکوراتیو)", "flow_type": "برگشت", "size_inch": "30x18", "size_fa": "۳۰×۱۸ اینچ", "count": 2, "install_location_fa": "استودیو", "notes_fa": "رنگ دکوراتیو"},
    {"damper_id": "DM-037", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "30x18", "size_fa": "۳۰×۱۸ اینچ", "count": 2, "install_location_fa": "استودیوهای تلویزیونی", "notes_fa": None},
    {"damper_id": "DM-038", "category": "سقفی مشبک", "flow_type": "برگشت", "size_inch": "30x20", "size_fa": "۳۰×۲۰ اینچ", "count": 2, "install_location_fa": "استودیو تلویزیونی", "notes_fa": None},
]
# ============================================================
# شیت ۹: HVAC_Equipment - تجهیزات مکانیکی
# ============================================================
HVAC_EQUIPMENT = [
    # --- هوارسان‌ها (AHU) ---
    {"equipment_id": "HE-001", "equipment_type": "هوارسان (AHU)", "tag": "AHU-1", "name_fa": "هوارسان شماره ۱", "serves_fa": "استودیو رادیویی A و B", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-002", "equipment_type": "هوارسان (AHU)", "tag": "AHU-2", "name_fa": "هوارسان شماره ۲", "serves_fa": "استودیو رادیویی C و D", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-003", "equipment_type": "هوارسان (AHU)", "tag": "AHU-3", "name_fa": "هوارسان شماره ۳", "serves_fa": "اتاق‌های اداری فنی", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-004", "equipment_type": "هوارسان (AHU)", "tag": "AHU-4", "name_fa": "هوارسان شماره ۴", "serves_fa": "اتاق‌های اداری طبقه اول", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-005", "equipment_type": "هوارسان (AHU)", "tag": "AHU-5", "name_fa": "هوارسان شماره ۵", "serves_fa": "اتاق‌های فنی و آرشیو", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-006", "equipment_type": "هوارسان (AHU)", "tag": "AHU-6 & AHU-7", "name_fa": "هوارسان شماره ۶ و ۷", "serves_fa": "استودیوهای تلویزیونی", "capacity_fa": None, "count": 2, "location_fa": "پشت‌بام", "executed": False},
    {"equipment_id": "HE-007", "equipment_type": "هوارسان (AHU)", "tag": "AUU-8", "name_fa": "هوارسان شماره ۸", "serves_fa": "سرویس بلوک A", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},

    # --- اگزاست فن‌ها ---
    {"equipment_id": "HE-008", "equipment_type": "اگزاست فن", "tag": "EF-01", "name_fa": "اگزاست فن سرویس‌های بهداشتی", "serves_fa": "سرویس‌های بهداشتی بلوک A", "capacity_fa": None, "count": 2, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-009", "equipment_type": "اگزاست فن", "tag": "EF-02", "name_fa": "اگزاست فن آبدارخانه", "serves_fa": "آبدارخانه‌ها", "capacity_fa": None, "count": 2, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-010", "equipment_type": "اگزاست فن", "tag": "EF-03", "name_fa": "اگزاست فن اتاق‌های فنی", "serves_fa": "اتاق‌های فنی و سرور", "capacity_fa": None, "count": 3, "location_fa": "پشت‌بام", "executed": True},

    # --- سیستم برودت سرور ---
    {"equipment_id": "HE-011", "equipment_type": "سیستم برودت (Chiller)", "tag": "CH-01", "name_fa": "چیلر سیستم برودت سرور", "serves_fa": "اتاق پشتیبان سرور", "capacity_fa": None, "count": 1, "location_fa": "پشت‌بام", "executed": True},
    {"equipment_id": "HE-012", "equipment_type": "فن‌کویل (FCU)", "tag": "FCU-01", "name_fa": "فن‌کویل اتاق سرور", "serves_fa": "اتاق پشتیبان سرور و اتاق فنی ویژه ۲", "capacity_fa": None, "count": 4, "location_fa": "داخل اتاق", "executed": True},

    # --- سیستم تهویه موتورخانه ---
    {"equipment_id": "HE-013", "equipment_type": "هواساز موتورخانه", "tag": "MAU-01", "name_fa": "هواساز موتورخانه", "serves_fa": "موتورخانه اصلی", "capacity_fa": None, "count": 1, "location_fa": "موتورخانه", "executed": True},

    # --- پمپ‌ها ---
    {"equipment_id": "HE-014", "equipment_type": "پمپ سیرکولاسیون", "tag": "P-01", "name_fa": "پمپ سیرکولاسیون گرمایش", "serves_fa": "سیستم گرمایش", "capacity_fa": None, "count": 2, "location_fa": "موتورخانه", "executed": True},
    {"equipment_id": "HE-015", "equipment_type": "پمپ سیرکولاسیون", "tag": "P-02", "name_fa": "پمپ سیرکولاسیون سرمایش", "serves_fa": "سیستم سرمایش", "capacity_fa": None, "count": 2, "location_fa": "موتورخانه", "executed": True},
]
# ============================================================
# شیت ۱۰: Insulation - عایق‌های حرارتی و صوتی
# ============================================================
INSULATION = [
    {"insulation_id": "IN-001", "insulation_type": "پشم سنگ پانلی", "application_fa": "دیوار استودیوها (لایه میانی)", "spec_fa": "دانسیته ۸۰ کیلوگرم بر مترمکعب", "thickness_cm": 10, "area_m2": None, "notes_fa": "لایه اصلی ایزولاسیون صوتی"},
    {"insulation_id": "IN-002", "insulation_type": "پشم سنگ پانلی", "application_fa": "سقف استودیوها", "spec_fa": "دانسیته ۸۰ کیلوگرم بر مترمکعب", "thickness_cm": 10, "area_m2": None, "notes_fa": None},
    {"insulation_id": "IN-003", "insulation_type": "عایق الاستومری", "application_fa": "لوله‌های تأسیسات مکانیکی", "spec_fa": "الاستومری انعطاف‌پذیر", "thickness_cm": 2, "area_m2": None, "notes_fa": "عایق حرارتی لوله‌ها"},
    {"insulation_id": "IN-004", "insulation_type": "پشم شیشه", "application_fa": "کانال‌های هوا", "spec_fa": "پشم شیشه رول", "thickness_cm": 5, "area_m2": None, "notes_fa": None},
    {"insulation_id": "IN-005", "insulation_type": "عایق رطوبتی", "application_fa": "بام‌ها", "spec_fa": "ایزوگام پیش‌ساخته", "thickness_cm": 0.4, "area_m2": None, "notes_fa": None},
    {"insulation_id": "IN-006", "insulation_type": "عایق رطوبتی", "application_fa": "سرویس‌های بهداشتی", "spec_fa": "عایق رطوبتی زیر سرامیک", "thickness_cm": 0.3, "area_m2": None, "notes_fa": None},
    {"insulation_id": "IN-007", "insulation_type": "عایق حرارتی", "application_fa": "لوله‌های آب گرم و سرد", "spec_fa": "فوم پلی‌اتیلن", "thickness_cm": 3, "area_m2": None, "notes_fa": None},
    {"insulation_id": "IN-008", "insulation_type": "عایق صوتی", "application_fa": "کانال‌های اگزاست استودیو", "spec_fa": "پشم سنگ با روکش آلومینیوم", "thickness_cm": 5, "area_m2": None, "notes_fa": None},
]
# ============================================================
# شیت ۱۱: Plumbing_Fixtures - تأسیسات بهداشتی
# ============================================================
PLUMBING_FIXTURES = [
    {"fixture_id": "PF-001", "fixture_type": "روشویی", "model_fa": "روشویی چینی", "count": 24, "material_fa": "چینی", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-002", "fixture_type": "توالت فرنگی", "model_fa": "توالت فرنگی", "count": 18, "material_fa": "چینی", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-003", "fixture_type": "توالت ایرانی", "model_fa": "توالت ایرانی", "count": 6, "material_fa": "چینی", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-004", "fixture_type": "دوش", "model_fa": "دوش حمام", "count": 4, "material_fa": "کروم", "location_fa": "سرویس‌های دوش", "notes_fa": None},
    {"fixture_id": "PF-005", "fixture_type": "سینک آبدارخانه", "model_fa": "سینک استیل", "count": 6, "material_fa": "استیل ضدزنگ", "location_fa": "آبدارخانه‌ها", "notes_fa": None},
    {"fixture_id": "PF-006", "fixture_type": "شیرآلات", "model_fa": "شیر اهرمی", "count": 30, "material_fa": "کروم", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-007", "fixture_type": "فلاش تانک", "model_fa": "فلاش تانک", "count": 24, "material_fa": "چینی", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-008", "fixture_type": "سیفون", "model_fa": "سیفون", "count": 24, "material_fa": "پلاستیک", "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"fixture_id": "PF-009", "fixture_type": "شیر فلکه", "model_fa": "شیر فلکه", "count": 15, "material_fa": "برنجی", "location_fa": "موتورخانه و تونل تأسیسات", "notes_fa": None},
    {"fixture_id": "PF-010", "fixture_type": "شیر یک‌طرفه", "model_fa": "شیر یک‌طرفه", "count": 12, "material_fa": "برنجی", "location_fa": "موتورخانه و تونل تأسیسات", "notes_fa": None},
]
# ============================================================
# شیت ۱۲: Electrical_Items - کلید، پریز و متعلقات برقی
# ============================================================
ELECTRICAL_ITEMS = [
    {"item_id": "EL-001", "item_type": "پریز", "name_fa": "پریز روکار تک‌فاز", "count": 19, "unit": "عدد", "location_fa": "راهروها و فضاهای عمومی", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-002", "item_type": "پریز", "name_fa": "پریز روکار سه‌فاز", "count": 3, "unit": "عدد", "location_fa": "اتاق‌های فنی", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-003", "item_type": "پریز", "name_fa": "پریز ارت‌دار ۱۶ آمپر", "count": 377, "unit": "عدد", "location_fa": "کل ساختمان", "brand_fa": "لگراند یا مشابه", "notes_fa": "پریز توکار"},
    {"item_id": "EL-004", "item_type": "پریز", "name_fa": "پریز ارت‌دار ۱۶ آمپر (اضطراری)", "count": 359, "unit": "عدد", "location_fa": "کل ساختمان", "brand_fa": "لگراند یا مشابه", "notes_fa": "مدار اضطراری"},
    {"item_id": "EL-005", "item_type": "کلید", "name_fa": "کلید تک‌پل ۱۰ آمپر", "count": 112, "unit": "عدد", "location_fa": "کل ساختمان", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-006", "item_type": "کلید", "name_fa": "کلید تبدیل ۱۰ آمپر", "count": 14, "unit": "عدد", "location_fa": "راهروها", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-007", "item_type": "کلید", "name_fa": "کلید دوپل ۱۰ آمپر", "count": 30, "unit": "عدد", "location_fa": "اتاق‌های فنی و اداری", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-008", "item_type": "قوطی", "name_fa": "قوطی کلید و پریز", "count": 240, "unit": "عدد", "location_fa": "کل ساختمان", "brand_fa": None, "notes_fa": "توکار"},
    {"item_id": "EL-009", "item_type": "جعبه تقسیم", "name_fa": "جعبه تقسیم ۱۵۰×۱۵۰", "count": 8, "unit": "عدد", "location_fa": "اتاق‌های فنی", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-010", "item_type": "جعبه تقسیم", "name_fa": "جعبه تقسیم گالوانیزه ۸۰×۸۰", "count": 87, "unit": "عدد", "location_fa": "کل ساختمان", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-011", "item_type": "پریز", "name_fa": "پریز ۱۶ آمپر با اتصال زمین (توکار)", "count": 17, "unit": "عدد", "location_fa": "استودیوهای تلویزیونی", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-012", "item_type": "پریز", "name_fa": "پریز ۱۶ آمپر با اتصال زمین", "count": 2, "unit": "عدد", "location_fa": "اتاق‌های گرمی", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-013", "item_type": "کلید", "name_fa": "کلید یک پل و یک خانه - توکار", "count": 15, "unit": "عدد", "location_fa": "اتاق‌های اداری", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-014", "item_type": "کلید", "name_fa": "کلید ۱۰ آمپر ۲۵۰ ولت دو پل، یک راه برای نصب توکار", "count": 1, "unit": "عدد", "location_fa": "اتاق‌های اداری", "brand_fa": None, "notes_fa": None},
    {"item_id": "EL-015", "item_type": "ترمینال", "name_fa": "ترمینال پیچی برای هادی ۲.۵ میلی‌متر مربع", "count": 42, "unit": "عدد", "location_fa": "تابلوهای برق", "brand_fa": None, "notes_fa": None},
]
# ============================================================
# شیت ۱۳: Lighting_Items - انواع چراغ‌های روشنایی
# ============================================================
LIGHTING_ITEMS = [
    {"light_id": "LT-001", "name_fa": "چراغ LED روکار ۴۷ وات", "model_fa": "مازی‌نور یا مشابه", "watt": 47, "lumen": 4500, "ip_rating": "IP65", "count": 14, "location_fa": "اتاق پشتیبان سرور", "notes_fa": "ضد نم و بخار"},
    {"light_id": "LT-002", "name_fa": "چراغ دیواری LED روکار ۱۵ وات", "model_fa": None, "watt": 15, "lumen": None, "ip_rating": None, "count": 8, "location_fa": "سرویس‌های بهداشتی بلوک A و B3", "notes_fa": "بدنه ورق فولادی با رنگ الکترواستاتیک پودری"},
    {"light_id": "LT-003", "name_fa": "چراغ دیواری دکوراتیو با دو لامپ LED ۹ وات", "model_fa": None, "watt": 9, "lumen": None, "ip_rating": None, "count": 51, "location_fa": "استودیوهای تلویزیونی", "notes_fa": "پایه قابل تنظیم"},
    {"light_id": "LT-004", "name_fa": "چراغ LED ریلی ۳۰ وات", "model_fa": "هانی مازی‌نور یا مشابه", "watt": 30, "lumen": 3200, "ip_rating": None, "count": 30, "location_fa": "استودیوهای رادیویی", "notes_fa": None},
    {"light_id": "LT-005", "name_fa": "چراغ سیلندری توکار با رفلکتور آلومینیومی", "model_fa": None, "watt": 9, "lumen": None, "ip_rating": None, "count": 15, "location_fa": "سرویس‌های بهداشتی، ورودی بخش فنی", "notes_fa": "قطر فریم ۱۰ سانتی‌متر"},
    {"light_id": "LT-006", "name_fa": "چراغ آویز HIGH BAY", "model_fa": "مدل SH-6157-18B یا مشابه", "watt": None, "lumen": None, "ip_rating": None, "count": 66, "location_fa": "استودیوهای تلویزیونی", "notes_fa": "روشنایی صنعتی"},
    {"light_id": "LT-007", "name_fa": "پروژکتور بالای ستون‌های نما", "model_fa": None, "watt": None, "lumen": None, "ip_rating": "IP65", "count": 40, "location_fa": "نمای خارجی", "notes_fa": None},
    {"light_id": "LT-008", "name_fa": "چراغ سقفی توکار ۶۰×۶۰ LED", "model_fa": "M521SLED2865-W مازی‌نور", "watt": None, "lumen": None, "ip_rating": None, "count": 47, "location_fa": "راهرو و کلاس‌های اداری", "notes_fa": "در شبکه سقف"},
    {"light_id": "LT-009", "name_fa": "چراغ LED توکار ۶۰×۶۰ با ماژول یکپارچه", "model_fa": None, "watt": None, "lumen": 5000, "ip_rating": "IP65", "count": 12, "location_fa": "اتاق‌های فنی ویژه", "notes_fa": None},
    {"light_id": "LT-010", "name_fa": "چراغ خطی توکار LED", "model_fa": None, "watt": None, "lumen": 2800, "ip_rating": None, "count": 31, "location_fa": "راهروها", "notes_fa": "عرض ۶ سانتی‌متر"},
    {"light_id": "LT-011", "name_fa": "چراغ روشویی LED", "model_fa": None, "watt": None, "lumen": None, "ip_rating": None, "count": 47, "location_fa": "سرویس‌های بهداشتی", "notes_fa": None},
    {"light_id": "LT-012", "name_fa": "چراغ LED با ماژول یکپارچه (Integrated)", "model_fa": None, "watt": None, "lumen": 4000, "ip_rating": "IP65", "count": 80, "location_fa": "فضاهای صنعتی و فنی", "notes_fa": "طول ۱۲۰ سانتی‌متر"},
    {"light_id": "LT-013", "name_fa": "چراغ تونلی (بیمیضی) LED", "model_fa": None, "watt": None, "lumen": 800, "ip_rating": "IP54", "count": 38, "location_fa": "تونل تأسیسات", "notes_fa": "بدنه و سبد گالوانیزه"},
    {"light_id": "LT-014", "name_fa": "چراغ نورافکن LED IP65", "model_fa": None, "watt": None, "lumen": 3000, "ip_rating": "IP65", "count": 3, "location_fa": "نما", "notes_fa": None},
    {"light_id": "LT-015", "name_fa": "چراغ On Air (قرمز/سبز)", "model_fa": None, "watt": None, "lumen": None, "ip_rating": None, "count": 5, "location_fa": "سردرب استودیوها", "notes_fa": "برای نمایش وضعیت پخش"},
]
# ============================================================
# شیت ۱۴: Power_Panels - تابلوهای برق
# ============================================================
POWER_PANELS = [
    {"panel_id": "PN-001", "tag": "EMP", "name_fa": "تابلو برق اضطراری اصلی", "panel_type": "تابلو اصلی اضطراری", "location_fa": "اتاق برق همکف", "serves_fa": "سیستم‌های اضطراری", "executed": True},
    {"panel_id": "PN-002", "tag": "PR(1-4)U", "name_fa": "تابلو برق ۴ گانه", "panel_type": "تابلو توزیع فرعی", "location_fa": "اتاق برق همکف", "serves_fa": "مصارف عمومی", "executed": True},
    {"panel_id": "PN-003", "tag": "R3(E&U)", "name_fa": "تابلو برق رادیویی ۳", "panel_type": "تابلو تخصصی", "location_fa": "نزدیک استودیو رادیویی C", "serves_fa": "استودیو رادیویی C", "executed": True},
    {"panel_id": "PN-004", "tag": "R4(E&U)", "name_fa": "تابلو برق رادیویی ۴", "panel_type": "تابلو تخصصی", "location_fa": "نزدیک استودیو رادیویی D", "serves_fa": "استودیو رادیویی D", "executed": True},
    {"panel_id": "PN-005", "tag": "T1(E&U)", "name_fa": "تابلو برق تلویزیونی ۱", "panel_type": "تابلو تخصصی", "location_fa": "نزدیک استودیو تلویزیونی A", "serves_fa": "استودیو تلویزیونی A", "executed": False},
    {"panel_id": "PN-006", "tag": "T2-T4(E&U)", "name_fa": "تابلو برق تلویزیونی ۲ و ۴", "panel_type": "تابلو تخصصی", "location_fa": "نزدیک استودیوهای تلویزیونی B و D", "serves_fa": "استودیو تلویزیونی B و D", "executed": True},
    {"panel_id": "PN-007", "tag": "T3(E&U)", "name_fa": "تابلو برق تلویزیونی ۳", "panel_type": "تابلو تخصصی", "location_fa": "نزدیک استودیو تلویزیونی C", "serves_fa": "استودیو تلویزیونی C", "executed": False},
    {"panel_id": "PN-008", "tag": "ULP1", "name_fa": "تابلو برق ULP1", "panel_type": "تابلو توزیع", "location_fa": "اتاق برق", "serves_fa": "مصارف عمومی", "executed": True},
    {"panel_id": "PN-009", "tag": "ULP2", "name_fa": "تابلو برق ULP2", "panel_type": "تابلو توزیع", "location_fa": "اتاق برق", "serves_fa": "مصارف عمومی", "executed": True},
    {"panel_id": "PN-010", "tag": "UP", "name_fa": "تابلو برق اصلی UP", "panel_type": "تابلو توزیع اصلی", "location_fa": "اتاق برق همکف", "serves_fa": "کل ساختمان", "executed": True},
]
# ============================================================
# شیت ۱۵: Fire_Safety - سیستم اعلام حریق
# ============================================================
FIRE_SAFETY = [
    {"fire_id": "FS-001", "item_type": "دتکتور", "name_fa": "دتکتور حرارتی فتوالکتریک آدرس‌پذیر", "count": 302, "unit": "عدد", "location_fa": "کل ساختمان به‌جز استودیوها", "notes_fa": "مطابق آخرین نقشه + ۸ عدد زیر سقف استودیوهای رادیویی"},
    {"fire_id": "FS-002", "item_type": "دتکتور", "name_fa": "دتکتور دودی فتوالکتریک هوشمند", "count": 40, "unit": "عدد", "location_fa": "استودیوهای رادیویی و اتاق‌های کنترل", "notes_fa": "نشان‌دهنده عملکرد دتکتور"},
    {"fire_id": "FS-003", "item_type": "شستی اعلام حریق", "name_fa": "شستی اعلام حریق", "count": 14, "unit": "عدد", "location_fa": "راهروها و ورودی‌ها", "notes_fa": None},
    {"fire_id": "FS-004", "item_type": "زنگ اعلان", "name_fa": "زنگ اعلام حریق", "count": 14, "unit": "عدد", "location_fa": "راهروها", "notes_fa": "قطر ۱۵ سانتی‌متر"},
    {"fire_id": "FS-005", "item_type": "پنل کنترل", "name_fa": "پنل اعلام حریق آدرس‌پذیر ۸ لوپ", "count": 1, "unit": "دستگاه", "location_fa": "اتاق کنترل اعلام حریق", "notes_fa": "کنترل مرکزی"},
    {"fire_id": "FS-006", "item_type": "کابل اعلام حریق", "name_fa": "کابل نسوز اعلام حریق شیلددار", "count": 444, "unit": "متر", "location_fa": "طبقه همکف", "notes_fa": None},
    {"fire_id": "FS-007", "item_type": "کابل اعلام حریق", "name_fa": "کابل نسوز اعلام حریق شیلددار", "count": 98, "unit": "متر", "location_fa": "طبقه اول", "notes_fa": None},
    {"fire_id": "FS-008", "item_type": "لوله", "name_fa": "لوله PVC توکار ۱۳.۵", "count": 5, "unit": "متر", "location_fa": "طبقه همکف", "notes_fa": None},
    {"fire_id": "FS-009", "item_type": "لوله", "name_fa": "لوله PVC توکار ۱۳.۵", "count": 6, "unit": "متر", "location_fa": "طبقه اول", "notes_fa": None},
    {"fire_id": "FS-010", "item_type": "جعبه آتش‌نشانی", "name_fa": "جعبه آتش‌نشانی توکار", "count": 9, "unit": "عدد", "location_fa": "بلوک A، B2، B3", "notes_fa": "شامل B2 طبقه همکف و اول، بلوک A، تحریریه B3"},
]
# ============================================================
# شیت ۱۶: Cables_Trunking - کابل‌ها، سیم‌ها و سینی‌ها
# ============================================================
CABLES_TRUNKING = [
    # --- سیم‌ها ---
    {"cable_id": "CB-001", "cable_type": "سیم افشان", "spec_fa": "سیم افشان ۱.۵ و ۲.۵ میلی‌متر مربع", "length_m": 480, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-002", "cable_type": "کابل مسی افشان", "spec_fa": "سیم مسی افشان ۱.۵ میلی‌متر مربع NYAF", "length_m": 350, "location_fa": "اتاق هواساز و گرمی", "notes_fa": None},

    # --- کابل‌های اصلی ---
    {"cable_id": "CB-003", "cable_type": "کابل", "spec_fa": "کابل زمینی NYY ۳×۱.۵", "length_m": 190, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-004", "cable_type": "کابل", "spec_fa": "کابل زمینی NYY ۳×۲.۵", "length_m": 220, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-005", "cable_type": "کابل", "spec_fa": "کابل زمینی NYY ۳×۴", "length_m": 265, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-006", "cable_type": "کابل", "spec_fa": "کابل زمینی NYY ۳×۶", "length_m": 96, "location_fa": "اتاق‌های راهروی شرقی", "notes_fa": None},

    # --- کابل‌های شیلددار و نسوز ---
    {"cable_id": "CB-007", "cable_type": "کابل شیلددار", "spec_fa": "کابل شیلد دار زیرزمینی NYCY ۲×۱.۵+۱.۵", "length_m": 126, "location_fa": "کل ساختمان", "notes_fa": "برای اعلام حریق"},
    {"cable_id": "CB-008", "cable_type": "کابل نسوز", "spec_fa": "کابل صوتی و نسوز اعلام حریق شیلددار", "length_m": 175, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-009", "cable_type": "کابل پلاستیکی", "spec_fa": "کابل پلاستیکی NYMHY ۴×۰.۵", "length_m": 89, "location_fa": "اتاق‌های فنی", "notes_fa": None},

    # --- لوله‌ها ---
    {"cable_id": "CB-010", "cable_type": "لوله فولادی", "spec_fa": "لوله کشی توکار با لوله فولادی سایز ۱۶", "length_m": 306, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-011", "cable_type": "لوله PVC", "spec_fa": "لوله کشی توکار با لوله PVC ۱۳.۵", "length_m": 5, "location_fa": "طبقه همکف", "notes_fa": None},
    {"cable_id": "CB-012", "cable_type": "لوله PVC", "spec_fa": "لوله کشی توکار PVC ۱۶", "length_m": 39, "location_fa": "اتاق‌های فنی", "notes_fa": None},
    {"cable_id": "CB-013", "cable_type": "لوله فلکسی", "spec_fa": "لوله کشی روکار یا توکار فلکسی", "length_m": 20, "location_fa": "اتاق‌های گرمی و اداری", "notes_fa": None},
    {"cable_id": "CB-014", "cable_type": "لوله PVC", "spec_fa": "لوله کشی توکار PVC ۲۱ و ۲۹", "length_m": 306, "location_fa": "کل ساختمان", "notes_fa": None},

    # --- سینی کابل ---
    {"cable_id": "CB-015", "cable_type": "سینی کابل", "spec_fa": "سینی کابل به عرض ۲۰۰ میلی‌متر", "length_m": 32, "location_fa": "اتاق‌های فنی و راهروها", "notes_fa": None},
    {"cable_id": "CB-016", "cable_type": "سینی کابل", "spec_fa": "سینی کابل به عرض ۳۰۰ میلی‌متر", "length_m": 12, "location_fa": "راهروهای اصلی", "notes_fa": None},
    {"cable_id": "CB-017", "cable_type": "سینی کابل", "spec_fa": "سینی کابل به عرض ۵۰۰ میلی‌متر", "length_m": 90, "location_fa": "راهروهای اصلی", "notes_fa": None},
    {"cable_id": "CB-018", "cable_type": "زانویی سینی", "spec_fa": "زانویی افقی سینی کابل به عرض ۲۰۰ میلی‌متر", "count": 2, "location_fa": "راهروها", "notes_fa": None},
    {"cable_id": "CB-019", "cable_type": "زانویی سینی", "spec_fa": "زانویی افقی سینی کابل به عرض ۵۰۰ میلی‌متر", "count": 5, "location_fa": "راهروها", "notes_fa": None},
    {"cable_id": "CB-020", "cable_type": "سینی کابل", "spec_fa": "سه راهی سینی کابل به عرض ۵۰۰ میلی‌متر", "count": 3, "location_fa": "راهروها", "notes_fa": None},
    {"cable_id": "CB-021", "cable_type": "سینی کابل", "spec_fa": "چهار راهی سینی کابل به عرض ۵۰۰ میلی‌متر", "count": 2, "location_fa": "راهروها", "notes_fa": None},

    # --- متعلقات ---
    {"cable_id": "CB-022", "cable_type": "کابلشو", "spec_fa": "کابلشوی پرسی مسی ۱۵۰-۱۸۵", "count": 7, "location_fa": "تابلوهای برق", "notes_fa": None},
    {"cable_id": "CB-023", "cable_type": "سرسیم", "spec_fa": "سرسیم برای کابلهای ۱.۵ تا ۲.۵", "count": 320, "location_fa": "تابلوهای برق", "notes_fa": None},
    {"cable_id": "CB-024", "cable_type": "گلند", "spec_fa": "گلند برنجی لوله ۱۱، ۱۳.۵ و ۱۶", "count": 380, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-025", "cable_type": "بست", "spec_fa": "بست چنگالی فلزی", "count": 320, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-026", "cable_type": "بست", "spec_fa": "بست پلاستیکی کمربندی", "count": 500, "location_fa": "کل ساختمان", "notes_fa": None},
    {"cable_id": "CB-027", "cable_type": "قاب", "spec_fa": "قاب و بست آهنی جهت ساپورت", "length_kg": 131, "location_fa": "کل ساختمان", "notes_fa": "بر حسب کیلوگرم"},
]
# ============================================================
# شیت ۱۷: QS_Items - اقلام متره به تفکیک رشته
# ============================================================
QS_ITEMS = [
    # ============ ابنیه ============
    {"item_id": "QS-001", "discipline": "ابنیه", "chapter_number": 1, "chapter_name": "تخریب", "description_fa": "تخریب دیوارهای موجود و برداشت نخاله", "unit": "مترمربع", "quantity": 850, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-002", "discipline": "ابنیه", "chapter_number": 4, "chapter_name": "بنایی با سنگ", "description_fa": "اجرای بنایی با سنگ قلوه", "unit": "مترمکعب", "quantity": 87.5, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-003", "discipline": "ابنیه", "chapter_number": 8, "chapter_name": "بتن درجا", "description_fa": "اجرای بتن کف‌سازی", "unit": "مترمکعب", "quantity": 45.2, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-004", "discipline": "ابنیه", "chapter_number": 9, "chapter_name": "کارهای فولادی سنگین", "description_fa": "اجرای وال پست و نبشی ۴۰×۴۰×۲", "unit": "مترطول", "quantity": 30, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-005", "discipline": "ابنیه", "chapter_number": 11, "chapter_name": "آجرکاری و شفته‌ریزی", "description_fa": "اجرای نما با آجر نسوز آذرخش", "unit": "مترمربع", "quantity": 242, "source_fa": "ریزمتره نما"},
    {"item_id": "QS-006", "discipline": "ابنیه", "chapter_number": 13, "chapter_name": "عایق‌کاری رطوبتی", "description_fa": "اجرای عایق رطوبتی بام", "unit": "مترمربع", "quantity": 445, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-007", "discipline": "ابنیه", "chapter_number": 14, "chapter_name": "عایق‌کاری حرارتی", "description_fa": "اجرای عایق حرارتی لوله‌ها", "unit": "مترمربع", "quantity": 320, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-008", "discipline": "ابنیه", "chapter_number": 16, "chapter_name": "کارهای فولادی سبک", "description_fa": "اجرای وال پست", "unit": "مترمربع", "quantity": 145, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-009", "discipline": "ابنیه", "chapter_number": 18, "chapter_name": "اندودکاری و بندکشی", "description_fa": "اجرای لایه گچ زیرکار دیوارها", "unit": "مترمربع", "quantity": 2450, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-010", "discipline": "ابنیه", "chapter_number": 18, "chapter_name": "اندودکاری و بندکشی", "description_fa": "اجرای لایه گچ رویه دیوارها", "unit": "مترمربع", "quantity": 2180, "source_fa": "ریزمتره ابنیه"},
    {"item_id": "QS-011", "discipline": "ابنیه", "chapter_number": 19, "chapter_name": "کارهای چوبی", "description_fa": "اجرای چارچوب و درب چوبی", "unit": "عدد", "quantity": 88, "source_fa": "لیست درب"},
    {"item_id": "QS-012", "discipline": "ابنیه", "chapter_number": 20, "chapter_name": "کاشی و سرامیک", "description_fa": "اجرای سرامیک کف سرویس‌ها (۳۰×۳۰)", "unit": "مترمربع", "quantity": 55.9, "source_fa": "شیت سرامیک"},
    {"item_id": "QS-013", "discipline": "ابنیه", "chapter_number": 20, "chapter_name": "کاشی و سرامیک", "description_fa": "اجرای کاشی دیوار سرویس‌ها", "unit": "مترمربع", "quantity": 285, "source_fa": "شیت کاشی"},
    {"item_id": "QS-014", "discipline": "ابنیه", "chapter_number": 21, "chapter_name": "موزائیک", "description_fa": "اجرای موزائیک ایرانی کف اتاق‌های فنی", "unit": "مترمربع", "quantity": 1180, "source_fa": "شیت موزائیک"},
    {"item_id": "QS-015", "discipline": "ابنیه", "chapter_number": 22, "chapter_name": "کارهای سنگی با سنگ پلاک", "description_fa": "اجرای سنگ گرانیت نهبندان ۱۰۰×۴۰", "unit": "مترمربع", "quantity": 1050, "source_fa": "شیت گرانیت"},
    {"item_id": "QS-016", "discipline": "ابنیه", "chapter_number": 22, "chapter_name": "کارهای سنگی با سنگ پلاک", "description_fa": "اجرای سنگ مرمریت ۶۰×۶۰ آرمی", "unit": "مترمربع", "quantity": 1820, "source_fa": "شیت سنگ مرمریت"},
    {"item_id": "QS-017", "discipline": "ابنیه", "chapter_number": 22, "chapter_name": "کارهای سنگی با سنگ پلاک", "description_fa": "اجرای سنگ تراورتن نما", "unit": "مترمربع", "quantity": 245, "source_fa": "شیت SANG_NAMA"},
    {"item_id": "QS-018", "discipline": "ابنیه", "chapter_number": 23, "chapter_name": "کارهای پلاستیکی و پلیمری", "description_fa": "اجرای کفپوش ونیل", "unit": "مترمربع", "quantity": 780, "source_fa": "شیت کفپوش ونیل"},
    {"item_id": "QS-019", "discipline": "ابنیه", "chapter_number": 23, "chapter_name": "کارهای پلاستیکی و پلیمری", "description_fa": "اجرای ونیل تایل", "unit": "مترمربع", "quantity": 84.4, "source_fa": "شیت ونیل تایل"},
    {"item_id": "QS-020", "discipline": "ابنیه", "chapter_number": 25, "chapter_name": "رنگ‌آمیزی", "description_fa": "رنگ‌آمیزی دیوارها", "unit": "مترمربع", "quantity": 1920, "source_fa": "ریزمتره ابنیه"},

    # ============ مکانیک ============
    {"item_id": "QS-021", "discipline": "مکانیک", "chapter_number": 1, "chapter_name": "لوله", "description_fa": "لوله‌کشی فولادی سیاه سیستم گرمایش", "unit": "مترطول", "quantity": 285, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-022", "discipline": "مکانیک", "chapter_number": 3, "chapter_name": "لوله‌های پلی‌پروپلین", "description_fa": "لوله‌کشی پلی‌پروپلین آب گرم و سرد", "unit": "مترطول", "quantity": 420, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-023", "discipline": "مکانیک", "chapter_number": 4, "chapter_name": "لوله‌های پلی‌اتیلن", "description_fa": "لوله‌کشی پلی‌اتیلن آب باران", "unit": "مترطول", "quantity": 145, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-024", "discipline": "مکانیک", "chapter_number": 6, "chapter_name": "لوله‌های مسی", "description_fa": "لوله‌کشی مسی سیستم برودت سرور", "unit": "مترطول", "quantity": 68, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-025", "discipline": "مکانیک", "chapter_number": 19, "chapter_name": "کانال هوا و دریچه", "description_fa": "اجرای کانال هوای گالوانیزه", "unit": "مترمربع", "quantity": 385, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-026", "discipline": "مکانیک", "chapter_number": 19, "chapter_name": "کانال هوا و دریچه", "description_fa": "نصب دریچه‌های هوا (رفت و برگشت)", "unit": "عدد", "quantity": 285, "source_fa": "شیت ListDaricheh"},
    {"item_id": "QS-027", "discipline": "مکانیک", "chapter_number": 25, "chapter_name": "عایق الاستومری", "description_fa": "عایق‌کاری الاستومری لوله‌ها", "unit": "مترمربع", "quantity": 165, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-028", "discipline": "مکانیک", "chapter_number": 34, "chapter_name": "بست‌ها و تکیه‌گاه‌ها", "description_fa": "ساخت و نصب ساپورت لوله‌ها و کانال‌ها", "unit": "کیلوگرم", "quantity": 320, "source_fa": "ریزمتره مکانیک"},
    {"item_id": "QS-029", "discipline": "مکانیک", "chapter_number": None, "chapter_name": "تجهیزات", "description_fa": "نصب و راه‌اندازی هوارسان‌ها", "unit": "دستگاه", "quantity": 8, "source_fa": "شیت HVAC"},
    {"item_id": "QS-030", "discipline": "مکانیک", "chapter_number": None, "chapter_name": "تجهیزات", "description_fa": "نصب اگزاست فن‌ها", "unit": "دستگاه", "quantity": 7, "source_fa": "شیت HVAC"},
    {"item_id": "QS-031", "discipline": "مکانیک", "chapter_number": None, "chapter_name": "تجهیزات", "description_fa": "نصب سیستم برودت سرور (چیلر و فن‌کویل)", "unit": "دستگاه", "quantity": 5, "source_fa": "شیت HVAC"},
    {"item_id": "QS-032", "discipline": "مکانیک", "chapter_number": None, "chapter_name": "تجهیزات", "description_fa": "نصب شیرآلات بهداشتی", "unit": "عدد", "quantity": 30, "source_fa": "شیت Plumbing"},
    {"item_id": "QS-033", "discipline": "مکانیک", "chapter_number": None, "chapter_name": "تجهیزات", "description_fa": "نصب سرویس‌های بهداشتی (توالت، روشویی، دوش)", "unit": "عدد", "quantity": 48, "source_fa": "شیت Plumbing"},

    # ============ برق ============
    {"item_id": "QS-034", "discipline": "برق", "chapter_number": 6, "chapter_name": "سیم‌ها", "description_fa": "اجرای سیم افشان ۱.۵ و ۲.۵", "unit": "مترطول", "quantity": 480, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-035", "discipline": "برق", "chapter_number": 7, "chapter_name": "کابل‌های فشار ضعیف", "description_fa": "اجرای کابل زمینی NYY ۳×۱.۵ تا ۳×۶", "unit": "مترطول", "quantity": 771, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-036", "discipline": "برق", "chapter_number": 7, "chapter_name": "کابل‌های فشار ضعیف", "description_fa": "اجرای کابل شیلددار NYCY", "unit": "مترطول", "quantity": 126, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-037", "discipline": "برق", "chapter_number": 7, "chapter_name": "کابل‌های فشار ضعیف", "description_fa": "اجرای کابل صوتی و نسوز اعلام حریق", "unit": "مترطول", "quantity": 175, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-038", "discipline": "برق", "chapter_number": 12, "chapter_name": "لوله‌های فولادی", "description_fa": "لوله‌کشی توکار با لوله فولادی سایز ۱۶", "unit": "مترطول", "quantity": 306, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-039", "discipline": "برق", "chapter_number": 12, "chapter_name": "لوله‌های فولادی", "description_fa": "لوله‌کشی توکار PVC ۱۳.۵، ۱۶، ۲۱، ۲۹", "unit": "مترطول", "quantity": 350, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-040", "discipline": "برق", "chapter_number": 12, "chapter_name": "لوله‌های فولادی", "description_fa": "لوله‌کشی روکار یا توکار فلکسی", "unit": "مترطول", "quantity": 20, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-041", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب و راه‌اندازی تابلوهای برق", "unit": "عدد", "quantity": 10, "source_fa": "شیت تابلوها"},
    {"item_id": "QS-042", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب جعبه تقسیم", "unit": "عدد", "quantity": 95, "source_fa": "ریزمتره برق"},
    {"item_id": "QS-043", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب کلید و پریز", "unit": "عدد", "quantity": 826, "source_fa": "شیت کلید و پریز"},
    {"item_id": "QS-044", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب چراغ‌های روشنایی", "unit": "عدد", "quantity": 499, "source_fa": "شیت چراغ"},
    {"item_id": "QS-045", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب دتکتور اعلام حریق و شستی و زنگ", "unit": "عدد", "quantity": 360, "source_fa": "شیت Fire_Safety"},
    {"item_id": "QS-046", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "نصب پنل اعلام حریق آدرس‌پذیر ۸ لوپ", "unit": "دستگاه", "quantity": 1, "source_fa": "شیت Fire_Safety"},
    {"item_id": "QS-047", "discipline": "برق", "chapter_number": 28, "chapter_name": "متفرقه", "description_fa": "اجرای سینی کابل به عرض ۲۰۰، ۳۰۰ و ۵۰۰", "unit": "مترطول", "quantity": 134, "source_fa": "شیت Cables"},
]
# ============================================================
# شیت ۱۸: QS_Summary - خلاصه برآورد احجام
# ============================================================
QS_SUMMARY = [
    # --- ابنیه ---
    {"summary_id": "SUM-001", "discipline": "ابنیه", "category": "تخریب", "quantity": 850, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-002", "discipline": "ابنیه", "category": "بتن و بلوکاژ", "quantity": 132.7, "unit": "مترمکعب", "notes_fa": "بتن + سنگ قلوه"},
    {"summary_id": "SUM-003", "discipline": "ابنیه", "category": "گچ زیرکار و رویه", "quantity": 4630, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-004", "discipline": "ابنیه", "category": "گرانیت نهبندان", "quantity": 1050, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-005", "discipline": "ابنیه", "category": "سنگ مرمریت ۶۰×۶۰", "quantity": 1820, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-006", "discipline": "ابنیه", "category": "سنگ تراورتن نما", "quantity": 245, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-007", "discipline": "ابنیه", "category": "کفپوش ونیل", "quantity": 780, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-008", "discipline": "ابنیه", "category": "ونیل تایل", "quantity": 84.4, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-009", "discipline": "ابنیه", "category": "موزائیک", "quantity": 1180, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-010", "discipline": "ابنیه", "category": "کاشی و سرامیک", "quantity": 340.9, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-011", "discipline": "ابنیه", "category": "کف کاذب", "quantity": 199.75, "unit": "مترمربع", "notes_fa": "برای سرور روم، اتاق برق، یو پی اس"},

    # --- مکانیک ---
    {"summary_id": "SUM-012", "discipline": "مکانیک", "category": "لوله‌کشی فولادی", "quantity": 285, "unit": "مترطول", "notes_fa": None},
    {"summary_id": "SUM-013", "discipline": "مکانیک", "category": "لوله‌کشی پلی‌پروپلین", "quantity": 420, "unit": "مترطول", "notes_fa": None},
    {"summary_id": "SUM-014", "discipline": "مکانیک", "category": "کانال هوا", "quantity": 385, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-015", "discipline": "مکانیک", "category": "دریچه هوا", "quantity": 285, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-016", "discipline": "مکانیک", "category": "عایق الاستومری", "quantity": 165, "unit": "مترمربع", "notes_fa": None},

    # --- برق ---
    {"summary_id": "SUM-017", "discipline": "برق", "category": "سیم و کابل", "quantity": 1552, "unit": "مترطول", "notes_fa": "مجموع سیم و کابل"},
    {"summary_id": "SUM-018", "discipline": "برق", "category": "لوله‌کشی برق", "quantity": 676, "unit": "مترطول", "notes_fa": None},
    {"summary_id": "SUM-019", "discipline": "برق", "category": "چراغ", "quantity": 499, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-020", "discipline": "برق", "category": "کلید و پریز", "quantity": 826, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-021", "discipline": "برق", "category": "تابلو", "quantity": 10, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-022", "discipline": "برق", "category": "اعلام حریق", "quantity": 361, "unit": "عدد", "notes_fa": "دتکتور، شستی، زنگ، پنل"},

    # --- آکوستیک ---
    {"summary_id": "SUM-023", "discipline": "آکوستیک", "category": "تایل آکوستیک", "quantity": 1085, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-024", "discipline": "آکوستیک", "category": "کناف آکوستیک", "quantity": 842, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-025", "discipline": "آکوستیک", "category": "پشم سنگ (دانسیته ۸۰)", "quantity": 2240, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-026", "discipline": "آکوستیک", "category": "هبلکس (دیوار دوجداره)", "quantity": 1120, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-027", "discipline": "آکوستیک", "category": "وول‌پنل نورس‌پنل NP03", "quantity": 415, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-028", "discipline": "آکوستیک", "category": "پارچه دیواری نساج پایا", "quantity": 680, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-029", "discipline": "آکوستیک", "category": "MDF ازاره و دکوراتیو T107", "quantity": 460, "unit": "مترمربع", "notes_fa": None},
    {"summary_id": "SUM-030", "discipline": "آکوستیک", "category": "درب تمام آکوستیک", "quantity": 10, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-031", "discipline": "آکوستیک", "category": "درب نیمه‌آکوستیک", "quantity": 12, "unit": "عدد", "notes_fa": None},
    {"summary_id": "SUM-032", "discipline": "آکوستیک", "category": "پنجره ویزور آکوستیک", "quantity": 9, "unit": "عدد", "notes_fa": None},
]
# ============================================================
# شیت ۱۹: QS_Insulation - متره تفصیلی عایق‌ها
# ============================================================
QS_INSULATION = [
    {"row_id": "INS-001", "category": "عایق رطوبتی", "location_fa": "بام بلوک A", "area_m2": 320, "notes_fa": "ایزوگام پیش‌ساخته"},
    {"row_id": "INS-002", "category": "عایق رطوبتی", "location_fa": "بام بلوک B2", "area_m2": 125, "notes_fa": None},
    {"row_id": "INS-003", "category": "عایق رطوبتی", "location_fa": "سرویس‌های بهداشتی", "area_m2": 82, "notes_fa": "عایق زیر سرامیک"},
    {"row_id": "INS-004", "category": "عایق حرارتی لوله", "location_fa": "لوله‌های آب گرم و سرد", "length_m": 285, "notes_fa": "فوم پلی‌اتیلن ضخامت ۳ سانتی‌متر"},
    {"row_id": "INS-005", "category": "عایق الاستومری", "location_fa": "لوله‌های سیستم برودت و گرمایش", "length_m": 420, "notes_fa": "الاستومری انعطاف‌پذیر"},
    {"row_id": "INS-006", "category": "عایق حرارتی کانال", "location_fa": "کانال‌های هوا", "area_m2": 385, "notes_fa": "پشم شیشه ضخامت ۵ سانتی‌متر"},
    {"row_id": "INS-007", "category": "عایق صوتی", "location_fa": "کانال‌های اگزاست استودیوها", "area_m2": 65, "notes_fa": "پشم سنگ با روکش آلومینیوم"},
    {"row_id": "INS-008", "category": "عایق صوتی", "location_fa": "دیوار استودیوها", "area_m2": 1120, "notes_fa": "پشم سنگ دانسیته ۸۰"},
]
# ============================================================
# شیت ۲۰: QS_Acoustic - متره تفصیلی آکوستیک
# ============================================================
QS_ACOUSTIC = [
    # --- استودیوهای رادیویی ---
    {"row_id": "AC-001", "space_name_fa": "استودیو رادیویی A", "element": "دیوار", "area_m2": 185.4, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-002", "space_name_fa": "استودیو رادیویی A", "element": "سقف", "area_m2": 70.4, "material_fa": "کناف + MDF پانچ + وول‌پنل", "notes_fa": None},
    {"row_id": "AC-003", "space_name_fa": "استودیو رادیویی B", "element": "دیوار", "area_m2": 118.8, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-004", "space_name_fa": "استودیو رادیویی B", "element": "سقف", "area_m2": 37.9, "material_fa": "کناف + MDF پانچ + وول‌پنل", "notes_fa": None},
    {"row_id": "AC-005", "space_name_fa": "استودیو رادیویی C", "element": "دیوار", "area_m2": 96.4, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-006", "space_name_fa": "استودیو رادیویی C", "element": "سقف", "area_m2": 19.4, "material_fa": "کناف + MDF پانچ + وول‌پنل", "notes_fa": None},
    {"row_id": "AC-007", "space_name_fa": "استودیو رادیویی D", "element": "دیوار", "area_m2": 142.0, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-008", "space_name_fa": "استودیو رادیویی D", "element": "سقف", "area_m2": 33.9, "material_fa": "کناف + MDF پانچ + وول‌پنل", "notes_fa": None},

    # --- استودیوهای تلویزیونی ---
    {"row_id": "AC-009", "space_name_fa": "استودیو تلویزیونی A", "element": "دیوار", "area_m2": 890.6, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": "اجرا نشده"},
    {"row_id": "AC-010", "space_name_fa": "استودیو تلویزیونی B", "element": "دیوار", "area_m2": 165.9, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-011", "space_name_fa": "استودیو تلویزیونی C", "element": "دیوار", "area_m2": 611.5, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": "اجرا نشده"},
    {"row_id": "AC-012", "space_name_fa": "استودیو تلویزیونی D", "element": "دیوار", "area_m2": 144.9, "material_fa": "هبلکس + پشم سنگ + تایل آکوستیک", "notes_fa": "اجرا نشده"},

    # --- اتاق‌های کنترل ---
    {"row_id": "AC-013", "space_name_fa": "اتاق کنترل رادیویی A", "element": "دیوار", "area_m2": 141.0, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-014", "space_name_fa": "اتاق کنترل رادیویی B", "element": "دیوار", "area_m2": 106.6, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-015", "space_name_fa": "اتاق کنترل رادیویی C", "element": "دیوار", "area_m2": 96.7, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-016", "space_name_fa": "اتاق کنترل رادیویی D", "element": "دیوار", "area_m2": 117.5, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-017", "space_name_fa": "اتاق کنترل تلویزیونی A", "element": "دیوار", "area_m2": 166.0, "material_fa": "تایل آکوستیک", "notes_fa": "اجرا نشده"},
    {"row_id": "AC-018", "space_name_fa": "اتاق کنترل تلویزیونی B", "element": "دیوار", "area_m2": 148.5, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-019", "space_name_fa": "اتاق کنترل تلویزیونی C", "element": "دیوار", "area_m2": 159.2, "material_fa": "تایل آکوستیک", "notes_fa": "اجرا نشده"},
    {"row_id": "AC-020", "space_name_fa": "اتاق کنترل تلویزیونی D", "element": "دیوار", "area_m2": 140.9, "material_fa": "تایل آکوستیک", "notes_fa": "اجرا نشده"},

    # --- اتاق‌های ادیت و بازشنوایی ---
    {"row_id": "AC-021", "space_name_fa": "اتاق ادیت A", "element": "دیوار", "area_m2": 88.3, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-022", "space_name_fa": "اتاق ادیت B", "element": "دیوار", "area_m2": 58.4, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-023", "space_name_fa": "اتاق ادیت C", "element": "دیوار", "area_m2": 58.4, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-024", "space_name_fa": "اتاق ادیت D", "element": "دیوار", "area_m2": 57.0, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-025", "space_name_fa": "اتاق ادیت E", "element": "دیوار", "area_m2": 63.0, "material_fa": "تایل آکوستیک", "notes_fa": None},
    {"row_id": "AC-026", "space_name_fa": "اتاق بازشنوایی", "element": "دیوار", "area_m2": 69.0, "material_fa": "تایل آکوستیک", "notes_fa": "اجرا نشده"},

    # --- جمع‌ها ---
    {"row_id": "AC-100", "space_name_fa": "جمع کل - تایل آکوستیک دیوار", "element": "دیوار", "area_m2": 1085.0, "material_fa": "جمع", "notes_fa": None},
    {"row_id": "AC-101", "space_name_fa": "جمع کل - کناف آکوستیک سقف", "element": "سقف", "area_m2": 842.0, "material_fa": "جمع", "notes_fa": None},
    {"row_id": "AC-102", "space_name_fa": "جمع کل - پشم سنگ دیوار", "element": "دیوار", "area_m2": 1120.0, "material_fa": "جمع", "notes_fa": None},
    {"row_id": "AC-103", "space_name_fa": "جمع کل - وول‌پنل نورس‌پنل", "element": "سقف", "area_m2": 415.0, "material_fa": "جمع", "notes_fa": None},
]
# ============================================================
# شیت ۲۱: Milestones - نقاط عطف پروژه
# ============================================================
MILESTONES = [
    {"milestone_id": "M-001", "name_fa": "شروع پروژه", "phase": "شروع", "status_fa": "انجام شده", "is_completed": True, "notes_fa": "شروع رسمی قرارداد"},
    {"milestone_id": "M-002", "name_fa": "تحویل نقشه‌های اجرایی", "phase": "شروع", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-003", "name_fa": "پایان سفت‌کاری بلوک A", "phase": "اجرا", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-004", "name_fa": "پایان سفت‌کاری بلوک B2", "phase": "اجرا", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-005", "name_fa": "پایان سفت‌کاری بلوک B3", "phase": "اجرا", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-006", "name_fa": "اتمام تأسیسات مکانیکی", "phase": "اجرا", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-007", "name_fa": "اتمام تأسیسات برقی", "phase": "اجرا", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-008", "name_fa": "تحویل زون‌های کلیدی (B2 شمالی)", "phase": "تحویل", "status_fa": "انجام شده", "is_completed": True, "notes_fa": "شامل هر دو طبقه همکف و اول"},
    {"milestone_id": "M-009", "name_fa": "تحویل بلوک A - همکف", "phase": "تحویل", "status_fa": "انجام شده", "is_completed": True, "notes_fa": "۴ استودیو رادیویی + اتاق‌های مجاور"},
    {"milestone_id": "M-010", "name_fa": "تحویل بلوک B3 - تحریریه", "phase": "تحویل", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-011", "name_fa": "تحویل موقت پروژه", "phase": "تحویل", "status_fa": "انجام شده", "is_completed": True, "notes_fa": None},
    {"milestone_id": "M-012", "name_fa": "بهره‌برداری رسمی", "phase": "تحویل", "status_fa": "در حال بهره‌برداری", "is_completed": True, "notes_fa": "پروژه در بهره‌برداری"},
]
# ============================================================
# شیت ۲۲: Schedule_Activities - فعالیت‌های زمان‌بندی (سلسله‌مراتبی)
# ============================================================
SCHEDULE_ACTIVITIES = [
    # ============ فاز ۱: ابنیه ============
    {"activity_id": "SA-001", "wbs": "1", "phase": "ابنیه", "block": None, "activity_fa": "فعالیت‌های ابنیه", "activity_type": "خلاصه", "duration_days": None, "predecessors": None, "executed": True},

    # --- سفت‌کاری بلوک A ---
    {"activity_id": "SA-002", "wbs": "1.1", "phase": "ابنیه", "block": "A", "activity_fa": "سفت‌کاری بلوک A", "activity_type": "خلاصه", "duration_days": 30, "predecessors": None, "executed": True},
    {"activity_id": "SA-003", "wbs": "1.1.1", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای دیوار هبلکس استودیوها", "activity_type": "اجرا", "duration_days": 12, "predecessors": "SA-002", "executed": True},
    {"activity_id": "SA-004", "wbs": "1.1.2", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای بتن کف‌سازی", "activity_type": "اجرا", "duration_days": 8, "predecessors": "SA-003", "executed": True},
    {"activity_id": "SA-005", "wbs": "1.1.3", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای بلوکاژ و زیرسازی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-002", "executed": True},

    # --- نازک‌کاری بلوک A ---
    {"activity_id": "SA-006", "wbs": "1.2", "phase": "ابنیه", "block": "A", "activity_fa": "نازک‌کاری بلوک A", "activity_type": "خلاصه", "duration_days": 60, "predecessors": "SA-002", "executed": True},
    {"activity_id": "SA-007", "wbs": "1.2.1", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای قرنیز", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-006", "executed": True},
    {"activity_id": "SA-008", "wbs": "1.2.2", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای سنگ دیوار", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-007", "executed": True},
    {"activity_id": "SA-009", "wbs": "1.2.3", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای لایه گچ دیوارها", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-008", "executed": True},
    {"activity_id": "SA-010", "wbs": "1.2.4", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای سقف تایل", "activity_type": "اجرا", "duration_days": 5, "predecessors": "SA-009", "executed": True},
    {"activity_id": "SA-011", "wbs": "1.2.5", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای سنگ کف", "activity_type": "اجرا", "duration_days": 5, "predecessors": "SA-010", "executed": True},

    # --- نازک‌کاری استودیوهای رادیویی ---
    {"activity_id": "SA-012", "wbs": "1.3", "phase": "ابنیه", "block": "A", "activity_fa": "استودیوهای رادیویی A تا D", "activity_type": "خلاصه", "duration_days": 140, "predecessors": "SA-002", "executed": True},
    {"activity_id": "SA-013", "wbs": "1.3.1", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای قرنیز استودیوهای رادیویی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-012", "executed": True},
    {"activity_id": "SA-014", "wbs": "1.3.2", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای دیوار از تایل آکوستیک", "activity_type": "اجرا", "duration_days": 30, "predecessors": "SA-013", "executed": True},
    {"activity_id": "SA-015", "wbs": "1.3.3", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای سقف کناف آکوستیک", "activity_type": "اجرا", "duration_days": 30, "predecessors": "SA-014", "executed": True},
    {"activity_id": "SA-016", "wbs": "1.3.4", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای موزائیک کف", "activity_type": "اجرا", "duration_days": 8, "predecessors": "SA-015", "executed": True},
    {"activity_id": "SA-017", "wbs": "1.3.5", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای موکت کف استودیو", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-016", "executed": True},
    {"activity_id": "SA-018", "wbs": "1.3.6", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای کفپوش ونیل", "activity_type": "اجرا", "duration_days": 8, "predecessors": "SA-016", "executed": True},

    # --- نازک‌کاری استودیو تلویزیونی B ---
    {"activity_id": "SA-019", "wbs": "1.4", "phase": "ابنیه", "block": "A", "activity_fa": "استودیو تلویزیونی B", "activity_type": "خلاصه", "duration_days": 80, "predecessors": "SA-002", "executed": True},
    {"activity_id": "SA-020", "wbs": "1.4.1", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای قرنیز", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-019", "executed": True},
    {"activity_id": "SA-021", "wbs": "1.4.2", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای دیوار از تایل آکوستیک", "activity_type": "اجرا", "duration_days": 30, "predecessors": "SA-020", "executed": True},
    {"activity_id": "SA-022", "wbs": "1.4.3", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای سقف کناف آکوستیک", "activity_type": "اجرا", "duration_days": 20, "predecessors": "SA-021", "executed": True},
    {"activity_id": "SA-023", "wbs": "1.4.4", "phase": "ابنیه", "block": "A", "activity_fa": "اجرای موزائیک کف", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-022", "executed": True},

    # --- سفت‌کاری و نازک‌کاری بلوک B2 (شمالی و جنوبی) ---
    {"activity_id": "SA-024", "wbs": "1.5", "phase": "ابنیه", "block": "B2", "activity_fa": "بلوک B2 - بال شمالی", "activity_type": "خلاصه", "duration_days": 200, "predecessors": None, "executed": True},
    {"activity_id": "SA-025", "wbs": "1.5.1", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای اندود سیمانی راهرو", "activity_type": "اجرا", "duration_days": 5, "predecessors": "SA-024", "executed": True},
    {"activity_id": "SA-026", "wbs": "1.5.2", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای قرنیز راهرو", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-025", "executed": True},
    {"activity_id": "SA-027", "wbs": "1.5.3", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای سنگ دیوار", "activity_type": "اجرا", "duration_days": 14, "predecessors": "SA-026", "executed": True},
    {"activity_id": "SA-028", "wbs": "1.5.4", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای لایه گچ دیوارها", "activity_type": "اجرا", "duration_days": 2, "predecessors": "SA-027", "executed": True},
    {"activity_id": "SA-029", "wbs": "1.5.5", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای لایه گچ رویه", "activity_type": "اجرا", "duration_days": 2, "predecessors": "SA-028", "executed": True},
    {"activity_id": "SA-030", "wbs": "1.5.6", "phase": "ابنیه", "block": "B2", "activity_fa": "رنگ‌آمیزی دیوارها", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-029", "executed": True},
    {"activity_id": "SA-031", "wbs": "1.5.7", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای سقف تایل", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-030", "executed": True},
    {"activity_id": "SA-032", "wbs": "1.5.8", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای سنگ کف", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-031", "executed": True},

    # --- اتاق‌های اداری فنی B2 (تکرار برای ۲۲ اتاق) ---
    {"activity_id": "SA-033", "wbs": "1.6", "phase": "ابنیه", "block": "B2", "activity_fa": "اتاق‌های اداری فنی ۱ تا ۱۶", "activity_type": "خلاصه", "duration_days": 85, "predecessors": "SA-024", "executed": True},
    {"activity_id": "SA-034", "wbs": "1.6.1", "phase": "ابنیه", "block": "B2", "activity_fa": "مضرس کردن لایه گچ موجود", "activity_type": "اجرا", "duration_days": 1, "predecessors": "SA-033", "executed": True},
    {"activity_id": "SA-035", "wbs": "1.6.2", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای لایه گچ رویه", "activity_type": "اجرا", "duration_days": 2, "predecessors": "SA-034", "executed": True},
    {"activity_id": "SA-036", "wbs": "1.6.3", "phase": "ابنیه", "block": "B2", "activity_fa": "رنگ‌آمیزی دیوار", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-035", "executed": True},
    {"activity_id": "SA-037", "wbs": "1.6.4", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای سقف کاذب", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-035", "executed": True},
    {"activity_id": "SA-038", "wbs": "1.6.5", "phase": "ابنیه", "block": "B2", "activity_fa": "اجرای سنگ کف", "activity_type": "اجرا", "duration_days": 2, "predecessors": "SA-037", "executed": True},

    # --- بلوک B3 ---
    {"activity_id": "SA-039", "wbs": "1.7", "phase": "ابنیه", "block": "B3", "activity_fa": "بلوک B3 - سفت‌کاری و نازک‌کاری", "activity_type": "خلاصه", "duration_days": 206, "predecessors": None, "executed": True},
    {"activity_id": "SA-040", "wbs": "1.7.1", "phase": "ابنیه", "block": "B3", "activity_fa": "اجرای رمپ ورودی تحریریه", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-039", "executed": True},
    {"activity_id": "SA-041", "wbs": "1.7.2", "phase": "ابنیه", "block": "B3", "activity_fa": "اجرای سنگ رمپ", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-040", "executed": True},
    {"activity_id": "SA-042", "wbs": "1.7.3", "phase": "ابنیه", "block": "B3", "activity_fa": "اجرای لایه گچ دیوار تحریریه", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-039", "executed": True},
    {"activity_id": "SA-043", "wbs": "1.7.4", "phase": "ابنیه", "block": "B3", "activity_fa": "اجرای سقف کاذب تحریریه", "activity_type": "اجرا", "duration_days": 5, "predecessors": "SA-042", "executed": True},
    {"activity_id": "SA-044", "wbs": "1.7.5", "phase": "ابنیه", "block": "B3", "activity_fa": "اجرای نما با آجر آذرخش", "activity_type": "اجرا", "duration_days": 4, "predecessors": "SA-039", "executed": True},

    # ============ فاز ۲: تأسیسات الکتریکال ============
    {"activity_id": "SA-045", "wbs": "2", "phase": "برق", "block": None, "activity_fa": "تأسیسات الکتریکال", "activity_type": "خلاصه", "duration_days": None, "predecessors": None, "executed": True},

    # --- بلوک A ---
    {"activity_id": "SA-046", "wbs": "2.1", "phase": "برق", "block": "A", "activity_fa": "تأسیسات برقی بلوک A", "activity_type": "خلاصه", "duration_days": 100, "predecessors": None, "executed": True},
    {"activity_id": "SA-047", "wbs": "2.1.1", "phase": "برق", "block": "A", "activity_fa": "علامت‌گذاری محل قوطی‌ها", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-046", "executed": True},
    {"activity_id": "SA-048", "wbs": "2.1.2", "phase": "برق", "block": "A", "activity_fa": "اجرای شیارهای علامت‌گذاری شده", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-047", "executed": True},
    {"activity_id": "SA-049", "wbs": "2.1.3", "phase": "برق", "block": "A", "activity_fa": "ساخت و نصب ساپورت لوله‌های برق", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-048", "executed": True},
    {"activity_id": "SA-050", "wbs": "2.1.4", "phase": "برق", "block": "A", "activity_fa": "اجرای قوطی کلید و پریز", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-049", "executed": True},
    {"activity_id": "SA-051", "wbs": "2.1.5", "phase": "برق", "block": "A", "activity_fa": "لوله‌گذاری‌های عمودی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-050", "executed": True},
    {"activity_id": "SA-052", "wbs": "2.1.6", "phase": "برق", "block": "A", "activity_fa": "لوله‌گذاری افقی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-051", "executed": True},
    {"activity_id": "SA-053", "wbs": "2.1.7", "phase": "برق", "block": "A", "activity_fa": "رایزر", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-052", "executed": True},
    {"activity_id": "SA-054", "wbs": "2.1.8", "phase": "برق", "block": "A", "activity_fa": "اجرای سینی‌های زیر سقف", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-052", "executed": True},
    {"activity_id": "SA-055", "wbs": "2.1.9", "phase": "برق", "block": "A", "activity_fa": "اجرای سیم‌کشی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-053", "executed": True},
    {"activity_id": "SA-056", "wbs": "2.1.10", "phase": "برق", "block": "A", "activity_fa": "اعلام حریق، ارتباطات داخلی و تجهیزات کنترلی", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-055", "executed": True},
    {"activity_id": "SA-057", "wbs": "2.1.11", "phase": "برق", "block": "A", "activity_fa": "نصب تابلوهای برق", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-056", "executed": True},
    {"activity_id": "SA-058", "wbs": "2.1.12", "phase": "برق", "block": "A", "activity_fa": "نصب جعبه تقسیم", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-057", "executed": True},
    {"activity_id": "SA-059", "wbs": "2.1.13", "phase": "برق", "block": "A", "activity_fa": "سربندی و کنترل خطوط در محل مصرف", "activity_type": "اجرا", "duration_days": 7, "predecessors": "SA-058", "executed": True},
    {"activity_id": "SA-060", "wbs": "2.1.14", "phase": "برق", "block": "A", "activity_fa": "آماده‌سازی محل نصب تجهیزات", "activity_type": "اجرا", "duration_days": 3, "predecessors": "SA-059", "executed": True},

    # --- بلوک B2 و B1 (نماینده) ---
    {"activity_id": "SA-061", "wbs": "2.2", "phase": "برق", "block": "B2", "activity_fa": "تأسیسات برقی بلوک B2", "activity_type": "خلاصه", "duration_days": 80, "predecessors": None, "executed": True},
    {"activity_id": "SA-062", "wbs": "2.3", "phase": "برق", "block": "B1", "activity_fa": "تأسیسات برقی بلوک B1", "activity_type": "خلاصه", "duration_days": 60, "predecessors": None, "executed": True},

    # ============ فاز ۳: تأسیسات مکانیکی ============
    {"activity_id": "SA-063", "wbs": "3", "phase": "مکانیک", "block": None, "activity_fa": "تأسیسات مکانیکی", "activity_type": "خلاصه", "duration_days": None, "predecessors": None, "executed": True},
    {"activity_id": "SA-064", "wbs": "3.1", "phase": "مکانیک", "block": "A", "activity_fa": "تأسیسات مکانیکی بلوک A", "activity_type": "خلاصه", "duration_days": 250, "predecessors": None, "executed": True},
    {"activity_id": "SA-065", "wbs": "3.1.1", "phase": "مکانیک", "block": "A", "activity_fa": "ورود مصالح به کارگاه", "activity_type": "اجرا", "duration_days": 0, "predecessors": None, "executed": True},
    {"activity_id": "SA-066", "wbs": "3.1.2", "phase": "مکانیک", "block": "A", "activity_fa": "اجرای کانال‌های هوا", "activity_type": "اجرا", "duration_days": 80, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-067", "wbs": "3.1.3", "phase": "مکانیک", "block": "A", "activity_fa": "اجرای لوله‌کشی سیستم گرمایش", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-068", "wbs": "3.1.4", "phase": "مکانیک", "block": "A", "activity_fa": "آبرسانی سرد و گرم", "activity_type": "اجرا", "duration_days": 15, "predecessors": "SA-067", "executed": True},
    {"activity_id": "SA-069", "wbs": "3.1.5", "phase": "مکانیک", "block": "A", "activity_fa": "اجرای فاضلاب و ونت", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-070", "wbs": "3.1.6", "phase": "مکانیک", "block": "A", "activity_fa": "حفر چاه جذبی", "activity_type": "اجرا", "duration_days": 20, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-071", "wbs": "3.1.7", "phase": "مکانیک", "block": "A", "activity_fa": "لوله‌کشی سیستم برودت سرور", "activity_type": "اجرا", "duration_days": 5, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-072", "wbs": "3.1.8", "phase": "مکانیک", "block": "A", "activity_fa": "نصب تجهیزات سیستم برودت", "activity_type": "اجرا", "duration_days": 20, "predecessors": "SA-071", "executed": True},
    {"activity_id": "SA-073", "wbs": "3.1.9", "phase": "مکانیک", "block": "A", "activity_fa": "لوله‌کشی تهویه مطبوع هواساز", "activity_type": "اجرا", "duration_days": 40, "predecessors": "SA-065", "executed": True},
    {"activity_id": "SA-074", "wbs": "3.1.10", "phase": "مکانیک", "block": "A", "activity_fa": "کانال‌های رفت و برگشت هواساز", "activity_type": "اجرا", "duration_days": 60, "predecessors": "SA-073", "executed": True},
    {"activity_id": "SA-075", "wbs": "3.1.11", "phase": "مکانیک", "block": "A", "activity_fa": "راه‌اندازی و تست سیستم هواساز", "activity_type": "اجرا", "duration_days": 8, "predecessors": "SA-074", "executed": True},
    {"activity_id": "SA-076", "wbs": "3.1.12", "phase": "مکانیک", "block": "A", "activity_fa": "اجرای اگزاست فن‌ها", "activity_type": "اجرا", "duration_days": 28, "predecessors": "SA-065", "executed": True},

    # --- بلوک B2 مکانیک (نماینده) ---
    {"activity_id": "SA-077", "wbs": "3.2", "phase": "مکانیک", "block": "B2", "activity_fa": "تأسیسات مکانیکی بلوک B2", "activity_type": "خلاصه", "duration_days": 230, "predecessors": None, "executed": True},
    {"activity_id": "SA-078", "wbs": "3.2.1", "phase": "مکانیک", "block": "B2", "activity_fa": "اجرای کانال‌های هوای بلوک B2", "activity_type": "اجرا", "duration_days": 87, "predecessors": "SA-077", "executed": True},
    {"activity_id": "SA-079", "wbs": "3.2.2", "phase": "مکانیک", "block": "B2", "activity_fa": "لوله‌کشی فاضلاب و ونت", "activity_type": "اجرا", "duration_days": 10, "predecessors": "SA-077", "executed": True},
    {"activity_id": "SA-080", "wbs": "3.2.3", "phase": "مکانیک", "block": "B2", "activity_fa": "سیستم برودت سرور روم و ماشین روم", "activity_type": "اجرا", "duration_days": 25, "predecessors": "SA-077", "executed": True},

    # ============ فاز ۴: تحویل و راه‌اندازی ============
    {"activity_id": "SA-081", "wbs": "4", "phase": "تحویل", "block": None, "activity_fa": "تحویل و راه‌اندازی", "activity_type": "خلاصه", "duration_days": None, "predecessors": None, "executed": True},
    {"activity_id": "SA-082", "wbs": "4.1", "phase": "تحویل", "block": "B2", "activity_fa": "تحویل بال شمالی B2 - همکف", "activity_type": "نقطه عطف", "duration_days": 2, "predecessors": "SA-032", "executed": True},
    {"activity_id": "SA-083", "wbs": "4.2", "phase": "تحویل", "block": "B2", "activity_fa": "تحویل بال شمالی B2 - طبقه اول", "activity_type": "نقطه عطف", "duration_days": 2, "predecessors": "SA-038", "executed": True},
    {"activity_id": "SA-084", "wbs": "4.3", "phase": "تحویل", "block": "A", "activity_fa": "تحویل بلوک A - همکف (۴ استودیو رادیویی)", "activity_type": "نقطه عطف", "duration_days": 2, "predecessors": "SA-018", "executed": True},
    {"activity_id": "SA-085", "wbs": "4.4", "phase": "تحویل", "block": "A", "activity_fa": "تحویل بلوک A - طبقه اول (شرقی)", "activity_type": "نقطه عطف", "duration_days": 2, "predecessors": "SA-006", "executed": True},
    {"activity_id": "SA-086", "wbs": "4.5", "phase": "تحویل", "block": "B3", "activity_fa": "تحویل بلوک B3 - تحریریه خبر", "activity_type": "نقطه عطف", "duration_days": 2, "predecessors": "SA-044", "executed": True},
    {"activity_id": "SA-087", "wbs": "4.6", "phase": "تحویل", "block": None, "activity_fa": "تحویل موقت پروژه", "activity_type": "نقطه عطف", "duration_days": 3, "predecessors": "SA-082,SA-083,SA-084,SA-085,SA-086", "executed": True},
    {"activity_id": "SA-088", "wbs": "4.7", "phase": "تحویل", "block": None, "activity_fa": "تحویل قطعی و بهره‌برداری", "activity_type": "نقطه عطف", "duration_days": 1, "predecessors": "SA-087", "executed": True},
]
# ============================================================
# شیت ۲۳: Meetings_Summary - خلاصه صورت‌جلسات
# ============================================================
MEETINGS_SUMMARY = [
    # --- ابنیه ---
    {"meeting_id": "MT-001", "discipline": "ابنیه", "chapter": "تخریب", "topic_fa": "احجام تخریب و برداشت نخاله", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-002", "discipline": "ابنیه", "chapter": "بنایی با سنگ", "topic_fa": "احجام بنایی با سنگ", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-003", "discipline": "ابنیه", "chapter": "بتن درجا", "topic_fa": "احجام بتن‌ریزی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-004", "discipline": "ابنیه", "chapter": "کارهای فولادی سنگین", "topic_fa": "احجام وال پست و نبشی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-005", "discipline": "ابنیه", "chapter": "آجرکاری و شفته‌ریزی", "topic_fa": "احجام آجرکاری نما", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-006", "discipline": "ابنیه", "chapter": "عایق‌کاری رطوبتی", "topic_fa": "احجام عایق رطوبتی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-007", "discipline": "ابنیه", "chapter": "عایق‌کاری حرارتی", "topic_fa": "احجام عایق حرارتی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-008", "discipline": "ابنیه", "chapter": "کارهای فولادی سبک", "topic_fa": "احجام وال پست سبک", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-009", "discipline": "ابنیه", "chapter": "اندودکاری و بندکشی", "topic_fa": "احجام گچ‌کاری", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-010", "discipline": "ابنیه", "chapter": "کارهای چوبی", "topic_fa": "احجام درب و چارچوب", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-011", "discipline": "ابنیه", "chapter": "کاشی و سرامیک", "topic_fa": "احجام کاشی و سرامیک", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-012", "discipline": "ابنیه", "chapter": "موزائیک", "topic_fa": "احجام موزائیک", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-013", "discipline": "ابنیه", "chapter": "کارهای سنگی", "topic_fa": "احجام سنگ پلاک", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-014", "discipline": "ابنیه", "chapter": "کارهای پلاستیکی و پلیمری", "topic_fa": "احجام ونیل و کفپوش", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-015", "discipline": "ابنیه", "chapter": "رنگ‌آمیزی", "topic_fa": "احجام رنگ‌آمیزی", "meeting_count": 1, "executed": True},

    # --- مکانیک ---
    {"meeting_id": "MT-016", "discipline": "مکانیک", "chapter": "لوله", "topic_fa": "احجام لوله‌کشی فولادی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-017", "discipline": "مکانیک", "chapter": "لوله پلی‌پروپلین", "topic_fa": "احجام لوله‌کشی پلی‌پروپلین", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-018", "discipline": "مکانیک", "chapter": "لوله پلی‌اتیلن", "topic_fa": "احجام لوله‌کشی پلی‌اتیلن", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-019", "discipline": "مکانیک", "chapter": "لوله مسی", "topic_fa": "احجام لوله‌کشی مسی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-020", "discipline": "مکانیک", "chapter": "کانال هوا و دریچه", "topic_fa": "احجام کانال و دریچه", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-021", "discipline": "مکانیک", "chapter": "عایق الاستومری", "topic_fa": "احجام عایق الاستومری", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-022", "discipline": "مکانیک", "chapter": "بست‌ها و تکیه‌گاه‌ها", "topic_fa": "احجام ساپورت‌ها", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-023", "discipline": "مکانیک", "chapter": "نصبیات سرویس‌ها", "topic_fa": "نصب سرویس‌های بهداشتی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-024", "discipline": "مکانیک", "chapter": "هوارسان‌ها", "topic_fa": "راه‌اندازی هوارسان‌ها", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-025", "discipline": "مکانیک", "chapter": "موتورخانه", "topic_fa": "احجام موتورخانه", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-026", "discipline": "مکانیک", "chapter": "نرده‌های حفاظ", "topic_fa": "ساخت نرده", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-027", "discipline": "مکانیک", "chapter": "صداگیرها", "topic_fa": "احجام صداگیرها", "meeting_count": 1, "executed": True},

    # --- برق ---
    {"meeting_id": "MT-028", "discipline": "برق", "chapter": "سیم‌ها", "topic_fa": "احجام سیم‌کشی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-029", "discipline": "برق", "chapter": "کابل‌های فشار ضعیف", "topic_fa": "احجام کابل‌کشی", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-030", "discipline": "برق", "chapter": "لوله‌کشی فولادی", "topic_fa": "لوله‌کشی برق در بلوک‌ها", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-031", "discipline": "برق", "chapter": "تابلوها", "topic_fa": "نصب تابلوهای برق", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-032", "discipline": "برق", "chapter": "متفرقه", "topic_fa": "احجام متفرقه برق", "meeting_count": 1, "executed": True},

    # --- بازدیدهای کارفرما ---
    {"meeting_id": "MT-033", "discipline": "بازدید", "chapter": "بازدید کارفرما", "topic_fa": "بازدید کارگاهی کارفرما - مرحله اول", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-034", "discipline": "بازدید", "chapter": "بازدید کارفرما", "topic_fa": "بازدید کارگاهی کارفرما - مرحله دوم", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-035", "discipline": "بازدید", "chapter": "بازدید کارفرما", "topic_fa": "بازدید کارگاهی کارفرما - مرحله سوم", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-036", "discipline": "بازدید", "chapter": "تحویل موقت", "topic_fa": "جلسه تحویل موقت پروژه", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-037", "discipline": "بازدید", "chapter": "لاین نوری", "topic_fa": "جلسه بررسی لاین نوری با پیمانکار برق", "meeting_count": 1, "executed": True},

    # --- صورت‌جلسات تکمیلی ---
    {"meeting_id": "MT-038", "discipline": "تکمیلی", "chapter": "ابنیه", "topic_fa": "صورت‌جلسات تکمیلی ابنیه - ۱۴۰۴", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-039", "discipline": "تکمیلی", "chapter": "برق", "topic_fa": "صورت‌جلسات تکمیلی برق - ۱۴۰۴", "meeting_count": 1, "executed": True},
    {"meeting_id": "MT-040", "discipline": "تکمیلی", "chapter": "مکانیک", "topic_fa": "صورت‌جلسات تکمیلی مکانیک - ۱۴۰۴", "meeting_count": 1, "executed": True},
]
# ============================================================
# شیت ۲۴: Assets - فایل‌های گرافیکی و مستندات
# ============================================================
ASSETS = [
    # --- تصاویر جلد و نمای کلی ---
    {"asset_id": "AS-001", "asset_type": "cover", "name_fa": "تصویر جلد پروژه", "file_path": "/assets/covers/P-001-cover.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "وب‌سایت، PDF، شبکه‌های اجتماعی", "notes_fa": "نمای کلی ساختمان"},
    {"asset_id": "AS-002", "asset_type": "hero", "name_fa": "تصویر هدر صفحه پروژه", "file_path": "/assets/covers/P-001-hero.jpg", "dimensions": "2400x1200", "is_public": True, "used_for": "وب‌سایت", "notes_fa": "نمای بیرونی ساختمان"},
    {"asset_id": "AS-003", "asset_type": "thumbnail", "name_fa": "تصویر بندانگشتی", "file_path": "/assets/covers/P-001-thumb.jpg", "dimensions": "600x400", "is_public": True, "used_for": "لیست پروژه‌ها", "notes_fa": None},

    # --- نقشه‌های معماری ---
    {"asset_id": "AS-004", "asset_type": "plan", "name_fa": "نقشه طبقه همکف - بلوک A و B", "file_path": "/assets/plans/ground-floor-AB.pdf", "dimensions": "A1", "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": "ناشناس‌شده"},
    {"asset_id": "AS-005", "asset_type": "plan", "name_fa": "نقشه طبقه اول - بلوک A و B", "file_path": "/assets/plans/first-floor-AB.pdf", "dimensions": "A1", "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": "ناشناس‌شده"},
    {"asset_id": "AS-006", "asset_type": "plan", "name_fa": "نقشه بلوک B3 - تحریریه", "file_path": "/assets/plans/block-B3.pdf", "dimensions": "A2", "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": None},
    {"asset_id": "AS-007", "asset_type": "plan", "name_fa": "نقشه بلوک B1 - مرکزی", "file_path": "/assets/plans/block-B1.pdf", "dimensions": "A2", "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": None},

    # --- برش‌ها و جزئیات ---
    {"asset_id": "AS-008", "asset_type": "section", "name_fa": "برش طولی ساختمان", "file_path": "/assets/sections/longitudinal.jpg", "dimensions": "A2", "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": None},
    {"asset_id": "AS-009", "asset_type": "detail", "name_fa": "جزئیات لایه‌بندی دیوار آکوستیک", "file_path": "/assets/details/acoustic-wall.jpg", "dimensions": "1200x800", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "دیاگرام ساده‌شده"},
    {"asset_id": "AS-010", "asset_type": "detail", "name_fa": "جزئیات لایه‌بندی سقف آکوستیک", "file_path": "/assets/details/acoustic-ceiling.jpg", "dimensions": "1200x800", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-011", "asset_type": "detail", "name_fa": "برش درب آکوستیک", "file_path": "/assets/details/acoustic-door.jpg", "dimensions": "1200x800", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-012", "asset_type": "detail", "name_fa": "جزئیات پنجره ویزور", "file_path": "/assets/details/visor-window.jpg", "dimensions": "1200x800", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-013", "asset_type": "detail", "name_fa": "جزئیات ایرلاک صوتی", "file_path": "/assets/details/airlock.jpg", "dimensions": "1200x800", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- رندرهای سه‌بعدی ---
    {"asset_id": "AS-014", "asset_type": "render", "name_fa": "رندر سه‌بعدی بلوک B3 - نمای بیرونی", "file_path": "/assets/renders/B3-exterior.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-015", "asset_type": "render", "name_fa": "رندر سه‌بعدی بلوک B3 - نمای داخلی", "file_path": "/assets/renders/B3-interior.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-016", "asset_type": "render", "name_fa": "رندر استودیو رادیویی", "file_path": "/assets/renders/radio-studio.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-017", "asset_type": "render", "name_fa": "رندر دکوراسیون لابی B1", "file_path": "/assets/renders/B1-lobby.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- عکس‌های اجرا (Before) ---
    {"asset_id": "AS-018", "asset_type": "photo-before", "name_fa": "عکس قبل از اجرا - سقف استودیو", "file_path": "/assets/photos/before-studio-ceiling.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "نمایش زیرسازی"},
    {"asset_id": "AS-019", "asset_type": "photo-before", "name_fa": "عکس قبل از اجرا - دیوارهای استودیو", "file_path": "/assets/photos/before-studio-wall.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- عکس‌های اجرا (During) ---
    {"asset_id": "AS-020", "asset_type": "photo-during", "name_fa": "عکس حین اجرا - نصب پانل‌های پانچ‌شده", "file_path": "/assets/photos/during-punch-panel.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "با لیزر تراز"},
    {"asset_id": "AS-021", "asset_type": "photo-during", "name_fa": "عکس حین اجرا - نصب درب آکوستیک", "file_path": "/assets/photos/during-acoustic-door.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "با پانیک بار"},
    {"asset_id": "AS-022", "asset_type": "photo-during", "name_fa": "عکس حین اجرا - کانال‌های هوا و شاسی‌کشی", "file_path": "/assets/photos/during-hvac-framing.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-023", "asset_type": "photo-during", "name_fa": "عکس حین اجرا - تایل آکوستیک دیوار", "file_path": "/assets/photos/during-acoustic-wall.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- عکس‌های نهایی (After) ---
    {"asset_id": "AS-024", "asset_type": "photo-after", "name_fa": "عکس نهایی - استودیو رادیویی کامل", "file_path": "/assets/photos/after-radio-studio.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-025", "asset_type": "photo-after", "name_fa": "عکس نهایی - سقف آکوستیک و روشنایی", "file_path": "/assets/photos/after-ceiling-lighting.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-026", "asset_type": "photo-after", "name_fa": "عکس نهایی - لابی B1", "file_path": "/assets/photos/after-B1-lobby.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-027", "asset_type": "photo-after", "name_fa": "عکس نهایی - نمای بیرونی", "file_path": "/assets/photos/after-exterior.jpg", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- نمودارها و دیاگرام‌ها ---
    {"asset_id": "AS-028", "asset_type": "chart", "name_fa": "نمودار WBS پروژه", "file_path": "/assets/charts/wbs.png", "dimensions": "1920x1080", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "سلسله‌مراتبی"},
    {"asset_id": "AS-029", "asset_type": "chart", "name_fa": "گانت چارت برنامه", "file_path": "/assets/charts/gantt.png", "dimensions": "2400x1600", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "استخراج از MPP"},
    {"asset_id": "AS-030", "asset_type": "chart", "name_fa": "نمودار S-Curve شماتیک", "file_path": "/assets/charts/s-curve.png", "dimensions": "1600x1000", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": "شماتیک - بر پایه مدت فعالیت‌ها"},
    {"asset_id": "AS-031", "asset_type": "chart", "name_fa": "نمودار توزیع متره به تفکیک رشته", "file_path": "/assets/charts/qs-distribution.png", "dimensions": "1600x1000", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},
    {"asset_id": "AS-032", "asset_type": "chart", "name_fa": "نمودار نسبت احجام آکوستیک", "file_path": "/assets/charts/acoustic-distribution.png", "dimensions": "1600x1000", "is_public": True, "used_for": "PDF، وب‌سایت", "notes_fa": None},

    # --- مستندات و شواهد ---
    {"asset_id": "AS-033", "asset_type": "document", "name_fa": "نمونه صورت‌وضعیت شماره ۸ - برق", "file_path": "/assets/docs/sv-08-electrical.pdf", "dimensions": None, "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": "صفحات ۱، ۲، ۴، ۶"},
    {"asset_id": "AS-034", "asset_type": "document", "name_fa": "نمونه صورت‌جلسه برق - اتاق هواساز", "file_path": "/assets/docs/sj-electrical-hvac.pdf", "dimensions": None, "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": "Z-40308"},
    {"asset_id": "AS-035", "asset_type": "document", "name_fa": "نمونه ریزمتره تکسا", "file_path": "/assets/docs/rizmetre-sample.pdf", "dimensions": None, "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": None},
    {"asset_id": "AS-036", "asset_type": "document", "name_fa": "نمونه گزارش ماهانه", "file_path": "/assets/docs/monthly-report.pdf", "dimensions": None, "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": None},
    {"asset_id": "AS-037", "asset_type": "document", "name_fa": "نمونه قرارداد پیمانکار جزء", "file_path": "/assets/docs/subcontract.pdf", "dimensions": None, "is_public": False, "used_for": "PDF ضمیمه", "notes_fa": "ناشناس‌شده"},

    # --- لوگو و برندینگ ---
    {"asset_id": "AS-038", "asset_type": "logo", "name_fa": "لوگوی شخصی - نسخه اصلی", "file_path": "/assets/branding/logo-main.svg", "dimensions": "Vector", "is_public": True, "used_for": "وب‌سایت، PDF", "notes_fa": None},
    {"asset_id": "AS-039", "asset_type": "logo", "name_fa": "لوگوی شخصی - تک‌رنگ", "file_path": "/assets/branding/logo-mono.svg", "dimensions": "Vector", "is_public": True, "used_for": "PDF چاپی", "notes_fa": None},
    {"asset_id": "AS-040", "asset_type": "icon", "name_fa": "آیکون‌های تخصصی", "file_path": "/assets/branding/icons.svg", "dimensions": "Vector", "is_public": True, "used_for": "وب‌سایت", "notes_fa": "آیکون برای ابنیه، برق، مکانیک، آکوستیک"},

    # --- ویدیو (اختیاری) ---
    {"asset_id": "AS-041", "asset_type": "video", "name_fa": "ویدیو کوتاه پروژه - ۳۰ ثانیه", "file_path": "/assets/videos/project-short.mp4", "dimensions": "1920x1080", "is_public": True, "used_for": "شبکه‌های اجتماعی", "notes_fa": "در صورت وجود"},
    {"asset_id": "AS-042", "asset_type": "video", "name_fa": "ویدیو کامل پروژه - ۳ دقیقه", "file_path": "/assets/videos/project-long.mp4", "dimensions": "1920x1080", "is_public": True, "used_for": "وب‌سایت", "notes_fa": "در صورت وجود"},
]
# ============================================================
# شیت ۲۵: Site_Content - متن‌های آماده وب‌سایت
# ============================================================
SITE_CONTENT = [
    # --- صفحه اصلی (Home) ---
    {"content_id": "SC-001", "page": "home", "section": "hero", "title_fa": "پروژه‌های فنی، دقیق، مستند", "body_fa": "تخصص من در دفتر فنی، کنترل پروژه و متره و برآورد، به‌همراه طراحی و اجرای آکوستیک، در خدمت پروژه‌های شماست. با نگاهی مهندسی، هر عدد و هر جزئیات را به سند تبدیل می‌کنم.", "cta_fa": "مشاهده پروژه‌ها", "order": 1},
    {"content_id": "SC-002", "page": "home", "section": "services", "title_fa": "خدمات تخصصی", "body_fa": "دفتر فنی و مستندسازی | کنترل پروژه و زمان‌بندی | متره و برآورد | صورت‌وضعیت و کنترل احجام | طراحی و اجرای آکوستیک", "cta_fa": None, "order": 2},
    {"content_id": "SC-003", "page": "home", "section": "featured-project", "title_fa": "پروژه شاخص", "body_fa": "تکمیل فاز ۱ یک ساختمان فنی و اداری با زیربنای حدود ۱۱,۰۰۰ مترمربع، شامل ۴ استودیو رادیویی، ۱ استودیو تلویزیونی، اتاق‌های کنترل، آرشیو و دفاتر اداری. مبلغ قرارداد حدود ۱۳۳.۷ میلیارد تومان و مدت اجرا ۱۸ ماه.", "cta_fa": "مشاهده جزئیات", "order": 3},
    {"content_id": "SC-004", "page": "home", "section": "stats", "title_fa": "آمار کلیدی", "body_fa": "۱۱,۰۰۰ مترمربع زیربنا | ۱۸ ماه مدت اجرا | ۵ زون مجزا (A، B1، B2، B3، B4) | ۴ استودیو رادیویی + ۱ استودیو تلویزیونی | ۸۸ درب | ۲۸۵ دریچه هوا", "cta_fa": None, "order": 4},

    # --- صفحه پروژه (Project Detail) ---
    {"content_id": "SC-005", "page": "project-P-001", "section": "overview", "title_fa": "معرفی پروژه", "body_fa": "پروژه تکمیل فاز ۱ یک ساختمان فنی و اداری، شامل پنج زون مجزا با کاربری‌های متنوع: بلوک A (بخش فنی و استودیوها)، بلوک B1 (لابی و کافه کتاب)، بلوک B2 (اداری و فنی)، بلوک B3 (تحریریه خبر) و بلوک B4 (خارج از دامنه). هدف پروژه، تجمیع و بهینه‌سازی فعالیت‌های فنی و اداری در یک مجتمع یکپارچه بود.", "cta_fa": None, "order": 1},
    {"content_id": "SC-006", "page": "project-P-001", "section": "role", "title_fa": "نقش من در پروژه", "body_fa": "در این پروژه، مسئولیت دفتر فنی، کنترل پروژه، متره و برآورد، و طراحی و اجرای آکوستیک را بر عهده داشتم. از تولید نقشه‌های As-built و صورت‌جلسات، تا تهیه ریزمتره و صورت‌وضعیت، تا طراحی لایه‌بندی آکوستیک استودیوها و نظارت بر اجرا، همه در دامنه فعالیت‌های من بود.", "cta_fa": None, "order": 2},
    {"content_id": "SC-007", "page": "project-P-001", "section": "technical-office", "title_fa": "دفتر فنی و مستندسازی", "body_fa": "در دفتر فنی، مدیریت مستندات پروژه شامل نقشه‌ها، RFIها، صورت‌جلسات و مکاتبات را بر عهده داشتم. تولید نقشه‌های As-built، هماهنگی بین‌رشته‌ای (ابنیه، برق، مکانیک، آکوستیک) و پیگیری مصوبات کارفرما، از جمله دستاوردهای این بخش بود.", "cta_fa": None, "order": 3},
    {"content_id": "SC-008", "page": "project-P-001", "section": "project-controls", "title_fa": "کنترل پروژه و زمان‌بندی", "body_fa": "برنامه زمان‌بندی پروژه در قالب MPP تهیه شد و به‌صورت دوره‌ای بروزرسانی می‌شد. تهیه S-Curve برنامه‌ای، گزارش‌های ماهانه پیشرفت، و تحلیل تأخیرات از جمله فعالیت‌های این بخش بود. هماهنگی با پیمانکاران جزء و پیگیری فعالیت‌های بحرانی، نقش کلیدی در تحویل به‌موقع پروژه داشت.", "cta_fa": None, "order": 4},
    {"content_id": "SC-009", "page": "project-P-001", "section": "qs", "title_fa": "متره، برآورد و صورت‌وضعیت", "body_fa": "تهیه متره و برآورد برای سه رشته ابنیه، مکانیک و برق، بر اساس فهرست‌بهای واحد پایه. تهیه ۸ صورت‌وضعیت دوره‌ای، کنترل احجام با تطبیق نقشه و اجرا، و تهیه صورت‌جلسات احجام کاری. مدیریت تغییرات و تهیه اسناد پشتیبان برای تأیید کارفرما.", "cta_fa": None, "order": 5},
    {"content_id": "SC-010", "page": "project-P-001", "section": "acoustic", "title_fa": "طراحی و اجرای آکوستیک", "body_fa": "طراحی لایه‌بندی آکوستیک استودیوها با ترکیب هبلکس دوجداره، پشم سنگ دانسیته ۸۰، تایل آکوستیک و وول‌پنل نورس‌پنل. طراحی درب‌های تمام آکوستیک با لنگه ۸ سانتی‌متری، نوار درزگیر فشاری و پاشنه فنی. طراحی پنجره‌های ویزور با شیشه زاویه‌دار و گاز آرگون. نظارت بر اجرا و کنترل کیفیت.", "cta_fa": None, "order": 6},
    {"content_id": "SC-011", "page": "project-P-001", "section": "results", "title_fa": "نتایج و دستاوردها", "body_fa": "پروژه در سال دوم به اتمام رسید و تحویل موقت و قطعی انجام شد. چهار استودیو رادیویی، یک استودیو تلویزیونی، اتاق‌های کنترل، آرشیوها و دفاتر اداری تحویل داده شد و پروژه هم‌اکنون در حال بهره‌برداری است.", "cta_fa": None, "order": 7},
    {"content_id": "SC-012", "page": "project-P-001", "section": "lessons", "title_fa": "درس‌آموخته‌ها", "body_fa": "هماهنگی بین‌رشته‌ای در پروژه‌های فنی با فضاهای حساس، نیازمند مستندسازی دقیق و برنامه‌ریزی منعطف است. در این پروژه، تجربه ارزشمندی در تعادل بین کیفیت آکوستیک، محدودیت‌های اجرایی و زمان‌بندی به دست آمد.", "cta_fa": None, "order": 8},

    # --- صفحات خدمات ---
    {"content_id": "SC-013", "page": "services", "section": "technical-office", "title_fa": "دفتر فنی و مستندسازی", "body_fa": "مدیریت مستندات، تولید نقشه‌های As-built، هماهنگی بین‌رشته‌ای، پیگیری RFI و صورت‌جلسات، و تهیه گزارش‌های فنی.", "cta_fa": "درخواست مشاوره", "order": 1},
    {"content_id": "SC-014", "page": "services", "section": "project-controls", "title_fa": "کنترل پروژه", "body_fa": "تهیه WBS، برنامه زمان‌بندی MPP، S-Curve، گزارش‌های پیشرفت، تحلیل تأخیرات و ارائه راهکارهای جبرانی.", "cta_fa": "درخواست مشاوره", "order": 2},
    {"content_id": "SC-015", "page": "services", "section": "qs", "title_fa": "متره، برآورد و صورت‌وضعیت", "body_fa": "متره تفصیلی و ریزمتره، برآورد احجام و هزینه، تهیه صورت‌وضعیت دوره‌ای، کنترل احجام، تهیه صورت‌جلسات احجام کاری.", "cta_fa": "درخواست مشاوره", "order": 3},
    {"content_id": "SC-016", "page": "services", "section": "acoustic", "title_fa": "طراحی و اجرای آکوستیک", "body_fa": "طراحی لایه‌بندی آکوستیک استودیو، اتاق کنترل، اتاق ادیت و بازشنوایی. طراحی درب آکوستیک، پنجره ویزور، ایرلاک صوتی و سیستم تهویه بی‌صدا.", "cta_fa": "درخواست مشاوره", "order": 4},

    # --- SEO ---
    {"content_id": "SC-017", "page": "global", "section": "seo", "title_fa": "پرتفولیو مهندسی عمران - دفتر فنی، کنترل پروژه، متره و آکوستیک", "body_fa": "پرتفولیوی تخصصی در حوزه دفتر فنی، کنترل پروژه، متره و برآورد و آکوستیک. نمونه پروژه‌های اجرایی با مستندات کامل.", "cta_fa": None, "order": 1},

    # --- تماس ---
    {"content_id": "SC-018", "page": "contact", "section": "cta", "title_fa": "آماده همکاری در پروژه‌های شما", "body_fa": "اگر به دنبال یک متخصص دفتر فنی، کنترل پروژه یا آکوستیک برای پروژه خود هستید، با من تماس بگیرید.", "cta_fa": "ارسال پیام", "order": 1},
]
# ============================================================
# شیت ۲۶: Social_Posts - پست‌های آماده شبکه‌های اجتماعی
# ============================================================
SOCIAL_POSTS = [
    # --- لینکدین ---
    {"post_id": "SP-001", "platform": "LinkedIn", "topic": "معرفی پروژه", "title_fa": "تکمیل فاز ۱ یک ساختمان فنی و اداری", "body_fa": "پروژه‌ای با زیربنای حدود ۱۱,۰۰۰ مترمربع و مبلغ قرارداد ۱۳۳.۷ میلیارد تومان، شامل ۵ زون مجزا. نقش من: دفتر فنی، کنترل پروژه، متره و آکوستیک.\n\n#دفترفنی #کنترل_پروژه #متره_برآورد #آکوستیک", "hashtags": "#Engineering #ProjectControls #Acoustics", "cta_fa": "پرتفولیو کامل در وب‌سایت", "scheduled_week": 1, "language": "fa"},
    {"post_id": "SP-002", "platform": "LinkedIn", "topic": "آکوستیک", "title_fa": "طراحی و اجرای آکوستیک استودیوها", "body_fa": "لایه‌بندی آکوستیک: هبلکس دوجداره + پشم سنگ دانسیته ۸۰ + تایل آکوستیک + وول‌پنل نورس‌پنل.\n\nدرب آکوستیک با لنگه ۸ سانتی‌متری، نوار درزگیر فشاری و پاشنه فنی.\n\nپنجره ویزور با شیشه زاویه‌دار و گاز آرگون.\n\n#آکوستیک #استودیو #عایق_صدا", "hashtags": "#Acoustics #StudioDesign #SoundIsolation", "cta_fa": "جزئیات بیشتر در وب‌سایت", "scheduled_week": 2, "language": "fa"},
    {"post_id": "SP-003", "platform": "LinkedIn", "topic": "متره و برآورد", "title_fa": "متره و برآورد پروژه در سه رشته", "body_fa": "تهیه متره و برآورد کامل برای ابنیه، تأسیسات مکانیکی و تأسیسات برقی.\n\n۸ صورت‌وضعیت دوره‌ای، کنترل احجام با تطبیق نقشه و اجرا، و تهیه صورت‌جلسات احجام کاری.\n\n#متره #برآورد #صورت_وضعیت", "hashtags": "#QuantitySurveying #QS #Construction", "cta_fa": "نمونه اسناد در وب‌سایت", "scheduled_week": 3, "language": "fa"},
    {"post_id": "SP-004", "platform": "LinkedIn", "topic": "کنترل پروژه", "title_fa": "کنترل پروژه در یک نگاه", "body_fa": "WBS سلسله‌مراتبی، برنامه زمان‌بندی MPP، S-Curve برنامه‌ای، گزارش‌های ماهانه پیشرفت.\n\nتحلیل تأخیرات و ارائه راهکارهای جبرانی، نقش کلیدی در تحویل به‌موقع پروژه داشت.\n\n#کنترل_پروژه #زمان_بندی", "hashtags": "#ProjectControls #Planning #Scheduling", "cta_fa": "مشاهده نمونه برنامه", "scheduled_week": 4, "language": "fa"},

    # --- اینستاگرام ---
    {"post_id": "SP-005", "platform": "Instagram", "topic": "تصویر استودیو", "title_fa": "استودیو رادیویی - قبل و بعد", "body_fa": "از زیرسازی تا فینیشینگ آکوستیک. یک استودیو حرفه‌ای با لایه‌بندی دقیق.\n\n#آکوستیک #استودیو #مهندسی_عمران", "hashtags": "#Acoustics #Studio #Engineering", "cta_fa": "مشاهده در وب‌سایت", "scheduled_week": 1, "language": "fa"},
    {"post_id": "SP-006", "platform": "Instagram", "topic": "درب آکوستیک", "title_fa": "جزئیات درب آکوستیک", "body_fa": "لنگه درب با روکش چرمی، نوار درزگیر فشاری، پاشنه فنی، دستگیره پانیک بار.\n\nهر جزئیات، داستانی از دقت دارد.\n\n#جزئیات_اجرایی #آکوستیک", "hashtags": "#Detailing #Acoustics #Doors", "cta_fa": None, "scheduled_week": 2, "language": "fa"},
    {"post_id": "SP-007", "platform": "Instagram", "topic": "پانل پانچ", "title_fa": "نصب پانل‌های پانچ‌شده", "body_fa": "نصب MDF پانچ‌شده با لیزر تراز، برای کنترل دقیق لایه‌بندی سقف آکوستیک.\n\n#اجرا #آکوستیک #دقت_مهندسی", "hashtags": "#Execution #Acoustics #Precision", "cta_fa": None, "scheduled_week": 3, "language": "fa"},
    {"post_id": "SP-008", "platform": "Instagram", "topic": "نمای نهایی", "title_fa": "نمای نهایی پروژه", "body_fa": "پروژه‌ای که ۱۸ ماه زمان برد و حالا در بهره‌برداری است.\n\n#پروژه #تحویل #مهندسی", "hashtags": "#Project #Delivery #Engineering", "cta_fa": None, "scheduled_week": 4, "language": "fa"},

    # --- تلگرام ---
    {"post_id": "SP-009", "platform": "Telegram", "topic": "معرفی خدمات", "title_fa": "خدمات تخصصی من", "body_fa": "دفتر فنی و مستندسازی\nکنترل پروژه و زمان‌بندی\nمتره، برآورد و صورت‌وضعیت\nطراحی و اجرای آکوستیک\n\nاگر در پروژه‌ای به این خدمات نیاز دارید، تماس بگیرید.", "hashtags": None, "cta_fa": "تماس با من", "scheduled_week": 1, "language": "fa"},
    {"post_id": "SP-010", "platform": "Telegram", "topic": "نمونه کار", "title_fa": "نمونه صورت‌وضعیت", "body_fa": "صورت‌وضعیت شماره ۸ - تأسیسات برقی.\n\nشامل: برگ مالی، خلاصه متره، ریزمتره.\n\nمستندات کامل در پرتفولیو.", "hashtags": None, "cta_fa": "مشاهده در وب‌سایت", "scheduled_week": 2, "language": "fa"},
    {"post_id": "SP-011", "platform": "Telegram", "topic": "آکوستیک", "title_fa": "جزئیات لایه‌بندی آکوستیک", "body_fa": "لایه‌بندی دیوار استودیو:\n\nهبلکس ۲۰ سانتی + پشم سنگ ۱۰ سانتی (دانسیته ۸۰) + هبلکس ۲۰ سانتی\n\nشاسی فولادی ۳۰×۳۰\n\nتایل آکوستیک + پارچه نساج پایا", "hashtags": None, "cta_fa": "جزئیات بیشتر", "scheduled_week": 3, "language": "fa"},

    # --- توییتر / X ---
    {"post_id": "SP-012", "platform": "Twitter/X", "topic": "معرفی کوتاه", "title_fa": "تخصص من", "body_fa": "دفتر فنی، کنترل پروژه، متره و برآورد و آکوستیک.\n\nنمونه پروژه: یک ساختمان فنی و اداری ۱۱,۰۰۰ مترمربعی در ۱۸ ماه.\n\n#مهندسی_عمران", "hashtags": "#Engineering #CivilEngineering", "cta_fa": "پرتفولیو در بایو", "scheduled_week": 1, "language": "fa"},
    {"post_id": "SP-013", "platform": "Twitter/X", "topic": "آکوستیک", "title_fa": "لایه‌بندی آکوستیک", "body_fa": "برای رسیدن به آکوستیک حرفه‌ای در استودیو، باید چند لایه روی هم کار کنند:\n\n▪ سازه (هبلکس + پشم سنگ)\n▪ شاسی‌کشی فولادی\n▪ ایزولاسیون صوتی\n▪ فینیشینگ\n\n#آکوستیک", "hashtags": "#Acoustics #StudioDesign", "cta_fa": None, "scheduled_week": 2, "language": "fa"},
    {"post_id": "SP-014", "platform": "Twitter/X", "topic": "نکته متره", "title_fa": "نکته متره", "body_fa": "در متره، اولین مقدار معتبر را مبنا بگیرید. تکرارها را حذف کنید.\n\nیک عدد اشتباه، تمام برآورد را زیر سؤال می‌برد.\n\n#متره #برآورد", "hashtags": "#QS #QuantitySurveying", "cta_fa": None, "scheduled_week": 3, "language": "fa"},

    # --- پست‌های تخصصی ---
    {"post_id": "SP-015", "platform": "LinkedIn", "topic": "درس‌آموخته", "title_fa": "درس‌آموخته از پروژه", "body_fa": "در پروژه‌های فنی با فضاهای حساس، هماهنگی بین‌رشته‌ای حیاتی است.\n\nهر تغییری در یک رشته، باید در سایر رشته‌ها هم منعکس شود.\n\nمستندسازی دقیق، بهترین بیمه پروژه است.\n\n#مدیریت_پروژه", "hashtags": "#ProjectManagement #Coordination", "cta_fa": None, "scheduled_week": 5, "language": "fa"},
    {"post_id": "SP-016", "platform": "LinkedIn", "topic": "تجهیزات", "title_fa": "مدیریت تجهیزات در پروژه", "body_fa": "۸ هوارسان، ۷ اگزاست فن، ۱۰ تابلو برق، ۲۸۵ دریچه هوا، ۴۹۹ چراغ، ۸۲۶ کلید و پریز.\n\nمدیریت این حجم تجهیزات، نیازمند مستندسازی دقیق و برنامه‌ریزی خرید است.\n\n#تأسیسات #مدیریت_پروژه", "hashtags": "#MEP #Procurement", "cta_fa": None, "scheduled_week": 6, "language": "fa"},
    {"post_id": "SP-017", "platform": "Instagram", "topic": "نقشه", "title_fa": "از نقشه تا واقعیت", "body_fa": "پلان طبقه همکف، بلوک A و B.\n\nهر خط، یک تصمیم مهندسی است.\n\n#نقشه #معماری #مهندسی", "hashtags": "#Architecture #Engineering", "cta_fa": None, "scheduled_week": 5, "language": "fa"},
    {"post_id": "SP-018", "platform": "Instagram", "topic": "تیم", "title_fa": "تیم پروژه", "body_fa": "پشت هر پروژه موفق، یک تیم منسجم است.\n\nاز پیمانکاران جزء تا مشاوران، همه در کنار هم.\n\n#تیم #پروژه #همکاری", "hashtags": "#Team #Project #Collaboration", "cta_fa": None, "scheduled_week": 6, "language": "fa"},
    {"post_id": "SP-019", "platform": "Telegram", "topic": "برنامه زمان‌بندی", "title_fa": "برنامه زمان‌بندی پروژه", "body_fa": "برنامه زمان‌بندی پروژه در ۴ فاز:\n\n▪ ابنیه\n▪ تأسیسات الکتریکال\n▪ تأسیسات مکانیکی\n▪ تحویل و راه‌اندازی\n\n۸۸ فعالیت شاخص، ۱۲ نقطه عطف.", "hashtags": None, "cta_fa": "مشاهده Gantt", "scheduled_week": 4, "language": "fa"},
    {"post_id": "SP-020", "platform": "LinkedIn", "topic": "تحویل پروژه", "title_fa": "تحویل موقت و قطعی", "body_fa": "تحویل موقت پروژه انجام شد و پس از رفع نقص‌ها، تحویل قطعی و بهره‌برداری رسمی آغاز شد.\n\nاین پروژه، تجربه ارزشمندی در هماهنگی بین‌رشته‌ای و مدیریت مستندات بود.\n\n#تحویل #پروژه", "hashtags": "#ProjectDelivery #Handover", "cta_fa": "مشاهده جزئیات", "scheduled_week": 7, "language": "fa"},
]


# ============================================================
# محاسبات خودکار
# ============================================================
def enrich_spaces(spaces_raw):
    """محاسبه area_m2 و perimeter_m و افزودن فیلدهای پیش‌فرض"""
    result = []
    for s in spaces_raw:
        s = s.copy()
        s["project_id"] = "P-001"
        s["area_m2"] = round(s["length_m"] * s["width_m"], 2)
        s["perimeter_m"] = round(2 * (s["length_m"] + s["width_m"]), 2)
        s["floor_finish"] = "موزائیک ایرانی + کفپوش ونیل"
        s["wall_finish"] = "تایل آکوستیک + MDF ازاره + پارچه نساج پایا"
        s["ceiling_finish"] = "کناف آکوستیک + وول‌پنل نورس‌پنل NP03"
        s["is_public"] = True
        s["notes_fa"] = ""
        s["display_group"] = s.get("display_group", None)  # فیلد جدید
        ordered = {
            "space_id": s["space_id"],
            "project_id": s["project_id"],
            "name_fa": s["name_fa"],
            "name_en": s["name_en"],
            "name_internal": s["name_internal"],
            "block": s["block"],
            "floor": s["floor"],
            "zone": s["zone"],
            "length_m": s["length_m"],
            "width_m": s["width_m"],
            "height_m": s["height_m"],
            "area_m2": s["area_m2"],
            "perimeter_m": s["perimeter_m"],
            "floor_finish": s["floor_finish"],
            "wall_finish": s["wall_finish"],
            "ceiling_finish": s["ceiling_finish"],
            "acoustic_class": s["acoustic_class"],
            "has_visor_window": s["has_visor_window"],
            "has_airlock": s["has_airlock"],
            "has_silencer": s["has_silencer"],
            "executed": s["executed"],
            "is_public": s["is_public"],
            "display_group": s["display_group"],
            "notes_fa": s["notes_fa"],
        }
        result.append(ordered)
    return result

SPACES = enrich_spaces(SPACES_RAW)


# ============================================================
# ساخت فایل اکسل
# ============================================================
def build_excel(filename="Master_Data.xlsx"):
    from openpyxl import load_workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

    df_projects = pd.DataFrame(PROJECTS)
    df_spaces = pd.DataFrame(SPACES)
    df_acoustic_layers = pd.DataFrame(ACOUSTIC_LAYERS)
    df_acoustic_doors = pd.DataFrame(ACOUSTIC_DOORS)
    df_acoustic_details = pd.DataFrame(ACOUSTIC_DETAILS)
    df_doors = pd.DataFrame(DOORS)
    df_windows_visors = pd.DataFrame(WINDOWS_VISORS)
    df_hvac_dampers = pd.DataFrame(HVAC_DAMPERS)
    df_hvac_equipment = pd.DataFrame(HVAC_EQUIPMENT)
    df_insulation = pd.DataFrame(INSULATION)
    df_plumbing_fixtures = pd.DataFrame(PLUMBING_FIXTURES)
    df_electrical_items = pd.DataFrame(ELECTRICAL_ITEMS)
    df_lighting_items = pd.DataFrame(LIGHTING_ITEMS)
    df_power_panels = pd.DataFrame(POWER_PANELS)
    df_fire_safety = pd.DataFrame(FIRE_SAFETY)
    df_cables_trunking = pd.DataFrame(CABLES_TRUNKING)
    df_qs_items = pd.DataFrame(QS_ITEMS)
    df_qs_summary = pd.DataFrame(QS_SUMMARY)
    df_qs_insulation = pd.DataFrame(QS_INSULATION)
    df_qs_acoustic = pd.DataFrame(QS_ACOUSTIC)
    df_schedule = pd.DataFrame(SCHEDULE_ACTIVITIES)
    df_milestones = pd.DataFrame(MILESTONES)
    df_meetings = pd.DataFrame(MEETINGS_SUMMARY)
    df_assets = pd.DataFrame(ASSETS)
    df_site_content = pd.DataFrame(SITE_CONTENT)
    df_social_posts = pd.DataFrame(SOCIAL_POSTS)

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df_projects.to_excel(writer, sheet_name="Projects", index=False)
        df_spaces.to_excel(writer, sheet_name="Spaces", index=False)
        df_acoustic_layers.to_excel(writer, sheet_name="Acoustic_Layers", index=False)
        df_acoustic_doors.to_excel(writer, sheet_name="Acoustic_Doors", index=False)
        df_acoustic_details.to_excel(writer, sheet_name="Acoustic_Details", index=False)
        df_doors.to_excel(writer, sheet_name="Doors", index=False)
        df_windows_visors.to_excel(writer, sheet_name="Windows_Visors", index=False)
        df_hvac_dampers.to_excel(writer, sheet_name="HVAC_Dampers", index=False)
        df_hvac_equipment.to_excel(writer, sheet_name="HVAC_Equipment", index=False)
        df_insulation.to_excel(writer, sheet_name="Insulation", index=False)
        df_plumbing_fixtures.to_excel(writer, sheet_name="Plumbing_Fixtures", index=False)
        df_electrical_items.to_excel(writer, sheet_name="Electrical_Items", index=False)
        df_lighting_items.to_excel(writer, sheet_name="Lighting_Items", index=False)
        df_power_panels.to_excel(writer, sheet_name="Power_Panels", index=False)
        df_fire_safety.to_excel(writer, sheet_name="Fire_Safety", index=False)
        df_cables_trunking.to_excel(writer, sheet_name="Cables_Trunking", index=False)
        df_qs_items.to_excel(writer, sheet_name="QS_Items", index=False)
        df_qs_summary.to_excel(writer, sheet_name="QS_Summary", index=False)
        df_qs_insulation.to_excel(writer, sheet_name="QS_Insulation", index=False)
        df_qs_acoustic.to_excel(writer, sheet_name="QS_Acoustic", index=False)
        df_schedule.to_excel(writer, sheet_name="Schedule_Activities", index=False)
        df_milestones.to_excel(writer, sheet_name="Milestones", index=False)
        df_meetings.to_excel(writer, sheet_name="Meetings_Summary", index=False)
        df_assets.to_excel(writer, sheet_name="Assets", index=False)
        df_site_content.to_excel(writer, sheet_name="Site_Content", index=False)
        df_social_posts.to_excel(writer, sheet_name="Social_Posts", index=False)

    # فرمت‌بندی
    wb = load_workbook(filename)
    header_font = Font(name="Tahoma", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
    cell_font = Font(name="Tahoma", size=10)
    border = Border(
        left=Side(style="thin", color="CCCCCC"),
        right=Side(style="thin", color="CCCCCC"),
        top=Side(style="thin", color="CCCCCC"),
        bottom=Side(style="thin", color="CCCCCC"),
    )

    for ws in wb.worksheets:
        # هدر
        for cell in ws[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.border = border
        # بدنه
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.font = cell_font
                cell.border = border
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        # تنظیم عرض ستون
        for col in ws.columns:
            max_len = max(len(str(c.value)) if c.value else 0 for c in col)
            ws.column_dimensions[col[0].column_letter].width = min(max_len + 4, 45)
        # فریز کردن سطر اول
        ws.freeze_panes = "A2"

    wb.save(filename)
    print(f"✅ فایل {filename} ساخته شد ({len(df_projects)} پروژه، {len(df_spaces)} فضا)")


# ============================================================
# ساخت فایل JSON برای وب‌سایت
# ============================================================
def build_json(filename="master_data.json"):
    data = {
        "version": VERSION,
        "build_date": BUILD_DATE,
        "projects": PROJECTS,
        "spaces": SPACES,
        "acoustic_layers": ACOUSTIC_LAYERS,
        "acoustic_doors": ACOUSTIC_DOORS,
        "acoustic_details": ACOUSTIC_DETAILS,
        "doors": DOORS,
        "windows_visors": WINDOWS_VISORS,
        "hvac_dampers": HVAC_DAMPERS,
        "hvac_equipment": HVAC_EQUIPMENT,
        "insulation": INSULATION,
        "plumbing_fixtures": PLUMBING_FIXTURES,
        "electrical_items": ELECTRICAL_ITEMS,
        "lighting_items": LIGHTING_ITEMS,
        "power_panels": POWER_PANELS,
        "fire_safety": FIRE_SAFETY,
        "cables_trunking": CABLES_TRUNKING,
        "qs_items": QS_ITEMS,
        "qs_summary": QS_SUMMARY,
        "qs_insulation": QS_INSULATION,
        "qs_acoustic": QS_ACOUSTIC,
        "schedule_activities": SCHEDULE_ACTIVITIES,
        "milestones": MILESTONES,
        "meetings_summary": MEETINGS_SUMMARY,
        "assets": ASSETS,
        "site_content": SITE_CONTENT,
        "social_posts": SOCIAL_POSTS,
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ فایل {filename} ساخته شد")


# ============================================================
# اجرا
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print(f"Master Data Builder - نسخه {VERSION}")
    print(f"تاریخ ساخت: {BUILD_DATE}")
    print("=" * 60)
    build_excel()
    build_json()
    print("=" * 60)
    print("🎉 همه فایل‌ها با موفقیت ساخته شدند")
    print("=" * 60)