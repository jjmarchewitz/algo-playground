"""
Functions that will generate summary statistics for a DataManager instance.

These functions MUST NOT rely on any columns that are not present by default
(i.e. other custom stats columns). This is a feature that may be supported in the
future.

"""


def dummy_420_69(df, last_row_index):
    """
    lol.

    Args:
        df: A dataframe of raw input data, almost straight from Alpaca.
        last_row_index: The index of the last valid row in the provided dataframe.

    Returns:
        -420.69

    """
    return -420.69


def avg_last_n(df, last_row_index, window_size=5):
    """
    Computes the average volume-weighted average price over the last n TimeFrames.

    Args:
        df: A dataframe of raw input data, almost straight from Alpaca.
        last_row_index: The index of the last valid row in the provided dataframe.
        window_size: The number of TimeFrames to go back for the average.

    Returns:
        The average volume-weighted average price over the last n TimeFrames.

    """

    total = 0

    for _, row in df.loc[last_row_index - window_size - 1:last_row_index].iterrows():
        total += row.vwap

    avg = total / 5

    return avg


def net_last_n(df, last_row_index, window_size=5):
    """
    Computes the net value over the last n TimeFrames.

    Args:
        df: A dataframe of raw input data, almost straight from Alpaca.
        last_row_index: The index of the last valid row in the provided dataframe.
        window_size: The number of TimeFrames to go back for the average.

    Returns:
        The net value over the last n TimeFrames.

    """

    net = df.loc[last_row_index].vwap - df.loc[last_row_index - window_size - 1].vwap

    return net
