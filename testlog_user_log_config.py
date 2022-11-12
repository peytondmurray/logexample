import logging
import logexample

logging.basicConfig(format="%(asctime)s: %(message)s")

logexample.data.dataset.get_data()
logexample.tune.runner.run()
logexample.util.do_stuff()
logexample.train.trainer.start()
