def insert(root, key):
    if root is None:
        return {"key": key, "left": None, "right": None}
    else:
        if key < root["key"]:
            root["left"] = insert(root["left"], key)
        else:
            root["right"] = insert(root["right"], key)
    return root

def search(root, key):
    if root is None or root["key"] == key:
        return root
    if key < root["key"]:
        return search(root["left"], key)
    return search(root["right"], key)

# Example usage:
tree = None
keys = [5, 3, 7, 1, 4, 6, 8]

for key in keys:
    tree = insert(tree, key)

# Search for a key in the tree
result = search(tree, 4)
print(result)
