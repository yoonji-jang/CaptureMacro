import time

from typing import List, Tuple


def parse_input_data(input_data: List[str]) -> Tuple[List[str], str, int]:
    dict_ = {}
    for line in input_data:
        key_value = line.strip().split("=")
        if len(key_value) == 2:
            dict_[key_value[0]] = key_value[1]

    websites = list(dict_["WEBSITE"].split(","))
    output_path = dict_["OUTPUT"]
    capture_interval = dict_["TIME_INTERVAL"]

    return websites, output_path, capture_interval
