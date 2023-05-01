name = input("enter name : ")
family = input("enter family : ")

geology = int(input("enter geology Score :"))
Meteorology = int(input("enter Meteorology Score :"))
biology = int(input("enter biology Score :"))

average = (geology+Meteorology+biology)/3
if average>=17:
    print("Greate")
elif 12<=average<17:
    print("Normal")
elif average<12:
    print("Fail")
