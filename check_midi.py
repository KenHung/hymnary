import os

expected_file_number = 716

for i in range(1, expected_file_number + 1):
    filename = "pianoteq_output/hymnary{:03d}.wav".format(i)
    if not os.path.exists(filename):
        print(f"File {filename} is missing!")
