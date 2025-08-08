# /// script
# requires-python = ">=3.11"
# dependencies = [
#    "click==8.1.8",
#   "ucimlrepo==0.0.7",
# ]
# ///

from enum import IntEnum, StrEnum, auto
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

class Operation(StrEnum):
    SUMMARY = auto()
    METADATA = auto()
 
@click.command()
@click.option( 
    "--operation",
    default=Operation.SUMMARY,
    type=click.Choice(Operation),
    help="Operation to perform: variable summary or dataset metadata",
)

@click.option(
    "--variable",
    type=click.Choice(IrisVariable),
    help="variable to summarize.",
    required=False,
)



def main(operation, variable):
    """Fetch the iris dataset from UCI."""
    print("Fetching iris dataset using ucimlrepo")
    iris = fetch_ucirepo(id=UCIDataset.IRIS.value)
    print("dataset fetched successfully")

    if operation is Operation.SUMMARY:
        if variable:
            print(f"{IrisVariable(variable)} summary:")
            pp(iris.data.features[IrisVariable(variable).value])
    elif operation == Operation.METADATA:
        print("Metadata summary:")
        pp(iris.metadata)

if __name__ == "__main__":
    main()
    
