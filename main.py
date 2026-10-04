# CS 1430 - Practice 1: Say It Again

#
# Ask for a whole number, then ask for a phrase, then print the phrase
# that many times. The steps are in README.md.
#
# Write your code below this comment.
def main():
    whole_number = int(input("Input a whole number: "))
    phrase = input("Enter a phrase: ")
    print(phrase * whole_number)
main()