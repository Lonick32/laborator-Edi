import string

text = "        Dota 2 promises to take the unique blend of online RTS and RPG action that has made Dota popular with tens of millions of gamers and expand upon it in every way.      "

def split_string(s):
    mid = len(s) // 2
    return s[:mid], s[mid:]

def first_function(first_part):
    return first_part.upper().strip()

def second_function(second_part):
    no_punctuation = second_part.translate(str.maketrans('', '', string.punctuation))
    return no_punctuation.capitalize()[::-1]

first_part, second_part = split_string(text)


first_transformed = first_function(first_part)
second_transformed = second_function(second_part)

print("Prima parte (Majuscule si eliminarea spatiilor goale):")
print(first_transformed)

print("\nA 2-a parte (Fara punctuatie si prima litera cu majuscule)")
print(second_transformed)
