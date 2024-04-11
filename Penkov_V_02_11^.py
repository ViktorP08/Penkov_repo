import numpy as np
import pandas as pd


# Question 3.
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child.
# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose)
# Versus those who were vaccinated but did not contract chicken pox. Return results by sex.

def vetryanka():
    vaccinated_with = int(input("Пожалуйста, введите количество привитых детей, заболевших ветрянкой: "))
    vaccinated_without = int(input("Пожалуйста, введите количество привитых детей, не заболевших ветрянкой: "))

    male = vaccinated_with / vaccinated_without
    female = vaccinated_with / vaccinated_without

    results = {
        "male": male,
        "female": female
    }

    return results


res = vetryanka()
print(res)

# Question 4.
# In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

w = int(input("Введите, пожалуйста, количество наблюдений: "))
had_vetryanka = []
num_doses = []

for i in range(w):
    had_vetryanka_val = int(input(f"Пожалуйста, введите значение had_vetryanka_column для наблюдения {i + 1}: "))
    num_vaccine_doses_val = int(input(f"Пожалуйста, введите значение num_vetryanka_vaccine_column для наблюдения {i + 1}: "))
    had_vetryanka.append(had_vetryanka_val)
    num_doses.append(num_vaccine_doses_val)

df = pd.DataFrame({"had_vetryanka_column": had_vetryanka,
                   "num_vetryanka_vaccine_column": num_doses})

correlation = df["had_vetryanka_column"].corr(df["num_vetryanka_vaccine_column"])
pval = 2 * (1 - abs(correlation))

print(f"Корреляция: {correlation}")
print(f"pval: {pval}")
