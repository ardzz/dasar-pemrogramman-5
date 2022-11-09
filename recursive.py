def recursive(n):
    if n > 0:
        print(n)
        recursive(n-1)
    else:
        print(n)


number = int(input("Enter a number: "))
recursive(number)