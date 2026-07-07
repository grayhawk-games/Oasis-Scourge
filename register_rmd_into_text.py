import os
import glob

# Path to your worldbuilding notes folder
folder_path = r'C:\Apps\Git\Oasis-Scourge\rmd'
output_file = os.path.join(folder_path, 'Master_Worldbuilding_Document.txt')

# Finds all Rmd files in that directory
rmd_files = glob.glob(os.path.join(folder_path, '*.rmd'))

with open(output_file, 'w', encoding='utf-8') as outfile:
    for file_path in rmd_files:
        # FIXED: Changed .append to .write
        outfile.write(f"\n\n--- START OF FILE: {os.path.basename(file_path)} ---\n\n")
        with open(file_path, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())

print(f"Success! Upload the new file located at: {output_file}")