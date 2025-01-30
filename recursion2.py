def countItemsRecursively(items):
    if len(items) == 0:
        return 0
    items.pop()
    return 1+ countItemsRecursively(items)

items = [{},{},{},{},{}]
result = countItemsRecursively(items)
print(f"result: {result}")