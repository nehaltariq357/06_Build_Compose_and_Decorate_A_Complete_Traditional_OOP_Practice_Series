# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("below 18 not allowed")
    else:
        print("allowed")


try:
    check_age(10)
except InvalidAgeError as e:
    print("custom error:", e)

