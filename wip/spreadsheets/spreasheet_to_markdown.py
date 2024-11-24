"""
Spreadsheet to Markdown Table Converter

This script converts various spreadsheet formats (CSV, TSV, Excel, Google Sheets, OpenDocument)
to neatly formatted Markdown tables. It supports the following file formats:
- CSV and TSV
- Excel (.xlsx and .xls)
- Google Sheets (downloaded as CSV)
- OpenDocument Spreadsheets (.ods)

The script reads the input file, converts its content to a Markdown table, and saves the
result to an output file. The Markdown table is formatted for improved readability in its
raw form, with aligned columns.

Usage:
    python script.py <input_file> <output_file> [delimiter]

Dependencies:
    - openpyxl
    - xlrd
    - pandas
    - ezodf

Install dependencies with:
    pip install openpyxl xlrd pandas ezodf

Author: [Your Name]
Date: [Current Date]
Version: 1.5
"""

import csv
import sys
from typing import List, Iterable, Any, Callable, Union
import openpyxl
import xlrd
import pandas as pd
import ezodf


def format_markdown_table(table_lines: List[str]) -> str:
    """
    Format a Markdown table for improved readability in raw form.

    Args:
        table_lines (List[str]): List of strings representing table rows.

    Returns:
        str: A formatted Markdown table with aligned columns.
    """
    rows = [line.strip().split("|")[1:-1] for line in table_lines]
    col_widths = [max(len(cell.strip()) for cell in col) for col in zip(*rows)]

    formatted_rows = []
    for i, row in enumerate(rows):
        formatted_cells = [
            " " + cell.strip().ljust(col_widths[j]) + " " for j, cell in enumerate(row)
        ]
        formatted_row = "|" + "|".join(formatted_cells) + "|"
        formatted_rows.append(formatted_row)

        if i == 0:
            separator = "|" + "|".join("-" * (width + 2) for width in col_widths) + "|"
            formatted_rows.append(separator)

    return "\n".join(formatted_rows)


def reader_to_markdown(reader: Iterable[Union[List[Any], tuple]]) -> str:
    """
    Convert an iterable of rows to a formatted Markdown table.

    Args:
        reader (Iterable[Union[List[Any], tuple]]):
        An iterable where each item is a list or tuple representing a row.

    Returns:
        str: A formatted Markdown table.
    """
    iterator = iter(reader)
    headers = next(iterator)
    markdown_lines = [f"| {' | '.join(str(h) for h in headers)} |"]
    markdown_lines.append(f"| {' | '.join('---' for _ in headers)} |")

    for row in iterator:
        markdown_lines.append(f"| {' | '.join(str(cell) for cell in row)} |")

    return format_markdown_table(markdown_lines)


def csv_tsv_to_markdown(file_path: str, delimiter: str = ",") -> str:
    """
    Convert a CSV or TSV file to a Markdown table.

    Args:
        file_path (str): Path to the input CSV or TSV file.
        delimiter (str, optional): Delimiter used in the file. Defaults to ','.

    Returns:
        str: A formatted Markdown table.
    """
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        return reader_to_markdown(reader)


def xlsx_to_markdown(file_path: str) -> str:
    """
    Convert an Excel (.xlsx) file to a Markdown table.

    Args:
        file_path (str): Path to the input .xlsx file.

    Returns:
        str: A formatted Markdown table.
    """
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    if sheet is None:
        raise ValueError("No active sheet found in the workbook.")
    return reader_to_markdown(sheet.iter_rows(values_only=True))


def xls_to_markdown(file_path: str) -> str:
    """
    Convert an old Excel (.xls) file to a Markdown table.

    Args:
        file_path (str): Path to the input .xls file.

    Returns:
        str: A formatted Markdown table.
    """
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    return reader_to_markdown(sheet.get_rows())


def gsheet_to_markdown(file_path: str) -> str:
    """
    Convert a Google Sheet (downloaded as CSV) to a Markdown table.

    Args:
        file_path (str): Path to the input Google Sheet CSV file.

    Returns:
        str: A formatted Markdown table.
    """
    df = pd.read_csv(file_path)
    return reader_to_markdown([df.columns] + df.values.tolist())


def ods_to_markdown(file_path: str) -> str:
    """
    Convert an OpenDocument Spreadsheet (.ods) file to a Markdown table.

    Args:
        file_path (str): Path to the input .ods file.

    Returns:
        str: A formatted Markdown table.
    """
    doc = ezodf.opendoc(file_path)
    sheet = doc.sheets[0]

    def ods_reader():
        for row in sheet.rows():
            yield [cell.value for cell in row]

    return reader_to_markdown(ods_reader())


def main():
    """
    Main function to handle command-line arguments and orchestrate the conversion process.
    """
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <output_file> [delimiter]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    delimiter = sys.argv[3] if len(sys.argv) > 3 else ","

    file_extension = input_file.split(".")[-1].lower()

    conversion_functions: dict[str, Callable[[str], str]] = {
        "csv": lambda f: csv_tsv_to_markdown(f, delimiter),
        "tsv": lambda f: csv_tsv_to_markdown(f, delimiter),
        "xlsx": xlsx_to_markdown,
        "xls": xls_to_markdown,
        "gsheet": gsheet_to_markdown,
        "sheet": gsheet_to_markdown,
        "ods": ods_to_markdown,
    }

    if file_extension not in conversion_functions:
        print(f"Unsupported file format: {file_extension}")
        sys.exit(1)

    try:
        markdown_content = conversion_functions[file_extension](input_file)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(markdown_content)

        print(f"Conversion complete. Formatted Markdown table saved to {output_file}")
    except (
        IOError,
        ValueError,
        KeyError,
        IndexError,
        csv.Error,
        xlrd.XLRDError,
        pd.errors.EmptyDataError,
    ) as e:
        print(f"An error occurred during conversion: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
