
## Python Indentation Practice with if Statements
## Objective: The aim of this assignment is to understand the importance of indentation in Python, especially with if statements.

## Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.


""" weather = "sunny"

if weather == "sunny":
print("Wear sunglasses!")
else:
print("Take an umbrella!") """


weather = "sunny"

if weather == "sunny":
    print ("Wear sunglasses")
else:
    print ("Take an umbrella!")

print("="* 50)

### Task 2: Your Mood Today  Create another if statement evaluating the users mood. Ask the user how they feel today using input(). If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented.

mood_selector = input("Enter your mood here: ")
print("You selected: " + mood_selector)

if mood_selector == "happy":
    print("That's great to hear")
elif mood_selector == "sad":
    print("I hope your day gets better")
else:
    print("incorrect entry, Please select between happy and sad")