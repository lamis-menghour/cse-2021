# this is partie A
total_cost= float(input("Enter the cost of your dream house :"))
portion_down_payment =0.25*total_cost # 25% دفعة أولى
print("The portion down payment is" , portion_down_payment)
annual_salary =float(input("Enter your annual salary:"))
portion_saved =float(input("Enter the percent of your salary to save, as a decimal:"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))

current_savings =0
r =0.04 #4%
monthly_saving = (annual_salary/12 ) *portion_saved 

number_of_months= 1
while current_savings < portion_down_payment :
	number_of_months = number_of_months +1 
	current_savings = current_savings + monthly_saving 
	current_savings = current_savings*r/12 + current_savings 

print('Current savings ', current_savings )
print('Number of months ', number_of_months)

# Test Case 1
# Enter your annual salary:​ 120000
# Enter the percent of your salary to save, as a decimal: ​ . 10
# Enter the cost of your dream home:​ 1000000
# Number of months:​ 183

#Test Case 2
# Enter your annual salary:​ 80000
# Enter the percent of your salary to save, as a decimal: ​ . 15
# Enter the cost of your dream home:​ 500000
# Number of months:​ 105