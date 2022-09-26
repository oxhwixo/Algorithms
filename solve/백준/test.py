func = list(input().split('-'))

for i in range(len(func)):
    if(func[i].isdigit()==False):
        func[i] = eval(func[i])
        
func2 = list(map(int, func))

for i in range(len(func2)):
    if(i>=1):
        func2[0] -= func2[i]


print(func2[0])