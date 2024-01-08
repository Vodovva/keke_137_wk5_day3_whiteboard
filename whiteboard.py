# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: 
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
# ["the","quick","brown","fox"] --> ["1: the","2: quick","3: brown","4: fox"]

# Need to write a function that creates an ouput that numbers each input with a colon
# Given a list of string with a return of list of strings with an appended correct line number
# Given a list of strings
# Go throguh each word and added a number to the beginning of each word starting from one and going up
# Adding a colon after each number before each word
# 


def solution(strings):
    line_count = 1
    output = []
    for i in strings:
        output.append(f"{line_count}: {i}")
        line_count += 1
    return output
