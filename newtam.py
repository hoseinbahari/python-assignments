a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

m = a + b
n = b + c
o = a + c
if (a < n):
    if (b < o):
        if (c < m):
                print("It is possible to draw a triangle")
        else :
             print("It is not possible to draw a triangle")
    else : 
         print("It is not possible to draw a triangle")     
else :
     print("It is not possible to draw a triangle")           
    