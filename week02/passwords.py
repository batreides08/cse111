import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
wordlist_path = os.path.join(script_dir, "wordlist.txt")
toplist_path = os.path.join(script_dir, "toppasswords.txt")


# Constants for character types
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["~","!","@","#","$","%","^","&","*","(",")","_","+","`","-","=","{","}","[","]","|",":",";","\\","\"", "'", "<", ">", ",", ".", "?", "/"]

# Function to check if a word is in a file
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not case_sensitive:
                if word.lower() == line.lower():
                    return True
            else:
                if word == line:
                    return True
    return False

# Function to check if a word has a character from a list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# Function to calculate the complexity of a word
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# Function to calculate password strength
def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, wordlist_path, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, toplist_path, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    complexity = word_complexity(password)
    score = 1 + complexity
    print(f"Password complexity score: {score}")
    return score

# Main function to drive the program
def main():
    while True:
        password = input("Enter a password to test or Q to quit: ")
        if password.lower() == 'q':
            break
        score = password_strength(password)
        print(f"Password strength score is: {score}")

# Entry point
if __name__ == "__main__":
    main()
