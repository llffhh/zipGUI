import zipfile
import pathlib

def zip(filepaths, dest_dir):
    destpath = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(destpath, "w") as file: 
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname = filepath.name)

if __name__ =="__main__":
    pass