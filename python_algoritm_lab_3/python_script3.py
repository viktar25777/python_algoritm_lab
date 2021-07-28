import random
from random import randint
randint(1, 150)
list = [randint(1, 150)]
def most_frequent(list):
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
            return num
        list = [randint(1, 150)]
        return list

print(most_frequent(list))

