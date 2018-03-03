def get_valid_input(input_string, valid_options):
    """
    str, str -> str
    Function returns user's answer on questions with some variants of answer
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Class for property representation
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Creates new property
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Property -> None
        Shows the information about some class instance
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        return dict(square_feet=input("Enter the square feet: "),
        beds=input("Enter number of bedrooms: "), baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class for apartment representation
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Creates new apartment
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Apartment -> None
        Shows the information about some class instance
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ",
        Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class for house representation
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        Creates new house
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        House -> None
        Shows the information about some class instance
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                    House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                House.valid_garage)

        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class for purchased thing representation
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        Creates new purchased thing
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Purchase -> None
        Shows the information about some class instance
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class for rentaled thing representation
    """
    def __init__(self, furnished='', utilities='',
            rent='', **kwargs):
        """
        Creates new rentaled thing
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Rental -> None
        Shows the information about some class instance
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
               "What are the estimated utilities? "),
            furnished = get_valid_input(
                "Is the property furnished? ",
                    ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Class for rentaled house representation
    """
    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class for rentaled apartment representation
    """
    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class for purchased apartment representation
    """
    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Class for purchased apartment representation
    """
    def prompt_init():
        """
        None -> dict
        Returns the dict with entered by user information about some class instance
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class for property agent representation
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        """
        Creates new agent
        """
        self.property_list = []

    def display_properties(self):
        """
        Agent -> None
        Shows information about properties
        """
        for property in self.property_list:
            property.display()

    def add_property(self):
        """
        Agent -> None
        Takes information about properties
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def display_by_property_types(self):
        """
        Agent -> None
        Shows information about houses or apartments
        """
        ans = get_valid_input("Print type of property which you want to see ", ("house", "apartment")).lower()
        if ans == "house":
            for property in self.property_list:
                if isinstance(property, HousePurchase) or isinstance(property, HouseRental):
                    property.display()
        else:
            for property in self.property_list:
                if isinstance(property, ApartmentPurchase) or isinstance(property, ApartmentRental):
                    property.display()

    def display_by_payment_types(self):
        """
        Agent -> None
        Shows information about purchased things or rented things
        """
        ans = get_valid_input("Print type of payment which you want to see ", ("purchase", "rental")).lower()
        if ans == "purchase":
            if isinstance(property, HousePurchase) or isinstance(property, ApartmentPurchase):
                property.display()
        else:
            if isinstance(property, ApartmentRental) or isinstance(property, HouseRental):
                property.display()
