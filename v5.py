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
