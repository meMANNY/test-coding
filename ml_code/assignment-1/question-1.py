# String Methods

# 1. capitalize()
text = "hello world"
print(text.capitalize())  # Expected output: "Hello world"

# 2. find()
print(text.find('world'))  # Expected output: 6

# 3. isdigit()
numeric_str = "123"
print(numeric_str.isdigit())  # Expected output: True

# 4. join()
separator = "-"
print(separator.join(['a', 'b', 'c']))  # Expected output: "a-b-c"

# 5. split()
print(text.split())  # Expected output: ['hello', 'world']


# List Methods

# 1. append()
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Expected output: [1, 2, 3, 4]

# 2. extend()
numbers.extend([5, 6])
print(numbers)  # Expected output: [1, 2, 3, 4, 5, 6]

# 3. index()
print(numbers.index(4))  # Expected output: 3

# 4. pop()
numbers.pop()
print(numbers)  # Expected output: [1, 2, 3, 4, 5]

# 5. reverse()
numbers.reverse()
print(numbers)  # Expected output: [5, 4, 3, 2, 1]


# Dictionary Methods

# 1. keys()
data = {'x': 1, 'y': 2}
print(data.keys())  # Expected output: dict_keys(['x', 'y'])

# 2. values()
print(data.values())  # Expected output: dict_values([1, 2])

# 3. items()
print(data.items())  # Expected output: dict_items([('x', 1), ('y', 2)])

# 4. get()
print(data.get('x'))  # Expected output: 1

# 5. popitem()
data.popitem()
print(data)  # Expected output: {'x': 1}
