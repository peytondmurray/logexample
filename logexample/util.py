import logging

log = logging.getLogger(__name__)

log.info('loaded foo.util')


def do_stuff():
    log.critical('doing stuff!')
