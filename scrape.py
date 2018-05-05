from bs4 import BeautifulSoup

from urllib.request import urlopen


textFile = open("textFile.txt", 'w')


page = urlopen("http://starcraft.wikia.com/wiki/List_of_StarCraft_II_units")





soup = BeautifulSoup(page, 'html.parser')

print(soup.a)


#textFile.write(soup.get_text())




textFile.close()



