"""I added the ability to receive suggestions to improve password security."""
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    print("Welcome to password strength!")
    while True:
        word = input("Test password: ")
        if word.lower() == "q":
            print("Bye :D")
            break
        print(f"password strength: {password_strength(word)}")

def word_in_file(word,filename,case_sensitive=False):
    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not case_sensitive:
                if word.lower() == line.lower():
                    return True
            else:
                if word == line:
                    return True
    return False
def word_has_character(word,character_list):
    return any(c in word for c in character_list)
        
def word_complexity(word):
    score = 1
    
    if word_has_character(word,LOWER):
        score= score + 1 
    if word_has_character(word,UPPER):
        score= score + 1 
    if word_has_character(word,DIGITS):
        score= score + 1 
    if word_has_character(word,SPECIAL):
        score= score + 1 
     
    
    return score
def password_strength(password,min_length=10,strong_length=16):

    if (word_in_file(password,"week2/toppasswords.txt",True)):
        print("Password is a commonly used password and is not secure.")
        return 0
    if (word_in_file(password,"week2/wordlist.txt")):
        print("Password is a dictionary word and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password")
        return 5
    suggest_improvements(password)
    return word_complexity(password)
    
def suggest_improvements(password):
    suggestions = []
    
    if not word_has_character(password, LOWER):
        suggestions.append("- Add lowercase letters")
    if not word_has_character(password, UPPER):
        suggestions.append("- Add uppercase letters")
    if not word_has_character(password, DIGITS):
        suggestions.append("- Add numbers")
    if not word_has_character(password, SPECIAL):
        suggestions.append("- Add special characters")
    if len(password) < 10:
        suggestions.append(f"- Make it longer (current: {len(password)}, recommended: 10+)")
    
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(suggestion)

if __name__ == "__main__":
    main()