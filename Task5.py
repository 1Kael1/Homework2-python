def shuffleArr(array):

    print(f'Массив для перемешивания: {array}')

    minEl = 0
    maxEl = len(array)-1

    print(f'Мин.индекс: {minEl} , макс. индекс: {maxEl}')

    import random
    for i in range(maxEl):
        idxRndm = random.randint(minEl, maxEl)
        print(f'Рандомный индекс: {idxRndm} ')

        val1 = array[idxRndm]
        vav2 = array[idxRndm - 1]

        array[idxRndm - 1] = val1
        array[idxRndm] = vav2

    print(f'Массив после перемешивания: {array}')


shuffleArr([1, 2, 3, 4, 5, 6, 7, 8])
