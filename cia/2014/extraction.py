import re
from typing import List
import math

# num_year_regex = re.compile(r"([\d]+)\s\(\w+(\d+).*\)")
num_year_regex = re.compile(r"\$?([\d,\.]+)(.*)\(.*(\d{4})")
key_num_unit_regex = re.compile(r"(.+):\s*\$?([\d,\.]+)([^\(]*)")
year_regex = re.compile(r".*\(.*(\d{4}).*\)")
mul_unit_regex = re.compile(r"(billion|million|trillion)")
clean_replace_regex = re.compile(r"[\(\),]")
space_replace_regex = re.compile(r"\s+")


def clean_number(num_str: str) -> float:
    return float(num_str.replace(",", ""))


def clean_key(key_str: str) -> str:
    # remove (",", "(", ")")
    key_str = clean_replace_regex.sub("", key_str)
    key_str = space_replace_regex.sub(" ", key_str)
    return key_str.strip().replace(" ", "-")


def normalize_number(num: float, unit: str) -> (float, str):
    result = mul_unit_regex.search(unit)
    if not result:
        unit = unit.strip()
        if unit == "":
            unit = "number"
        return num, unit
    mul_unit = result.group(1)
    if mul_unit == "million":
        num = num * 10**6
    elif mul_unit == "billion":
        num = num * 10**9
    elif mul_unit == "trillion":
        num = num * 10**12
    else:
        raise Exception("Unknown Mul Unit")

    unit = mul_unit_regex.sub("", unit).strip()
    if unit == "":
        unit = "number"
    return num, unit


def extract_year(last_str: str) -> int:
    result = year_regex.search(last_str)
    if not result:
        return None

    return int(result.group(1))


def extract_val_unit_year(data_str: str) -> (float, str, int):
    result = num_year_regex.search(data_str)
    if not result:
        return None
    val = clean_number(result.group(1))
    unit = result.group(2).strip()
    year = int(result.group(3))
    val, unit = normalize_number(val, unit)
    return (val, unit, year)


def extract_data_1(data_arr: List[str]):
    values = []
    unit = None
    for d in data_arr:
        if d.startswith("country") or d.startswith("note"):
            continue
        result = extract_val_unit_year(d)
        if result:
            values.append((result[0], result[2]))
            unit = result[1]

    return (values, unit)


def extract_key_val_unit(data_str: str):
    result = key_num_unit_regex.search(data_str)
    if not result:
        return None
    key = result.group(1)
    val = clean_number(result.group(2))
    unit = result.group(3)
    val, unit = normalize_number(val, unit)
    return (key, val, unit)


def extract_data_2(data_arr: List[str]):
    values = []
    unit = None
    year = None
    for d in data_arr:
        if d.startswith("country") or d.startswith("note"):
            continue
        result = extract_key_val_unit(d)
        if result:
            if not unit:
                unit = result[2]
            values.append((clean_key(result[0]), result[1]))

    year_res = extract_year(data_arr[-1])
    if year_res:
        year = year_res
    else:
        raise Exception("Year Not Found")

    return (values, unit, year)
