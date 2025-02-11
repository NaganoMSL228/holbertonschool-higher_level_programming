#!/usr/bin/python3
'''Module for Student class'''
import json


class Student:
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        '''Constructor for Student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary representation of Student'''
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for key in json:
            setattr(self, key, json[key])
