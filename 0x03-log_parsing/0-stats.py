#!/usr/bin/python3
"""Module that reads from stdin and computes metrics."""
import sys

# Initialize dictionary for status codes and counters
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        # Ensure that the line has the correct format (enough parts)
        if len(parts) > 4:
            code = parts[-2]

            try:
                size = int(parts[-1])
            except ValueError:
                continue  # Skip if file size is not a valid integer

            # Update metrics if the status code is valid
            if code in status_codes:
                status_codes[code] += 1
            total_size += size
            line_count += 1

        # Every 10 lines, print the accumulated statistics
        if line_count == 10:
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")
            line_count = 0

except KeyboardInterrupt:
    pass

finally:
    # Print final statistics before exiting
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
