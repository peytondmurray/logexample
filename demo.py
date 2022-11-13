import logging
import logexample


def clear_logging_config():
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])


def run_set_config():
    clear_logging_config()
    logexample.logconfig.set_log_config()
    logexample.data.dataset.get_data()
    logexample.tune.runner.run()
    logexample.util.do_stuff()
    logexample.train.trainer.start()


def run_conditional_config():
    clear_logging_config()
    logging.basicConfig(format="%(asctime)s: %(message)s")

    # Check if a logging configuration has been provided by the user. If not, then create one.
    if not logging.getLogger().hasHandlers():
        logexample.logconfig.set_log_config()

    logexample.data.dataset.get_data()
    logexample.tune.runner.run()
    logexample.util.do_stuff()
    logexample.train.trainer.start()


if __name__ == "__main__":
    print("run_set_config(), root logger should use rich formatting:\n")
    run_set_config()
    print("\n\n")
    print("run_conditional_config(), root logger uses basicConfig. Simple formatting expected:\n")
    run_conditional_config()
