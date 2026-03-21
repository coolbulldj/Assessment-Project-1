FILE_PATH = "saveData.txt"
SEPERATOR_KEY = " ;:; "

STRING_TO_BOOL = {
    "True" : True,
    "False" : False
}

# https://www.w3schools.com/python/python_file_open.asp source reference ()


def writeData(data):

    # file = open(FILE_PATH)

    # file.close()

    # Using the with open means file doesn't have to be closed
    with open(FILE_PATH, "w") as f: #uses w rather than a because w fully clears the file
        for key, val in data.items():
            f.write(key + SEPERATOR_KEY + str(val) + "\n") #\n create a new line

    # Read for debugging
    # with open(FILE_PATH) as f:
    #     print(f.read())
    testReturn = readData()


def attemptDataTypeConvertion(val):
    #attempt to convert to boolean
    if val in STRING_TO_BOOL:
        return STRING_TO_BOOL[val]

    #attempt to convert to int
    try:
        n = int(val)
        return n
    except ValueError:
        pass

    return val


def readData():
    data = {}

    with open(FILE_PATH) as f:
        for line in f:
            slicedLine = line.split(SEPERATOR_KEY)
            #print(slicedLine)
            key = slicedLine[0]
            val:str = slicedLine[1]
            val = val.replace("\n", "")


            # print(key, "key")
            # print(val, "val")
            data[key] = attemptDataTypeConvertion(val)
    
    return data


    

 
