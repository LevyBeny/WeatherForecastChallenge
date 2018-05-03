import PreProcess as preproc
import os
train_dir = "./data/train"
test_dir = "./data/test"

data_names = ["humidity", "maxTemp","minTemp","wind"]

all_sets=[]

data = preproc.read_data(train_dir, "train_Humidity.csv")
all_sets.append(preproc.merge_time1_time2(data,"humidity"))

data = preproc.read_data(train_dir, "train_minTemp.csv")
all_sets.append(preproc.merge_time1_time2(data,"minTemp"))

data = preproc.read_data(train_dir, "train_maxTemp.csv")
all_sets.append(preproc.merge_time1_time2(data,"maxTemp"))

data = preproc.read_data(train_dir, "train_Wind.csv")
all_sets.append(preproc.merge_time1_time2(data,"Wind"))

merged = preproc.merge_data(all_sets[0], all_sets[1])
for i in range(2,len(all_sets)):
    merged = preproc.merge_data(merged,all_sets[i])

