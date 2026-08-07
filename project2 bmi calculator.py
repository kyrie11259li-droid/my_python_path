height=float(input("enter your height(m)"))
weight=float(input("enter your weight(kg):"))
bmi=weight/(height*height)

print(f"Your bmi is: {bmi:.2f}")

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print("normal weight")
elif 25 <= bmi <=29.9:
    print("overweight")
else:
    print("obese")
