# # Under 18.5 they are underweight 

# # Over 18.5 but below 25 they have a normal weight 

# # Equal to or over 25 but below 30 they are slightly overweight 

# # Equal to or over 30 but below 35 they are obese 

# Equal to or over 35 they are clinically obese 

# "Your BMI is 18.28678, you are underweight." 

  

# Enter your height in meters e.g., 1.55 

height = float(input("Enter your height in meters. \n")) 

# Enter your weight in kilograms e.g., 72 

weight = int(input("Enter your weight in kilograms.\n")) 

bmi = weight / (height ** 2) 

if bmi < 18.5: 

  print(f"Your BMI is {bmi}, you are underweight.") 

elif bmi < 25: 

  print(f"Your BMI is {bmi}, you have a normal weight.") 

elif bmi < 30: 

  print(f"Your BMI is {bmi}, you are slightly overweight.") 

elif bmi < 35: 

  print(f"Your BMI is {bmi}, you are obese.") 

else: 

  print(f"Your BMI is {bmi}, you are clinically obese.") 

   

   