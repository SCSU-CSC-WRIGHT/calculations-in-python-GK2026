################ Lab 2 #####################
weight=float(input(("Enter your weight (kg): ")))
height=float(input(("Enter your height(m): ")))
BMI=float(weight//(height**2))
FinalBMI=print("Your BMI is: ", (BMI))
if BMI >= 18.5 and BMI <=24.9:
    print("You are within the healthy BMI range")
