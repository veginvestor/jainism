import os
import re

def get_file_number(filename):
    """Extract the number from the filename for sorting."""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def combine_files(input_folder, output_file):
    """Combine all text files in the input folder into a single output file, sorted by the number in the filenames."""
    # Get list of all text files in the input folder
    files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]
    
    # Sort files by the number in their filenames
    files_sorted = sorted(files, key=get_file_number)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, filename in enumerate(files_sorted):
            filepath = os.path.join(input_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as infile:
                # Write the contents of the file to the output file
                outfile.write(infile.read())
                
                # Add 5 newlines between files, except after the last file
                if i < len(files_sorted) - 1:
                    outfile.write('\n' * 5)
    
    print(f"Files combined into {output_file}")

if __name__ == "__main__":
    input_folder = "./16_8"  # Change to your input folder path
    output_file = "combined_output.txt"
    combine_files(input_folder, output_file)

