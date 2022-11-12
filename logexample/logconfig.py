import logging
from logging.config import dictConfig

try:
    import rich
except ImportError:
    rich = None
    logging.info(
        "rich is not installed. Run `pip install rich` for"
        " improved logging, progress, and tracebacks."
    )


def set_log_config():
    formatters = {
        "console": {
            "datefmt": "[%Y-%m-%d %H:%M:%S]",
        }
    }

    filters = {}

    if rich is not None:
        handlers = {
            "console": {
                "class": "rich.logging.RichHandler",
                "log_time_format": "[%Y-%m-%d %H:%M:%S]",
                "markup": True,
                "show_path": True,
            }
        }
    else:
        handlers = {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler"
            }
        }

    filters =

    loggers = {
        "": {  # root logger
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        }
    }

    dictConfig(
        {
            "version": 1,
            "formatters": formatters,
            "filters": filters,
            "handlers": handlers,
            "loggers": loggers,
            "disable_existing_loggers": False
        }
    )
