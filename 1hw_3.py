def jews_finder(jews, stns): #ищем наше богатсво 
    # jews - jewels, stns - stones
    jews_count = 0 #счётчик наших алмазов
    for j in stns: #проходимся по списку всех камней
        if j in jews: #если есть что-то из алмазов, считаем
            jews_count += 1
    return jews_count #выводим сколько есть

print(jews_finder('aA', "aAAbbbb")) #конец