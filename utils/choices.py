from django.db import models


class TypeOfPrice(models.TextChoices):
    PRICE = 'PRICE', 'Price'
    FREE = 'FREE', 'Free'
    EXCHANGE = 'EXCHANGE', 'Exchange'


class OptionType(models.TextChoices):
    SINGLE = 'SINGLE', 'Single'
    CHOICE = 'CHOICE', 'Choice'
    BUTTON = 'BUTTON', 'Button'
    TEXT = 'TEXT', 'Text'
    NUMBER = 'NUMBER', 'Number'
    MULTIPLE_CHOICE = 'MULTIPLE_CHOICE', 'Multiple_choice'


class TypeOfValuta(models.TextChoices):
    EURO = 'EURO', 'y.e'
    SUM = 'SUM', 'Sum'