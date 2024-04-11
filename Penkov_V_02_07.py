# Усложненное задание из CodeWars (5 уровень сложности)
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples:
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def hashtags(s):
    if not s.strip():
        return False

    word = [word.capitalize() for word in s.split()]
    hashtag = '#' + ''.join(word)

    if len(hashtag) > 140:
        return False

    return hashtag


print(hashtags(" Hello there thanks for trying my Kata"))
print(hashtags("    Hello     World   "))
print(hashtags(""))
