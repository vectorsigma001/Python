## Example 1 Converting Python Objects to JSON

To convert a Python object to a JSON string, you can use the json.dumps() method.
```python
import json

# Example Python dictionary
python_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_dict)
print(json_string)
# {"name": "Alice", "age": 30, "city": "New York"}
```

## Example 2 Writing Json to a File

You can write JSON data directly to a file using the json.dump() method.
```python
import json

# Example Python dictionary
python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}

# Writing JSON data to a file
with open('data.json', 'w') as json_file:
    json.dump(python_dict, json_file)
```

## Example 3 Reading JSON from a File

To read JSON data from a file, use the json.load() method.
```text
import json

# Reading JSON data from a file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)
# data.json contains
# {"name": "Bob", "age": 25, "city": "Los Angeles"}
# output
{'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
```

## Example 4 Converting JSON to Python Objects

To convert a JSON string to a Python object, use the json.loads() method.
```python
import json

# Example JSON string
json_string = '{"name": "Charlie", "age": 35, "city": "Chicago"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_string)
print(python_dict)
# output
# {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
``

## Example 5 Handling Complex Python Objects

If you have more complex Python objects, such as custom classes,

you may need to implement custom serialization methods.
```python
import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def person_to_dict(obj):
    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age,
            "city": obj.city
        }
    raise TypeError("Type not serializable")

# Example Person object
person = Person("David", 40, "San Francisco")

# Convert Person object to JSON string
json_string = json.dumps(person, default=person_to_dict)
print(json_string)

# output
# {"name": "David", "age": 40, "city": "San Francisco"}
```

## Example 6: Decoding Custom JSON to Python Objects

To convert JSON back into a custom Python object, you can define a custom decoding function.

```python
import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def dict_to_person(d):
    return Person(d['name'], d['age'], d['city'])

# Example JSON string
json_string = '{"name": "Eve", "age": 28, "city": "Seattle"}'

# Convert JSON string to Person object
person = json.loads(json_string, object_hook=dict_to_person)
print(person.name, person.age, person.city)

# output
# Eve 28 Seattle
```


## Example 7: CRUD in json
```python
import json
import os

class PhoneBook:
    def __init__(self, filename='phonebook.json'):
        self.filename = filename
        self.load_phonebook()

    def load_phonebook(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.phonebook = json.load(file)
        else:
            self.phonebook = {}

    def save_phonebook(self):
        with open(self.filename, 'w') as file:
            json.dump(self.phonebook, file, indent=4)

    def add_contact(self, name, phone):
        self.phonebook[name] = phone
        self.save_phonebook()

    def get_contact(self, name):
        return self.phonebook.get(name)

    def update_contact(self, name, phone):
        if name in self.phonebook:
            self.phonebook[name] = phone
            self.save_phonebook()
            return True
        return False

    def delete_contact(self, name):
        if name in self.phonebook:
            del self.phonebook[name]
            self.save_phonebook()
            return True
        return False

    def list_contacts(self):
        return self.phonebook

# Example usage
if __name__ == "__main__":
    pb = PhoneBook()

    # Add contacts
    pb.add_contact("Alice", "123-456-7890")
    pb.add_contact("Bob", "987-654-3210")

    # List contacts
    print("All Contacts:")
    print(pb.list_contacts())

    # Get a contact
    print("\nGetting Alice's Contact:")
    print(pb.get_contact("Alice"))

    # Update a contact
    print("\nUpdating Bob's Contact:")
    pb.update_contact("Bob", "111-222-3333")
    print(pb.get_contact("Bob"))

    # Delete a contact
    print("\nDeleting Alice's Contact:")
    pb.delete_contact("Alice")
    print(pb.list_contacts())
```

## Example 8: Interactive CRUD in Json
```python
import json
import os

class PhoneBook:
    def __init__(self, filename='phonebook.json'):
        self.filename = filename
        self.load_phonebook()

    def load_phonebook(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.phonebook = json.load(file)
        else:
            self.phonebook = {}

    def save_phonebook(self):
        with open(self.filename, 'w') as file:
            json.dump(self.phonebook, file, indent=4)

    def add_contact(self, name, phone):
        self.phonebook[name] = phone
        self.save_phonebook()

    def get_contact(self, name):
        return self.phonebook.get(name)

    def update_contact(self, name, phone):
        if name in self.phonebook:
            self.phonebook[name] = phone
            self.save_phonebook()
            return True
        return False

    def delete_contact(self, name):
        if name in self.phonebook:
            del self.phonebook[name]
            self.save_phonebook()
            return True
        return False

    def list_contacts(self):
        return self.phonebook

def main():
    pb = PhoneBook()

    while True:
        print("\nPhone Book Application")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            pb.add_contact(name, phone)
            print(f"Contact {name} added.")

        elif choice == '2':
            name = input("Enter name: ")
            contact = pb.get_contact(name)
            if contact:
                print(f"{name}: {contact}")
            else:
                print(f"Contact {name} not found.")

        elif choice == '3':
            name = input("Enter name: ")
            if name in pb.phonebook:
                phone = input("Enter new phone number: ")
                pb.update_contact(name, phone)
                print(f"Contact {name} updated.")
            else:
                print(f"Contact {name} not found.")

        elif choice == '4':
            name = input("Enter name: ")
            if pb.delete_contact(name):
                print(f"Contact {name} deleted.")
            else:
                print(f"Contact {name} not found.")

        elif choice == '5':
            contacts = pb.list_contacts()
            if contacts:
                print("\nContacts:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
