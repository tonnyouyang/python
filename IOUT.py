# check palindrome
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


i = 1
while (i):
    something = input("Enter text: ")
    if is_palindrome(something):
        print("Yes, it is a palindrome")
        i -= 1
    else:
        print("No, it is not a palindrome")
