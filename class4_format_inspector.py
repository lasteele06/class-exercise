import json
import logging
from pathlib import Path
import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    df = pd.read_csv(filepath)
    logger.info(f"Inspecting CSV file: {filepath}")
    print(df.head(3))  # Print the first three rows
    
    pass


def inspect_json(filepath):
    with open(filepath, "r") as f:
        dj = json.load(f)
    logger.info(f"Inspecting JSON file: {filepath}")
    print(dj)  # Print the contents of the JSON file
    pass


def inspect_yaml(filepath):
    with open(filepath, "r") as f:
        dy = yaml.safe_load(f)
    logger.info(f"Inspecting YAML file: {filepath}")
    print(dy)  # Print the contents of the YAML file
    pass


def inspect_env():
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    logger.info("Inspecting .env file: .env")
    print(f"Found keys: {keys}")  # Print the found keys
    # Do not print passwords, API keys, or other secret values.


def main():
    # TODO:
    data_dir = Path("data")  # 1. Create a Path object for the data directory.
    csv_path = data_dir / "sample.csv"  # 2. Use the / operator to build the CSV path.
    json_path = data_dir / "sample.json"  # 2. Use the / operator to build the JSON path.
    yaml_path = data_dir / "sample.yaml"  # 2. Use the / operator to build the YAML path.

    inspect_csv(csv_path)  # 3. Call each inspection function using the matching path.
    inspect_json(json_path)  # 3. Call each inspection function using the matching path
    inspect_yaml(yaml_path)  # 3. Call each inspection function using the matching path.
    inspect_env()  # 4. Call inspect_env() without an argument.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    pass


if __name__ == "__main__":
    main()