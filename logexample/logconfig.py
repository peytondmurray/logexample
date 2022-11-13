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


class ContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.name.startswith("logexample"):
            if record.name.startswith("logexample.data"):
                record.packagename = "[Ray Data]"
            elif record.name.startswith("logexample.tune"):
                record.packagename = "[Ray Tune]"
            elif record.name.startswith("logexample.train"):
                record.packagename = "[Ray Train]"
            else:
                record.packagename = "[Ray Core]"
        else:
            record.package.name = ""

        return True


def set_log_config():
    filters = {
        "contextfilter": {
            "()": ContextFilter
        }
    }

    if rich is not None:
        formatters = {
            "console": {
                "format": "\[[bold green]%(asctime)s[/bold green]][bold blue]%(packagename)s[/bold blue] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        }
        handlers = {
            "console": {
                "class": "rich.logging.RichHandler",
                # "log_time_format": "[%Y-%m-%d %H:%M:%S]",
                "markup": True,
                "show_path": True,
                "show_level": True,
                "show_time": False,
                "filters": ["contextfilter"],
                "formatter": "console",
            }
        }
    else:
        formatters = {
            "console": {
                "format": "[%(asctime)s]%(packagename)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        }
        handlers = {
            "console": {
                "class": "logging.StreamHandler",
                "filters": ["contextfilter"],
                "formatter": "console",
            }
        }

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
