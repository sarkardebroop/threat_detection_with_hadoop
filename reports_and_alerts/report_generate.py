import pandas as pd
from datetime import datetime

THREAT_DATA_PATH = 'detected_threats.csv'
OUTPUT_REPORT_PATH = f'reports/threat_report_{datetime.now().strftime("%Y%m%d_%H%M")}.csv'

def generate_report():
    try:
        df = pd.read_csv(THREAT_DATA_PATH)
        if df.empty:
            print("No data to generate report.")
            return

        threat_summary = df.groupby('threat_type').size().reset_index(name='count')
        df.to_csv(OUTPUT_REPORT_PATH, index=False)
        print(f"Full threat report saved to: {OUTPUT_REPORT_PATH}")
        print("\nThreat summary:\n", threat_summary)

    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == '__main__':
    generate_report()
