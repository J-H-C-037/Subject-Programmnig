"""

Generate a function that allows you to correctly write uppercase letters in a given text: The first
character of the string must be written in uppercase; also the “i” letter when it is followed by a
blank space and the previous one is a blank space too. In addition, the first non-blank character
after a ".", "!" or "?" For example, if the function is provided with the string "what time do i
have to be there? what is the address?", Then it should return the string "What
time do I have to be there? What is the address?" Include a program that
reads a user string, capitalizes the appropriate letters using this function and displays the result
on the screen.

"""


def capitalize(text, new_text="", previous_previous = ""):
    new_text += text[0].upper()

    for i in range(1, len(text)):
        if i >1:
            previous_previous = text[i-2]
        previous = text[i - 1]
        if i != len(text) - 1:
            next = text[i + 1]

        if previous == " " and next == " ":
            new_text += text[i].upper()
        elif previous_previous in ".!?" and previous == " ":
            new_text += text[i].upper()
        else:
            new_text += text[i]

    return new_text


