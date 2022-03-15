from typing import List, Hashable

import pandas as pd
from pandas import Series, DataFrame


class HappinessCSVRepository:
    """Repository implementation for Happiness data stored on CSV format."""

    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self) -> DataFrame:
        """Read the csv file and provides a Pandas DataFrame from it."""
        return pd.read_csv(self.data_path)
