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



#get molar mass (option 1 - all in one function)
def molarMass(formula):
    periodicTable = getElementDict()
    mass = 0
    element = ""
    number = ""
    while formula != "" or element != "":
        if element == "":
            element = formula[0]
            formula = formula[1:]

        elif formula != "" and element != "" and formula[0] in string.ascii_lowercase:
            element = element + formula[0]
            formula = formula[1:]
        
        else:
            while formula != "" and formula[0] in string.digits:
                number = number + formula[0]
                formula = formula[1:]
            if number == "":
                number = 1
            else:
                number = int(number)
            mass += float(periodicTable[element][1])*number
            number = ""
            element = ""
    return mass




#get molar mass (option 2 - split into multiple functions)

#get mass of a unit with just the element name and number
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

#break large formula into smaller formula units consisting of just the element and number
def getUnits(formula):
    elements = []
    while formula != "":
        new_element = formula[0]
        formula = formula[1:]
        while formula != "":
            if formula[0] not in string.ascii_uppercase:
                new_element += formula[0]
                formula = formula[1:]
            else:
                break
        elements.append(new_element)
    return elements


#call other functions to get molar mass
def molarMass1(formula):
    #slice formula into elements and their corresponding numbers
    elements = getUnits(formula)
    print(elements)
    #get the mass for each slice and add them together
    total_mass = 0
    for item in elements:
        mass = unitMass(item)
        total_mass += mass
    #return the total mass
    return total_mass

#get elemental composition of formula
def elementalComposition(formula):
    periodicTable = getElementDict()
    elements = getUnits(formula)
    total_mass = molarMass1(formula)
    print(f"The elemental composition of {formula} is:")

    #make dictionary to ensure that each element is partitioned correctly
    masses = {}
    for item in elements:
        name,mass = periodicTable[item.strip(string.digits)]
        mass = float(mass)
        if item.strip(string.ascii_letters) == "":
            number = 1
        else:
            number = int(item.strip(string.ascii_letters))
        mass = mass * number
        if name in masses:
            masses[name] += mass
        else:
            masses[name] = mass
    
    #find what percent of the total mass each element is and use percents to check with assert statements
    percents = []
    for key in masses:
        percent = masses[key]*100 / total_mass
        print(f"{percent:.4f}% {key}")
        percents.append(int(percent))
    return percents






#Test functions using data from a chem textbook
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
    assert periodicTable["Hg"][0] == "Mercury"

    #Test molarMass function:
    assert int(molarMass("NaCl")) == 58
    assert int(molarMass("H2O")) == 18
    assert int(molarMass("H2SO4")) == 98
    assert int(molarMass("C6H12O6")) == 180
    assert int(molarMass("C2H5OH")) == 46
    assert int(molarMass("C3H8")) == 44

    #Test molarMass1 function:
    assert int(molarMass1("NaCl")) == 58
    assert int(molarMass1("H2O")) == 18
    assert int(molarMass1("H2SO4")) == 98
    assert int(molarMass1("C6H12O6")) == 180
    assert int(molarMass1("C2H5OH")) == 46
    assert int(molarMass1("C3H8")) == 44

    #Test elementalComposition function:
    assert elementalComposition("NaCl") == [39,60]
    assert elementalComposition("H2O") == [11,88]
    assert elementalComposition("H2SO4") == [2,32,65]
    assert elementalComposition("C9H8O4") == [60,4,35]
    assert elementalComposition("C6H12O6") == [40,6,53]
    assert elementalComposition("C2H5OH") == [52,13,34]
    assert elementalComposition("Fe2O3") == [69,30]
    assert elementalComposition("C3H8") == [81,18]

    print("All assertions are correct")

test()




