#!/usr/bin/env python
# coding: utf-8

# # 1. if :

# In[4]:


#Example program to check the given num is +ve or -ve
n=int(input("Enter number to check"))
if n>0:
    print("+ve number")
if n<0:
    print("-ve number")


# In[6]:


#program to check the given num is even or odd
n=int(input("Enter number to check even or odd:"))
if n%2==0:
    print("Even number")

if n%2!=0:
    print("odd number")


# # 2. if else:

# In[8]:


#exampl program to check the given number is +ve or -ve
n=int(input("Enter number to check +ve or -ve:"))
if n>0:
    print("+ve number")
else:
    print("-ve number")


# In[10]:


#program to check the given num is even or odd
n=int(input("Enter number to check even or odd:"))
if n%2==0:
    print("Even number")
else:
    print("odd number")


# In[11]:


#program to find the biggest number of given two numbers
a=10
b=20
if a>b:
    print("a is big")
else:
    print("b is big")


# In[13]:


#program to find the biggest number of given two numbers
a=int(input("Enter a value"))
b=int(input("Enter b value"))
if a>b:
    print("a is big")
else:
    print("b is big")


# In[15]:


#program to check the password
oldpswd=9966
pswd=int(input("Enter paswrd:"))
if pswd==oldpswd:
    print("Correct pswrd")
else:
    print("Wrong pswrd")


# # 3. elif

# In[ ]:


syntax:
    if condition:
        ----------
        ----------
    elif condition2:
        -----------
        -----------
    elif condition3:
        -----------
        -----------
        .
        .
        .
        .
        .
        .
    else:
        -------------
        -------------


# In[6]:


m=int(input("Enter student marks to know the grade:"))
if (m>=40 and m<=50):
    print("C Grade")
elif (m>50 and m<=60):
    print("B Grade")
elif (m>60 and m<=70):
    print("A Grade")
elif (m>70 and m<=89):
    print("First class with distinction")
elif (m>=90 and m<=100):
    print("O Grade")
else:
    print("Failed")


# In[ ]:


Assignment :
    1. Write a program to find the biggest num of given three nums
    


# In[10]:


#program to convert digits to words
n=int(input("Enter number to convert into the word:"))
if n==0:
    print("ZERO")
elif n==1:
    print("ONE")
elif n==2:
    print("TWO")
elif n==3:
    print("THREE")
elif n==4:
    print("FOUR")
elif n==5:
    print("FIVE")
elif n==6:
    print("SIX")
elif n==7:
    print("SEVEN")
elif n==8:
    print("EIGHT")
elif n==9:
    print("NINE")
else:
    print("Enter numbers between 0 to 9:")


# ## Nested if else:

# In[14]:


#example program for ATM operations
PIN=1234
AB=5000
UPIN=int(input("Enter PIN Number:"))
if PIN==UPIN:
    UAMOUNT=int(input("ENter the amount to withdraw:"))
    if UAMOUNT<=AB:
        print("YOur transaction is in process.. Please collect your cash")
        AB=AB-UAMOUNT
        print("Remaning Balance in your account:",AB)
    else:
        print("Insufficient funds ...")
else:
    print("WRONG PIN ... Please Try again")


# In[15]:


#example program for ATM operations
PIN=1234
AB=5000
UPIN=int(input("Enter PIN Number:"))

print("1. WITHDRAW       \t 2.PIN CHANGE ")
print("3. BALANCE ENQUIRY\t 4.Mobile Number Change")
x=int(input("Press the number to process: "))

if x==1:
    if PIN==UPIN:
        UAMOUNT=int(input("ENter the amount to withdraw:"))
        if UAMOUNT<=AB:
            print("YOur transaction is in process.. Please collect your cash")
            AB=AB-UAMOUNT
            print("Remaning Balance in your account:",AB)
        else:
            print("Insufficient funds ...")
    else:
        print("WRONG PIN ... Please Try again")
elif x==2:
    xpin=int(input("Enter old pin to change ur pin:"))
    if PIN==xpin:
        PIN=8899
        print("PIN changed successfully ...please dont share with any one...")
    else:
        print("Old PIN is wrong please try again....")
elif x==3:
    print("Account Balance is :", AB)

elif x==4:
    print("Please contact your nearest bank to change phone number....")
else:
    print("Wrong option selected")


# In[7]:


#example program for ATM operations
PIN=1234
AB=5000
UPIN=int(input("Enter PIN Number:"))
if PIN==UPIN:
    print("1. WITHDRAW       \t 2.PIN CHANGE ")
    print("3. BALANCE ENQUIRY\t 4.Mobile Number Change")
    x=int(input("Press the number to process: "))

    if x==1:
        if PIN==UPIN:
            UAMOUNT=int(input("ENter the amount to withdraw:"))
            if UAMOUNT<=AB:
                print("YOur transaction is in process.. Please collect your cash")
                AB=AB-UAMOUNT
                print("Remaning Balance in your account:",AB)
            else:
                print("Insufficient funds ...")
        else:
            print("WRONG PIN ... Please Try again")
    elif x==2:
        xpin=int(input("Enter old pin to change ur pin:"))
        if PIN==xpin:
            ypin=int(input("Enter new pin to change old pin:"))
            PIN=ypin
            print("PIN changed successfully ...please dont share with any one...")
            print("Your new pin is:",PIN)
        else:
            print("Old PIN is wrong please try again....")
    elif x==3:
        print("Account Balance is :", AB)

    elif x==4:
        print("Please contact your nearest bank to change phone number....")
    else:
        print("Wrong option selected")
else:
    print("Wrong pin ... Please try again....")



# # II. Interative Statements

# In[ ]:


If we want execute a group of statements multiple times then we should use iterative statements.

1. for loop
2. while loop


# ## 1. for loop:

# In[ ]:


syntax:
    for i in sequence:
        -------------
        -------------
        -------------


# In[1]:


#Example program for for loop
s="Hello"
for i in s:
    print(i)


# In[3]:


#Example program for for loop
s="Hello"
i=2
for i in s:
    print(i)


# In[4]:


#Example program for for loop
l=[1,2,3,4,5,6,7,8]
for i in l:
    print(i)


# In[5]:


#Example program without for loop
l=[1,2,3,4,5,6,7,8]
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
print(l[6])
print(l[7])
    


# In[7]:


print("Venky")
print("Venky")
print("Venky")
print("Venky")
print("Venky")
print("Venky")
print("Venky")
print("Venky")


# In[11]:


for i in range(10):
    print("Venky")


# In[13]:


for i in range(1,21):
    if i%2==0:
        print(i)


# In[16]:


#program to print even nums between given range 
for i in range(2,20,2):
    print(i)


# In[17]:


#program to print even nums between given range 
for i in range(1,20,2):
    print(i)


# In[18]:


#program to print odd numbers using for loop
for i in range(1,21):
    if i%2!=0:
        print(i)


# In[21]:


#program to print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)


# In[22]:


#program to find sum of list values
l=[1,2,3,4,7,20,12]
sum=0
for i in l:
    sum=sum+i
print("Sum of list of values is:",sum)


# In[ ]:




