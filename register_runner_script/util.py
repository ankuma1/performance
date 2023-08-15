import os.path
import random
import string
import csv
import sys

from register_runner_script import buid_request


def build_partner_register_request():
    fisrtname = ''.join(random.choices(string.ascii_uppercase, k=5))
    lastname = ''.join(random.choices(string.ascii_uppercase, k=5))
    phone = ''.join(random.choices("5" + string.digits, k=9))
    buid_request.register.__init__(buid_request.register, 1, fisrtname, "WALKIN", lastname, phone)
    print(buid_request.register.to_dict(buid_request.register))
    return buid_request.register.to_dict(buid_request.register)


def read_csv_file(filepath):
    reader = csv.DictReader(open(filepath))
    data = []
    for element in reader:
        data.append(element)
    return data


def get_operator_credential():
    Root_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(Root_Dir)
    sys.path.append(Root_Dir)
    Data_folder = os.path.join(Root_Dir,"data")
    file_path = os.path.join(Data_folder,"credential.csv")
   # read_data = read_csv_file("/Users/anilkumar/PycharmProjects/Demo_Locust_Project/data/credential.csv")
    read_data = read_csv_file(file_path)
    return read_data

# build_partner_register_request()
