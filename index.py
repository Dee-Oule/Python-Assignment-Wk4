def read_and_modify_file(input_filename, output_filename):
    try:
        # Attempt to open and read the input file
        with open(input_filename, "r") as infile:
            # Read the contents of the file
            content = infile.readlines()
        
        # Modify the content (example: make all text uppercase)
        modified_content = [line.upper() for line in content]
        
        # Write the modified content to the output file
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)
        
        print(f"File has been successfully modified and saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read/write to the file(s). Please check the permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompting the user for input and output filenames
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")

# Call the function with user inputs
read_and_modify_file(input_file, output_file)
