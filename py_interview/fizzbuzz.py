def fizz_buzz(n):
    for i in range(1, n + 1):
        res = ""
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        print(res or i)

fizz_buzz(30)