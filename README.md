# CS50-Final-Project
# Title: Calculator
## Name: Atharva Ghorpade
## GitHub username: Drew3470
### Video Demo: https://youtu.be/LaLEn9AQOeI
### Date of Video Recording: 07/03/2025

### Description:

Hey so this is my final project on CS50P . So for this project, i decided to create a simple calculator that allows user to perform basic arithmetic operations interactively.The program is menu-driven and provide option for addition,subtraction,multiplication, and division.The user can repeatedly perform calculations untill they choose to exit

The program ensures that invalid Inputs for example non-numeric values do not cause it to crash. Additionally,it prevent errors like division by zero by displaying and appropriate error message instead of allowing the program to fail

# Working

When the program starts, the user is presented with a menu displaying five options:
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit

The user selects and option by entering the corresponding number(1-5).If the user selects an arithmetic operation, they are prompted to enter two numbers. The program then performs the requested calculation and displays the result.

a menu appears which allows the user to perform more calculations or exit.If the user enters an invalid option anything other than (5), they are given a chance to enter a valid input again.However, if they enter an alphabetic character instead of a number, the program immediately exits with an error message.

# Edge Cases Handling

This program includes various checks and validations to handle edge cases. If the user enters an invalid menu selection, they are prompted again to provide a correct input. The program ensures that only numeric values are accepted when entering numbers, preventing crashes due to incorrect inputs. It also prevents division by zero by detecting such cases and displaying an appropriate error message instead of failing. Additionally, users can perform multiple calculations continuously without needing to restart the program, making the experience seamless and user-friendly.


# Example


1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
5. Exit

select a option (1/2/3/4/5/): 1
Enter first number: 10
Enter second number: 5
Result: 10 + 5 = 15.0

The menu is displayed again so the user can continue performing calculations.

# features

The calculator follows a menu_driven approach,means users do not need to restart the program to perform multiple calculations

Input Validation: if the user enter non numeric value the program does not crash
                  if user enters wrong menu option they are prompted again

Handling Division: by zero: as we know we cant divide by 0 so if the user tries to divide by zero, the program catches the error and displays it

looping: user doesnt have to keep restarting the program

# Code Structure

add(): Prompts the user to enter two numbers, calculates the sum, and displays the result.

subtract(): the subtract Prompts the user to enter two numbers, calculates the difference, and displays the result.

multiply(): it Prompts the user to enter two numbers, calculates the product, and displays the result.

divide(): Prompts the user to enter two numbers, checks if the divisor is zero, and if not, performs division.

store(): Handles the menu display and user input processing, ensuring the correct functions are called.

# thoughts

so yeah thats it,
This project helped me reinforce fundamental programming concepts such as:
Functions and modular programming also the error handling

Im so glad that i got the chance to learn from my dream university. Im extremely grateful for the opportunity to complete CS50P, as it has expanded my knowledge and strengthened my coding abilities.
I am excited to explore more complex projects using the knowledge I gained from CS50P!

Thank you for checking the project
