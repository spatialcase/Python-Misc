import csv
import re

# Script tp parse all the file formats that FME reads and write their
# file extensions out to a CSV file.
# The formats read by FME are provided for the formats.db file which
# lives in C:\Program Files\FME folder
# formats.db is actually a CSV file using a "|" delimiter.
# Thanks to redgeographics for the tip about this file.

formats_file = "C:/Temp/formats.db"
out_file = "C:/Temp/data_formats.csv"
csvData = []

def main():
    with open(formats_file) as csvfile:
        data_csv = csv.reader(csvfile, delimiter="|")

        for row in data_csv:
            # search for file extensions eg (*.dgn)
            ext = re.search("\(\*(\.[^)]+)\)", str(row))
            if ext:
                extensions_str = ext.group(0).strip('()')
                extensions = extensions_str.split(";")

                for extension in extensions:
                    extension = extension.replace("*","")

                    #csvrow = str(row[0] + ", " + row[1] + "," + extension)
                    #print(csvrow)
                    csvData.append([row[0], row[1], extension])

    write_output()

    print("Done.")

def write_output():
    myFile = open(out_file, 'w', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(csvData)


main()
