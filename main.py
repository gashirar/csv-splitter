import csv
import sys

args = sys.argv
argc = len(args)

if (argc < 3):
    print("Usage: # python3 %s [input] [output] [column1] [column2] ..." % args[0])
    quit()

with open(args[1]) as input:
    reader = csv.DictReader(input, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    with open(args[2], "w") as output:
        writer = csv.DictWriter(output, fieldnames=args[3:])
        writer.writeheader()
        for row in reader:
            print({key:value for key,value in row.items() if key in args[3:]})
            writer.writerow({key:value for key,value in row.items() if key in args[3:]})
