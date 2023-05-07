def get_file_path(path: str):
    if isinstance(path, str):
        *pathFile, name_file, expansion = path.split("\\")
        return '\\'.join(pathFile), name_file, expansion
    else:
        print("Error path!")
        return None
