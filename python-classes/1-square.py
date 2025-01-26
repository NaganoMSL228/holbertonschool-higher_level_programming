#!/usr/bin/python3

'''
Module for the Square class
'''


class Square:
    '''A simple class representing a square.'''

    def __init__(self, size):
        '''Initializes the square with a given size.'''
        self.__size = size  # Attribut privé

    def area(self):
        '''Calculates the area of the square.'''
        return self.__size ** 2  # Calcul de l'aire


# Exemple d'utilisation de la classe Square
if __name__ == "__main__":
    mon_carre = Square(5)
    print(f"L'aire du carré est : {mon_carre.area()}.")
