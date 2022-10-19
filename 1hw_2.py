def matches_count(n): #n -команды
    end_cnt = 0 #счётчик всех матчей
    cnt = 0 #промежуточные матчи
    while n > 1:
        if n%2 == 0:
            n //= 2
            cnt = n
            end_cnt += cnt #считаем
        else:
            cnt = n//2
            end_cnt += cnt
            n = n//2 + 1 #считаем для нечётных
    return end_cnt #выводим результат

print(matches_count(14)) #конец