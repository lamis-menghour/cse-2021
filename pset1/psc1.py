# this is partie C
total_cost= 1000000
portion_down_payment =0.25*total_cost # 25% دفعة أولى
print("The portion down payment is" , portion_down_payment)
annual_salary =float(input("Enter your annual salary:"))
portion_saved =float(input("Enter the percent of your salary to save, as a decimal:"))
semi_annual_raise = 0.07

current_savings =0
r =0.04 #4%

number_of_months= 1
while current_savings < portion_down_payment :
	number_of_months = number_of_months +1 
	current_savings = current_savings + (annual_salary/12 ) *portion_saved 
	current_savings = current_savings*r/12 + current_savings 
	if number_of_months % 6 == 0 :
		annual_salary = annual_salary + annual_salary*semi_annual_raise
print("current saving", current_savings )
print('Number of months ', number_of_months)








# Test Case 1   
# Enter your starting annual salary:​ 150000 
# Best savings rate:​ 0.4411  
# Steps in bisection search:​ 12 

 
# Test Case 2   
# Enter your starting annual salary:​ 30000 
# Best savings rate:​ 0.2206 
# Steps in bisection search:​ 9
 
 
# Test Case 3 
# Enter your starting annual salary:​ 10000 
# It is not possible to pay the down payment in three years.