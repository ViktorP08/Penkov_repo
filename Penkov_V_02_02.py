# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

def w(s):
    return "".join(["(" if s.lower().count(x) == 1 else ")" for x in s.lower()])
s = input("Введите свой текст или символы: ")
print(w(s))