a=input()
def polindrome(a):
    if a==a[::-1]:
        print(True)
    else:
        print(False)
polindrome(a)