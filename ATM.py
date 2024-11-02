class ATM:
    def __init__(self):
        # Initialize the ATM with a balance of 0
        self.balance = 0

    def check_balance(self):
        # Return the current balance
        return self.balance

    def deposit(self, amount):
        # Deposit a positive amount into the ATM
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        # Withdraw a positive amount if sufficient funds are available
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        self.balance -= amount


class ATMController:
    def __init__(self):
        # Initialize the ATM controller with an ATM instance
        self.atm = ATM()

    def get_number(self, prompt):
        # Get a valid number input from the user
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    def display_menu(self):
        # Display the ATM menu options
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')    

    def check_balance(self):
        # Display the user's current balance
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance}')    

    def deposit(self):
        # Handle the deposit process
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount}.')
                break
            except ValueError as error:
                print(error)    

    def withdraw(self):
        # Handle the withdrawal process
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew ${amount}.')
                break
            except ValueError as error:
                print(error)    

    def run(self):
        # Main loop to run the ATM interface
        while True: 
            self.display_menu()
            choice = input('Please choose an option: ')
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid choice. Please try again.')


def main():
    # Start the ATM application
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()  # Execute the main function