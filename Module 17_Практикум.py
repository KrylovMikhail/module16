def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array_sort, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array_sort[middle] == element:
        return middle
    elif element < array_sort[middle]:
        return binary_search(array_sort, element, left, middle - 1)
    else:
        return binary_search(array_sort, element, middle + 1, right)


array = list(map(int, input('Введите последовательность чисел через пробел: \n').split()))
element = int(input('Введите число: \n'))
array.append(element)

array_sort = merge_sort(array)
print('Значения в порядке возрастания:', array_sort)

right = array_sort[-1]
left = array_sort[0]
print('Максимальное значение:', right)
print('Минимальное значение:', left)

idx = binary_search(array_sort, element, left, right)
print('Индекс значения:', idx)
print('Индекс значения слева: ', idx - 1)
print('Индекс значения справа: ', idx + 1)




