import time

def quick_sort(data, left, right, draw, speed):
    if left < right:
        pos = partition(data, left, right)
        quick_sort(data, left, pos - 1, draw, speed)
        quick_sort(data, pos + 1, right, draw, speed)
        draw(data, ["Blue" if x >= left and x < pos else "Red" if x == pos
                    else "Yellow" if x > pos and x <= right else "#a871e3" for x in range(len(data))])
        time.sleep(speed)
        
def partition(data, left, right):
    i, j = left, right-1 
    pivot = data[right]
    
    while i < j:
        while i < right and data[i] < pivot:
            i += 1
        while j > left and data[j] >= pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    if data[i] > pivot:
        data[i], data[right] = data[right], data[i] 
      
    return i