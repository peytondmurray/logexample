import logging
import logexample


def clear_logging_config():
    """Clear the current logging configuration."""
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])


def generate_msgs():
    """Run some example code which generates log messages."""
    logexample.data.dataset.get_data()
    logexample.tune.runner.run()
    logexample.util.do_stuff()
    logexample.train.trainer.start()


def run_conditional_config():
    """Use the `rich` logging config if no logging configuration is set. Otherwise, use the existing
    logging configuration.
    """
    if not logging.getLogger().hasHandlers():
        logexample.logconfig.set_log_config()
        logging.info("Using `rich` config.")
    else:
        logging.info("Using existing config.")


if __name__ == "__main__":
    print(
        "No default logging configuration exists to start. "
        "A `rich` logger config is generated first:\n"
    )
    run_conditional_config()
    generate_msgs()
    print("\n\n")
    print("Now try the case where user config has been set.\n")
    clear_logging_config()
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO)
    run_conditional_config()
    generate_msgs()
