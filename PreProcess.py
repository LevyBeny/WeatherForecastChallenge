import pandas as pd
import numpy as np
import datetime as dt


# date parser for reading the data as datetime objects
def _date_parser(string):
    return dt.datetime.strptime(string, "%d/%m/%Y")


def read_data(dir_path, file_name):
    parse_dates = ['Basis_date', 'Validity_date']

    data = pd.read_csv(dir_path + "/" + file_name, parse_dates=parse_dates,
                       date_parser=_date_parser)
    data.set_index()

def merge_time1_time2(data):
    columns_names = list(data)
    columns_to_remove=['Time','Basis_date','Validity_date','City']

    new_data = pd.DataFrame()
