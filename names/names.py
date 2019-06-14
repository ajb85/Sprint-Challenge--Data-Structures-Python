import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

end_time = time.time()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # value is greater or less than, move right or left.  If the same, do nothing
        # When moving left or right, check for None.  If None is found, create the node
        # Else, move to next node to repeat
        # if(self.value == None):
        #     self.value = value
        # elif(value > self.value):
        #     if(self.right == None):
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        # elif(value < self.value):
        #     if(self.left == None):
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)   
        if(self.value == None):
            self.value = value
        else:
            node = self
            while(node != None):
                if(value > node.value):
                    if(node.right is not None):
                        node = node.right
                    else:
                        node.right = BinarySearchTree(value)
                        node = None
                else:
                    if(node.left is not None):
                        node = node.left
                    else:
                        node.left = BinarySearchTree(value)
                        node = None

    def contains(self, target):
        # if(target == self.value):
        #     return True
        # elif(target > self.value):
        #     rightContains = self.right.contains(target) if self.right != None else False
        #     leftContains = False
        # else:
        #     leftContains = self.left.contains(target) if self.left != None else False
        #     rightContains = False
        # return leftContains or rightContains
        node = self
        while node != None:
            if(target == node.value):
                return True
            elif(target > node.value):
                node = node.right
            else:
                node = node.left
        return False

# BST SOLUTION

# name_tree = BinarySearchTree(None)
# for name in names_1: # O(n)
#     name_tree.insert(name.lower()) # log(n)
# duplicates = []
# for name in names_2: # O(m)
#     if(name_tree.contains(name.lower())):
#         duplicates.append(name) # log(n)


# DICT SOLUTION

# names = {}
# for name in names_1:
#     if(not name in names):
#         names[name] = True
# duplicates = []
# for name in names_2:
#     if(name in names):
#         duplicates.append(name)

# Stretch Solution

def insert_index(arr, name):
    if(not len(arr) or name < arr[0]):
        return 0
    elif(name > arr[len(arr)-1]):
        return len(arr)
    start = 0
    end = len(arr)-1
    while(True):
        half = round((start + end) / 2)
        if(arr[half] > name and arr[half-1] < name):
            return half
        elif(arr[half]<name and arr[half+1] > name):
            return half + 1
        elif(arr[half] > name):
            end = half
        elif(arr[half] < name):
            start = half

def find_name(arr, name):
    if(not len(arr) or name < arr[0] or name > arr[len(arr)-1]):
        return False
    start = 0
    end = len(arr)-1
    while(True):
        half = round((start + end) / 2)
        if((arr[half] > name and arr[half-1] < name) or (arr[half] < name and arr[half+1] > name)):
            return False
        elif(arr[half] == name):
            return True
        elif(arr[half] > name):
            end = half
        elif(arr[half] < name):
            start = half

name_list = []
for name in names_1:
    if(not name in name_list):
        if(not len(name_list)):
            name_list.append(name.lower())
        else:
            index = insert_index(name_list, name.lower())
            if(index > len(name_list)-1):
                name_list.append(name.lower())
            else:
                name_list.insert(index, name.lower())

duplicates = []
for name in names_2:
    if(find_name(name_list, name.lower())):
        duplicates.append(name)


    
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

