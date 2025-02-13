#!/usr/bin/python3
import csv
import json

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'w') as file:
                writer = csv.writer(file)
                writer.writerow([self.name, self.age, self.is_student])
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                return cls(data[0][0], int(data[0][1]), json.loads(data[0][2].lower()))
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
