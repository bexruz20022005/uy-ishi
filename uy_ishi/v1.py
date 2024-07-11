'''
v1-misol

def ikki_had_mus_man(numbers):
    for i in range(len(numbers) - 1):
        if (numbers[i] > 0 and numbers[i + 1] > 0) or (numbers[i] < 0 and numbers[i + 1] < 0):
            print(numbers[i], numbers[i + 1])
numbers = [int(x) for x in input("Iltimos, sonlarni vergul bilan ajrating: ").split(",")]
ikki_had_mus_man(numbers)
'''

'''
def find_value(d):
    k_nol = 0
    k_bir = 0
    kay = []
    for vel,key in enumerate(d):
        kay.append(key)
    k_nol = key.count("0")
    k_bir = key.count("1")
    if k_nol >k_bir:
        return "0"
    elif k_bir >k_nol:
        return "1"
    else:
        return d
dictionary = {}
for i in range(6):
    key = input(f"Ismni kiriting ({i+1}-chi element uchun): ")
    value = input(f"Velyuni kiriting ({key} uchun, faqat '0' yoki '1' bo'lishi mumkin): ")
    dictionary[key] = value
kop_values = find_value(dictionary)
if kop_values==dictionary:
    print("0")
    for v,k in enumerate(dictionary):
        if k=='0':
            print(v)
    print("1")
    for ve,ke in enumerate(dictionary):
        if ke=="1":
            print(ve)
else:
    print(kop_values)
    for key,val in enumerate(dictionary):
        if val == kop_values:
            print(key)
'''

'''
lst = [[], [], [], [], []]
for x in range(len(lst)):
    input_str = input("ism, lavozm,oylik, bonus,bolm(1,2,3): ")
    lst[x] = input_str.split(",")
for ls in lst:
    ism, lav, oy, bon, bolm = ls
    bon = int(bon)
    if bon > 0:
        print(bolm)
'''

'''
n = int(input("List uzunligini kiriting: "))
lst = []
for i in range(n):
    element = input(f"{i+1}-elementni kiriting: ")
    lst.append(element)
sorted_lst = sorted(lst, key=lambda x: sum(map(int, str(x))))
print(sorted_lst)
'''

naqsh = []
c = 0
for i in range(5):
	rang = input(f"rang {i+1}: ")
	naqsh.append(rang)
for x in range(len(naqsh)-1):
	if naqsh[x].lower()!=naqsh[x+1].lower():
		c = c+1
c = c+5*2
print(c)

