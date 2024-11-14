import time
import sys

def perform_calculation():
    print("Please note this calculator can only do math with 2 numbers only.")
    print("We/I am working on providing more digits.")

    # Operations Menu
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    # Take user input for the operation
    operation_choice = input("Please enter the number corresponding to the operation: ")

    # Validation for correct operation choice
    if operation_choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please restart the program and choose a valid operation.")
        return

    # Ask for confirmation
    operation_names = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Division',
        '4': 'Multiplication'
    }

    operation = operation_names[operation_choice]
    confirmation = input(f"You selected {operation}. Are you sure you want to continue? (Yes/No): ")

    if confirmation.lower() != "yes":
        print(f"You chose not to continue with {operation}.")
        return

    # Try to get two numbers from the user
    try:
        num_1 = float(input("Please provide the first digit: "))
        num_2 = float(input("Please provide the second digit: "))
    except ValueError:
        print("Invalid input. Please make sure you enter numeric values.")
        return

    # Perform the selected operation
    if operation == "Addition":
        result = num_1 + num_2
    elif operation == "Subtraction":
        result = num_1 - num_2
    elif operation == "Division":
        if num_2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num_1 / num_2
    elif operation == "Multiplication":
        result = num_1 * num_2

    print(f"Here's your answer: {result}")
    print("Thanks for using my calculator!")
    print("Made with Love By Kim Pirun.")
    print("Chat-GPT made the bones, I made the brains, the skin, the hair and everything else if you get what I mean:)")

def main():
    while True:
        perform_calculation()
        
        # Ask if the user wants to perform another calculation
        repeat = input("\nWould you like to perform another calculation? (Yes/No): ")
        if repeat.lower() != "yes":
            break

    # Countdown before exit
    print("\nThe program will close in 20 seconds...")
    for i in range(20, 0, -1):
        print(f"Closing in {i} seconds...")
        time.sleep(1)  # Delay for 1 second

    print("Goodbye!")  # This will print right before the program exits

# Run the main function
if __name__ == "__main__":
    main()
