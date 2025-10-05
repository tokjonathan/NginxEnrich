import re
from datetime import datetime
from typing import Dict, Optional, List
from pathlib import Path

TIME_PATTERN = "%d/%b/%Y:%H:%M:%S %z"
LOG_PATTERN = re.compile(
    r"(?P<remote_addr>\S+)\s+"  # source ip, remote address
    r"(?P<ident>\S+)\s+"  # ident (usual value '-')
    r"(?P<authuser>\S+)\s+"  # authuser (usual value '-')
    r"\[(?P<time>.+?)\]\s+"  # [04/Oct/2025:14:45:30 +0800]
    r'"(?P<request>.*?)"\s+'  # e.g. "GET /path HTTP/1.1"
    r"(?P<status>\d{3})\s+"  # 200, ,400, 404, 500, 502, etc
    r"(?P<body_bytes_sent>\S+)\s+"  # 615 or '-'
    r'"(?P<http_referrer>.*?)"\s+'  # "-" or "https://ref"
    r'"(?P<user_agent>.*?)"'  # User Agent
)


# Nginx Access Log Format Parsing, returns dictionary
def parse_log_entry(line: str) -> Optional[Dict]:
    # Conduct Regex match on log
    match_object = LOG_PATTERN.match(line.strip())
    if not match_object:
        print("Log entry does not match known regex pattern for Nginx Access Logs")
        return None

    log_dict = match_object.groupdict()

    # Parse request field
    method = path = protocol = None
    parts = log_dict["request"].split()
    if len(parts) == 3:
        method, path, protocol = parts
    elif len(parts) == 2:
        method, path = parts

    # Add standardize ISO-8601 timestamp for universality
    time_iso = None
    try:
        time_iso = datetime.strptime(log_dict["time"], TIME_PATTERN).isoformat()
    except Exception:
        time_iso = log_dict["time"]  # fallback

    # Reconstruct dictionary, add parsed values into dict
    if protocol:
        log_dict["protocol"] = protocol
    log_dict["method"] = method
    log_dict["path"] = path
    log_dict["iso_time"] = time_iso

    return log_dict


# def parse_file(input_path: Path) -> List[Dict]:

if __name__ == "__main__":
    sample = '127.0.0.1 - - [04/Oct/2025:14:34:09 +0800] "GET / HTTP/1.1" 200 615 "-" "curl/8.7.1"'
    result = parse_log_entry(sample)
    print(result)
