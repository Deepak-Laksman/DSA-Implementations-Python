# In this method we use a hash function.
# A hash function is a function that converts a given key into some value which is pretty small.
# We could then create an array of a certain size "m" where this is the range of possible key values for any value
# (0, m - 1)
# But here there is another problem, 2 or more values can have same hash value which leads to collision.
# So what we do is, we store this a data structure which is array of linked lists. So whenever a hash value collides,
# we just append to the end of the linked list.
# We can another data structure like array of self balancing trees.