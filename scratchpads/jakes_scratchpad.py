from algo_pg.algorithms.bang_bang.alg import BangBang
from algo_pg.signals import AlpacaDataManager
from algo_pg.machine import TradingMachine, DataSettings
from algo_pg.portfolio import Portfolio
from algo_pg.stat_calculators import avg_last_n, net_last_n
from algo_pg.util import apg_init
from alpaca_trade_api import TimeFrame
from datetime import timedelta
from functools import partial


def main():
    alpaca_api = apg_init()

    # Keys will become column names and the function object that is the value will be
    # called on every row of every Position's DataManager
    stat_dict = {
        "avg_l5_vwap": partial(avg_last_n, window_size=5),
        "net_l5_vwap": partial(net_last_n, window_size=5),
        "avg_l10_vwap": partial(avg_last_n, window_size=10),
        "net_l10_vwap": partial(net_last_n, window_size=10),
    }

    # A dataclass that stores general information about data settings and how the data
    # should be collected
    data_settings = DataSettings(
        start_date="2021-09-09",
        end_date="2021-10-20",
        time_frame=TimeFrame.Hour,
        stat_dict=stat_dict,
        max_rows_in_df=10_000,
        start_buffer_time_delta=timedelta(days=4),
        time_frames_between_algo_runs=1
    )

    adm = AlpacaDataManager(alpaca_api, data_settings)
    # adm.add_asset("AAPL")
    # adm.add_asset("GOOG")
    # adm.add_asset("IVV")

    breakpoint()


if __name__ == "__main__":
    main()
