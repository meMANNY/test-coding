# Initialize the counter
counter = 0
# Loop while counter is less than 5
while counter < 5:
    print(counter)
    # Increment the counter by 1
    counter += 1

# Reset the counter
counter = 0
# Loop while counter is less than 10
while counter < 10:
    print(counter)
    # Stop the loop if counter reaches 5
    if counter == 5:
        break
    # Increment the counter by 1
    counter += 1
# The loop breaks when counter equals 5

# Reset the counter
counter = 0
# Loop while counter is less than 5
while counter < 5:
    # Increment the counter by 1
    counter += 1
    # Skip the rest of the loop when counter equals 3
    if counter == 3:
        continue
    print(counter)
# Skips printing when counter equals 3
