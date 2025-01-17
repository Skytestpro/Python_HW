def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: return False


y = int(input("Введите год: "))
result = is_year_leap(y)
print(f"Год {y}: {result}")
