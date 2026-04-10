# Answers

Question 1: What is stored in obj.__dict__?

Answer:
The __dict__ attribute stores all object attributes in a dictionary form.
It maps attribute names to their values.
This is useful for inspecting and modifying object data dynamically.

---

Question 2: What is the difference between a class and an object?

Answer:
A class is a blueprint that defines properties and behavior.
An object is an instance of that class.
Classes define structure, objects store actual data.

---

Question 3: What does __init__ do?

Answer:
The __init__ method initializes a new object.
It sets initial values for attributes.
It is automatically called when a new object is created.

---

Question 4: Who calls __str__, and when?

Answer:
The __str__ method is called by Python when we use print() on an object.
It provides a human-readable representation.
This helps make output easier to understand.

---

Question 5: What is the difference between == and is?

Answer:
== compares values.
is compares object identity (memory location).
This is important to distinguish equality from identity.

---

Question 6: Why do we use other: object in __eq__ and __lt__?

Answer:
Using object allows comparison with any type.
It ensures compatibility with Python's data model.
It also forces us to safely check types before comparing.
