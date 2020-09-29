#Palindromy

def palindrome(given_string):
    string_without_space = given_string.replace(" ","").upper()
    string_list = list(string_without_space)
    string_reversed = string_list.copy()
    string_reversed.reverse()
    
    if string_list == string_reversed:
        print("True. Given sentence is a palindrome.")
    else:
        print("False. Given sentence is not palindrome!")
    

palindrome("Kajak")

