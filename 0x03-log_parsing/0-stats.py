#!/usr/bin/env python3
import sys
import signal

# Global variables to store metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Prints the accumulated statistics."""
    global total_file_size, status_code_count
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def handle_interrupt(signal, frame):
    """Handles keyboard interrupt (Ctrl + C) to print statistics and exit."""
    print_statistics()
    sys.exit(0)

def process_line(line):
    """Processes a line and updates the statistics if the format matches."""
    global total_file_size, status_code_count, line_count
    
    # Example of expected input: 123.123.123.123 - [12/Oct/2024:12:45:59] "GET /projects/260 HTTP/1.1" 200 1024
    parts = line.split()
    if len(parts) < 7:
        return
    
    try:
        # Extract and process the status code and file size
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        total_file_size += file_size
        line_count += 1
    except (ValueError, IndexError):
        # Skip the line if it doesn't match the expected format
        return

def main():
    """Main function to read from stdin and compute the statistics."""
    global line_count

    # Handle keyboard interruption
    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            process_line(line)
            
            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        print_statistics()
        sys.exit(0)

if __name__ == "__main__":
    main()
