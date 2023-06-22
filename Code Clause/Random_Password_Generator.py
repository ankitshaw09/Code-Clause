import  string
import random

if __name__=="__main__":
    string1 = string.ascii_lowercase
    #  gives letters in lower characters
    string2 = string.ascii_uppercase
    #  gives  letters in upper character
    string3 = string.digits
    #  gives  numeric characters 
    string4 = string.punctuation
    #  gives special characters 

    password_length = int(input("enter passward length : \n"))

    s=[]
    s.extend(list(string1))
    s.extend(list(string2))
    s.extend(list(string3))
    s.extend(list(string4))

    random.shuffle(s)
    
    print("Your password is :")
    print("".join(s[0:password_length]))
    

    