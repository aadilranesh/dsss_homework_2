import random


def generate_random_int(min_val, max_val):
    """
    Generates a random integer within the specified range.

    Args: 
        min_val (int): The minimum value for the random integer.
        max_val (int): The maximum value for the random integer.
    
    Returns: 
        int: A random integer within the range [min_val, max_val].
    """
    return random.randint(min_val, max_val)


def select_random_operator():
    """
    Selects a random mathematical operator from the defined set.

    Returns: 
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Creates a mathematical problem and calculates the answer based on the provided operator.
    
    Args:
        num1 (int): First operand.
        num2 (int): Second operand.
        operator (str): The arithmetic operator ('+', '-', or '*').
    
    Returns:
        tuple: A tuple containing:
            - str: The formatted math problem as a string.
            - int: The resulting answer of the math problem.

    Raises:
        ValueError: If an invalid operator is input by the user.
    """
    problem = f"{num1} {operator} {num2}"

    # Perform the calculation based on the operator
    if operator == '+': 
        ans = num1 + num2
    elif operator == '-': 
        ans = num1 - num2
    elif operator == '*':
        ans = num1 * num2
    else:
        raise ValueError("Invalid operator")

    return problem, ans

def math_quiz():
    """
    Runs a math quiz game with randomly generated math problems.
    The user is asked to answer each problem and their score is displayed at the end.
    """
    score = 0
    total_questions = 3 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_int(1, 10); 
        num2 = generate_random_int(1, 5); 
        operator = select_random_operator()

        problem, correct_ans = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_ans = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue 

        # Check if the user's answer is correct
        if user_ans == correct_ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_ans}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
