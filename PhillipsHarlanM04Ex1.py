num = int(input("Enter The Number: "))
if num > 1:
    num = num+1
    list = []
    for j in range (2,num,1):
        flag = 0
        for i in range (2,int(j/2)+1,1):
            if(j%i)== 0:
                flag = 1
                break
        if flag==0:
            list.append(j)
    print(list)  
else:
    print("Enter Number Greater Than 1")