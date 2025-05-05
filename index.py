def modify_file_content(content):
    """
    Modifies the content of the file.
    For this example, we'll:
    1. Convert the text to uppercase
    2. Add line numbers
    3. Add a header and footer
    """
    lines = content.split('\n')
    modified_lines = []

    # Add header
    modified_lines.append("=" * 50)
    modified_lines.append("MODIFIED FILE CONTENT")
    modified_lines.append("=" * 50)
    modified_lines.append("")

    # Add line numbers and convert to uppercase
    for i, line in enumerate(lines, 1):
        if line.strip():  # Skip empty lines for numbering
            modified_lines.append(f"LINE {i}: {line.upper()}")
        else:
            modified_lines.append(line)  # Keep empty lines as they are

    # Add footer
    modified_lines.append("")
    modified_lines.append("=" * 50)
    modified_lines.append("END OF MODIFIED CONTENT")
    modified_lines.append("=" * 50)

    return '\n'.join(modified_lines)

def main():
    print("File Read & Write Challenge with Error Handling")
    print("=" * 40)

    # Ask for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Generate output filename based on input filename
        if '.' in input_filename:
            # Insert 'modified' before the file extension
            base_name = input_filename.rsplit('.', 1)[0]
            extension = input_filename.rsplit('.', 1)[1]
            output_filename = f"{base_name}_modified.{extension}"
        else:
            # If no extension, just append '_modified'
            output_filename = f"{input_filename}_modified"

        # Ask if user wants to use a different output filename
        print(f"Default output filename: {output_filename}")
        custom_output = input("Enter a different output filename (or press Enter to accept default): ")

        if custom_output.strip():
            output_filename = custom_output

        # Modify the content
        modified_content = modify_file_content(content)

        # Write the modified content to the output file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
            print(f"\nSuccess! Modified content written to '{output_filename}'")
        except IOError as e:
            print(f"\nError writing to file '{output_filename}': {e}")

    except FileNotFoundError:
        print(f"\nError: File '{input_filename}' not found. Please check the filename and try again.")
    except PermissionError:
        print(f"\nError: You don't have permission to read '{input_filename}'.")
    except IOError as e:
        print(f"\nError reading file '{input_filename}': {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    print("\nProgram completed. Thank you for using the File Modifier!")

if __name__ == "__main__":
    main()
