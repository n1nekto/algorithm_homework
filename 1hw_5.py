def removing_trash(s): #передаём строку
    res = '' #переменная для финального результата
    stack = [] #кидаем сюда открывающие или удаляем отсюда, если закрывающие
    prev = '' #промежуточный результат
    for i in s: #проходимся по строке
        if i == '(':
            stack.append(i)
        else:
            stack.pop()
        prev += i
        if not stack:
            res += prev[1:-1] #удаление лишних скобок путём среза
            prev = ''          
    return res #возвращаем результаты

print(removing_trash('((())())(())(()(()))')) #конец