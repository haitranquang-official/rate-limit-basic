import datetime

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Read the first line
    first_line = lines[0].strip().split()
    num_lines = int(first_line[0])
    rate_limit = int(first_line[1])
    
    # Read the timestamps
    timestamps = [line.strip() for line in lines[1:num_lines+1]]
    unix_timestamps = []

    for timestamp in timestamps:
        unix_timestamp = (int) (datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').timestamp())
        print(unix_timestamp)
        unix_timestamps.append(unix_timestamp)
    
    return num_lines, rate_limit, unix_timestamps

if __name__ == "__main__":
    input_file = 'input.txt'
    num_lines, rate_limit, unix_timestamps = read_input(input_file)
    print(f"Number of lines: {num_lines}")
    print(f"Another number: {rate_limit}")

    window = []

    # Relatively naive algorithm, but it works correctly. However, it is not efficient in terms of both time and space.
    
    def valid(timestamp, rate_limit):
        global window

        while window and window[0] < timestamp - 60 * 60:
            window.pop(0)

        if (len(window) < rate_limit):
            window.append(timestamp)
        else:
            return False

        return len(window) <= rate_limit

    for timestamp in unix_timestamps:
        print(valid(timestamp, rate_limit))
    