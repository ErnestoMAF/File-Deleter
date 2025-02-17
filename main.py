import os
from seeder import seeder

def delete_by_extension(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = file.split('.')[1]
            if file_extension in extensions:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file}")
                except Exception as e:
                    print(f"Can't delete file: {file}: {e}")

if __name__ == "__main__":
    dir = './Test'
    extensions = ("log", "jpg", "txt", "png", "xlsx")  # Cambia esto por las extensiones que desees eliminar

    """ONLY USE FOR DEMO DATA (FILES AND FOLDERS)"""
    #seeder(dir, ["log", "jpg", "txt", "png", "xlsx"])

    delete_by_extension(dir, extensions) 