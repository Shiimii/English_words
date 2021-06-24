import random

def choose_word():
    level = random.randint(1,12)
    num = random.randint(1, 1000)
    with open('.\SVL12000\Level{0:0>2}.txt'.format(level), 'r', encoding='UTF-8') as file:
        data = file.readlines()
    # print(data[num])
    return (data[num].rstrip("\n"), level)

# print(choose_word())