###
# A program which calculates wether a tree can be cut down
#
tree_circumference = int(input("Enter tree circumference (in cm): "))
tree_cut = tree_circumference >= 150                   # <---- ??? if it was 50 as the task says then all trees would be cut down
print(f'Tree can be cut down: {tree_cut}')