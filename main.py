from parse import parse_file
from enrich import enrich_user_agent
from transform import write_json
from datetime import datetime
import os
import sys


def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 1. Paths to access.log and output location (Edit filepath as needed [Entry Point])
    filepath = "access.log"
    output_path = f"enriched_output_{timestamp}.json"

    if not os.path.exists(filepath):
        print(f"Error: File not found — {filepath}")
    if os.path.isdir(filepath):
        print(f"Error: Path provided is directory, not a file — {filepath}")
        sys.exit(1)

    try:
        # 2. Parse log file
        parsed_logs = parse_file(filepath)
        if not parsed_logs:
            print("Warning: No entries found in log file.")
            return

        # 3. Enrich each record with user-agent information
        enriched_logs = []
        for i in parsed_logs:
            if i.get("parse_error"):
                print("")
                continue
            enriched_entry = enrich_user_agent(i)
            enriched_logs.append(enriched_entry)

        # 4. Convert to JSON and write output
        write_json(enriched_logs, output_path)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
