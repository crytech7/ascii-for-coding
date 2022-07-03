inp = open("stylish-capybara", "r")

for line in inp:
    if line != '\n':
        print('message("' + line[20:-20] + '")')
        # print(line[40:-40])
