import random


class Generate_numbers(object):
    def numbers(self):
        return random.sample(range(10000000), 100000)


nums = Generate_numbers()
f = open("numbers.txt", "w+")
for num in nums.numbers():
    f.write("%i\n" % num)
f.close()
