"""
This module provides functions to retrieve and categorize information
about installed Python packages.
"""

import json
from collections import defaultdict
import importlib.metadata
from typing import Dict, Any


def get_package_info() -> Dict[str, Dict[str, Any]]:
    """
    Retrieves information about all installed packages using importlib.metadata.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary containing package information.
    """
    package_info = {}
    for dist in importlib.metadata.distributions():
        try:
            metadata = dist.metadata
            name = metadata["Name"]
            description = metadata["Summary"] if "Summary" in metadata else "No description found"
            classifiers = metadata.get_all("Classifier", [])
            category = next(
                (c.split(" :: ", 2)[-1] for c in classifiers if c.startswith("Topic :: ")),
                "Uncategorized",
            )
            package_info[name] = {
                "version": dist.version,
                "description": description,
                "category": category,
            }
        except (KeyError, AttributeError) as e:
            print(f"Error processing {dist.name}: {str(e)}")
            package_info[dist.name] = {
                "version": dist.version,
                "description": "Unable to fetch description",
                "category": "Uncategorized",
            }
    return package_info


def categorize_packages(package_info: Dict[str, Dict[str, Any]]) -> Dict[str, list]:
    """
    Categorizes packages based on their category information.

    Args:
        package_info (Dict[str, Dict[str, Any]]): A dictionary containing package information.

    Returns:
        Dict[str, list]: A dictionary with categories as keys and lists of package names as values.
    """
    categories = defaultdict(list)
    for name, info in package_info.items():
        categories[info["category"]].append(name)
    return dict(categories)


def main() -> None:
    """
    Main function to retrieve package information, categorize packages,
    and save results to JSON files.
    """
    package_info = get_package_info()
    categorized_packages = categorize_packages(package_info)

    with open("package_info.json", "w", encoding="utf-8") as f:
        json.dump(package_info, f, indent=2, sort_keys=True)

    with open("package_categories.json", "w", encoding="utf-8") as f:
        json.dump(categorized_packages, f, indent=2, sort_keys=True)

    print("Package information saved to 'package_info.json'")
    print("Package categories saved to 'package_categories.json'")


if __name__ == "__main__":
    main()
