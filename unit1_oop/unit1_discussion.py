"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# x Include at least one class variable.
# x Include at least two instance variables.
# x Include a constructor (__init__).
# x Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

#
class Incident:
    # Class variable for the agency
    agency = "Generic Agency"

    #Constructor taking the location and incident type, and default setting an incident to open
    def __init__(self, location, inc_type):
        self.location = location
        self.inc_type = inc_type
        self.status = "Open"

    #Display the formatted incident
    def incident_info(self):
        return f"Location: {self.location}, Type: {self.inc_type}\nStatus: {self.status}"

    #Close the incident
    def close_incident(self):
        self.status = "Closed"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# X Use inheritance.
# X Add at least one new class variable.
# X Add at least two new instance variables.
# X Add at least one new method.
# X Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class DispatchIncident(Incident):
    resource = "Police"

    # Constructor using the super() construct as well
    def __init__(self, location, inc_type, priority, sector):
        super().__init__(location, inc_type)
        self.priority = priority
        self.sector = sector
        self.units = []

    # Override parent method for displaying incident
    def incident_info(self):
        return f"Location: {self.location}, Type: {self.inc_type}\nStatus: {self.status}, Priority: {self.priority}, Sector: {self.sector}\nUnits Assigned: {self.units}"

    # Dispatch units to the incident
    def dispatch_unit(self, unit):
        self.units.append(unit)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# x Create at least two objects of the child class.
# x Access a class variable through the class itself.
# x Access the same class variable through an object.
# x Add a new attribute to only one object after it is created.
# x Display each object's namespace using __dict__.
# x Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects of the child
    inc3 = DispatchIncident("100 Third Ave", "Threat", 3, 1)
    inc4 = DispatchIncident("200 Fourth Dr", "Weapon", 1, 1)

    # Access the class variable
    print(f"Class variable through Class: {DispatchIncident.resource}")
    print(f"Class variable through Object: {inc3.resource}")

    # Add a value to the first incident after creation
    inc3.report_num = 260012345
    # Display the __dict__ values for each object
    print(f"inc3 with added field for report number: {inc3.__dict__}")
    print(f"inc4 without additional field: {inc4.__dict__}")



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# x Create an object that contains nested mutable data.
# x Create a shallow copy.
# x Create a deep copy.
# x Modify the original object's nested data.
# x Display the original object, shallow copy, and deep copy.
# x Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # Create an object to copy
    inc5 = DispatchIncident("4321 A St", "Theft", 2, 4)
    inc5.dispatch_unit("2A10")

    # Create copies, one shallow and one deep
    inc6 = copy(inc5)
    inc7 = deepcopy(inc5)

    # Update the original with another unit
    inc5.dispatch_unit("2A11")

    # Display the three versions to show that the shallow copy was also updated
    # while the deep copy doesn't have the change
    print("Original:")
    print(inc5.incident_info())
    print("\nShallow Copy:")
    print(inc6.incident_info())
    print("\nDeep Copy:")
    print(inc7.incident_info())


# TODO 5:
# Complete the main function.
#
# Requirements:
# x Create at least one object from the parent class.
# x Create at least one object from the child class.
# x Demonstrate inheritance by calling methods.
# x Call your namespace demonstration function.
# x Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n===Parent Object Demonstration===")

    # Create an Incident object, display it, close the incident, and then display it again
    inc1 = Incident("1234 Main St", "Theft")
    print(inc1.incident_info(),"\n")
    inc1.close_incident()
    print(inc1.incident_info())

    # Create a  DispatchIncidnet object and display it before and after several changes
    print("\n===Child Object Demonstration===")
    inc2 = DispatchIncident("54321 Second Dr", "Assault", 1, 3)
    print(inc2.incident_info(),"\n")
    inc2.dispatch_unit("1B14")
    inc2.dispatch_unit("1B15")
    print(inc2.incident_info(),"\n")
    inc2.close_incident()
    print(inc2.incident_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()