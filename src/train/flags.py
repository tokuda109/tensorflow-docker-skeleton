# -*- coding: utf-8 -*-

import tensorflow as tf

__all__ = (
    "FLAGS",
)


#: Training parameters

tf.flags.DEFINE_integer(
    "max_steps",
    100000,
    "Number of training steps."
)
tf.flags.DEFINE_integer(
    "num_gpus",
    0,
    ""
)
tf.flags.DEFINE_float(
    "learning_rate",
    0.001,
    "Initial learning rate."
)
tf.flags.DEFINE_integer(
    "batch_size",
    24,
    ""
)
tf.flags.DEFINE_integer(
    "num_readers",
    2,
    "The number of parallel readers that read data from the dataset."
)
tf.flags.DEFINE_integer(
    "save_checkpoint_steps",
    10,
    ""
)
tf.flags.DEFINE_integer(
    "save_summary_steps",
    10,
    "The frequency with which summaries are saved, in steps."
)

#: Path

tf.flags.DEFINE_string(
    "checkpoint_path",
    "/root/tmp/checkpoint",
    ""
)
tf.flags.DEFINE_string(
    "dataset_path",
    "/root/tmp/dataset",
    ""
)
tf.flags.DEFINE_string(
    "tensorboard_path",
    "/root/tmp/tensorboard",
    ""
)

FLAGS = tf.flags.FLAGS
