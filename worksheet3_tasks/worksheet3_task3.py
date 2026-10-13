# Define Variables


total_monthly_SMS = 650
# Calculate and store results for each option
optionA_result = ((total_monthly_SMS - 500) * float(0.10))
optionB_result = (total_monthly_SMS * float(0.02))

# Output the result of each plan
print(f"With option A: €{float(optionA_result)}\nWith option B: €{float(optionB_result)}")