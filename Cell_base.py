#!/usr/bin/python3

"""
Cell_base.py

This script modelise the behavior of the proteins inside the cell. 

"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("aliaga.benoit@gmail.com")
__version__ = "0.1"
__date__ = "06/06/2020"



class Cell:
    def __init__(self, length, width):
        """
           Intialisation d'un objet
           Definition des attributs avec des valeurs par defauts.
        """
        self.x = length
        self.y = width

    def cell_area(self):
        """
           Methode qui calcule la surface de la cellule.
        """
        area = self.x * self.y
        return area

class Protein():
    def __init__(self, pos_x, pos_y):
        """
           Classe qui definie une proteine
        """
        self.coordx = pos_x
        self.coordy = pos_y

    def prot_coord(self):
        """
           Methode qui calcule les coordonnees de la proteine.
        """
        position = self.coordx + self.coordy
        return position

# Main section
if __name__ == "__main__":
    my_cell = Cell(2,1)
    print("Width = ", my_cell.x, "Length = ", my_cell.y)
    print("The cell area is:", my_cell.cell_area())
    my_prot = Protein(4,6)
    print("The coordinate of my protein is:", my_prot.prot_coord())
    
