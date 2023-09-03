# Finger exercise: Write a function is_in that accepts two strings as
# arguments and returns True if either string occurs anywhere in the
# other, and False otherwise. Hint: you might want to use the built-in
# str operator in.

def is_in(strOne, strTwo):
    if strOne in strTwo or strTwo in strOne:
        return True
    return False

if (is_in("Ahmed", "DreamOfAhmed")):
    print("Yes")
else:
    print("No")