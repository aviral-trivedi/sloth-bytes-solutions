

def format_phone_number(num_list: list):
    """
    Formates the number according `(123) 456-7890`

    Args:
        num_list (list) : the list of the single number
        
    Returns:
        formated_number (str) : the formated number.
    """

    #we first convert the integers to str using map function then join them
    formated_number = f"({ ''.join(     map(str,num_list[0:3])    ) }) {''.join(map(str,num_list[3:6]))}-{''.join(map(str,num_list[6:]))}" 
    print(formated_number)
    return formated_number


format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])
format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])

output = "(123) 456-7890"
output = "(519) 555-4468"
output = "(345) 501-2527"