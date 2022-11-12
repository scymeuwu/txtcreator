import os

fname = input("Vytvorte soubor [name.type] (example: file.txt): ")
_fname = fname

try:
    fcount = int(input("Zadejte kolik chcete souboru vytvorit: "))
except:
    raise ValueError("Zadana hodnota musi byt int")


for x in range (fcount):
    fname = _fname
    _list = fname.split(".")
    fname = [_list[0],x+1,".",_list[1]]

    newString =""

    for y in fname:
        newString+=str(y)
    fname = newString

    save_path = "soubory/"
    completeName = os.path.join(save_path, fname )        
    
    #Create file + Write in it
    f = open(completeName, 'a')
    text = input("Zadejte text do {0}: ".format(fname))
    f.write(text)
    f.close() #Close file
    




    
    








