def steps_to_zero(n):
    step = 0 #счётчик для шагов
    if n == 0:
        return step #просто для вывода, если 0
    else: #вообще не особо нужно, но да ладно
        while n != 0:
            if n%2 == 0: 
                n = n//2
                step += 1 #считаем шаги
            else:
                n -= 1
                step += 1 #тут тоже
    return step

print(steps_to_zero(14)) #готово

