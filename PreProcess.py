import pandas as pd
import numpy as np
import datetime as dt


# date parser for reading the data as datetime objects
def _date_parser(string):
    return dt.datetime.strptime(string, "%d/%m/%Y")


def read_raw_data(dir_path, file_name):
    parse_dates = ['Basis_date', 'Validity_date']

    data = pd.read_csv(dir_path + "/" + file_name, parse_dates=parse_dates,
                       date_parser=_date_parser)
    del data['Basis_date']
    return data


def read_merged_data(dir_path, file_name):
    parse_dates = ['Validity_date']

    data = pd.read_csv(dir_path + "/" + file_name, parse_dates=parse_dates,
                       date_parser=_date_parser)
    return data


def merge_time1_time2(data, data_name):
    columns_to_duplicate = list(data)
    columns_to_remove = ['Time', 'Validity_date', 'City', 'Persist_value_' + data_name]
    columns_common = ['Validity_date', 'City', 'Persist_value_' + data_name]
    for column in columns_to_remove:
        columns_to_duplicate.remove(column)

    duplicated = []
    for column in columns_to_duplicate:
        duplicated.append(column + "_1")
        duplicated.append(column + "_2")

    new_columns = ['Validity_date', 'City', 'Persist_value_' + data_name] + duplicated
    new_data = pd.DataFrame(columns=new_columns)

    for index, row in data.iterrows():
        new_row = {}
        instance_index = new_data.index[(new_data['City'] == row['City']) & (new_data['Validity_date'] == row['Validity_date'])]


        if len(instance_index) == 0:
            for column in columns_common:
                new_row[column] = row[column]

            for column in columns_to_duplicate:
                new_row[column + "_" + str(row["Time"])] = row[column]
            new_data = new_data.append(new_row, ignore_index=True)

        else:
            for column in columns_to_duplicate:
                new_data.at[instance_index,column + "_" + str(row["Time"])] = row[column]
    return new_data

def merge_data(data, to_add):
    common_columns = ['Validity_date', 'City']

    columns_to_append = list(to_add)
    for column in common_columns:
        columns_to_append.remove(column)

    data = data.sort_values(by=common_columns, axis=0)
    to_add = to_add.sort_values(by=common_columns, axis=0)
    to_add = pd.DataFrame(to_add[columns_to_append])
    return pd.concat([data, to_add], axis=1)