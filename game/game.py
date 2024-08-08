import random
import requests

def save_score(username, score):
    url = "http://<webapp-service-url>/save_score"  # Replace with your web app service URL
    data = {'username': username, 'score': score}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Score saved successfully!")
        else:
            print(f"Failed to save score. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending score: {e}")

def play_game():
    print("Welcome to the Number Guessing Game!")
    username = input("Enter your username: ")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
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
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_game()
