

def para(data):
    for index in range(0,len(data),2):
        yield data[index]
gen = para("Parzyste")
print(gen)
print(next(gen))
print(next(gen))
            
        

