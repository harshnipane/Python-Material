#write a program to print "*" 5 times on same line

'''idx =0
while(idx < 5):
    print("*",end=" ")
    idx +=1

print("a" * 10)   ''' 




#while_else





#wap to ask order from user show menu and take one iten at a Time
#when user says q the stop and print msg "complete"
#limit of orders - 5
#a - Thali b- chapati c-lassi d-paratha q- quit

'''order=1
count=0
while(order !='q'):
    print("Menu: a-Thali b-chapati c-lassi d-paratha q-quit")
    order = input("enter order ")  
    count += 1
    if(count > 5):
        print("Limit Reached")
        break
else:
    print("Thank you")'''




#for_loops





# range(5) = 0,1,2,3,4
for idx in range(5):
    print('a',end=" ")

#for_else

marks= [45,50,69,70,40,89,90]
for m in marks:
    print(m)
    if m <=50:
        print("FAIL")
        break
else:
    print("All pass")    










