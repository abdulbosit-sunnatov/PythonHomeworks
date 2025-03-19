# Task 1
name = input("Enter your name: ")
year = int(input("Enter your birth year: "))
age = 2024 - year
print(f"Hello {name}, you are {age} years old.")

# Task 2
txt = "LMaasleitbtui"
print(txt[::2])  

# Task 3
text = input("Enter a string: ")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Task 4
text = input("Enter a string: ")
print("Palindrome" if text == text[::-1] else "Not a palindrome")

# Task 5
text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Task 6
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Contains" if str2 in str1 else "Does not contain")

# Task 7
sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("New word: ")
print(sentence.replace(old_word, new_word))

# Task 8
text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# Task 9
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# Task 10
sentence = input("Enter a sentence: ")
print("Word count:", len(sentence.split()))

# Task 11
text = input("Enter a string: ")
print("Contains digits" if any(char.isdigit() for char in text) else "No digits")

# Task 12
words = ["apple", "banana", "cherry"]
separator = "-"
print(separator.join(words))

# Task 13
text = input("Enter a string: ")
print("Without spaces:", text.replace(" ", ""))

# Task 14
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Equal" if str1 == str2 else "Not equal")

# Task 15
sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)

# Task 16
text = input("Enter a string: ")
char_to_remove = input("Character to remove: ")
print("Result:", text.replace(char_to_remove, ""))

# Task 17
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("Result:", "".join("*" if char in vowels else char for char in text))

# Task 18
text = input("Enter a string: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")
print("Matches" if text.startswith(start_word) and text.endswith(end_word) else "Does not match")




