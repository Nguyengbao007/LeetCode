# Creating a hashmap
hashmap = {"apple": 1, "banana": 2}
Index=0
map={"":Index}
# Adding or updating values
hashmap["orange"] = 3
hashmap["banana"] = 4
# Accessing values
print(hashmap["apple"])  # Output: 1
print(hashmap.get("grape", "Not Found"))  # Output: "Not Found"
print(map["apple"])
# Checking existence
print("orange" in hashmap)  # Output: True

# Removing a key-value pair
del hashmap["apple"]
print(hashmap)

# Iterating over the hashmap
for key, value in hashmap.items():
    print(f"{key}: {value}")
