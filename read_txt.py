file = open("podval.txt", 'r')
datelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

instruments = dict(EURO='EURO FX FUT', BRIT='BRIT PND FUT', SWISS='SWISS FRNC FUT', CANAD='CANADA DLR FUT',
                   JAPAN='JAPAN YEN FUT', GC='GC FUT', CL='CL FUT', SP='EMINI S&P FUT')

EURO = open('EURO FX FUT.txt', 'w')
BRIT = open('BRIT PND FUT.txt', 'w')
SWISS = open('SWISS FRNC FUT.txt', 'w')
CANAD = open('CANADA DLR FUT.txt', 'w')
JAPAN = open('JAPAN YEN FUT.txt', 'w')
GC = open('GC FUT.txt', 'w')
CL = open('CL FUT.txt', 'w')
SP = open('EMINI S&P FUT.txt', 'w')

while True:
    str = file.readline()

    if "Дата" in str:
        if "FINAL" in str:
            statusstr = "FINAL"
        else:
            statusstr = "PRELIM"
        datestr = ""
        for c in str:
            if c in datelist:
                datestr += c
        EURO.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        BRIT.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        SWISS.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        CANAD.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        JAPAN.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        GC.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        CL.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')
        SP.write(datestr + '\t' + statusstr + '\t' + "TOTAL" + '\t')

    for key, value in instruments.items():
        if value in str:
            str1 = str.split(':')[1]
            str_split = str1.split(',')
            print(str_split)
            globals()[key].write(str_split[-3] + '\t')
            for i in range(0, len(str_split) - 5, 3):
                name = str_split[i]
                print(name)
                name = name[0] + name[1] + name[2] + ' ' + name[3] + name[4]
                globals()[key].write(name + '\t' + str_split[i + 1] + '\t')
            globals()[key].write('\n')

    if not str:
        break