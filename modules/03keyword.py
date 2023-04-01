import keyword

def contains_keyword(Keywords_list):
    for key in Keywords_list:
        if keyword.iskeyword(key):
            return True
    return False

print(contains_keyword(["iif","elseif","for"]))
