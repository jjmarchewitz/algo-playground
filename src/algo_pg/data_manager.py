"""
DOC:
"""

from algo_pg.util import get_list_of_trading_days_in_range
from alpaca_trade_api import TimeFrame
from datetime import timedelta
from dateutil.parser import isoparse
import pandas as pd

# TODO: Get rid of this class in favor of PositionDataFrameBuilder


class DataManager():
    """
    The DataManager is meant to handle acquiring and synchronizing data from Alpaca, as
    well as building and formatting an output dataframe.
    """

    # TODO: can handle switching between allowing and disallowing after-hours data

    def __init__(self, alpaca_api, data_settings, symbol):
        """
        Constructor for the DataManager object.

        Args:
            alpaca_api: A bundle of Alpaca APIs all created and authenticated with the
                keys in the repo's alpaca.config.
            data_settings: An instance of the DataSettings dataclass.
            symbol: A string for the market symbol of this position (i.e. "AAPL" or
                "GOOG").
        """

        self.alpaca_api = alpaca_api
        self.data_settings = data_settings
        self.symbol = symbol

    #     self.time_frame = data_settings.time_frame

    #     self._df_columns = self._raw_df_columns
    #     self.df = pd.DataFrame(columns=self._df_columns)

    #     self.max_rows = self.data_settings.max_rows_in_df
    #     self._next_df_index = 0
    #     self._next_raw_df_index = 0

    #     # This is not the same as self.stat_dict, this is the constructor's argument
    #     if self.data_settings.stat_dict is not None:
    #         self.add_stat_dict(data_settings.stat_dict)

    #     if self.data_settings.start_buffer_time_delta is not None:
    #         self._add_start_buffer_data_to_raw_df()

    # def add_stat_dict(self, stat_dict):
    #     """
    #     Add a new statistics calculating dictionary and update the main dataframe with
    #     a column for each statistic.

    #     Args:
    #         stat_dict: A dictionary where the keys are strings that represent the name of
    #             a statistic, and where the values are function objects that calculate
    #             the given statistic.
    #     """
    #     self.stat_dict = stat_dict

    #     # Update the columns to include the statistics passed in
    #     self._df_columns.extend(self._get_statistics_column_names())

    #     # Recreate the dataframe with the new columns added in
    #     self.df = pd.DataFrame(columns=self._df_columns)

    # def _get_statistics_column_names(self):
    #     """
    #     Extract the column names from the stat_dict (i.e. the keys of the dict).

    #     Returns:
    #         A list of column names.
    #     """

    #     stat_column_names = []

    #     if self.stat_dict is not None:
    #         for key, _ in self.stat_dict.items():
    #             stat_column_names.append(key)

    #     return stat_column_names

    # def _update_df(self):
    #     """
    #     Updates self.df with the newest input data from self._raw_df and then calculates
    #     summary statistics from those new entries and adds them to the appropriate
    #     column.
    #     """

        # if not self.generator_at_end_of_day:

        #     # Add a new row to the main dataframe
        #     self.df.loc[self._next_df_index] = ["ERROR_NOT_REPLACED"
        #                                         for _ in self._df_columns]

        #     last_row_of_raw_df = self._raw_df.loc[self._next_raw_df_index - 1]

        #     # Copy over columns from raw_df
        #     for column, value in last_row_of_raw_df.items():
        #         setattr(self.df.loc[self._next_df_index], column, value)

        #     # Calculate any statistics from the stat dict and add them to the appropriate
        #     # column in self.df
        #     for column, func in self.stat_dict.items():
        #         last_raw_df_row_index = self._next_raw_df_index - 1
        #         value = func(self._raw_df, last_raw_df_row_index)
        #         setattr(self.df.loc[self._next_df_index], column, value)

        #     self._next_df_index += 1
