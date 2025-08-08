# /// script
# requires-python = ">=3.11"
# dependencies = [
#    "click==8.1.8",
#   "ucimlrepo==0.0.7",
# ]
# ///

from enum import IntEnum, StrEnum
from pprint import pprint as pp

import click
from ucimlrepo import fetch_ucirepo

class UCIDataset(IntEnum):
    IRIS = 53

class IrisVariable(StrEnum):
    PETAL_LENGTH = "petal length"
    PETAL_WIDTH  = "petal width"
    SEPAL_WIDTH  = "sepal width"
    SEPAL_LENGTH = "sepal length"
 
@click.command()
@click.option(
    "--operation",
    default="summary",
    type=click.Choice(["summary", "metadata"]),
    help="Operation to perform: variable summary or dataset metadata",
)

def main(operation):
    """Fetch the iris dataset from UCI."""
    print("Fetching iris dataset using ucimlrepo")
    iris = fetch_ucirepo(id=UCIDataset.IRIS.value)
    print("dataset fetched successfully")

    if operation == "summary":
        print("variable summary:")
        pp(iris.variables)
    elif operation == "metadata":
        print("dataset metadata:")
        pp(iris.metadata)

if __name__ == "__main__":
    main()
    
