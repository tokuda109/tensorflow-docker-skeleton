# -*- coding: utf-8 -*-

import tensorflow as tf

__all__ = (
    "get_logger",
)

logger = None


def get_logger():
    global logger

    if logger is None:
        logger = tf.logging
        logger.set_verbosity(logger.DEBUG)

    return logger
