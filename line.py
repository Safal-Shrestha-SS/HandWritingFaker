f = open("content.txt", "r")
g = open("demofile3.txt", "w")
fPosition = 0
store = f.read()
f.seek(0)
for index, s in enumerate(f):
    character = 0
    hell = s.strip()
    check = len(s)
    for i, c in enumerate(hell):
        if (check < 35):
            g.write(c)
            if(i == check-2):
                g.write("\n")
        else:
            if(character < 50):
                g.write(c)
                character += 1
            else:
                if(hell[i] == ' ' or store[fPosition+2] == ' '):
                    g.write(c+"\n")
                else:
                    g.write(c+"-\n")
                character = 0
        print(hell[i]+'  '+store[fPosition+1])
        fPosition += 1
    g.write('\n')


f.close()
g.close()
