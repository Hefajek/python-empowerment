def get_tree_pieces(height):
  pieces = []
  full_width = height * 2 - 1
  for level in range(1, height + 1):
    asterix_multiplier = int(level * 2 - 1)
    space_multiplier = int((full_width - asterix_multiplier) / 2)
    pieces.append((' ' * space_multiplier) + ('*' * asterix_multiplier) + (' ' * space_multiplier))
  else:
    space_multiplier = int((full_width - 1) / 2)
    pieces.append(' ' * space_multiplier + '*' + ' ' * space_multiplier)
    pieces.append(' ' * space_multiplier + '*' + ' ' * space_multiplier)

  return pieces

def connect_tree(splited_tree):
  return '\n'.join(splited_tree)

def main():
  height = int(input("Put height of the christmas tree: "))

  if height < 1:
    raise ValueError("Height can't be lower then 1")

  splited_tree = get_tree_pieces(height)
  connected_tree = connect_tree(splited_tree)
  print(connected_tree)

if __name__ == "__main__":
  try:
    main()
  except ValueError as error:
    print(error)
