Name = input(str("Please enter your name: "))
print("Hello", Name, "welcome to Who wants to be a millionaire" )
print()
print("Here are is how the game works: You will be provided with a Question with 4 options and you have to choose the correct option for each correct option you will be rewarded with 100 points on the first question and with each question there will be an incriment of 100 points and the last question having 1 million points")
print()

import random

Questions_answers =[f"1. What is the capital of Japan?\nA. Beijing\nB. Tokyo\nC. Seoul\nD. Bangkok",
    f"2. Which data type is immutable in Python?\nA. List\nB. Dictionary\nC. Tuple\nD. Set",
    f"3. What planet is known as the Red Planet?\nA. Venus\nB. Jupiter\nC. Saturn\nD. Mars",
    f"4. Which element has the chemical symbol 'O'?\nA. Gold\nB. Oxygen\nC. Silver\nD. Osmium",
    f"5. Who wrote Harry Potter?\nA. Stephen King\nB. J.K. Rowling\nC. George R.R. Martin\nD. Suzanne Collins",
    f"6. What is the largest mammal?\nA. Elephant\nB. Blue Whale\nC. Giraffe\nD. Orca",
    f"7. In math, what is 9 multiplied by 6?\nA. 42\nB. 54\nC. 63\nD. 48",
    f"8. What does CPU stand for?\nA. Central Processing Unit\nB. Computer Personal Utility\nC. Control Power Unit\nD. Central Peripheral Unit",
    f"9. Which of these is a prime number?\nA. 12\nB. 9\nC. 17\nD. 21",
    f"10. Which ocean is the largest?\nA. Indian\nB. Atlantic\nC. Pacific\nD. Arctic"]

# Correct answers
correct_answers = ['B', 'C', 'D', 'B', 'B', 'B', 'B', 'A', 'C', 'C']
score = 0
question_value = 100

# Loop through questions
for i in range(len(Questions_answers)):
    print(Questions_answers[i])
    answer = input("Your answer (A/B/C/D): ").upper()
    
    if answer == correct_answers[i]:
        if i == 9:  
            score += 1000000
            print("Correct! You won 1,000,000 points! Congratulations, you are a Millionaire!")
        else:
            score += question_value
            print(f"Correct! You won {question_value} points!")
        question_value += 100
    else:
        print(f"Wrong! The correct answer was {correct_answers[i]}")
        print(f"Game Over! Your final score is {score} points")
        break

    print()
           

