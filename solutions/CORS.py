


def bridgeShuffle(array1: list,array2: list):
    """
    Shuffles the two lists according to "Bridge Shuffle"

    Args:
        array1 (list) : first list to include in shuffle
        array2 (list) : second list to include in shuffle
    
    Returns:
        shuffled_array (list) : the shuffled array.
    """

    shuffled_array = []

    no_error_1,no_error_2 = True,True

    for times in range(0, max(len(array1), len(array2)) ):  

        if no_error_1:
            try:
                shuffled_array.append(array1.pop(0))
            except Exception:
                no_error_1 = False 

        if no_error_2:
            try:
                shuffled_array.append(array2.pop(0))
            except Exception:
                no_error_2 = False 
    
    print(shuffled_array)
    return shuffled_array


bridgeShuffle(["A", "A", "A"], ["B", "B", "B"])
output = ["A", "B", "A", "B", "A", "B"]

bridgeShuffle(["C", "C", "C", "C"], ["D"])
output = ["C", "D", "C", "C", "C"]

bridgeShuffle([1, 3, 5, 7], [2, 4, 6])
output = [1, 2, 3, 4, 5, 6, 7]