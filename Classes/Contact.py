class Contact:
    id: str
    name: str
    phone: str
    comment: str

    def __init__(self, id: str, name: str, phone: str, comment: str, *args, **kwargs):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def items(self):
        return self.id, self.name, self.phone, self.comment
