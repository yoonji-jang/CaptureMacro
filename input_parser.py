from typing import List, Tuple

def parse_input_data(input_data: List[str]) -> Tuple[List[str], str, int]:
    websites = []
    dict_ = {}

    for line in input_data:
        parts = line.strip().split("=", 1)  # 최대 1번만 나누기
        if len(parts) == 2:
            key, value = parts
            dict_[key] = value

    website_urls = dict_.get("WEBSITE", "").split(",")
    for url in website_urls:
        websites.append(url.strip())

    output_path = dict_.get("OUTPUT", "")
    capture_interval = int(dict_.get("TIME_INTERVAL", 0))

    return websites, output_path, capture_interval