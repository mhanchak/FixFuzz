
def fixlen(data):
    fixstring = bytes(data).decode('utf-8')
    return fixstring.find("10=") - fixstring.find("35=")

def fixchecksum(data):
    fixstring = bytes(data).decode('utf-8')
    end = fixstring.find("10=")
    checksum=0
    for i in range (0, end):
        checksum += ord(fixstring[i])
    return "%03d" % (checksum % 256)
