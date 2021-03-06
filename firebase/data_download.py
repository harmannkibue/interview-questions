import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from openpyxl import Workbook
from dotenv import load_dotenv

load_dotenv()


def initialize_credentials():
    """
    Initialization for google cloud console
    :return:
    """
    # initializations
    key_file = os.getenv("KASHPOA_CREDENTIALS")
    cred = credentials.Certificate(key_file)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def quickstart_get_collection():
    db = initialize_credentials()
    emp_ref = db.collection('users')
    docs = emp_ref.stream()
    return docs


# Todo: To be worked on. 1.Add the upper alphabet list
def set_headers(sheet, header_names: list):
    header_value = ["A""Z"]

    for i in range(len(header_names)):
        header_anotation = header_value[i] + str(i+1)
        sheet[header_anotation] = header_names[i]
    return sheet


def write_xls_file():
    print("FUnction called")
    docs = quickstart_get_collection()
    workbook = Workbook()
    sheet = workbook.active

    # Todo: To be passed
    sheet = set_headers(sheet, ["NAME", "EMAIL", "PHONE", "LOCATION"])

    row = 2
    for doc in docs:
        print("Function Called>>>>><<<<")
        dict_data = doc.to_dict()
        sheet[f"A{row}"] = str(dict_data.get("name"))
        sheet[f"B{row}"] = str(dict_data.get("email"))
        sheet[f"C{row}"] = str(dict_data.get("phone"))
        sheet[f"D{row}"] = str(dict_data.get("location"))
        row += 1
    workbook.save("kashpoa_cleaned_data.xlsx")
    print("Success>>>>>>>")
    return None


print(write_xls_file())
