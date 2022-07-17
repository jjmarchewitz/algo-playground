from algo_pg.util import get_list_of_trading_days_in_range
from enum import Enum
from multiprocessing import Process, Queue


class AlpacaAsset:
    def __init__(self, alpaca_api, data_settings):
        pass


class AlpacaDataManager:
    def __init__(self, alpaca_api, data_settings):
        """DOC:"""
        self.alpaca_api = alpaca_api
        self.data_settings = data_settings
        self.assets = {}

    def add_new_asset(self, symbol):
        pass

    def get_asset(self, symbol):
        pass


# class AlpacaDataManager:

#     def __init__(self, alpaca_api, data_settings):
#         """DOC:"""
#         self.alpaca_api = alpaca_api
#         self.data_settings = data_settings
#         self.asset_dfs = {}

#         self.asset_df_queue = Queue()
#         self.manager_to_producer_queue = Queue()

#         self.producer_process = self.spawn_producer_process()

#         # TODO: Remove this?
#         self.consume()

#         self.trading_machine_current_day = None

#     def add_asset(self, symbol):
#         """DOC:"""
#         if symbol in self.asset_dfs.keys():
#             raise ValueError("Symbol is already in the asset manager!")

#         self.asset_dfs[symbol] = None

#         # TODO: Catch-up code here

#     def contains_asset(self, symbol):
#         """DOC:"""
#         return symbol in self.assets.keys()

#     def consume(self):
#         """DOC:"""

#         self.manager_to_producer_queue.put("START")

#         while True:
#             msg = self.asset_df_queue.get()

#             if msg == "DONE":
#                 self.teardown()
#                 break

#             print(msg)

#     def teardown(self):
#         """DOC:"""
#         self.producer_process.join()

#     def spawn_producer_process(self):
#         """DOC:"""
#         alpaca_data_producer = AlpacaDataProducer(
#             self.alpaca_api, self.data_settings, self.manager_to_producer_queue,
#             self.asset_df_queue)

#         producer_process = Process(target=alpaca_data_producer.produce, args=[])
#         producer_process.start()

#         return producer_process


# class AssetListUpdateType(Enum):
#     ADD = "ADD"
#     REMOVE = "REMOVE"


# class AlpacaDataProducer:

#     def __init__(self, alpaca_api, data_settings, manager_to_producer_queue,
#                  asset_df_queue):
#         self.alpaca_api = alpaca_api
#         self.data_settings = data_settings
#         self.manager_to_producer_queue = manager_to_producer_queue
#         self.asset_df_queue = asset_df_queue
#         self.symbols_list = []

#         # Generates a list of MarketDay instances in order from self.start_date to
#         # self.end_date to represent all of the days the market is open, and *only*
#         # the days the market is open.
#         self.trading_days = get_list_of_trading_days_in_range(
#             self.alpaca_api, self.data_settings.start_date, self.data_settings.end_date)

#     def produce(self):

#         # Wait infinitely until the "START" message is recieved
#         while True:
#             msg = self.manager_to_producer_queue.get()

#             if msg == "START":
#                 break

#         for trading_day in self.trading_days:
#             self.asset_df_queue.put(trading_day)

#         self.asset_df_queue.put("DONE")

#     def get_raw_data_for_trading_day(self):
#         pass
