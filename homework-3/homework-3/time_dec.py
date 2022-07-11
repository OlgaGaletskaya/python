import time

def decorator(call_count=1, start_sleep_time=1, factor=2, border_sleep_time=10):
    def decorator(func):
        def wrapper():
            print(f"Кол-во запусков = call_count ({call_count})")
            print("Начало работы")
            t = start_sleep_time
            for call in range(call_count):
                time.sleep(t)
                print(f"Запуск номер {call+1}. Ожидание: {t} секунд. Результат декорируемой функций = {func()}.")
                if t < border_sleep_time:
                    t *= 2**(factor)
                if t >= border_sleep_time:
                    t  = border_sleep_time
            print("Конец работы")
        return wrapper
    return decorator

@decorator (call_count=5)
def function(): 
    return ("function result")



if __name__ == "__main__":
    function()