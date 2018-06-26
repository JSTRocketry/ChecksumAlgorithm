def checksum(data):
    storedData = " ".join("{:02X}".format(ord(c)) for c in data)
    splitData = storedData.split()
    hexData = []
    for i in splitData:
        hexData.append(int(i, 16))
    cs = 0
    for x in hexData:
        cs ^= x
    toReturn = "{:02X}".format(cs)
    return toReturn

def compare(cs1, cs2):
    if(len(cs1) == len(cs2)):
        for i in range(0, len(cs1)):
            if(cs1[i] != cs2[i]): return False
        return True
    return False

def main():
    testData = "@{PA:56.2;TS:5000}@"
    chksum = "3E"
    dataCS = checksum(testData)
    print(dataCS)
    print(compare(chksum, dataCS))

main()
