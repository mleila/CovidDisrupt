'''
This module contains generic input/output utils
'''
import json

import pandas as pd


def read_json_file(path: str):
    """Read a json file into a dict."""
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def read_excel_file(path: str):
    """Read single sheet excel file as pandas df."""
    return pd.read_excel(path)


def read_csv_file(path: str, encoding: str = None):
    """Read csv file as a pandas dataframe"""
    return pd.read_csv(path, encoding=encoding)


def write_text_to_s3(
        s3_resource,
        bucket: str,
        text: str,
        filepath: str):
    """Write an in-memory string as a text file to S3."""
    s3_resource.Object(bucket, filepath).put(Body=text)
