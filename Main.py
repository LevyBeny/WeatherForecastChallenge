import PreProcess as preproc

train_dir = "./data/train"
test_dir = "./data/test"

file_name = "train_Humidity.csv"

preproc.read_data(train_dir,file_name)
