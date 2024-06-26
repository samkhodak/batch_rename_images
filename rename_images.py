import traceback
import pathlib
import time
import os

VALID_EXTENSIONS = [".PNG", ".NEF", ".JPG", ".JPEG"]

def gather_changes(file_prefix: str) -> list[(str,str)]:
    """ Creates a list of matching files that are set to be changed, returning an array of old and new filenames.

    :param file_prefix: Prefix to prepend to old filename.
    :type file_prefix: str
    :return: List of (old_name, new_name) filename tuples.
    :rtype: List[(str,str)]
    """
    file_changes = []
    for filename in os.listdir("."):
        conditions_to_check = [
            os.path.isfile(filename),
            pathlib.Path(filename).suffix.upper() in VALID_EXTENSIONS
        ]

        if (all(conditions_to_check)):
            try: 
                # Get number suffix and extension from DSC_000.extension file.
                after_underscore = filename.split('_')

                # If no underscore, leave the filename the same.
                if (len(after_underscore) <= 1):
                    new_filename = filename
                else:
                    new_filename = f"{file_prefix}_{after_underscore[-1]}"

                file_changes.append((filename, new_filename))
            except Exception:
                traceback.print_exc()
        
    return file_changes

def display_changes(file_changes: list[(str,str)]) -> None:
    """ Displays all of the potential file renamings from the list passed in.

    :param file_changes: List of (old_name, new_name) tuples.
    :type file_changes: list[(str,str)]
    """
    num_files = len(file_changes)

    print(f"\n\n\nDisplaying a list of potential changes.... ({num_files} files) \n\n\n")
    time.sleep(2)

    for file, new_file in file_changes:
        print(f"Old filename: {file}\t\tNew filename: {new_file}\n")



def main():


    print("\n\n\nTHIS SCRIPT IS AUTHORIZED BY SAM KHODAK. DO NOT RUN ANY OTHER UNKNOWN SCRIPTS ON YOUR PC.")
    print("\nBEFORE RENAMING, MAKE A BACKUP COPY OF THIS FOLDER WITH IMAGES. THEN DELETE IF EVERYTHING LOOKS FINE.\n\n\n")

    time.sleep(3)

    print("\nThis script will take the jpg/png images and NEF files in your current directory and rename them with a certain prefix, keeping the number suffix.")
    file_prefix = input("\n\nWhat would you like the prefix to be? Enter it now, then press enter:  ")


    file_changes = gather_changes(file_prefix)
    display_changes(file_changes)

    confirmation = input(f"\n\nWARNING: This will rename all of the previously displayed files. Proceed with renaming? Enter \"yes\":  ")
    if (confirmation != "yes"):
        print("\n\nYou did not enter yes. Goodbye!\n\n")
        return

    for filename, new_filename in file_changes:
        os.replace(filename, new_filename)

    print("\n\nSuccessfully renamed. Have a good day.\n\n")
 


if __name__ == "__main__":
    main()