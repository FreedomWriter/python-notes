def do_stuff(num=0):
    try:
        if num == 0 or num:
            return float(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err