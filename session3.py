# list
int_list = [1, 2, 3, 4, 5] # list of integers
string_list = ["apple", "banana", "cherry"] # list of strings
mix_list = [1, "hello", 3.14, True] # list with different data types


# accessing list elements
print(int_list[1]) # Output: 2
print(string_list[0]) # Output: apple
print(mix_list[-1]) # Output: True (negative index accesses from the end)


# modifying elements
string_list[2] = "Orange"
print(string_list) # Output: ['apple', 'banana', 'orange']


# adding elements
int_list= [5, 10, 20, 35, 50]
print("Original list:", int_list)
# print(f"Original list: {int_list}")

int_list.insert(3, 25) # Inserts 25 at index 3
print("After insert:", int_list) # Output: After insert: [5, 10, 20, 25, 35, 50]

int_list.append(60) # Adds 60 to the end
print("After append:", int_list) # Output: After append: [5, 10, 20, 25, 35, 50, 60]


# removing elements
int_list = [5, 10, 20, 25, 30]
print("Original list:", int_list)

del int_list[1] # Deletes the element at index 1 (10)
print("After del:", int_list) # Output: [5, 20, 25, 30]

int_list.remove(25) # Removes the value 25
print("After remove:", int_list) # Output: [5, 20, 30]

last_item = int_list.pop() # Removes the last element (30)
print("After pop:", int_list) # Output: [5, 20]
print("Popped item:", last_item) # Output: 30


# loop
# .title() for capital letter
magicians = ["alice", "david", "carolina"] #list of magicians
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
