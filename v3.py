lst = [[], [], [], [], []]
for x in range(len(lst)):
    input_str = input("ism, lavozm,oylik, bonus,bolm(1,2,3): ")
    lst[x] = input_str.split(",")
for ls in lst:
    ism, lav, oy, bon, bolm = ls
    bon = int(bon)
    if bon > 0:
        print(bolm)
