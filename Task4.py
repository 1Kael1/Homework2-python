# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
def listUser(nPlus):
    nMinus = -nPlus
    
    arr = [i*1 for i in range(nMinus, nPlus+1)]
    print(arr)  

    return arr  


def compare(arr, arrIdx):
    print(arr, arrIdx)

    arrValue = list()
    

    for i in arr:
       

        for j in arrIdx:
         

            if(arr.index(i)  == j):
               
                arrValue.append(i)
    print(f'Массив для обработки: {arrValue}')

    return arrValue 

def multi(compareArr):
    accumMulti = 1     

    for i in compareArr:
        accumMulti *= i

    print(f'произведение значений массива {compareArr} = {accumMulti}') 

newArr = listUser(5)
compareArr = compare(newArr, [1,2,10,9])
multi(compareArr)
