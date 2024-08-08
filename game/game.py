import random
import requests

def save_score(username, score):
    url = "http://<webapp-service-url>/save_score"
    data = {'username': username, 'score': score}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Score saved successfully!")
    else:
        print("Failed to save score.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    username = input("Enter your username: ")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations, {username}! You guessed the number in {attempts} attempts.")
            save_score(username, attempts)
            break

if __name__ == "__main__":
    play_game()
