import re
import csv

input_log_file = 'C:/logs/syslog.log'  
output_csv_file = 'C:/logs/new_syslog.csv'

log_pattern = re.compile(r'^(?P<timestamp>\w+\s+\d+\s[\d:]+)\s[\w.-]+\s(?P<process>[\w/.-]+)(?:\[\d+\])?:\s(?P<message>.+)')

ip_pattern = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')

def parse_logs():
    with open(input_log_file, 'r') as infile, open(output_csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['timestamp', 'process', 'ip_address', 'message'])

        for line in infile:
            match = log_pattern.match(line)
            if match:
                timestamp = match.group('timestamp')
                process = match.group('process')
                message = match.group('message')
                ip_match = ip_pattern.search(message)
                ip_address = ip_match.group(0) if ip_match else ''
                writer.writerow([timestamp, process, ip_address, message])
            else:
                #if unmatch then skip
                continue

    print(f"Log parsing completed.")

if __name__ == '__main__':
    parse_logs()
