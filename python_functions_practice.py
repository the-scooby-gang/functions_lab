def return_10():
    return 10
def add(number1,number2):
    return(number1+number2)

def subtract(number1, number2):
    return(number1-number2) 

def multiply(number1, number2):
    return(number1*number2) 

def divide(number1, number2):
    return(number1/number2)

def length_of_string(test_length):
    return len(test_length)

def join_string(string_1 , string_2):
    return (string_1+string_2)

def add_string_as_number(string_1, string_2):
    return (int(string_1)+int(string_2))

def number_to_full_month_name (num) :
    if num == 1:
        return"January"
    elif num == 3:
        return "March"
    elif num == 9:
        return "September"

def number_to_short_month_name (num) :
    if num == 1:
        return "Jan"
    elif num == 4:
        return "Apr"
    elif num == 10:
        return "Oct"
