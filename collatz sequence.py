def collatz(x):
    for i in range(x):
        print(f"[{i}]", end=",")
        if i % 2 == 0:
            print(i // 2)
        elif i % 2 == 1:
            i = 3*i + 1
            print(int(i))

collatz(30)

