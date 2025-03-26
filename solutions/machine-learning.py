def hoursPassed(t1 : str, t2 : str):
    """
    Calculates the total time passed
    Args:
        t1 (str) : start time
        t2 (str) : end time

    Returns:
        time2 - time1 : Total Time Passed
    """
    time1 = int(t1.split(":")[0])
    time2 = int(t2.split(":")[0])

    if "PM" in t1:
        time1 = 12 + time1
    if "PM" in t2:
        time2 = 12 + time2

    if time2 == time1:
        return "No Time Passed"

    return time2 - time1

hoursPassed("3:00 AM", "9:00 AM")
output = "6 hours"

hoursPassed("2:00 PM", "4:00 PM")
output = "2 hours"

hoursPassed("1:00 AM", "3:00 PM")
output = "14 hours"

hoursPassed("4:00 PM", "4:00 PM")
output = "no time passed"