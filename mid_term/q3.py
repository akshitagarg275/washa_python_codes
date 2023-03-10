lst = [3,4,1,2,9 ]
sum_of_pair = 10

# dictionary to store the number
d = {}

# iterate through the list
for x in lst:
    # finding the diff 
    diff = sum_of_pair - x

    # checking if the difference value key is present in dictionary 
    if diff in d:
        # giving the pair whose sum is equal to 10
        print(x , diff)
    else:
        # creating key of element and giving value 1
        d[x] = 1