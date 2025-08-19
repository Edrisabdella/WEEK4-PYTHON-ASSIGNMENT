# File Handling and Exception Handling Assignment
# Author: Edris Abdella
# Date: August 2025

def file_read_write():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the filename to read: ").strip()
        
        # Open and read file
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = "modified_" + input_filename
        
        # Write modified content to new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"✅ File has been successfully read and modified version saved as '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don’t have access to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run program
if __name__ == "__main__":
    file_read_write()
