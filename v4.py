n = int(input("List uzunligini kiriting: "))
lst = []
for i in range(n):
    element = input(f"{i+1}-elementni kiriting: ")
    lst.append(element)
sorted_lst = sorted(lst, key=lambda x: sum(map(int, str(x))))
print(sorted_lst)
