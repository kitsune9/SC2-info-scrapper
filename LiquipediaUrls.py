# urls for pages

####################################
#   Buildings

buildingInput = open("buildings.txt", 'r')
buildingOutput = open("buildingUrls.txt", 'w')

for line in buildingInput:
    unitName = line.strip("\n")
    unitName = unitName.strip()
    unitName = "_".join(unitName.split(" "))





    str = "http://liquipedia.net/starcraft2/" + unitName + "_(Legacy_of_the_Void)\n"
    buildingOutput.write(str)






buildingOutput.close()
buildingInput.close()



####################################
#   units

unitInput = open("units.txt", 'r')
unitOutput = open("unitUrls.txt", 'w')

for line in unitInput:
    unitName = line.strip("\n")
    unitName = unitName.strip()
    unitName = "_".join(unitName.split(" "))


    str = "http://liquipedia.net/starcraft2/" + unitName + "_(Legacy_of_the_Void)\n"
    unitOutput.write(str)


unitInput.close()
unitOutput.close()

