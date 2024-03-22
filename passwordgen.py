import random
import string
import sys

passw = ''
#Constants
LOWER_CASE = list(string.ascii_lowercase)
UPPER_CASE = list(string.ascii_uppercase)
DIGITS = list(string.digits)
SPECIAL_CHARACTERS = list(string.punctuation)

while True:
    def choice_input():
        while True:
            try:
                choice = int(input('How long do you want the password to be(12-16) and (99) for quit: '))
                if 12 <= choice <= 16:
                    break
                elif choice == 99:
                    sys.exit()
                else:
                    print('It must be within the range of 12 - 16 only.')
            except ValueError:
                print('Invalid Input!')
        return choice


    def rand_structure(length):
        while True:
            lowercase_number = random.randint(1,6)
            uppercase_number = random.randint(1,6)
            digit_number = random.randint(1,4)
            special_characters_number = random.randint(1,4) 
            if lowercase_number + uppercase_number + digit_number + special_characters_number == length:
                return lowercase_number,uppercase_number,digit_number,special_characters_number
                break



    def rand_index():
        lc_rand = [0]*lc
        for i in range(lc):
            lc_rand[i] = random.randint(0,25)
            
        uc_rand = [0]*uc
        for i in range(uc):
                uc_rand[i] = random.randint(0,25)
        
        digits_rand = [0]*digit
        for i in range(digit):
            digits_rand[i] = random.randint(0,9)
            
        sc_rand = [0]*sc
        for i in range(sc):
            sc_rand[i] = random.randint(0,31)

        return lc_rand,uc_rand,digits_rand,sc_rand
        
    #Calling Functions
    lc,uc,digit,sc = rand_structure(choice_input())
    lc_list,uc_list,digit_list,sc_list = rand_index() 

    lc_letters = ['']*lc
    uc_letters = ['']*uc
    digit_number = ['']*digit
    sc_letters = ['']*sc


    def rand_assign():
        for i in range(lc):
            lc_letters[i] = LOWER_CASE[lc_list[i]]
        
        for i in range(uc):
            uc_letters[i] = UPPER_CASE[uc_list[i]]

        for i in range(digit):
            digit_number[i] = DIGITS[digit_list[i]]
            
        for i in range(sc):
            sc_letters[i] = SPECIAL_CHARACTERS[sc_list[i]]
    
    #Calling rand_assign function
    rand_assign()

    def pass_output():
        result_arr = lc_letters + uc_letters + digit_number + sc_letters
        random.shuffle(result_arr)
        result_string = ''.join(result_arr)
        print(f'Generated Password: {result_string}')
        return result_string


    #Calling pass_output function
    passw = pass_output()

    def store_file():
        #Storing in a file(Unsafe)
        while True:
                    with open('password.txt','a') as file_password:
                        user_textline = input('Enter username or account name: ')
                        file = file_password.write(f'{user_textline}: {passw}\n')
                        break
                
    store_file()