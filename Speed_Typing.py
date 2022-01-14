# Importing important libraries
import random
import time
# Taking an empty list to store scores
score=[]
# List of random words
random_words=["Mexico","Sixpep","India","Burger","Pizza"]

# Function to display a new word
def New_Word():
    # Choosing a word randomly from the random_words list
    word = random.choice(random_words)
    print(f"Your new word is {word}")

    # Initial time
    initial=time.time()
    # Taking word from user
    user=input("Type now ")
    # Final time
    final = time.time()
    # Time taken to type a word
    time_taken = final - initial

    print(f"\nTime taken to type {word} is {time_taken} seconds")
    # Scoring pattern if word is correct
    if word==user:
        print("Correct!")
        if time_taken < 2:
            score.append(2)
        elif 2 < time_taken < 3:
            score.append(1)
        elif time_taken > 3:
            score.append(0)
    #Score given for wrong word
    else:
        print("Wrong!")
        score.append(-1)
    total=0
    for item in range(len(score)):
        total=total+score[item]

    print(f"You scored {score} points and your total score is {total}\n")

# Function to display the score
def Score():
    # printing score table
    print(f"Score table")
    for item in score:
        print(item)
    # Printing sum of scores
    total = 0
    for item in range(len(score)):
        total = total + score[item]
    print(f"Total Score: {total}\n")

# Function to display high score
def High_Score():
    try:
        total = 0
        for item in range(len(score)):
            total = total + score[item]
        print(f"High Score: {total}\n")
    except Exception as e:
        print("High Score is 0")

# Driver Code
if __name__ == '__main__':
    print("\t\t\t Test your typing speed")
    # Creating an infinite loop
    while True:
        print("1.New Word 2.Score 3.HighScore 4.Save 5.Quit")
        try:
            choice=int(input("Player input is "))
        except Exception as e:
            print("Choose a valid option!\n")
            continue
        # To choose option 1 to display a new word
        if choice==1:
            New_Word()
        # To choose option 2 to display the score
        elif choice==2:
            Score()
        # To choose option 3 to display high score
        elif choice==3:
            High_Score()
        # To choose option 4 to save any changes
        elif choice==4:
            print("Saving score and exiting the application\n")
        # To choose option 5 to quit and display last high score
        elif choice==5:
            High_Score()
            break
        # If any other option is selected
        else:
            print("Enter a valid option!\n")

