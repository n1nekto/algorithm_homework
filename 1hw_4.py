def min_diff(arr): #сюда массив кидаем
    list_of_lists = [] #создаем список со списками
    na = sorted(arr) #сортируем для магии
    mini = abs(na[1] - na[0]) #находим минимальную разницу
    for i in range(2, len(na)): #проходимся по всем элементам и ищем есть ли меньшая разница
        mini = min(mini, abs(na[i] - na[i-1]))
    for j in range(1, len(arr)): #опять проходимся
        if abs(na[j]-na[j-1]) == mini: #ищем пары с разницей
            list_of_lists.append(list([na[j-1], na[j]])) #кидаем их в тот самый список
    return list_of_lists #возвращаем его

print(min_diff([3,8,-10,23,19,-4,-14,27])) #я гений