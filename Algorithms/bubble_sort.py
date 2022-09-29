def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [6,12,2,11,77,38,55,20,4]
    elements = [1000221,100001,10001,1001,101]
    #elements = ["kan", "air", "gar", "mah", "alka"]

    bubble_sort(elements)
    print(elements)