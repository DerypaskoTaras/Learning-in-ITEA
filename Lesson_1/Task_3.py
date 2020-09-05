i = 1
while i <= 100:
    if i % 15 == 0:
        print('FizzBuzz')
        i += 1
        continue
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
    i += 1
