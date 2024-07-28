import os
import re

def remove_checksums_from_file(input_file, debug_file):
    chunk_size = 0x4020  # 16,384 in hex
    checksum_size = 32

    with open(input_file, 'rb') as f:
        data = f.read()

    output_data = bytearray()
    offset = 0x4020
    start = 0

    with open(debug_file, 'w') as debug_f:
        while offset < len(data):
            debug_f.write(f"Processing chunk from {start} to {offset - checksum_size}\n")
            output_data.extend(data[start:offset - checksum_size])
            start = offset
            offset += chunk_size

        # Remove the last 32 bytes of the file
        output_data.extend(data[start:-checksum_size])
        debug_f.write(f"Removing last 32 bytes of the file\n")
        debug_f.write(f"Original file size: {len(data)} bytes\n")
        debug_f.write(f"Processed file size: {len(output_data)} bytes\n")

    return output_data

def process_folder(folder_path):
    pattern = re.compile(r'.*\.MPQ\.(\d{1,2})$')
    files_to_process = []

    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            files_to_process.append((int(match.group(1)), filename))

    # Sort files based on the numerical part
    files_to_process.sort()

    concatenated_data = bytearray()
    total_size = 0

    for _, filename in files_to_process:
        input_file = os.path.join(folder_path, filename)
        debug_file = os.path.join(folder_path, f"debug_{filename}.txt")
        output_data = remove_checksums_from_file(input_file, debug_file)
        concatenated_data.extend(output_data)
        total_size += len(output_data)

    # Write the concatenated result to a new file
    output_file = os.path.join(folder_path, 'output.MPQ')
    with open(output_file, 'wb') as f:
        f.write(concatenated_data)

    # Write overall debug information
    overall_debug_file = os.path.join(folder_path, 'overall_debug.txt')
    with open(overall_debug_file, 'w') as debug_f:
        for _, filename in files_to_process:
            debug_f.write(f"Processed file: {filename}\n")
        debug_f.write(f"Total concatenated file size: {total_size} bytes\n")

# Folder path
folder_path = 'folder'

process_folder(folder_path)
