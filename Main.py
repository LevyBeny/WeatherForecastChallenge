import PreProcess as preproc
import os

train_dir = "./data/train"
test_dir = "./data/test"

data_names = ["humidity", "maxTemp", "minTemp", "wind"]

all_sets = []

# merge time_1 and time_2 for all sets
# for data_name in data_names:
#     data = preproc.read_raw_data(train_dir, "train_"+data_name+".csv")
#     all_sets.append(preproc.merge_time1_time2(data,data_name))
#     all_sets[-1].to_csv("train_"+data_name+"_merged.csv")


# create one data set
for data_name in data_names:
    data = preproc.read_merged_data(train_dir, "train_" + data_name + "_merged.csv")
    all_sets.append(data)

merged = preproc.merge_data(all_sets[0], all_sets[1])
for i in range(2, len(all_sets)):
    merged = preproc.merge_data(merged, all_sets[i])

merged.to_csv("train_merged.csv")

# merge time_1 and time_2 for all sets
# for data_name in data_names:
#     data = preproc.read_raw_data(test_dir, "test_"+data_name+".csv")
#     data.sort_values(['Validity_date', 'City'])
#     all_sets.append(preproc.merge_time1_time2(data,data_name))
#     all_sets[-1].to_csv("test_"+data_name+"_merged.csv")

# data = preproc.read_raw_data(train_dir, "train_minTemp.csv")
# data = preproc.merge_time1_time2(data, "minTemp")

# # create one data set
# for data_name in data_names:
#     data = preproc.read_merged_data(test_dir, "test_" + data_name + "_merged.csv")
#     all_sets.append(data)
#
# merged = preproc.merge_data(all_sets[0], all_sets[1])
# for i in range(2, len(all_sets)):
#     merged = preproc.merge_data(merged, all_sets[i])
#
# merged.to_csv("test_merged.csv")
