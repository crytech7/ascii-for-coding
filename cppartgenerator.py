inp = open("stylish-capybara-v2", "r")

for line in inp:
    print('message("' + line[3:-3] + '")')
