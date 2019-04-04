
# def high_and_low(numbers):
#     numbers = numbers.split()
#     min = numbers[0]
#     max = numbers[0]
#     for i in numbers:
#         if int(i) > int(max):
#             max = i
#         if int(i) < int(min):
#             min = i
#
#     numbers = max + " "  + min
#     return numbers
#
#
# numbers = high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
# print(numbers)


def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = [ int(i) for i in numbers]
    numbers =  str(max(numbers)) + " " + str(min(numbers))
    return numbers

numbers = high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
print(numbers)
