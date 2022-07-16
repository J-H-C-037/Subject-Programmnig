"""Write a program that asks the user to enter a sentence. Then, it introduces each character of the
sentence in a tuple, ignoring the repeated characters. The characters introduced in the tuple
should be capitalized (you can use the upper() method of strings). Finally, it prints the tuple.
For instance:
Write a sentence: Hi, how are you?

(’H’, ’I’, ’,’, ’ ’, ’O’, ’W’, ’A’, ’R’, ’E’, ’Y’, ’U’, ’?’"""

str1 = input("Enter a sentence: ")

repeated_characters = ()
characters = ()

for letter in str1:
    if not letter in repeated_characters:
        characters += (letter,)

    repeated_characters += (letter,)

print(characters)
