inp = open("pushkin-capybara", "r")

for line in inp:
    if line != '\n':
        print('message("' + line[10:-10] + '")')
