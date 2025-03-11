def remove(l,word):
    for item in l:
       l.remove(word)
       return l
        

l = ['sahil','sourav','karan','tinku','pankaj','subham']

print(remove(l,'sahil'))