def print_menu():
    # Display the todo list menu options
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_choice():
    # Prompt the user for a menu choice and validate the input
    while True:
        choice = input('Enter your choice: ')
        valid_choices = ('1', '2', '3', '4')
        if choice not in valid_choices:
            print('Invalid choice')
            continue
        else:
            return choice


def display_tasks(tasks):
    # Display the current list of tasks
    if not tasks:
        print('No tasks in the list.')
        return
  
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    # Add a new task to the todo list after validating input
    while True:
        task = input('Enter a new task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Invalid task!')


def remove_task(tasks):
    # Remove a task from the todo list based on user input
    display_tasks(tasks)

    while True:
        try:
            task_number = int(input('Enter the task number: '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)  # Remove the selected task
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number')


def main():
    # Main function to run the todo list application
    tasks = []

    while True:
        print_menu()  # Display the menu
        choice = get_choice()  # Get user choice

        if choice == '1':
            display_tasks(tasks)  # View tasks
        elif choice == '2':
            add_task(tasks)  # Add a new task
        elif choice == '3':
            remove_task(tasks)  # Remove an existing task
        else:
            break  # Exit the application
  

if __name__ == '__main__':
    main()  # Start the application