from os import walk
import GCampAnalysis

def listfiles(directory, extension):
    filelist = []
    for(dirpath, dirnames, filenames) in walk(directory):
        for f in filenames:
             if f.endswith(extension):
                 #print(dirpath+"/"+ f)
                 filelist.append(dirpath+"/" + f)
    return(filelist)

a = listfiles("./", "filtered_backward.tif")

for file in a:
    filename = file.split("./")[1].split("/")[0]
    GCampAnalysis.CalciumConc(file, filename)
