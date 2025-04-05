def read_and_modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content - here we make it uppercase as an example
        modified_content = content.upper()

        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Could not read from '{input_file}' or write to '{output_file}'.")

# Ask the user for filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the new file to write to: ")

read_and_modify_file(input_filename, output_filename)
