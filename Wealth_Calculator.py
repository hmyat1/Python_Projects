import sys

def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    # Initialize total savings with current wealth
    total_savings = current_wealth
    # Loop through each year to calculate wealth
    for year in range(1, years + 1):
        # Calculate interest earned for the year
        interest = total_savings * (rate_of_return / 100)
        # Update total savings with interest and annual contributions
        total_savings += interest + (monthly_savings * 12)
        # Print the total wealth for the current year
        print(f"Year {year}: Total wealth = {total_savings:.2f}")
    return 0

def calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth):
    # Initialize total savings with current wealth
    total_savings = current_wealth
    years_to_freedom = 0
    # Loop until the target wealth is reached
    while True:
        years_to_freedom += 1
        # Calculate interest earned for the year
        interest = total_savings * (rate_of_return / 100)
        # Update total savings with interest and annual contributions
        total_savings += interest + (monthly_savings * 12)
        # Check if the target wealth is reached
        if total_savings > target_wealth:
            print(f"You will reach financial freedom in {years_to_freedom} years! Keep grinding!! ")
            return 0

def main():
    # Prompt user for which program to run
    prog = input("Which program would you like to run? Type 'returns' or 'freedom' ")
    try:
        # Get user inputs for current wealth, rate of return, and monthly savings
        current_wealth = float(input("Enter your current wealth: "))
        rate_of_return = float(input("Enter estimated rate of return (%): "))
        monthly_savings = float(input("Enter how much you can save per month: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input. You must only enter numbers, dumbass!! ")
        sys.exit()
    
    # Execute the appropriate function based on user choice
    if prog == 'returns':
        years = int(input("Enter investment period in years: "))
        calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)
    elif prog == 'freedom':
        try:
            # Get user input for target wealth
            target_wealth = float(input("How much money do you need to be financially free? "))
        except ValueError:
            # Handle invalid input
            print("Invalid input. You must only enter numbers, dumbass!! ")
            sys.exit()
        calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth)
    else:
        # Handle invalid program choice
        print("Invalid input. Type 'returns' or 'freedom'")

# Run the main function
main()