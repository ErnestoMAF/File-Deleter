import os
import random
import string

def generate_random_name(length=8):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_file(directory, extension):
    """Create an empty file with a random name and the given extension in the specified directory."""
    filename = f"{generate_random_name()}.{extension}"
    with open(os.path.join(directory, filename), 'w') as file:
        pass  # Creates an empty file

def seeder(root_directory, extensions, min_subfolders=1, max_subfolders=2, min_files=1, max_files=3, max_depth=2, current_depth=0):
    """
    Recursively create a folder structure with random subfolders and files.
    
    Args:
        root_directory (str): The root directory where the structure will be created.
        extensions (list): List of file extensions to use for creating files.
        min_subfolders (int): Minimum number of subfolders to create in each folder.
        max_subfolders (int): Maximum number of subfolders to create in each folder.
        min_files (int): Minimum number of files to create in each folder.
        max_files (int): Maximum number of files to create in each folder.
        max_depth (int): Maximum depth of the folder structure.
        current_depth (int): Current depth in the folder structure (used for recursion).
    """
    # Create the root directory if it doesn't exist
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)

    # Generate a random number of subfolders
    num_subfolders = random.randint(min_subfolders, max_subfolders)
    for i in range(num_subfolders):
        subfolder_name = generate_random_name()
        subfolder_path = os.path.join(root_directory, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        # Generate a random number of files in the subfolder
        num_files = random.randint(min_files, max_files)
        for _ in range(num_files):
            extension = random.choice(extensions)  # Choose a random extension
            create_file(subfolder_path, extension)

        print(f"Created subfolder: {subfolder_path} with {num_files} files.")

        # If we haven't reached the maximum depth, create subfolders within this subfolder
        if current_depth < max_depth:
            seeder(
                subfolder_path,  # New root for recursion
                extensions,
                min_subfolders,
                max_subfolders,
                min_files,
                max_files,
                max_depth,
                current_depth + 1  # Increment the current depth
            )

    if current_depth == 0:
        print(f"Folder structure created at: {root_directory}")

# Example usage
if __name__ == "__main__":
    root_dir = "example_root"
    file_extensions = ["txt", "csv", "log"]
    seeder(root_dir, file_extensions)