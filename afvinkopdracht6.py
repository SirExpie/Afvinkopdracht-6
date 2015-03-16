def main():
    file="C:\Users\Patrick\Afvinkopdracht-6\sequence.gb"
    text = gettext(file)
    cds = getcds(text)
    gcPercentage(cds)
    print("GC percentage: ", gcPercentage(seq))

def gettext() :
    read = False
    cds = ""
    for regel in bestand :
        bestand.readline()
        if "ORIGIN" in regel :
            lijn = regel.replace(" ","").replace("CDS","").replace("\n","")
            global begin
            global eind
            begin,eind = lijn.split("..")
           
## met deze line haal je alle spaties, en niet relevante letters en cijfers uit het bestand ##
        regel = regel.replace(" ","").replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("\n","")

## als read op True staat begint het te lezen.
## wanneer er "ORIGIN" wordt gelezen, wordt read op true gezet       
        if read == True :
            cds = cds + regel
            
        if "ORIGIN" in regel :
            read = True
       
    return cds

# deze functie zorgt ervoor dat je alleen de CDS krijgt
def getcds(t):
    return t[int(begin):int(eind)]   

def gcPercentage (cds):
    gc = 0

    for a in cds.upper():
      if a in "GC":
        gc += 1

    return gc/len(cds)*100

