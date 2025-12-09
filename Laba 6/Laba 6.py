# main.py
from decorator import exception_logger, get_exception_count

@exception_logger
def divide(a, b):
    """Проста функція ділення — може кидати ZeroDivisionError або TypeError."""
    return a / b

# Тестові виклики — ловимо помилки у блоках try, щоб програма не падала повністю
try:
    print("10 / 2 =", divide(10, 2))   # нормальний виклик
except Exception as e:
    print("Caught in main:", e)

try:
    divide(5, 0)   # викличе ZeroDivisionError
except Exception:
    pass

try:
    divide("a", 5)  # викличе TypeError
except Exception:
    pass

# Показуємо скільки винятків сталося для функції divide
print("Exceptions for 'divide':", get_exception_count("divide"))
# Показати всі лічильники (якщо додасться ще декорованих функцій)
print("All exception counts:", get_exception_count())
