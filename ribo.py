def read_count_file(dirc):
    import pandas as pd
    with open(dirc, 'r') as readFile:
        unique = int(next(readFile).split()[-1])
        total = int(next(readFile).split()[-1])
        next(readFile)
        seqList = [line.split() for line in readFile]
    return seqList, unique, total
