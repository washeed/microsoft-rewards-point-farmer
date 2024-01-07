def insert_single_quotes(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            # Read each line and enclose each word in single quotes
            lines = [f"'{line.strip()}'" for line in infile]

            # Join the lines with commas
            modified_content = ','.join(lines)

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Single quotes inserted and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found - {input_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_file_path = 'words_alpha.txt'  # Replace with the actual path to your input text file
output_file_path = 'output.txt'  # Replace with the desired path for the output text file

insert_single_quotes(input_file_path, output_file_path)
