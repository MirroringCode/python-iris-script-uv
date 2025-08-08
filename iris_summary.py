# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "click==8.1.8",
#   "pandas==2.2.3",
#   "ucimlrepo==0.0.7",
# ]
# ///


import logging
import sys
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum, auto
from pprint import pformat, pprint as pp


import click
import pandas as pd
from ucimlrepo import fetch_ucirepo

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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
 

@dataclass
class DescriptiveStatistics:
    data: pd.Series
    mean: float = field(init=False)
    median: float = field(init=False)
    mm_diff: float = field(init=False)

    def __post_init__(self):
        if not isinstance(self.data, pd.Series):
            raise TypeError(f"Data must be a panda Series, got {type(self.data)}")
        self.mean = self.data.mean()
        self.median = self.data.median()
        self.mm_diff = self.mean - self.median
    
    def __str__(self):
        return pformat(self)


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
            # pp(iris.data.features[IrisVariable(variable).value])
            print(DescriptiveStatistics(
                iris.data.features[IrisVariable(variable).value]
            ))
        else:
            print("All variables:")
            pp(iris.variables)
    elif operation == Operation.METADATA:
        print("Metadata summary:")
        pp(iris.metadata)

if __name__ == "__main__":
    main()
    
