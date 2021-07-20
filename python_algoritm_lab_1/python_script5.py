import random
a = input("Введите буквы: ")
def generate_random_string(a):
    letters = 'abcdef'
    rand_string = ''.join(random.choice(letters) for i in range(a))
    print("Random string of a", a, "is:", rand_string, a)

generate_random_string(1)


