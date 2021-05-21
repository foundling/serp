# exercise 1
def constrain(value, low, high):
    ''' low if value is < low, high if value is > high. otherwise, return value. '''
    # implement me


# exercise 2
def valid_identifier(s):
    ''' 
        todo: return true if s:
            - is a string (there's a built-in func for this)
            - isn't empty
            - first character is either an alphabetic character or an underscore '_'.

            otherwise, return false
    '''
    # implement me

# exercise 3
def fix_assignments():

    // set a, b and c so that the result is true
    a, b, c = None, None, None

    points = 0

    if a or b and not c:
        points += 1

    return points
