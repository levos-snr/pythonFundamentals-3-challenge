def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in the input string."""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

def calculate_factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """Apply the decorator_func to the input function."""
    return decorator_func(func)

def sort_by_age(people):
    """Sort a list of (name, age) tuples by age in ascending order."""
    return sorted(people, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    """Merge two dictionaries, summing values for common keys."""
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """Print the car's information."""
        print(f"{self.year} {self.make} {self.model}")

if __name__ == '__main__':
    while True:
        print("\nChoose a function to run:")
        print("1. Add Numbers")
        print("2. Check if a Number is Even")
        print("3. Reverse a String")
        print("4. Count Vowels in a String")
        print("5. Calculate Factorial")
        print("6. Sort a List of People by Age")
        print("7. Merge Two Dictionaries")
        print("8. Display Car Information")
        print("9. Exit")

        choice = input("Enter the number of the function you want to run: ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {add_numbers(num1, num2)}")

        elif choice == '2':
            number = int(input("Enter a number: "))
            print(f"Is the number even? {is_even(number)}")

        elif choice == '3':
            text = input("Enter a string to reverse: ")
            print(f"Reversed string: {reverse_string(text)}")

        elif choice == '4':
            text = input("Enter a string to count vowels: ")
            print(f"Number of vowels: {count_vowels(text)}")

        elif choice == '5':
            n = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {n} is: {calculate_factorial(n)}")

        elif choice == '6':
            people = []
            n = int(input("Enter the number of people: "))
            for _ in range(n):
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                people.append((name, age))
            print(f"Sorted by age: {sort_by_age(people)}")

        elif choice == '7':
            dict1 = eval(input("Enter the first dictionary (e.g., {'a': 1, 'b': 2}): "))
            dict2 = eval(input("Enter the second dictionary (e.g., {'b': 3, 'c': 4}): "))
            print(f"Merged dictionaries: {merge_dicts(dict1, dict2)}")

        elif choice == '8':
            make = input("Enter the car make: ")
            model = input("Enter the car model: ")
            year = input("Enter the car year: ")
            my_car = Car(make, model, year)
            my_car.display_info()

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
