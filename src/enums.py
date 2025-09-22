from enum import StrEnum

class Audience(StrEnum):
    CHILDREN = "ბავშვებისთვის"
    ADOLESCENT = "მოზარდებისთვის"
    ADULT = "უფროსებისთვის"

class Booktype(StrEnum):
    ONLINE = "ონლაინ წიგნი"
    PRINT = "დაბეჭდილი წიგნი"
    AUDIO = "ხმის წიგნი"
    INTERACTIVE = "ინტერაქტიური წიგნი"

class CoverType(StrEnum):
    HARD = "მყარი"
    SOFT = "რბილი"