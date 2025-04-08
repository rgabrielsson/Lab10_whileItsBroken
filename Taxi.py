#make_small_file
#PUlocation is index 7 and tipamount is index 13

# def make_small_file():
#     infile = open("yellow_tripdata_2018-01.csv", "r")
#     outfile = open("small-taxi.csv", "w")
#     for i in range(1000):
#         line = infile.readline()
#         outfile.write(line)
#     infile.close()
#     outfile.close()

# make_small_file()

#get the taxi data from the file and put it in a list
def get_taxi_data(file):
    infile = open(file, "r")
    infile.readline()
    infile.readline()
    taxi_data = []
    for line in infile:
        line = line.strip()
        line = line.split(",")
        PULocation = line[7]
        tipAmount = line[13]
        data = (PULocation, tipAmount)
        taxi_data.append(data)
    infile.close()
    return taxi_data

#make a dictionary of the average tip amount for each PULocation
def get_taxi_dict(file):
    taxi_data = get_taxi_data(file)
    taxi_dict = {}
    for data in taxi_data:
        PULocation = data[0]
        tipAmount = float(data[1])
        if PULocation not in taxi_dict:
            taxi_dict[PULocation] = []
            taxi_dict[PULocation].append(tipAmount)
        else:
            taxi_dict[PULocation].append(tipAmount)
    for key in taxi_dict:
        taxi_dict[key] = sum(taxi_dict[key])/len(taxi_dict[key])
    return taxi_dict

#make a dictionary of the taxi zone names and their IDs
def get_loc_names():
    infile = open("taxiZoneLookup.csv", "r")
    infile.readline()
    loc_names = {}
    for line in infile:
        line = line.strip()
        line = line.split(",")
        loc_names[line[0]] = line[1] + ", " + line[2] + ", " + line[3]
    infile.close()
    return loc_names

def main():
    taxi_dict = get_taxi_dict("yellow_tripdata_2018-01.csv")
    loc_names = get_loc_names()
    taxi_list = []
    for key in taxi_dict:
        loc, tip = key, taxi_dict[key]
        taxi_list.append((tip, loc_names[key]))
    taxi_list.sort()

    for i in range(20):
        print(taxi_list[-(1+i)][0], taxi_list[-(1+i)][1])

main()