from datetime import datetime

class SAIDValidator:
    def __init__(self, id_number):
        self.id_number = id_number

    def generate_luhn_digit(self, input_string):
        total = 0
        count = 0
        for i in range(len(input_string)):
            multiple = count % 2 + 1
            count += 1
            temp = multiple * int(input_string[i])
            temp = temp // 10 + temp % 10
            total += temp
        total = (total * 9) % 10
        return total

    def check_id_number(self, id_number):
        number = id_number[:-1]
        return self.generate_luhn_digit(number) == int(id_number[-1])

    def get_birthdate(self, id_number):
        year = id_number[:2]
        current_year = datetime.now().year % 100
        prefix = "19"
        if int(year) < current_year:
            prefix = "20"
        month = id_number[2:4]
        day = id_number[4:6]
        birthdate = datetime.strptime(f"{prefix}{year}/{month}/{day}", "%Y/%m/%d").date()
        return birthdate

    def get_gender(self, id_number):
        return "female" if int(id_number[6]) < 5 else "male"

    def get_citizenship(self, id_number):
        return "citizen" if int(id_number[10]) == 0 else "resident"

    def extract_data(self):
        result = {}
        result["valid"] = self.check_id_number(self.id_number)
        result["birthdate"] = self.get_birthdate(self.id_number)
        result["gender"] = self.get_gender(self.id_number)
        result["citizen"] = self.get_citizenship(self.id_number)
        return result

# Example usage:
# id_number = ""
# validator = SAIDValidator(id_number)
# data = validator.extract_data()

# print("ID Number:", id_number)
# print("Valid:", data["valid"])
# print("Birthdate:", data["birthdate"])
# print("Gender:", data["gender"])
# print("Citizenship:", data["citizen"])
