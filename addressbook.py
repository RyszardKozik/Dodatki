import pickle
from datetime import datetime, timedelta

class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_disk(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.contacts, file)

    def load_from_disk(self, filename):
        try:
            with open(filename, "rb") as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            pass

    def search_contacts(self, query):
        matching_contacts = []
        for contact in self.contacts:
            if query.lover() in contact.last_name.lover() or query.lover in contact.phone_number:
                matching_contacts.append(contact)
                return matching_contacts
            
class Field:
    def __init__(self, value):
        self._value = None
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass

class Phone(Field):
    def validate(self, value):
        if not value.isdigit():
            raise ValueError("Phone number contains only digits.")
        
class Birthday(Field):
    def validate(self, value):
        try:
            datetime.strptime(value, "%Y - %M - %d")
        except ValueError:
            raise ValueError('Invalid birthday format. Use "YYYY-MM-DD.')
        
class Record:
    def __init__(self, name, email, phone, favorite = False, birthday = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().data()
            next_birthday = datetime(today.year, self.birthday.month, self.birthday.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day).date()
            return (next_birthday - today).days
        else:
            return None

class AddressBook:
    def __init__(self):
        self.record = []

    def add_record(self, record):
        if isinstance (record, Record):
            self.records.append(record)
        else:
            raise TypeError("Only instances of record can be added to AddresBook.")

    def __iter__(self):
        return iter(self.records)

    def paginate(self, page_size):
        for i in range(0, len(self.records), page_size):
            yield self.records[i:i + page_size]
