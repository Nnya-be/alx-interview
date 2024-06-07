#!/usr/bin/python3
import sys
import re

# Status codes we are interested in
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

def print_metrics(total_size, status_counts):
    """Prints metrics based on the current data collected."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if code in VALID_STATUS_CODES:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """Parses a single log line and returns (status_code, file_size) if valid, otherwise None."""
    pattern = r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        return (status_code, file_size)
    return None

def main():
    total_size = 0
    status_counts = {code: 0 for code in VALID_STATUS_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_data = parse_line(line)
            if parsed_data:
                status_code, file_size = parsed_data
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
