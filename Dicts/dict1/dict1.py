def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    # pass  # implement me
    zip_iterator= dict(zip(keys, values))
    return zip_iterator

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    # pass  # implement me
    return {**d1, **d2}

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    # pass  # implement me
    new_dict={}
    for i in lst:
        new_dict[i]= d1
    return new_dict


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    # pass  # implement me


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        datadict.pop(key)
    return datadict


def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    if key in datadict:
     return True
    else:
     return False


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    # Can I do this with lambdas?
    min_value = min(ddd, key=ddd.get)
    return min_value


def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    max_value = max(ddd, key=ddd.get)
    return max_value