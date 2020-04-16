user_input = input()

number, k = user_input.split(" ")
number, k = int(number), int(k)

while k != 0:
    if number % 10 == 0:
        number //= 10
    else:
        number -= 1
    k -= 1
print(int(number))