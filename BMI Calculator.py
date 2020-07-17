print(" ")
print("  This tool will calculate your BMI (Body Mass Index).")
input("  ")
x = True
while x == True:
    MEASURE = input("  Would you like to input your data in Imperial or Metric units?: ")
    if MEASURE.lower() == "imperial":
        height = (float(input("  What is your height in inches?: ")))*0.0254
        weight = (float(input("  What is your weight in lbs?: ")))/2.2
        BMI = round(float(weight/(height**2)),1)
        x = False
    elif MEASURE.lower() == "metric":
        height = (float((input("  What is your height in cm?: "))))/100
        weight = float((input("  What is your weight in kgs?: ")))
        BMI = round(float(weight/(height**2)),1)
        x = False
print("  Your BMI is",BMI)
underweight = range(20)
normal = range(20,25)
overweight = range(25,30)
obese = range(30,40)
extreme = range(40,99**9)
LOSE = round(weight - 24*(height**2),1)
GAIN = round((20*(height**2) - weight),1)
UNIT = "kgs"
if MEASURE.lower() == "imperial":
    GAIN = round((GAIN*2.2),1)
    UNIT = "lbs"
if round(BMI) in underweight:
    print("  You are underweight. Consider healthier lifestyle choices.")
    print("  You need to gain at least",GAIN,UNIT,"to be at a normal BMI")
elif round(BMI) in normal:
    print("  You are a normal weight! Make sure you're living a healthy lifestyle.")
elif round(BMI) in overweight:
    print("  You are overweight. Consider a better diet and exercise plan.")
    print("  You need to lose at least",LOSE,UNIT,"to be at a normal BMI")
elif round(BMI) in obese:
    print("  You are obese. Consider healthier lifestyle choices.")
    print("  You need to lose at least",LOSE,UNIT,"to be at a normal BMI")
elif round(BMI) in extreme:
    print("  You are extremely obese. Consult a healthcare professional.")
    print("  You need to lose at least",LOSE,UNIT,"to be at a normal BMI")

input()
