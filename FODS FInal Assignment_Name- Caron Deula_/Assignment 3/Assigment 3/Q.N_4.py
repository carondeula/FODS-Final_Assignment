'''
CSV File Reader and Display

This program reads a CSV file and displays its contents in a tabular format.
The program handles different column widths and properly aligns the data.
'''

import csv


def display_csv(filename):
    """
    Read a CSV file and display its contents in a tabular format.

    Args:
        filename (str): The name of the CSV file to read

    Returns:
        bool: True if file was read and displayed successfully, False otherwise
    """
    try:
        # Open the CSV file
        with open(filename, 'r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Read all rows
            rows = list(csv_reader)

            if not rows:
                print("The CSV file is empty.")
                return False

            # Determine the maximum width needed for each column
            col_widths = []
            for row in rows:
                # Extend col_widths if this row has more columns
                while len(col_widths) < len(row):
                    col_widths.append(0)

                # Update column widths based on current row
                for i, cell in enumerate(row):
                    col_widths[i] = max(col_widths[i], len(str(cell)))

            # Print header row
            print("\nCSV File Contents:")
            print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))

            # Print each row in tabular format
            for i, row in enumerate(rows):
                row_str = "| "
                for j, cell in enumerate(row):
                    if j < len(col_widths):
                        row_str += str(cell).ljust(col_widths[j]) + " | "
                print(row_str)

                # Print separator after header row
                if i == 0:
                    print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))

            print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            return True

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False
    except csv.Error as e:
        print(f"CSV Error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    # Get filename from user
    filename = input("Enter the CSV filename to display: ")

    # Display the CSV content
    display_csv(filename)


# Execute the main function when script is run
if __name__ == "__main__":
    main()