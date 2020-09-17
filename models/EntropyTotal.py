from models.Infor.IndividualInfor import nodeInformationentropy


def entropyTotal(tree):
    entropyTotal = 0
    for i in tree.index:
        entropyTotal = entropyTotal + nodeInformationentropy(i, tree)
    return entropyTotal
