def cash_decorator(func):
    cash = {}
    def wrapper(arg):
        if (cash.get(arg)) == None:
            cash[arg] = func(arg)
        return cash.get(arg)
    return wrapper

@cash_decorator
def multiplier(number: int):
    return number * 2


check = (5, 2, 4, 2, 6, 5, 4)
for i in check:
    print(multiplier(i))