def listNum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listNum(numList[1:])

        