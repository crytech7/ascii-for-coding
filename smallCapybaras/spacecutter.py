inp = open("stylish-capybara-v2", "r")
for line in inp:
    if len(line) > 2:
        print("message(\"" + line[:-1] + "\")")
