# Function Runner CLI
A powerful Python command-line interface (CLI) tool designed to allow users to
interactively execute a variety of essential functions. 
With enhanced output formatting using the rich library, 
this utility provides a versatile and visually appealing user experience.


## Features ##

- **Add Numbers**: Adds two numbers and returns the result.
- **Check Even Number**: Checks whether a number is even.
- **Reverse String**: Reverses a given string.
- **Count Vowels**: Counts the number of vowels in a string.
- **Calculate Factorial**: Computes the factorial of a given non-negative integer.
- **Sort by Age**: Sorts a list of `(name, age)` tuples by age in ascending order.
- **Merge Dictionaries**: Merges two dictionaries, summing values for common keys.
- **Display Car Information**: Creates a car object and displays its information.

## Getting Started ##

### Prerequisites
- Python 3.12
- pipenv (Python dependency manager)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/levos-snr/pythonFundamentals-3-challenge.git
   cd pythonFundamentals-3-challenge
   ```
2. **Install the required dependencies**:

   ```bash
   pipenv install
   pipenv shell
   ```
3. **Run the application**:

   ```bash
   pipenv run python main.py
   ```
   
### Usage ##
- Launch the CLI: Upon running the application, 
you will be presented with a menu of functions.
4. **Choose a function to run**:
- Enter the number corresponding to the function you want to execute.
- Input the required data as prompted.
- The result will be displayed after execution.

5. **Exit the application**:
- Enter `9` to exit the application.

## Example ##
  
   ```bash
   Choose a function to run:
   1. Add Numbers
   2. Check if a Number is Even
   3. Reverse a String
   4. Count Vowels in a String
   5. Calculate Factorial
   6. Sort a List of People by Age
   7. Merge Two Dictionaries
   8. Display Car Information
   9. Exit
   Enter the number of the function you want to run: 1
   Enter the first number: 5
   Enter the second number: 7
   Result: 12
   ```
   
## Enhanced Output with `rich` ##
- This application uses the rich package to display beautifully 
formatted text, tables, and more.
Enjoy a better visual experience while interacting with the CLI.

## Project Dependencies ##

- Python 3.12: The core programming language used.
- pipenv: For managing virtual environments and dependencies.
- rich: For enhanced output formatting.

## License ##

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Contact ##

For any questions or issues, please contact me at [lewisodero27@gmail.com](mailto:lewisodero27@gmail.com).

Happy coding!
This `README.md` provides a clear and concise overview of the project, its usage, and how others can contribute.






