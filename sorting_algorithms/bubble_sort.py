import time
    
def bubble_sort(data, draw, speed):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["orange" if x == j or x == j+1 else "#a871e3" for x in range(len(data))])
                time.sleep(speed)  