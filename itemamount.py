
sum=0
i=0
while i<=4:
    if sum<=5000:
        item=int(input("Enter the item amount"))
        sum=sum+item
        i=i+1
        print("Total items",i,"selected and total amount is:",sum)
    else:
        print("Account limit crossed")
        break
    
