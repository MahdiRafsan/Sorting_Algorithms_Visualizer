import time

def insertion_sort(data, draw, speed):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
            draw(data, ["Orange" if x == j or x == i else "#a871e3" for x in range(len(data))])
            time.sleep(speed)
