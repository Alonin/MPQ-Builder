# MPQ Builder
This tool processes partial MPQ files used for streaming content from World of Warcraft CDNs pre-CASC (6.0.1.18125). The tool removes checksums, truncates the last 32 bytes from each file, and merges them in sequential order to create a complete MPQ file.

## Purpose
Before CASC, World of Warcraft used MPQ.X files to stream data from a CDN. These files are split into smaller parts for streaming purposes, and each file ends with a number (e.g., *.MPQ.0, *.MPQ.1, *.MPQ.2, etc.). These partial files are part of a larger MPQ archive, and this tool is designed to merge these files into a single, full MPQ file. 

## Usage

Put .MPQ.X files in a folder

Change folder_path to the folder where the MPQ.X files are

py MPQ-Builder.py


