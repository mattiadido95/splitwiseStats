def getMonth(date):
    tokens = date.split("/")
    return tokens[1]

def getYear(date):
    tokens = date.split("/")
    return tokens[2]
