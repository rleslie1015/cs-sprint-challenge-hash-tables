"""
U
    [1, 2, 3, -1, -2]
    [1, 2]
P
    create a ht
    loop through once and get all positive numbers, placing them in ht
    
    does it really matter what the value is ? 

    create array to return
    loop again checking for negative number that are in dictionary
    if they are then append and return array

E
R
 I thought since we were returning only one number the value didnt' matter. duhhh it should be negative

"""



def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    result = []
    for i in a:
        if i < 0:
            ht[-i] = i

    for i in a:
        if i > 0 and i in ht:
            result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

