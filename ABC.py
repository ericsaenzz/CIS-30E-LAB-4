import re 
from abc import ABC, abstractmethod

class DataIntegrityChecker(ABC):
    @abstractmethod
    def check_integrity(self,data):
        pass

class AgeDataIntegrityChecker(DataIntegrityChecker):
    def check_integrity(self,data):
        try:
            age = int(data)
            if 0 <= age <= 120:
                return f"Age {age} is valid."
            else:
                return f"Invalid. Age {age} is INVALID. Age MUST be between 0 and 120."
        except ValueError:
            return f"Invalid. Age '{data}' is invalid. Input must be a number."

class EmailDataIntegrityChecker(DataIntegrityChecker):
    def check_integrity(self,data):

        emailFormat = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not isinstance(data,str):
            return f"\n!! ERROR. Email '{data}' is not a valild Email !!\n"
        if re.match(emailFormat, data):
            return f"Email '{data}' is a valid email."
        else:
            return f"\n!! ERROR. Email '{data}' is not a valild Email. !!\n"

def run_tests():
    ageCheck = AgeDataIntegrityChecker()
    emailCheck = EmailDataIntegrityChecker()

    print("\n>-- Testing AgeDataIntegrityChecker ---<\n")
    age_test = [
        21,
        -1,
        225,
        'a',
        0,
        120,
        43,
        '-',
        121
    ]

    for test in age_test:
        result = ageCheck.check_integrity(test)
        print(f">> Test Input: {test} -> {result}\n")

    print("\n>-- Testing EmailDataIntegrityChecker ---<\n")
    email_test = [
        "mrbeast@gmail.com",
        "the.original.username@outlook.com",
        "invalidTest.com",
        'a',
        0,
        "@yahoo.com",
        "therealdeal@microsoft",
        '-'
    ]

    for test in email_test:
        result = emailCheck.check_integrity(test)
        print(f">> Test Input: {test} -> {result}\n")

def main():
    run_tests()

main()