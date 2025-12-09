# decorator.py
import functools

# словник для зберігання кількості винятків по іменах функцій
exception_counts = {}

def exception_logger(func):
    """
    Декоратор, який рахує кількість винятків, що виникають у конкретній функції.
    Логінг виводиться в консоль, а потім виняток перекидається далі.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # інкрементуємо лічильник для конкретної функції
            exception_counts.setdefault(func.__name__, 0)
            exception_counts[func.__name__] += 1

            # лог у консоль
            print(f"[LOG] Function '{func.__name__}' raised an exception: {e!r}")
            print(f"[LOG] '{func.__name__}' exceptions so far: {exception_counts[func.__name__]}")

            # перекидаємо виняток далі, щоб не «глушити» помилки
            raise
    return wrapper

def get_exception_count(func_name: str = None):
    """
    Повертає кількість винятків для функції з іменем func_name.
    Якщо func_name == None — повертає копію всіх лічильників.
    """
    if func_name is None:
        return dict(exception_counts)
    return exception_counts.get(func_name, 0)
