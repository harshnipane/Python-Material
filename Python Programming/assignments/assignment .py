'''print(5e200 *2.0e210)
print(3.4e-320 / 1e100)'''




'''print(1/3)
print(format(1/3, '.3f'))
print(format(1/3, '.1f'))
print(6*1/3)
print(1/3 + 1/3 + 1/3 + 1/3 + 1/3 + 1/3)'''




'''print(format(22/7,'.5f'))
f = "{:>10}".format("Hello")
print(f)
fs = "{:<10}".format("Hello")
print(fs)
print(format("Hello", '>10'))
print(format("Hello", '<10'))

print(format("Hello",'#^15'))'''





#find ASCII of characters'a' , 'A' , 'z' , 'Z' using ord() one by one
'''print(ord('a')) #97
print(ord('A')) #65
print(ord('z')) #122
print(ord('Z')) #90'''

#find ASCII of characters '0', '9', ' ', "\n" , "\t" using ord() one by one
'''print(ord('0')) #48
print(ord('9')) #57
print(ord(' ')) #32
print(ord("\n")) #10
print(ord("\t")) #9'''


#Find characters for ASCII values 35, 67, 50, 99
'''print(chr(35)) #
print(chr(67)) #C
print(chr(50)) #2
print(chr(99)) #c'''

#start from 97-'a' 
#end at 122-'z'.





'''print("abc","\n","bcd")
print("abc\nbcd")
print(1,'\n',2)
print("hello \n\n!!")
print("This is '\t' means tab")'''


'''print("This","is","different",sep='\t')
print("This","is","different",sep='#')
print("This","is","different",sep='\n') 
print("This","is","different",end='\n')'''




'''print(0 / 2)         #0.0
print(10 // 2.0)     #5.0
print(101 / 3)       #33.666666664
print(101 // 3)      #33
print(101 % 3)       #2
print(2 ** 4)        #16
print(3 ** 2)        #9
print(abs(-10))      #10 give absolute value 
print(divmod(101,3)) #(33,2) divmod gives two values , interger division and remainder
print(8 << 1)        #16
print(8 << 2)        #32
print(32 >> 2)       #8
print(16 >> 1)       #8'''



#Write a program to take marks of 3 subjects from a student. Calculate total in variable name 'total'.
'''a=int(input("Enter marks 1 "))
b=int(input("Enter marks 2 "))
c=int(input("Enter marks 3 "))

total = a+b+c
print(total)'''



'''print(2 + 3 * (4 -1))            #11
print(2 + ((3 *4) - 8))          #6
print((2 + 3) * 4)               #20
print(-10 + 25 / (16 + 12))      #-9.10714...
print(2 ** 2 ** 2)               #16
print((3 ** 2) ** 3)             #729
x = y = 3 + 5                    #x=8 y=8
print(8/2*(2+2))                 #16
'''



'''
x = y = 10
print(x)      #10
print(y)      #10
#x1 = 20 = y1  #error'''


'''x=10
y=34.4
print(x and y) #34.5
print(x or y)  #10'''





#Write a program check whether an years is leap year or not the year is leap if it satisfies following condition  
#It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 400 then it is leap year 

'''year = int(input("enter the year"))

if(year % 4 == 0 or year % 400 == 0):
    print("year is leap year")
else:
    print("Not a leap year")'''






'''Write a program to accept the price of a bike and display the road tax and insurance to be paid according to the following criteria . also display total amount to be paid.  
      
        Cost price (in Rs)           Tax                Inssurance  
        > 100000                     15 %                   20%  
        > 50000 and <= 100000        10%                    8%  
        <= 50000                     5%                     5%'''


'''cost = int(input("enter the cost"))
tax=0
insurance =0
total =0
if(cost > 100000):
    tax = cost *0.15
    insurance = 0.20* cost
elif(50000 < cost <= 100000) :
    tax = 0.10*cost 
    insurance = 0.8 * cost
else:
    tax = 0.5*cost
    insurance = 0.5*cost    

total = cost+tax+insurance
print("TAX=",tax,"Insurance=",insurance,"Totalcost=",total,sep=" ")   ''' 



#notes
'''
notes=[2000,500,100,50,10,5,2,1]
count =0
amount = int(input("enter the amount"))
for i in notes:
    if(amount >= i):
        count = amount // i
        print(i," ",count)
        amount -= count*i
'''




#Loop_assignment


#Accept 10 integers from user  and print their average value on the screen 

sum =0
for i in range(10):
    num = int(input("enter the number"))
    sum = sum + num
average = sum/10
print(average)   













