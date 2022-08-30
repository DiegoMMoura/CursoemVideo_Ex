so = 0
co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        so += c
        co += 1
print(f'The result of all of the {co} numbers are {so}.')
