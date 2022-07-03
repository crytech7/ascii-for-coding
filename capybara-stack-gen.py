img = open("angry-capybara", "r")
msg = open("asm-is-pain-2", "r")

img = img.read().split('\n')
msg = msg.read().split('\n')

delta = 3
for i in range(len(img)):
    if img[i] != '\n':
        # print( + line[:-20] )
        if (i > (len(img) - len(msg)) // 2 + delta and i < (len(img) + len(msg)) // 2 + delta):
            print(('message("' + (img[i][40:img[i].find('|')] + msg[i - (len(img) - len(msg)) // 2 - delta]).replace('\\', '\\\\').replace('"', '\\"')+ '")'))
        else:
            print('message("' + (img[i][40:img[i].find('|')]).replace('\\', '\\\\').replace('"', '\\"') + '")')


