#!/usr/bin/python3

def lookup(obj):
    """Retourne une liste des attributs et méthodes disponibles d'un objet."""
    return dir(obj)

# Classes d'exemple pour tester la fonction lookup
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    
    def my_meth(self):
        pass

if __name__ == "__main__":
    # Test de la fonction lookup avec différentes classes
    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
