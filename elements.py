import string

def getElementDict():
    infile = open("elements.csv", 'r')
    elements = {}
    for line in infile:
        line = line.strip()
        line = line.split(",")
        data = []
        for item in line:
            data.append(item)
        elements[data[1]] = (data[2],data[3])
    infile.close()
    return elements


def molarMass(formula):
    periodicTable = getElementDict()
    mass = 0
    element = ""
    number = ""
    while formula != "" or element != "":
        if element == "":
            element = formula[0]
            formula = formula.replace(formula[0], "")

        elif formula != "" and element != "" and formula[0] in string.ascii_lowercase:
            element = element + formula[0]
            formula = formula.replace(formula[0], "")
        
        else:
            while formula != "" and formula[0] in string.digits:
                number = number + formula[0]
                formula = formula.replace(formula[0], "")
            if number == "":
                number = 1
            else:
                number = int(number)
            mass += float(periodicTable[element][1])*number
            number = ""
            element = ""
    return mass

print(molarMass("NaCl"))
print(molarMass("H2O"))
print(molarMass("H2SO4"))




def unitMass(formula):
    periodicTable = getElementDict()

    #seperate element name and number, and make sure that it doesn't break if no number is provided
    element = formula.strip(string.digits)
    if formula.strip(string.ascii_letters) == "":
        number = 1
    else:
        number = int(formula.strip(string.ascii_letters))

    #calculate and return mass
    mass = float(periodicTable[element][1])*number
    return mass

def getUnits(formula):
    elements = []
    while formula != "":
        new_element = formula[0]
        formula = formula.replace(formula[0],"")
        while formula != "":
            if formula[0] not in string.ascii_uppercase:
                new_element += formula[0]
                formula = formula.replace(formula[0],"")
            else:
                break
        elements.append(new_element)
    return elements



def molarMass1(formula):
    #slice formula into elements and their corresponding numbers
    elements = getUnits(formula)

    #get the mass for each slice and add them together
    total_mass = 0
    for item in elements:
        mass = unitMass(item)
        total_mass += mass

    #return the total mass
    return total_mass


print(molarMass1("NaCl"))
print(molarMass1("H2O"))
print(molarMass1("H2SO4"))


def elementalComposition(formula):
    periodicTable = getElementDict()
    elements = getUnits(formula)
    total_mass = molarMass(formula)
    print(f"The elemental composition of {formula} is:")
    for item in elements:
        name,mass = periodicTable[item.strip(string.digits)]
        mass = float(mass)
        if item.strip(string.ascii_letters) == "":
            number = 1
        else:
            number = int(item.strip(string.ascii_letters))
        mass = mass * number
        percent = mass*100 / total_mass
        print(f"{percent:.4f}% {name}")

elementalComposition("NaCl")
elementalComposition("H2O")
elementalComposition("H2SO4")


def test():
    #Test getElementDict function:
    periodicTable = getElementDict()
    assert periodicTable["H"][0] == "Hydrogen"
    assert periodicTable["He"][0] == "Helium"
    assert periodicTable["Li"][0] == "Lithium"
    assert periodicTable["Be"][0] == "Beryllium"
    assert periodicTable["B"][0] == "Boron"
    assert periodicTable["C"][0] == "Carbon"
    assert periodicTable["N"][0] == "Nitrogen"
    assert periodicTable["O"][0] == "Oxygen"
    assert periodicTable["F"][0] == "Fluorine"
    assert periodicTable["Ne"][0] == "Neon"

    #Test molarMass function:
    assert molarMass("NaCl") == 58.4428
    assert molarMass("H2O") == 18.01528
    assert molarMass("H2SO4") == 98.079
    assert molarMass("C6H12O6") == 180.156
    assert molarMass("C2H5OH") == 46.06844
    assert molarMass("C3H8") == 44.096





