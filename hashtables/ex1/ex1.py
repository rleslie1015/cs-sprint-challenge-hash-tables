"""
Understand
    G
    weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
                   |       |
                    \     /
                       21  # output is [3, 1] 

    weights = [ 9 ], length = 1, limit = 9
                # output is None


P

   create a dictionary 
   loop through list for each item check if dictionary contains limit- weight at each loop 
        set markers for both the weight and (limit-weight)
        
        if (limit - weight) is in dictionary then return tuple
        if not place weight and index into dictionary
        (placing weight as key and index as value)


E
R
"""



def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashtable = {}

    for i in range(length):
        # key = weights[i] # didn't need this
        weight2find = limit - weights[i]

        if weight2find in hashtable:
            weight1 = hashtable[weight2find]
            tup = (i, weight1) 
            return tup
        else: 
            hashtable[weights[i]] = i
            # print(hashtable[weights[i]])
    return None




weightlist = [ 4, 6, 10, 15, 16 ]
print(get_indices_of_item_weights(weightlist, 5, 21))