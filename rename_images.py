import traceback
import pathlib
import time
import os

def main():

    valid_extensions = [".png", ".NEF", ".jpg"]

    print("\n\n\nTHIS SCRIPT IS AUTHORIZED BY SAM KHODAK. DO NOT RUN ANY OTHER UNKNOWN SCRIPTS ON YOUR PC.")
    print("\nBEFORE RENAMING, MAKE A BACKUP COPY OF THIS FOLDER WITH IMAGES. THEN DELETE IF EVERYTHING LOOKS FINE.\n\n\n")

    time.sleep(3)

    print("\nThis script will take the jpg/png images and NEF files in your current directory and rename them with a certain prefix, keeping the number suffix.")
    file_prefix = input("\n\nWhat would you like the prefix to be? Enter it now, then press enter:  ")

    confirmation = input(f"\n\nWARNING: This will rename all of your jpg/png/NEF files to {file_prefix}_num.extension. Would you like to continue? Enter \"yes\":  ")
    if (confirmation != "yes"):
        print("\n\nYou did not enter yes. Goodbye!\n\n")
        return

    for filename in os.listdir("."):
        conditions_to_check = [
            os.path.isfile(filename),
            pathlib.Path(filename).suffix in valid_extensions
        ]

        if (all(conditions_to_check)):
            try: 
                extension = pathlib.Path(filename).suffix
                print(f"filename: {filename}, extension: {extension}")

                # Get number suffix and extension from DSC_000.extension file.
                after_underscore = filename.split('_')

                # If no underscore, leave the filename the same.
                if (len(after_underscore) <= 1):
                    new_filename = filename
                else:
                    new_filename = f"{file_prefix}_{after_underscore[-1]}"

                print(f"New filename: {new_filename}")
                os.replace(filename, new_filename)
            except Exception:
                traceback.print_exc()


if __name__ == "__main__":
    main()