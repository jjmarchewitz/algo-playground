from multiprocessing import Process, Queue
from time import sleep


class AlpacaDataManager:

    def __init__(self, alpaca_api, data_settings):
        """DOC:"""
        self.alpaca_api = alpaca_api
        self.data_settings = data_settings

        queue = Queue()
        self.producer_process = self.spawn_producer_process(queue, 50)
        self.consume(queue)

    def consume(self, queue):
        """DOC:"""
        while True:
            msg = queue.get()

            if msg == "DONE":
                self.teardown()
                break

            print(msg)

    def teardown(self):
        """DOC:"""
        self.producer_process.join()

    def spawn_producer_process(self, queue, num):
        """DOC:"""
        alpaca_data_producer = AlpacaDataProducer(
            self.alpaca_api, self.data_settings, queue)
        producer_process = Process(target=alpaca_data_producer.produce, args=[num])
        producer_process.start()

        return producer_process


class AlpacaDataProducer:

    def __init__(self, queue):
        self.queue = queue

    def produce(self, num):
        for i in range(num):
            self.queue.put(i)
            sleep(0.125)
        self.queue.put("DONE")
