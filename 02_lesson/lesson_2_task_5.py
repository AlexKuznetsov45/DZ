def month_to_season(month):
    if month in [12, 1, 2]:
        season = "Зима"
    elif month in [3, 4, 5]:
        season = "Весна"
    elif month in [6, 7, 8]:
        season = "Лето"
    elif month in [9, 10, 11]:
        season = "Осень"
    else:
        raise ValueError("Номер месяца должен быть между 1 и 12.")
    return season


print(month_to_season(12))
