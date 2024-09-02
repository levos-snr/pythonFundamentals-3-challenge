from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel

console = Console()

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
        console.print("[bold yellow]Decorator Applied[/bold yellow]")
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
        console.print(f"[bold green] Make: {self.make}")
        console.print(f"[bold green] Model: {self.model}")
        console.print(f"[bold green] Year: {self.year}")

def main_menu():
    table = Table(title="Function Menu")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    
    table.add_row("1", "Add Numbers")
    table.add_row("2", "Check if a Number is Even")
    table.add_row("3", "Reverse a String")
    table.add_row("4", "Count Vowels in a String")
    table.add_row("5", "Calculate Factorial")
    table.add_row("6", "Sort a List of People by Age")
    table.add_row("7", "Merge Two Dictionaries")
    table.add_row("8", "Display Car Information")
    table.add_row("9", "Exit")
    
    console.print(table)

if __name__ == '__main__':
    while True:
        main_menu()
        
        choice = Prompt.ask("\n[bold blue]Enter the number of the function you want to run[/bold blue]", choices=[str(i) for i in range(1, 10)])

        if choice == '1':
            num1 = float(Prompt.ask("[bold yellow]Enter the first number[/bold yellow]"))
            num2 = float(Prompt.ask("[bold yellow]Enter the second number[/bold yellow]"))
            result = add_numbers(num1, num2)
            console.print(f"[bold green]Result: {result}[/bold green]")

        elif choice == '2':
            number = int(Prompt.ask("[bold yellow]Enter a number[/bold yellow]"))
            even = is_even(number)
            console.print(f"[bold green]Is the number even? {even}[/bold green]")

        elif choice == '3':
            text = Prompt.ask("[bold yellow]Enter a string to reverse[/bold yellow]")
            reversed_text = reverse_string(text)
            console.print(f"[bold green]Reversed string: {reversed_text}[/bold green]")

        elif choice == '4':
            text = Prompt.ask("[bold yellow]Enter a string to count vowels[/bold yellow]")
            vowel_count = count_vowels(text)
            console.print(f"[bold green]Number of vowels: {vowel_count}[/bold green]")

        elif choice == '5':
            n = int(Prompt.ask("[bold yellow]Enter a number to calculate its factorial[/bold yellow]"))
            factorial = calculate_factorial(n)
            console.print(f"[bold green]Factorial of {n} is: {factorial}[/bold green]")

        elif choice == '6':
            people = []
            n = int(Prompt.ask("[bold yellow]Enter the number of people[/bold yellow]"))
            for _ in range(n):
                name = Prompt.ask("[bold yellow]Enter name[/bold yellow]")
                age = int(Prompt.ask("[bold yellow]Enter age[/bold yellow]"))
                people.append((name, age))
            sorted_people = sort_by_age(people)
            console.print(Panel.fit(str(sorted_people), title="Sorted by Age", border_style="green"))

        elif choice == '7':
            dict1 = eval(Prompt.ask("[bold yellow]Enter the first dictionary (e.g., {'a': 1, 'b': 2})[/bold yellow]"))
            dict2 = eval(Prompt.ask("[bold yellow]Enter the second dictionary (e.g., {'b': 3, 'c': 4})[/bold yellow]"))
            merged_dict = merge_dicts(dict1, dict2)
            console.print(Panel.fit(str(merged_dict), title="Merged Dictionaries", border_style="green"))

        elif choice == '8':
            make = Prompt.ask("[bold yellow]Enter the car make[/bold yellow]")
            model = Prompt.ask("[bold yellow]Enter the car model[/bold yellow]")
            year = Prompt.ask("[bold yellow]Enter the car year[/bold yellow]")
            my_car = Car(make, model, year)
            my_car.display_info()

        elif choice == '9':
            console.print("[bold red]Exiting...[/bold red]")
            break

        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
