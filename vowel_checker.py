user_input = input()
vowel_checker = ["a", "e", "i", "o", "u"]

for words in user_input:
    if words in vowel_checker:
        continue        
    print(words)
