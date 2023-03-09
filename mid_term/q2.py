str1 = "245"

str2 = "45"
# It is a flag for checking if both strings are equal
is_number_equal = 0


if len(str1) == 0 and len(str2) == 0:
    print("Both strings are empty")
    is_number_equal = 1
elif len(str1) == 0:
    print("String 2 is greater")
    is_number_equal = 1
elif len(str2) == 0:
    print("String 1 is greater")
    is_number_equal = 1
else:
    if len(str1) > len(str2):
        print(f"{str1} > {str2}")
        # setting the value of flag, telling that strings are unequal
        is_number_equal = 1
    elif len(str2) > len(str1):
        print(f"{str2} > {str1}")
        is_number_equal = 1
    else:
        # loop for comparing each word, to find bigger one
        for i in range(len(str1)):
            # comparing each word, to find if str1 is the bigger one
            if str1[i] > str2[i]:
                print(f"{str1} is greater than {str2}")
                is_number_equal = 1
            # comparing each word, to find if str2 is the bigger one
            elif str2[i] > str1[i]:
                print(f"{str2} is greater than {str1}")
                is_number_equal = 1
                
# checking if strings are equal
if is_number_equal == 0 :
    print(f"{str1} is equal to {str2}")