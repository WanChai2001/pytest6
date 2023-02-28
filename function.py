def number_to_month(number):
    month = ["january", "february", "march", "april", "may", "june", 
    "july", "august", "september", "october", "november", "december"]
    return month[number-1]



def validate_number(number):
    if type(number) != int:
        if type(number) == str:
            return "input integer"
        elif number >= 1 and number <= 12:
            return "input integer"
        else: 
            return "out of range"
    elif number >= 1 and number <= 12:
        return number
    else: 
        return "out of range"


def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    else:
        return result
 

