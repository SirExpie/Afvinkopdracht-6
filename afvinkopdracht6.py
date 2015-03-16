
def main():
<<<<<<< HEAD
    bestand = "sequence.gb"
    text = gettext(bestand)
    cds = getcds(text)
=======
    bestand = open("sequentie.gbk", "r")
    cds = gettext(bestand)
>>>>>>> f2852890ee6ea48ee8b40457dcc2f505e5ca1f93
    gcPercentage(cds)
    print("GC percentage: ", gcPercentage(cds))

def gettext(bestand):
    read = False
    cds = ""
    for regel in bestand :
        if "ORIGIN" in regel :
            lijn = regel.replace(" ","").replace("ORIGIN","").replace("\n","")
            print ("test")
## met deze line haal je alle spaties, en niet relevante letters en cijfers uit het bestand ##
        regel = regel.replace(" ","").replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("\n","")

## als read op True staat begint het te lezen.
## wanneer er "ORIGIN" wordt gelezen, wordt read op true gezet       
        if read == True :
            cds = cds + regel
            
        if "ORIGIN" in regel :
            read = True
       
    return cds


def gcPercentage (cds):
    gc = 0

    for a in cds.upper():
      if a in "GC":
        gc += 1

    return gc/len(cds)*100

main()
