#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Directory containing input files
input_dir="../../midi/alvinwong"
# Directory for output files
output_dir="../../midi/alvinwong_ai"

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

cd src

# Iterate over each file in the input directory
for infile in "$input_dir"/*; do
  # Get the base name of the file (without the directory path)
  base_name=$(basename "$infile")
  # Define the output file path
  outfile="$output_dir/$base_name"
  
  # Call the command with infile and outfile
  python machine_pianist_inference.py "$infile" "$outfile"
  
  # Optional: Print the command being executed
  echo "Processed $infile -> $outfile"
done