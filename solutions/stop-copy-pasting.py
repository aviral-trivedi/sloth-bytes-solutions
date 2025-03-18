def turnCalc(number : int):
    """
    Turns the `number` 180 degrees according to a set table 

    Args:
        number (int) : the integral number to turn
    
    Returns:
        turned_num (str) : the rotated number.
    """

    data_table = {1:"I", 2:"Z", 3:"E", 4:"H", 5:"S", 6:"G", 7:"L", 8:"B", 9:"-", 0:"O"}
    turned_num = ""

    #Ignore the int -> str -> int conversion for now 

    for digit in str(number):
        turned_num += data_table[int(digit)]

    #Since `turned_num` is a string we flip the result in the end
    return turned_num[::-1]

print(turnCalc(8008))
