str1 = "234".strip()

str2 = "  45 ".strip()


# It is a flag for checking if both strings are equal
is_number_equal = 0

# print(str2.isdecimal())
# print(str2.isdigit())
# print(str1.isdigit())

if (not str1.isdigit()) or ( not str2.isdigit()) :
    print("Please enter valid string inputs")
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
                break
            # comparing each word, to find if str2 is the bigger one
            elif str2[i] > str1[i]:
                print(f"{str2} is greater than {str1}")
                is_number_equal = 1
                break
                
# checking if strings are equal
if is_number_equal == 0 :
    print(f"{str1} is equal to {str2}")