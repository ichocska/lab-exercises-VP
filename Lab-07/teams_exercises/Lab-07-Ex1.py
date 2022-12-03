def file_name(file_name):
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    file_content = f.read()
    f.close()
    return file_content


try:
    file_name('file_name.txt')
except FileNotFoundError as err:
    print(err)
