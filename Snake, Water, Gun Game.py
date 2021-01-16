# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
import random

lst = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("--- Snake,Water,Gun Game ---")
print("s for snake \nw for water \ng for gun ")
print('You have 10 chance to win\n')
name = input('Enter your name : ')

# making the game in while
while no_of_chance < chance:
    _input = input('\nSnake, Water, Gun : ')
    _random = random.choice(lst)

    if _input == _random:
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print("Tie")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")

    # if user enter g
    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"{name}: {_input}")
        print(f"Computer: {_random}")
        print(f"Score: {name} {human_point}  computer {computer_point} \n ")

    else:
        print("Please enter s w g\n")

    no_of_chance = no_of_chance + 1
    print(f"Left {chance - no_of_chance} out of {chance}")

print("--- Game over ---")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print('Better luck next time')

else:
    print(f'congratulations you won')

print(f"Score: {name} {human_point}  computer {computer_point} \n ")





