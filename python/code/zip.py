import zipfile

file = zipfile.ZipFile("file.zip", "r")

# list filenames
for name in file.namelist():
    print(name)

# list file information
for info in file.infolist():
    print(info.filename, info.date_time, info.file_size)
