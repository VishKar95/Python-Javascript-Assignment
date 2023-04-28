n = input("Enter the number of elements: ")
elements = []

for i in range(n):
    element = input("Enter an element: ")
    elements.append(element)


elements.sort(key=lambda x: x[-2])

print("Sorted list:", elements)
