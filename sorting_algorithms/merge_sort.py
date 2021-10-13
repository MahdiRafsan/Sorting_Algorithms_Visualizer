import time

def merge_sort(data, left, right, draw, speed):
    if left < right:

        mid = (left+right) // 2
        merge_sort(data, left, mid, draw, speed)
        merge_sort(data, mid+1, right, draw, speed)
        merge(data, left, mid, right)
        
        draw(data, ["Blue" if x >= left and x < mid else "Red" if x == mid 
                    else "Yellow" if x > mid and x <= right else "#a871e3" for x in range(len(data))]) 
        time.sleep(speed) 
    
def merge(data, left, mid, right):        
    
    left_half = data[left : mid + 1]
    right_half = data[mid + 1 : right + 1]  
    
    # i → index for left_half
    # j → index for right_half
    i, j, sort_index = 0, 0, left
            
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[sort_index] = left_half[i]
            i += 1        
        else:
            data[sort_index] = right_half[j] 
            j += 1
        sort_index += 1
    
    # adds remaining elements to the sorted list 
    # when one of the left or right lists is empty           
    while i < len(left_half):
        data[sort_index]= left_half[i]
        i += 1
        sort_index += 1
    while j < len(right_half):
        data[sort_index] = right_half[j]
        j += 1
        sort_index += 1
     
   
