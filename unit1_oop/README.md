## Design Implementation

For this project I decided to use my background as a 911 operator and police dispatcher to create an object for a 911/emergency incident, bending reality a little bit to fit the constraints of this assignment.

I created the parent object "Incident" using the two variables that are required at my work to create a call: a location, and an incident type. Along with those pieces of info every incident gets a status, open by default.
The next thing I did was create a function that can be used to close the incidents as that's another function that is available by default for every incident.

Before moving on to the child class I started working on the main function, deciding it would be easier to test as I worked. I created a simple object, displayed the info, and then tried the "close_incident" function to make sure it worked.

Once I knew the parent class was working and displaying properly I created the child class for an incident that gets dispatched. For this one the extra variables were a priority, sector, and then a list of units dispatched to the call.
This is where it breaks from reality since in real life every incident gets a priority, sector, and can have units get dispatched to it.

After I programmed the child class, I tested it out in the main method to ensure everything was working as intended.

The hardest part for me was figuring out how namespaces work within python. Displaying an object with "__dict__" was a new concept to me so it was interesting messing with that and seeing how it worked!

Programming the portion for shallow and deep copying was fairly simple since I understood how copying works. What was interesting was seeing in action how editing the original object affects the shallow copy.

# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
