LEAD = "CA"
MSB_FORMAT = "00"
LSB_FORMAT = "01"
CHECKSUM_LEAD_TAG = LEAD + MSB_FORMAT + LSB_FORMAT

def checksum(data):
    storedData = " ".join("{:02X}".format(ord(c)) for c in data)
    splitData = storedData.split()
    hexData = []
    toReturn = CHECKSUM_LEAD_TAG + "%02X" % int(hex(len(splitData)), 16)
    for i in splitData:
        hexData.append(int(i, 16))
        toReturn += "%s" % i
    addedData = 0x00 + 0x01 + int(hex(len(splitData)), 16)
    for x in hexData:
        addedData += x
    if(addedData > 0xFF):
        addedData %= 0x100
    xorData = hex(addedData ^ 0xFF)
    toReturn += "%02X" % int(xorData, 16)
    return toReturn

def compare(cs1, cs2):
    if(len(cs1) == len(cs2)):
        for i in range(0, len(cs1)):
            if(cs1[i] != cs2[i]): return False
        return True
    return False

def main():
    testData = "Bye"
    cs = "CC000103427965DB"
    cs2 = checksum(testData)
    if(compare(cs, cs2)):
        print("True")
    else:
        print("False")

main()
