import logging
import logexample

logging.basicConfig(format="%(message)s: %(asctime)s")

# Check if a logging configuration has been provided by the user. If not, then create one.
if not logging.getLogger().hasHandlers():
    logexample.logconfig.set_log_config()

logexample.data.dataset.get_data()
logexample.tune.runner.run()
logexample.util.do_stuff()
logexample.train.trainer.start()
