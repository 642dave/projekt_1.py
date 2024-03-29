"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Rakovsky
email: david.rakovsky@centrum.cz
discord: David R.#9097
"""


from task_template import TEXTS
import math

cleaned_text = list()
title_words = list()
upper_words = list()
lower_words = list()
number_count = list()
sum_of_numbers = 0
len_of_words = list()
graf_symbol = "*"
delimiter = "-" * 40

users = {"bob" : "123",
         "ann" : "pass123", 
         "mike": "password123", 
         "liz" : "pass123"
}


#přihlašovací jméno a heslo
username = input("username: ")
password = input("password: ")
print(delimiter)


#zjisti, jestli zadané údaje odpovídají 
# někomu z registrovaných uživatelů
if users.get(username) == password:
    

#pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print(f"welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(delimiter)


    
#pokud není registrovaný, upozorni jej a ukonči program 
else:
    print("$ python projekt1.py")
    print(f"username: {username}")
    print(f"password: {password}")
    print("unregistered user, terminating the program..")
    quit()


# Program nechá uživatele vybrat mezi třemi texty,
#  uloženými v proměnné TEXTS:

selected_number = input("Enter a number btw. 1 and 3 to select: ")
print(delimiter)



# Pokud uživatel vybere takové číslo textu, které není v zadání,
#  program jej upozorní a skončí,
if not selected_number.isdigit():
    print("Invalid selection, terminating the program..")
    quit()

elif 0 < int(selected_number) <= 3:
    selected_text = TEXTS[int(selected_number) - 1].split()
    for words in selected_text:
        cleaned_text.append(words.strip(".,:"))
 
   
# pokud uživatel zadá jiný vstup než číslo,
#  program jej rovněž upozorní a skončí
else:
    print("Invalid selection, terminating the program..")
    quit()   

 

# Pro vybraný text spočítá následující statistiky:

 # počet slov,
print("There are", len(selected_text), "words in the selected text.")


# počet slov začínajících velkým písmenem
for words in selected_text:
    if words.istitle():
        title_words.append(words)
    else:
        pass

print("There are", len(title_words), "titlecase words.")



# počet slov psaných velkými písmeny
for words in selected_text:
    if not words.isalpha() and words.isupper():
        upper_words.append(words)
    else:
        pass

print("There are", len(upper_words), "uppercase words.")  




# počet slov psaných malými písmeny,
for words in selected_text:
    if words.islower():
        lower_words.append(words)
    else:
        pass

print("There are", len(lower_words), "lowercase words.")  

# počet čísel (ne cifer)
for words in selected_text:
    if words.isdigit():
        number_count.append(words)
    else:
        pass

print("There are", len(number_count), "numeric strings.") 

# sumu všech čísel (ne cifer) v textu
for words in selected_text:
    if words.isdigit():
        sum_of_numbers += int(words)
    else:
        pass

print("The sum of all the numbers", sum_of_numbers)

print(delimiter)
print("LEN| OCCURENCES",    "|NR.".rjust(12))
print(delimiter)


# Program zobrazí jednoduchý sloupcový graf, 
# který bude reprezentovat četnost různých délek slov v textu.
#  Například takto:
for words in cleaned_text:
    len_of_words.append(len(words))
for words_graf in range(1, 12):
    print(str(words_graf).center(2),"|".center(1), 
    graf_symbol * len_of_words.count(words_graf),
    "|".rjust(19 - len_of_words.count(words_graf)),
     len_of_words.count(words_graf))
   
    




