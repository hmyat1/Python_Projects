def get_amount():
    # Prompt the user for a positive amount and validate input
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()  # Ensure amount is positive
            return amount
        except ValueError:
            print('Invalid amount')  # Handle invalid input

def get_currency(label):
    # Prompt the user for a valid currency (USD, EUR, CAD)
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if currency not in currencies:
            print('Invalid currency')  # Handle invalid currency
        else:
            return currency

def convert(amount, source_currency, target_currency):
    # Convert the amount from source currency to target currency
    exchange_rates = {
        'USD': { 'EUR': 0.85, 'CAD': 1.25 },
        'EUR': { 'USD': 1.18, 'CAD': 1.47 },
        'CAD': { 'USD': 0.80, 'EUR': 0.68 },
    }

    if source_currency == target_currency:
        return amount  # No conversion needed if currencies are the same
  
    return amount * exchange_rates[source_currency][target_currency]  # Return converted amount

def main():
    # Main function to execute currency conversion
    amount = get_amount()  # Get the amount to convert
    source_currency = get_currency('Source')  # Get source currency
    target_currency = get_currency('Target')  # Get target currency
    converted_amount = convert(amount, source_currency, target_currency)  # Perform conversion
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')  # Display result

if __name__ == "__main__":
    main()  # Run the main function