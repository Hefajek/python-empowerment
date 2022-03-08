def get_tree_height():
    TREE_HEIGHT = int(input("Podaj wysokość choinki: "))
    while TREE_HEIGHT <= 0:
        print("Nie możesz wydrukować samego pnia!")
        TREE_HEIGHT = int(input("Podaj wysokość choinki: "))
    return TREE_HEIGHT

def print_tree(TREE_HEIGHT):
    incisions = TREE_HEIGHT - 1
    branches = 1
    for height in range(TREE_HEIGHT):
        line = ''
        line = line + line.join(" ")*incisions
        line = line + line.join("*")*branches
        print(line)
        branches += 2
        incisions -= 1
    trunk_incisions = TREE_HEIGHT-1
    line = ''
    for trunk in range(2):
        line = line + line.join(" ")*trunk_incisions
        line = line + line.join('*')
        print(line)
        line = ''


while True:
    try:
        TREE_HEIGHT = get_tree_height()
        print_tree(TREE_HEIGHT)
        break
    except:
        print("Musisz podać LICZBĘ (większą od 0)!")

