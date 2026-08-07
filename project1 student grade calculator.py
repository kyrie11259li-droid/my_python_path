math=int(input("math score:"))
english=int(input("english score:"))
chinese=int(input("chinese score:"))
average=((math+english+chinese)/3)

print("average score:",average)

if average >= 90:
    print("you get A")
elif average >= 80:
    print("you get B")
elif average >= 70:
    print("you get C")
elif average >= 60:
    print("you will get D")
else:
    print("your grade is below D")

if  math < 40 or english < 40 or chinese < 40:
    print("you are fail.")
else:
    print("you pass")
