# Here we are just going to convert the given value into a key and put the value in array with index value as the key
# Here the problem is we need so much memory to store very few values.
# For example, lets assume we need to store phone numbers in a phone book.
# We need to create an array with indices of all possible phone numbers and then put True or False
# in their value if they exist or not in the phonebook.
# The retrieval and update operations are just O(1).
# But the memory usage is very high that its practically impossible to create such a big phonebook
# for each and every device.