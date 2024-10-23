from enum import Enum

class Atom:
    def __init__(self, name_ = "C" , 
                 atomic_mass_unit = 0, neutrons_number = 10, 
                 protons_number = 11, electrons_number = 12,  
                 atomtype = "STABLE", atomtype_value = 0):
        
        self.__name_ = name_
        self.__atomic_mass_unit = atomic_mass_unit
        
        self.neutrons_number = neutrons_number
        self.protons_number = protons_number
        self.electrons_number = electrons_number
        self.atomtype = atomtype
        self.atomtype_value = atomtype_value

    def get_name(self):
        return self.__name_
    
    def get_atomic_mass_unit(self):
        return self.__atomic_mass_unit

    
    def isNeutral(self):
        neytrons = self.neutrons_number
        electrons = self.electrons_number
        
        if neytrons == electrons:
            print("Neutrons number equels electrons number:", True)
        else:
            print("Neutrons number equels electrons number:", False)
        
    def __str__(self):
        return (f"{self.get_name()} : atomic mass - {self.get_atomic_mass_unit()}, "
                f"neytrons - {self.neutrons_number}, "
                f"protons - {self.protons_number}, "
                f"electrons - {self.electrons_number}, "
                f"atomtype - {self.atomtype}: {self.atomtype_value}")
    
    def __del__(self):
        print("\n", f"Atom '{self.get_name()}' is deconstructed.")



class AtomType(Enum):
    ISOTYPE = 1
    RADIOACTIVE = 0
    ION = 1
    ANTIMATTER = 1
    STABLE = 5



class Molecule:
    def __init__(self, name_el):
        self.name_el = name_el
        self.elements = []
    
    def add_elem(self, elem):
        self.elements.append(elem)

    def sort_atomic_mass(self):
        n = len(self.elements)
        for i in range(n):
            first_index = i
            for j in range(i + 1, n):
                if self.elements[j].get_atomic_mass_unit() < \
                   self.elements[first_index].get_atomic_mass_unit():
                    first_index == j
                
            if first_index != i:
                self.elements[i], self.elements[first_index] = \
                self.elements[first_index], self.elements[i]

        print(f"Sorted elements: ")
        for elem in self.elements:
            print("-", elem)
        

    def findAverageMass(self):
        term = 0
        n = len(self.elements)
        
        for el in self.elements:
            term += el.get_atomic_mass_unit()
        average = term / n
        return average
    
    def make_formula(self):
        formula = ""
        counted_H = 0
        counted_O = 0

        for atom in self.elements:
            name_el = atom.get_name()
            if name_el == "H":
                counted_H += 1
            elif name_el == "O":
                counted_O += 1

        if counted_H > 0:
            formula += "H" + (str(counted_H) if counted_H > 1 else "")
        if counted_O > 0:
            formula += "O" + (str(counted_O) if counted_O > 1 else "")
        
        return formula



    def __del__(self):
        print("\n", f"Molecule {self.name_el} is deconstructed.")


def main():
    atoms = [
        Atom("H", 1, 0, 1, 1, AtomType.STABLE.name, AtomType.STABLE.value),
        Atom("O", 16, 8, 8, 2, AtomType.ION.name, AtomType.ION.value),
        Atom("N", 14.5, 7, 7, 3, AtomType.RADIOACTIVE.name, AtomType.RADIOACTIVE.value)
    ]

    info_atoms = [str(atom) for atom in atoms]
    print("\n".join(info_atoms))

    for atom in atoms:
        atom.isNeutral()
    
    
    
    water = Molecule("water")
    
    inputed_elements = input("Enter elements to molecule 'water' by coma: ").split(',')
    
    for el in inputed_elements:
        found = False
        el = el.strip()
        for atom in atoms:
            if atom.get_name() == el:
                water.add_elem(atom)
                found = True
                break
        if not found:    
            print("Not found")

    print("\n", f"Formula of water: {water.make_formula()}.")
    print(f" Average mass: {water.findAverageMass()}")
    water.sort_atomic_mass()


main()

