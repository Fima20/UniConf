from . import convertype
from typing import Union
import configparser
import os
import ast
import datetime


class Config:
    """
    Note:
        save() - forcibly save the config;
        load() - loads the config;
        get() - gets data;
        set() - changes data;
        get_data() - gets the data inside the field;

    Args:
        datadict_ (: obj: `dict`): config structure
        path_ (: obj: `str`): path to config file

    """

    datadict_info = {
        'info': {'name': {"data": 'ABC', "type": 'str'},
                 'number': {"data": '999', "type": 'int'},
                 },
    }
    path_info = "config.ini"  # standard path to save the config file
    list_convert_type = {"int": convertype.conv_int,
                         "str": convertype.conv_str,
                         "float": convertype.conv_float,
                         "bool": convertype.conv_bool,
                         "list": convertype.conv_list,
                         "dict": convertype.conv_dict,
                         "tuple": convertype.conv_tuple,
                         "datetime": convertype.conv_datetime,
                         }

    def __init__(self,
                 datadict_: dict = None,
                 path_: str = None
                 ):
        if datadict_:
            self.datadict = datadict_
        else:
            self.datadict = self.datadict_info
        if path_:
            self.path = path_
        else:
            self.path = self.path_info
        self.load()

    def __call__(self,
                 head: Union[str, int] = None,
                 field: Union[str, int] = None,
                 data: str = None
                 ):
        return self.get(head, field, data)

    def struct(self,
               dict: bool = False,
               res=""
               ):

        """
        Displays the structure of the config

        Note:
            with dict = False - displays the general structure, otherwise - the entire dictionary;

        Args:
            dict (: obj: `bool`): output mode;

        Returns:
            : obj: `dict` | : obj: `str`.
        """

        if dict:
            return self.datadict
        else:
            for head in self.datadict:
                res = res + "[" + str(head) + "]\n"
                for fields in self.datadict[head]:
                    res = res + " \t" + str(fields) + ":{" + str(self.datadict[head][fields]["type"]) + "}\n"
            print(res)

    def get(self,
            head: str = None,
            field: str = None,
            data: str = None
            ):

        """
        Receives data

        Note:
            if no arguments are specified, it returns a dictionary;

        Args:
            head (: obj: `str`): heading;
            field (: obj: `str`): field;
            data (: obj: `str`): for additional entries;

        Returns: : obj: `str` | : obj: `int` | : obj: `float` | : obj: `list` | : obj: `dict` | : obj: `datetime`
            from: obj:` datetime.datetime`.
        """

        if head:
            if field:
                if data:
                    return self.datadict[head][field][data]
                else:
                    return self.list_convert_type[self.datadict[head][field]["type"]](
                        self.datadict[head][field]["data"])
            else:
                return self.datadict[head]
        else:
            return self.datadict

    def set(self,
            head: str,
            field: str = None,
            var: Union[int, str, float, bool, list, dict, datetime.datetime] = None,
            type_: str = None
            ):

        """
        Adds or changes data

        Note:
            also called when accessing the <uniconf.Config> (head: str, field: str) class instance directly;
            you can create a new record without specifying the type - the type will be set automatically based on the specified variable;

        Args:
            head (: obj: `str`): section;
            field (: obj: `str` |: obj:` int` |: obj: `float` |: obj:` list` |: obj: `dict` |: obj:` datetime` from: obj: `datetime. datetime`): field;
            var (: obj: `any`): content;
            data (: obj: `str`): record name;

        Raises:
            : `KeyError`: Invalid arguments.

        """

        def insert_field(self, head, field):
            if not head in self.datadict:
                self.datadict[head] = {}
            if not field in self.datadict[head]:
                self.datadict[head][field] = {}

        if type_ is None: type_ = convertype.type_list[str(type(var))]
        var = convertype.str_conv(var)

        if field:
            if type_ in self.list_convert_type and var:
                insert_field(self, head, field)
                self.datadict[head].update({field: {"data": var, "type": type_}})
            elif self.datadict[head][field][type_] != None:
                if convertype.type_control_fail(str(type(var)), self.datadict[head][field][type_]): raise TypeError
                insert_field(self, head, field)
                self.datadict[head].update({field: {"data": var, "type": self.datadict[head][field][type_]}})
            else:
                raise KeyError
        else:
            if not head in self.datadict: self.datadict[head] = {}
        self.save()

    def delete(self,
               head: str,
               field: str = None,
               data: str = None
               ):

        """
        Deletes sections and fields

        Args:
            head (: obj: `str`): section;
            field (: obj: `str`): field;
            data (: obj: `str`): record name;

        """

        if field:
            if data:
                del self.datadict[head][field][data]
            else:
                del self.datadict[head][field]
        else:
            del self.datadict[head]
        self.save()

    def set_data(self,
                 head: str,
                 field: str,
                 data: str,
                 var: str
                 ):
        """
        Makes additional entries inside the field

        Note:
            the number of entries is unlimited;
            reading is also carried out using .get, but specifying the record of interest (data (: obj: `str`));

        Args:
            head (: obj: `str`): section;
            field (: obj: `str`): field;
            data (: obj: `str`): record name;
            var (: obj: `str`): content

        """

        self.datadict[head][field][data] = var
        self.save()

    def save(self):
        """
        Saves changes to file

        """

        config_file = configparser.ConfigParser()
        for head in self.datadict:
            config_file[head] = self.datadict[head]

        with open(self.path, "w", encoding='utf-8-sig') as file_object:
            config_file.write(file_object)

    def load(self):
        """
        Uploads a file

        Note:
            in most cases, manual download is not required;

        """

        if not os.path.exists(self.path):
            if not self.datadict:
                self.datadict = self.datadict_info
            self.save()
        else:
            self.datadict.clear()
            create_config = configparser.ConfigParser()
            create_config.read(self.path, encoding='utf-8-sig')
            _datadict = create_config._sections

            for head in _datadict:
                self.datadict[head] = {}
                for fields in _datadict[head]:
                    self.datadict[head].update({fields: ast.literal_eval(_datadict[head][fields])})
