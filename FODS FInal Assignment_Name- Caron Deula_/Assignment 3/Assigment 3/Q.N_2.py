def copy_file(source_file, destination_file):
    """
    Copy the contents of the source file to the destination file.

    Args:
        source_file (str): Name of the file to copy from
        destination_file (str): Name of the file to copy to

    Returns:
        bool: True if copy was successful, False otherwise
    """
    try:
        # Open source file in read mode
        with open(source_file, 'r') as source:
            # Read the entire content
            content = source.read()

            # Open destination file in write mode
            with open(destination_file, 'w') as destination:
                # Write content to destination file
                destination.write(content)

            print(f"File copied successfully from '{source_file}' to '{destination_file}'")
            return True

    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied. Check if you have proper access rights.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    # Get filenames from user
    source = input("Enter the source filename: ")
    destination = input("Enter the destination filename: ")

    # Perform file copy operation
    copy_file(source, destination)


# Execute the main function when script is run
if __name__ == "__main__":
    main()