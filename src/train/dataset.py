# -*- coding: utf-8 -*-

import glob
import os

import tensorflow as tf
from tensorflow.contrib.data import Dataset

from flags import FLAGS
from logger import get_logger

__all__ = (
    "configure_dataset",
)


def configure_dataset():
    """
    :returns:
    """
    logger = get_logger()

    image_list = []
    image_list.extend(glob.glob(os.path.join(
        FLAGS.dataset_path,
        "ch4_training_images",
        "*.jpg"
    )))

    image_list_op = tf.constant(image_list)

    logger.debug("image_list_op: {}".format(image_list_op))

    dataset_iterator = Dataset.from_tensor_slices(image_list_op)

    next_images = dataset_iterator.make_one_shot_iterator().get_next()

    #: Create a random shuffle queue.
    queue = tf.RandomShuffleQueue(
        capacity=20,
        min_after_dequeue=int(0.9 * 20),
        shapes=next_images.shape,
        dtypes=next_images.dtype
    )

    #: Create an op to enqueue one item.
    enqueue = queue.enqueue(next_images)

    #: Create a queue runner.
    qr = tf.train.QueueRunner(queue, [enqueue] * 2)

    tf.train.add_queue_runner(qr)

    return queue.dequeue_many(FLAGS.batch_size)
