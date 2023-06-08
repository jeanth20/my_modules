import itertools


def Convert_list_to_dictionary1(list):
    converted_dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return converted_dict


def Convert_list_to_dictionary2(list):
    it = iter(list)
    converted_dict = dict(zip(it, it))
    return converted_dict


def Convert_list_to_dictionary3(list):
    converted_dict = {}
    for i in range(0, len(list), 2):
        converted_dict[list[i]] = list[i + 1]
    return converted_dict
 

def Convert_list_to_dictionary4(list):
    pairs = itertools.zip_longest(*[iter(list)] * 2, fillvalue=None)
    dict = {key: value for key, value in pairs}
    return dict


def Convert_list_to_dictionary5(list):
    keys = list[::2]
    values = list[1::2]
    res_dict = {keys[i]: values[i] for i in range(len(keys))}
    return res_dict


