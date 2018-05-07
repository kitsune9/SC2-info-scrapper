from bs4 import BeautifulSoup

from urllib.request import urlopen







def writeResults(txt):
    txt = txt.strip()

    txt = str(lineCounter) + "     " + txt
    textFile.write(txt)

textFile = open("textFile.txt", 'w')
lineCounter = 0

urlList = ["http://liquipedia.net/starcraft2/Marine_(Legacy_of_the_Void)",
           "http://liquipedia.net/starcraft2/Banshee_(Legacy_of_the_Void)",
           "http://liquipedia.net/starcraft2/Bunker_(Legacy_of_the_Void)",
           "http://liquipedia.net/starcraft2/Starport_(Legacy_of_the_Void)"]

for urlAddress in urlList:
    page = urlopen(urlAddress)
    print("######################################################")
    i = 0



    soup = BeautifulSoup(page, 'html.parser')

    name_box = soup.findAll("div", attrs="infobox-cell-2")
    for name in name_box:
        i += 1

    for number in range(0, i):
        writeResults(name_box[number].text)



#textFile.write(soup.get_text())




textFile.close()




