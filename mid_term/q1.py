# binary search is a user defined
# It takes 4 parameters: list, low index, high index and result list
def binary_search(lst, low, high, result):
    if low <= high:
        # calculate the middle index
        mid = (low + high) // 2
        # we will search on the right side of mid, will discard the left side
        if lst[mid] < mid:
            binary_search(lst, mid+1, high, result)
        # we will search on the left side of mid, will discard the right side
        elif lst[mid] > mid:
            binary_search(lst, low, mid-1, result)
        else:
            # we will check left side from mid
            binary_search(lst, low, mid-1, result)
            # index number and the value on that index are same
            result.append(mid)
            # we will check right side from list
            binary_search(lst, mid+1, high, result)
    return result


lst= [-2,0,2,3,6,7,9]
low = 0 
high = len(lst) - 1 
result = []
# arguments of the function
# result_elements variable stores the result list returned by the function
result_elements = binary_search(lst, low, high, result)

# whether we are getting elements in the result
if len(result_elements) == 0 :
    print("No element found")
else:
    for ele in result_elements:
        print(f"List index[{ele}] is equal to the list item {ele}")

