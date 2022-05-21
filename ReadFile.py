with open("Excel_data_Libre_file.csv") as f:
    line = f.readlines()
    for li in line:
        print(li.split(",")[0])
f.close()

# only in branch
