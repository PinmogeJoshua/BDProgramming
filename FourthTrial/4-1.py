def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def process(line):
    # Add your processing logic here
    print(line)

for line in read_large_file('第四次上机/pi.txt'):
    process(line)
