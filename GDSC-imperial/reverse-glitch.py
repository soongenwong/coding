# Goal: Create a function that takes a string and returns it in reverse.
# Example: "hello" should become "olleh".
# There's a small but critical error in the function. What is it?

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = reversed_s + char  # This line is the problem!
    return reversed_s



