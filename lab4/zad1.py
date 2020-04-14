lista=[]
for i in range(0, 100,4):
        lista += [i]
plik=open("lista.txt","a+")
plik.writelines(str(lista))
plik.close