tree_height = int(input("Podaj wysokość choinki: "))
while tree_height <= 0:
    print("Nie możesz wydrukować samego pnia!") 
    tree_height = int(input("Podaj wysokość choinki: "))

incisions = tree_height - 1
levels = tree_height
level = 1
branches = 1
line = ''

for height in range(tree_height):
    line = ''
    for incision in range(incisions):
        line = line + line.join(" ")
    for branch in range(branches):
        line = line + line.join("")
    print(line)
    branches = branches + 2
    incisions = incisions - 1


trunk_incisions = tree_height-1
line = ''
for trunk in range(2):
    for trunk_incision in range(trunk_incisions):
        line = line + line.join(' ')
    line = line + line.join('') 
    print(line)
    line = ''