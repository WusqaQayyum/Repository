#!/usr/bin/env python
# coding: utf-8

# In[12]:


print("\033[1m-----------------BMI CALCULATOR-----------------\033[0m")
weight = float(input("Enter your weight in kilograms: "))
print("Weight is: "+ str(weight))
height = float(input("Enter your height in meters: "))
print("Height is: "+ str(height))

if weight <= 0 or height <= 0:
    print("Please enter valid values for weight and height.")
else:
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("\n------BMI Result------")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


# In[ ]:




