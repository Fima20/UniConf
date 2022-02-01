import datetime
import ast

date_format = '%Y-%m-%d %H:%M:%S.%f'

type_list = {"<class 'int'>": "int",
             "<class 'str'>": "str",
             "<class 'float'>": "float",
             "<class 'bool'>": "bool",
             "<class 'list'>": "list",
             "<class 'dict'>": "dict",
             "<class 'tuple'>": "tuple",
             "<class 'datetime.datetime'>": "datetime"}

def conv_int(str):
    return int(str)

def conv_str(str):
    return str

def conv_float(str):
    return float(str)

def conv_bool(str):
    if str == "True": return True
    elif str == "False": return False
    else: raise Exception

def conv_list(str):
    return list(item for item in str[1:-1:].split(', '))

def conv_dict(str_):
    return ast.literal_eval(str(str_))

def conv_tuple(str):
    return tuple(item for item in str[1:-1:].split(', '))

def conv_datetime(str):
    return datetime.datetime.strptime(str, date_format)

def str_conv(data):
    if type(data) == "<class 'datetime.datetime'>": data.strftime(date_format)
    return str(data)

def type_control_fail(type_now, type_rec):
    if type_rec == None: return True
    elif type_now in type_list and type_list[type_now] == type_rec: return False
    else: return True

if __name__ == '__main__':
    print("convrtype.py")


