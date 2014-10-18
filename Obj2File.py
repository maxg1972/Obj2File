"""
    Obj2File - read/write object from/to files
    ==========================================
    Utilities to save python objects to file. TThis is accomplished with an object that give you methods to read/write
    object (like lists, dictionaries, etc) from/to disk files

    Requires
    -----
    pickle and json module

    Usage
    -----
    Import the Obj2File.py file into your project and use the Obj2File object.

    Authors & Contributors
    ----------------------
        * Massimo Guidi <maxg1972@gmail.com>,

    License
    -------
    This module is free software, released under the terms of the Python
    Software Foundation License version 2, which can be found here:

        http://www.python.org/psf/license/

"""

__author__ = "Massimo Guidi"
__author_email__ = "maxg1972@gmail.com"
__version__ = '1.1'

import pickle, json, os

class Obj2File:
    JSON = 0
    OBJ = 1

    def __init__(self,file_name,output_type=JSON):
        """
        Class contructor

        @param file_name: Object dump filename
        @param output_type: Dump format (values: Obj2File.JSON, Obj2File.OBJ; default: Obj2File.JSON)
        """
        self.__file_name = file_name
        self.__output_type = output_type

    def __load_obj(self):
        """
        Internal method to return an object loaded from defined file (dump format: Obj2File.OBJ)

        @return: Object loaded
        """
        if os.path.exists(self.__file_name):
            with open(self.__file_name,'r') as fh:
                data = pickle.load(fh)
                return data

        return None

    def __save_obj(self,data):
        """
        Internal method to save an object into defined file (dump format: Obj2File.OBJ)

        @param data: Object to be saved
        """
        with open(self.__file_name,'w') as fh:
            pickle.dump(data,fh)

    def __load_json(self):
        """
        Internal method to return an object loaded from defined file (dump format: Obj2File.JSON)

        @return: Object loaded
        """
        if os.path.exists(self.__file_name):
            with open(self.__file_name,'r') as fh:
                data = json.load(fh)
                return data

        return None

    def __save_json(self,data):
        """
        Internal method to save an object into defined file (dump format: Obj2File.JSON)

        @param data: Object to be saved
        """
        with open(self.__file_name,'w') as fh:
            json.dump(data,fh)

    def save(self,data):
        """
        Save an object into defined file

        @param data: Object to be saved
        """
        if self.__output_type == self.JSON:
            self.__save_json(data)
        else:
            self.__save_obj(data)

    @property
    def load(self):
        """
        Return an object loaded from defined file

        @return: Object loaded
        """
        if self.__output_type == self.JSON:
            return self.__load_json()
        else:
            return self.__load_obj()

