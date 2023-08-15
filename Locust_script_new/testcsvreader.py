import random
import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from utility.readCsvFile import ReadCsvFile

data_folder = os.path.join(root_dir, "data")
file_path = os.path.join(data_folder, "credential.csv")


class printValue:
    def printva(self):
        reader = ReadCsvFile(file_path).reader()
        print(reader)
        randomval = random.choice(reader)
        print(randomval["username"])
        print(randomval["password"])


val = printValue()
val.printva()
