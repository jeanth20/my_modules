def random_data(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append({
            "id": i,
            "name": random.choice(["John", "Mary", "Bob", "Jane", "Peter", "Angela", "Zoe"]),
            "age": random.randint(0, 100),
            "email": random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + "@" + random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + ".com"
        })
    return mylist


def random_data2(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.choice(["John", "Mary", "Bob", "Jane", "Peter", "Angela", "Zoe"]))
        mylist.append(random.randint(0,100))
        mylist.append(random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + "@" + random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + ".com")
    return mylist


def random_numbers(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.randint(0,100))
    return mylist


def random_names(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.choice(["John", "Mary", "Bob", "Jane", "Peter", "Angela", "Zoe"]))
    return mylist


def random_emails(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + "@" + random.choice(["gmail", "hotmail", "yahoo", "outlook"]) + ".com")
    return mylist


def random_dates1(quantity):
    import random
    import datetime
    mylist = []
    for i in range(quantity):
        mylist.append(datetime.date(random.randint(1900, 2020), random.randint(1,12), random.randint(1,28)))
    return mylist


def random_dates2(quantity):
    import random
    import datetime
    mylist = []
    for i in range(quantity):
        start_date = datetime.date(2018, 1, 1)
        end_date = datetime.date(2019, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        mylist.append(random_date)
    return mylist


def random_addresses(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.choice(["123", "1", "5", "6", "10", "20"]) + " " + random.choice(["Main", "High", "Low", "Grove", "Park", "Maple"]) + " Street")
    return mylist


def random_cities(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(random.choice(["London", "New York", "Paris", "Madrid", "Barcelona", "Lisbon", "Tokyo", "Berlin", "Rome", "Athens", "Cairo", "Rio", "Moscow", "Dubai", "Hong Kong", "Sydney"]))
    return mylist


def random_passwords(quantity):
    import random
    import string
    mylist = []
    for i in range(quantity):
        mylist.append("".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(8,20))))
    return mylist


def random_cpf(quantity):
    import random
    mylist = []
    for i in range(quantity):
        mylist.append(str(random.randint(100, 999)) + "." + str(random.randint(100, 999)) + "." + str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)))
    return mylist


data = random_data(10)
print(data)


data = random_passwords(10)
print(data)


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    People = [
        Person("John", 36, random_emails(1)[0]),
        Person("Mary", 25, random_emails(1)[0]),
        Person("Bob", 27, random_emails(1)[0]),
        Person("Jane", 32, random_emails(1)[0]),
        Person("Peter", 45, random_emails(1)[0]),
        Person("Angela", 19, random_emails(1)[0]),
    ]
    
    