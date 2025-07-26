fruits=['Orange', 'Mango', 'Apple', 'Grape', 'Papaya','Pineapple'] 

print(fruits) 

price=(60, 80, 220, 80, 90,150) 

purchase_quantity=eval(input("Enter the number of quantiy of each item in order: ")) 

purchase_total=tuple() 

a=tuple() 

sum1=0 

for i in range(len(fruits)): 

     purchase_total+=((purchase_quantity[i],purchase_quantity[i]*price[i]),) 

     a+=(purchase_quantity[i]*price[i],) 

     sum1+=purchase_quantity[i]*price[i] 

x=tuple(zip(fruits,price,purchase_quantity,a)) 

purchase_receipt=tuple() 
for i in x: 

    if i[2]!=0: 

        purchase_receipt+=i 

         

print("Fruit       Price       Qty         Total Price") 

for  i in purchase_receipt: 
    
    if purchase_receipt.index(i)% 4 ==0:
        print()
    print(i,end=' '*(12-len(str(i))))
print()
print("Total Amt", sum1)        
