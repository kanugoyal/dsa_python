#Python program to interchange first and last elements in a list

def swapList(li):
    size = len(li)
     
    # Swapping
    temp = li[0]
    li[0] = li[size - 1]
    li[size - 1] = temp
     
    return li

def swapPositions(li, pos1, pos2):
     
    li[pos1], li[pos2] = li[pos2], li[pos1]
    return li
     
if __name__ == '__main__':
    li = [22, 45, 58, 98, 78]
    print(swapList(li))

    pos1 , pos2 = 0,1    #give index number
    print(swapPositions(li, pos1, pos2))