import csv
import json

input_csv = 'C:/logs/new_syslog.csv'
output_csv = 'C:/logs/threats_detected.csv'
rules_file = 'rules.json'

# Load detection rules
def load_rules(path):
    with open(path, 'r') as f:
        return json.load(f)

# Apply rules to a log entry
def is_threat(entry, rules):
    ip_address = entry['ip_address']
    message = entry['message'].lower()

    if ip_address in rules['ip_blacklist']:
        return True

    for keyword in rules['keywords']:
        if keyword.lower() in message:
            return True

    return False

def detect_threats():
    rules = load_rules(rules_file)

    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['threat_detected'])
        writer.writeheader()

        for row in reader:
            threat = is_threat(row, rules)
            row['threat_detected'] = 'Yes' if threat else 'No'
            writer.writerow(row)

    print(f"Threat detection complete.")

if __name__ == '__main__':
    detect_threats()
