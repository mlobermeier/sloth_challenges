def remove_virus(files):
    good= []
    part_files= files.split(" ")
    #print(part_files)
    bad_things= ["virus", "malware"]
    not_bad_things= ["antivirus", "notvirus"]
    for i in part_files:
         if bad_things[0] not in i and bad_things[1] not in i:
                good.append(i)
         if not_bad_things[0] in i or not_bad_things[1] in i:
                good.append(i)
         #print(good)
         res = " ".join(good)
         if res == "PC Files:":
               res += " Empty"
    print(res)
remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")  
remove_virus("PC Files: notvirus.exe, funnycat.gif") 
remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
remove_virus("PC Files: virus")