
subs = list(map(int, input('Числа через пробел: ').split()))
num = int (input('Введите число: '))
print('Последовательность:', (subs))

if num not in subs:
    subs.append(num)
print('Число добавилось в последовательность:',(subs))

subs.sort()
print("Отсортировано по возрастанию: ", (subs))

def search_position():
    if num == subs[0]:
        x = num
        print("Нет элементов меньше введенного числа")
    else:
        array = subs

        def Binsearch(array, element, left, right):
            if left > right:
                return False
            middle = (right + left) // 2
            if array[middle] == element:
                return middle

            elif element < array[middle]:
                return Binsearch(array, element,left,middle - 1)
            else:
                return Binsearch(array, element, middle + 1, right)
        print('Номер позиции элемента (меньше введенного пользователем числа): ', (Binsearch(array, num, 0, len(array)-1)-1))

search_position()


