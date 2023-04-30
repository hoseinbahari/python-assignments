name = input("enter name : ")
family = input("enter family : ")

geology = int(input("enter geology Score :"))
Meteorology = int(input("enter Meteorology Score :"))
biology = int(input("enter biology Score :"))

avrage = (geology+Meteorology+biology)/3
if avrage>=17:
    print("Your educational status is excellent")
elif 10<avrage<17:
    print("Your academic grade is average")
elif 0<avrage<10:
    print("You have been rejected")
