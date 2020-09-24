from os import listdir


def get_files(directory):
    return [name for name in listdir(directory) if name[:1] != "." and name[:2] != "__" and name != "_DS_Store"]
