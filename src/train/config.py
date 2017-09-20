# -*- coding: utf-8 -*-

import tensorflow as tf

__all__ = (
    "get_config",
)


config = None


def get_config():
    global config

    if config is None:
        config = tf.ConfigProto()
        config.allow_soft_placement = True

    return config
