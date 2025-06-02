# Initialize a list with various data types
varied_data = [1, "hello", 3.14, True, None, [1, 2], (3, 4), {5, 6}, {'a': 7}, 8+9j, b"bytes", 
frozenset([10]), range(5), bytearray(5), memoryview(b"xyz"), -10, 0.0, "Python", 7, False]

# Create empty lists to categorize each data type
integers = []
strings = []
floats = []
booleans = []
none_type = []
lists = []
tuples = []
sets = []
dictionaries = []
complex_numbers = []
bytes_data = []
frozensets = []
ranges = []
bytearrays = []
memoryviews = []

# Loop through the mixed data list and categorize each item based on its type
for element in varied_data:
    if isinstance(element, int):
        integers.append(element)
    elif isinstance(element, str):
        strings.append(element)
    elif isinstance(element, float):
        floats.append(element)
    elif isinstance(element, bool):
        booleans.append(element)
    elif element is None:
        none_type.append(element)
    elif isinstance(element, list):
        lists.append(element)
    elif isinstance(element, tuple):
        tuples.append(element)
    elif isinstance(element, set):
        sets.append(element)
    elif isinstance(element, dict):
        dictionaries.append(element)
    elif isinstance(element, complex):
        complex_numbers.append(element)
    elif isinstance(element, bytes):
        bytes_data.append(element)
    elif isinstance(element, frozenset):
        frozensets.append(element)
    elif isinstance(element, range):
        ranges.append(element)
    elif isinstance(element, bytearray):
        bytearrays.append(element)
    elif isinstance(element, memoryview):
        memoryviews.append(element)

# Output the categorized lists
print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)
print("Booleans:", booleans)
print("None Type:", none_type)
print("Lists:", lists)
print("Tuples:", tuples)
print("Sets:", sets)
print("Dictionaries:", dictionaries)
print("Complex Numbers:", complex_numbers)
print("Bytes:", bytes_data)
print("Frozensets:", frozensets)
print("Ranges:", ranges)
print("Bytearrays:", bytearrays)
print("Memoryviews:", memoryviews)
