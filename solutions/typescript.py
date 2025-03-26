

def lemonade(payments: list):
    """
    A simple lemonade stand simulation of money exchange

    Args:
        payments (list) : list of all the payments done in order

    Returns:
        bool value : True or False
    """

    bills5 = []
    bills10 = []
    bills20 = []
    
    for trans in payments:
        if trans == 5: bills5.append(5)
        elif trans == 10: bills10.append(10)
        elif trans == 20: bills20.append(20)

        if trans == 5:
            continue
        
        elif trans == 10 and len(bills5) >= 1:
            bills5.pop()
            continue

        elif trans == 20 and len(bills5) >= 3:
            for _ in range(3):
                bills5.pop()
            continue

        elif trans == 20 and len(bills5) >= 1 and len(bills10) >= 1  :
            bills5.pop()
            bills10.pop()
            continue

        return False   

    return True        



print(lemonade([5, 5, 5, 10, 20]))
output = True

print(lemonade([10, 10]))
output = False

print(lemonade([5, 5, 10]))
output = True




