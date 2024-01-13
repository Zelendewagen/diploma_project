from Classes import Contact


class PhoneBook:
    contacts: list = []
    last_id: str = '0'

    def __init__(self):
        pass

    def add(self, name: str, phone: str, comment: str, id: str = None):
        if id:
            user = Contact.Contact(id, name, phone, comment)
            self.last_id = id
        else:
            user = Contact.Contact(self.last_id, name, phone, comment)
        self.last_id = str(int(self.last_id) + 1)
        self.contacts.append(user)

    def remove(self, id):
        for (index, user) in enumerate(self.contacts):
            if user.id == str(id):
                print('KEK')
                self.contacts.pop(index)

    def get_contacts(self):
        all_users = []
        for user in self.contacts:
            all_users.append(user.items())
        return all_users

    def get(self, id):
        get_id = None
        for (index, user) in enumerate(self.contacts):
            if user.id == str(id):
                get_id = index
                break
        return self.contacts[get_id] if get_id else None

    def set(self, id: int, name: str, phone: str, comment: str):
        for (index, user) in enumerate(self.contacts):
            if int(user.id) == id:
                self.contacts[index].name = name
                self.contacts[index].phone = phone
                self.contacts[index].comment = comment

    def clear(self):
        self.contacts.clear()
        self.last_id = '0'
