from bs4 import BeautifulSoup

from urllib.request import urlopen





def handleUnitPage(address):
    page = urlopen(address)
    print("######################################################")
    textFile.write("######################################################\n")
    i = 0
    count = 0

    soup = BeautifulSoup(page, 'html.parser')


    #############
    # unit name
    print(soup.find(id="firstHeading").contents[1].get_text())
    textFile.write(soup.find(id="firstHeading").contents[1].get_text() + "\n")

    name_box = soup.findAll("div", attrs="infobox-cell-2")



    ##########
    # line writer
    for name in name_box:
        writeResults(name.text, count)
        count += 1

def handleBuildingPage(address):
    page = urlopen(address)
    print("######################################################")
    textFile.write("######################################################\n")
    i = 0
    count = 0

    soup = BeautifulSoup(page, 'html.parser')
    print(soup.find(id="firstHeading").contents[1].get_text())
    textFile.write(soup.find(id="firstHeading").contents[1].get_text() + "\n")

    name_box = soup.findAll("div", attrs="infobox-cell-2")

    ##########
    # line writer
    for name in name_box:
        writeResults(name.text, count)
        count += 1
        if(count > 3):
            break

def writeResults(txt, lineCounter):
    txt = txt.strip()

    txt = str(lineCounter) + "     " + txt + "\n"
    textFile.write(txt)


textFile = open("textFile.txt", 'w')


unitUrlList = open("unitUrls.txt", 'r')
buildingUrlList = open("buildingUrls.txt", 'r')



for urlAddress in unitUrlList:
    handleUnitPage(urlAddress)

for urlAddress in buildingUrlList:
    handleBuildingPage(urlAddress)

print()
print()
print("######################################################")
print("######################################################")
print("  SUCCESS")
print("######################################################")
print("######################################################")


unitUrlList.close()
buildingUrlList.close()
textFile.close()




