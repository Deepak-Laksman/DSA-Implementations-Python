# In this method we just create a linear data structure to store all the values. If the size occupied crosses
# 50% of size available, we then double the total size and copy all the elements in this new data structure.
# There are quite a few types of probing.
# 1. Linear Probing
# Here we just find the hash value of a given value and take % with some value and check whether that index
# is occupied or not. If occupied we check at hash(x) + 1 % m and so on. So while searching we do linear search.
# While deleting we need to specifically mention that the cell is deleted because there may be empty cells in between
# filled cells.
# 2. Quadratic Probing
# Its the same as Linear Probing but here the calculation of index is different. hash(x) + 1 * 2 % m if this is
# filled, then hash(x) + 2 * 2 % m will be checked and so on.
# 3. Double Hashing
#  hash(x) + 1 * hash2(x) % m and so on.
# CACHE PERFORMANCE COMPARISON
# linear probing > quadratic probing > double hashing
# COLLISION RESISTANCE COMPARISON
# double hashing > quadratic probing > linear probing
