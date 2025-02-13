#!/usr/bin/env python3

import pickle


class Serialization:
    '''class for serialization'''
    @staticmethod
    def serialize_and_save_to_file(data, filename):
        '''function to serialize and save data to a file'''
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_and_deserialize(filename):
        '''function to load and deserialize data from a file'''
        with open(filename, 'rb') as file:
            return pickle.load(file)


if __name__ == '__main__':
    data = {'name': 'Holberton', 'type': 'school', 'topics': ('Python', 'C', 'Javascript')}
    filename = 'data.pkl'
    Serialization.serialize_and_save_to_file(data, filename)
    print(Serialization.load_and_deserialize(filename))
