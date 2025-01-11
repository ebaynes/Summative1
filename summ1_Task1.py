import random

def welcome_message():
    """Display the welcome message to the user."""
    print("Welcome to your simple equation test!")
    print("You will be presented with 5 simple equations.")
    print("Enter your answer to each equation and your score will be calculated out of 5. Good Luck!")

def generate_equation():
    """Generate a random equation and the answer.
    
    Returns:
        tuple: Equation, string (?), and the calculated answer.
    """

    # Generate random numbers for each element of the equation so all 5 are different.
    randnum1 = random.randint(1, 5)
    randnum2 = random.randint(1, 10)
    randnum3 = random.randint(1, 10)
    # Calculate the answer.
    answer = randnum1 * (randnum2 + randnum3)
    # Generate the equation.
    equation = f"{randnum1} X ({randnum2} + {randnum3}) = ?"
    #return the equation and the answer.
    return equation, answer

def check_valid_answer(prompt):
    """Get the users answer and check that it's a number.

    Args:
        prompt (str): Prompts the user to input a number.

    Returns:
        int or None: The user's answer if it's a number or None.
    """
    try:
        user_answer = input(prompt)
        return int(user_answer)
    except ValueError:
        print("Invalid input. A number is required.")
        return None

def evaluate_user_answer(user_answer, correct_answer):
    """Evaluate the user's answer and return the result.

    Args:
        user_answer (int): The user's answer.
        correct_answer (int): The correct answer.

    Returns:
        tuple: Boolean if the answer is correct and a feedback message.
    """
    if user_answer == correct_answer:
        return True, "Correct, well done!"
    else:
        return False, f"Incorrect, the answer is {correct_answer}"

def display_equation(equation, index):
    """display the 5 equations to the user.

    Args:
        equation (str): Display the equation.
        index (int): The index number of the equation.

    Returns:
        str: The equation index place (first and last).
    """
    if index == 0:
        return f"Your first equation is:\n{equation}"
    elif index < 4:
        return f"Your next equation is:\n{equation}"
    else:
        return f"Your final equation is:\n{equation}"

def simple_equation_test():
    """Run the test for 5 equations and return the score."""
    userscore = 0
    for i in range(5):
        equation, answer = generate_equation()
        print(display_equation(equation, i))

        user_answer = check_valid_answer("Enter the answer: ")
        if user_answer is not None:
            is_correct, feedback = evaluate_user_answer(user_answer, answer)
            print(feedback)
            if is_correct:
                userscore += 1

    return userscore

def display_result(userscore):
    """Display the final score and a message based on performance."""
    print("Your final score is:", userscore, "/5")
    if userscore >= 3:
        print("Well done, you did well!")
    else:
        print("Better luck next time!")

def run_equation_test():
    """Main function to run the simple equations test."""
    welcome_message()
    repeat_test = "yes"

    while repeat_test == "yes" or repeat_test == "Yes":
        userscore = simple_equation_test()
        display_result(userscore)
        repeat_test = input("Would you like to take the test again? (yes/no): ")

    print("Thank you for taking the test!")

run_equation_test()