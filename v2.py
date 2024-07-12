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
