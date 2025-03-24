# Task 1 
year = int(input("Years: "))
name = input("name: ")
print(f"{name} is {2024-year} year")

# Task 2
# Task 3
my_string = input("String: ")
print(len(my_string))
my_string.upper()
my_string.lower()

#Task 4
print(my_string == my_string[::-1])

# Task 5
vowel_count = 0
vowels = "aeiouAEIOU"
for char in my_string:
    if char in vowels:
        vowel_count += 1
print(vowel_count)
print(len(my_string) - vowel_count)
  

# Task 6
g = "qw"
print(g in my_string)

# Task 7
sentence = input("sentence: ")
word_replace = input("replace: ")
replacement_word = input("replacement: ")
updated_sentence = sentence.replace(word_replace, replacement_word)
print(updated_sentence)

# Task 8
print(my_string[0])
print(my_string[-1])

# Task 9
print(my_string[::-1])

# Task 10
print(len(sentence.split()))

# Task 11
for i in my_string:
    if i.isdigit():
        print(True)
        break
else:
    print(False)

# Task 12
new_string = my_string+"_"+replacement_word
print(new_string)

# Task 13
new = my_string.replace(" ", "")

# Task 14
a = input()
b = input()
a == b

# Task 15
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print(acronym)

# Task 16
strr = input("Enter: ")
charr = input("Char")
strr.replace(charr, "")

# Task 17
sen = input()
start = input()
end = input()
sen.startswith(start) and sen.endswith(end)