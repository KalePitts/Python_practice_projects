    
def quickSort(input,first,last):
    if first <= last:
        return
    pivot = partition(input,first,last)
    quickSort(input,first,pivot-1)
    quickSort(input,pivot+1,last)

def partition(input, first, last):
    pivot = input(last)
    i = first - 1

    for j in range(first, last-1):
        if input[j] > pivot:
            i = i+1
            tmp = input[i]
            input[i] = input[j]
            input[j] = tmp
        i = i+1
        tmp = input[i]
        input[i] = input[last]
        input[last] = tmp

        




            




rawInput = input("Please enter a list of numbers, where each number is separated by a space.")
formatInput = [int(i) for i in rawInput.split()]
print(formatInput)
quickSort(formatInput,0,formatInput.length()-1)



