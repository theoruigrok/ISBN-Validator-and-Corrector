# ISBN-Validator-and-Corrector
ISBN number checker and correcter

This is an assignment for the course 'Analysis' belonging to the first semester of the foundation year, bachelor Information technology course.
Here's a summary of what the code does:

It imports the string module.
There is a function called load_data() that reads input from a CSV file and stores the book names and ISBN numbers in the list_of_book_isbn variable. However, the function is not called immediately after its definition.
The code defines a short example input list as a substitute for the CSV file.
The script processes the data in list_of_book_isbn and performs various operations on the ISBN numbers.
The ISBN numbers are cleaned by removing the "ISBN " prefix and hyphens from each string.
The cleaned ISBN numbers are stored in the clean_isbn_list variable.
The script iterates through the clean_isbn_list and performs operations to check the validity of the ISBN numbers.
For each ISBN number, it determines if there are missing digits and checks if the calculated checksum matches the last digit of the ISBN number.
The results are stored in output_A and output_B lists, where output_A contains the book names and output_B contains error descriptions such as "Missing Digits" or "Wrong Check Number."
Finally, the script prints the output_list, which is a list of tuples containing the book names and their corresponding error descriptions.
Please note that the code includes comments to explain each step of the process.
