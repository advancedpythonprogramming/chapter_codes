# inheritance_wrong.py


class AddressHolder:

    def __init__(self, street, number, city, state):
        self.street = street
        self.number = number
        self.city = city
        self.state = state


class Contact:

    contact_list = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contact_list.append(self)


class Customer(Contact, AddressHolder):

    def __init__(self, name, email, phone,
                 street, number, state, city):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, number,
                               state, city)
        self.phone = phone


if __name__ == "__main__":

    c = Customer('John Davis', 'jp@g_mail.com', '23542331',
                 'Beacon Street', '231', 'Cambridge', 'Massachussets')

    print("name: {}\nemail: {}\naddress: {}, {}"
          .format(c.name, c.email, c.street, c.state))
