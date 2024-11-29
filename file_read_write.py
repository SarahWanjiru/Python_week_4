def read_and_write(input_file, output_file):
    try:
        # Read content from the input file
        with open(input_file, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Example usage
input_file = "README.md"
output_file = "output.txt"
read_and_write(input_file, output_file)
