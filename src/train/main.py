# -*- coding: utf-8 -*-

import tensorflow as tf

from config import get_config
from device import get_device
from flags import FLAGS
from logger import get_logger


def main(unused_argv):
    """
    """
    config = get_config()
    logger = get_logger()
    device = get_device()

    input_images = tf.placeholder(
        tf.float32,
        shape=[None, None, None, 3],
        name="input_images"
    )

    logger.debug("input_images: {}".format(input_images))

    for i, device_id in enumerate(device.device_list):
        device_name = device.make_device_name(device_id)

        logger.debug("device_name: {}".format(device_name))

    init_op = tf.global_variables_initializer()

    with tf.Session(config=config) as sess:
        sess.run(init_op)

        coord = tf.train.Coordinator()

        enqueue_threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        for step in range(FLAGS.max_steps):
            logger.debug("step: {:06d}".format(step))

            if step % FLAGS.save_checkpoint_steps == 0:
                pass

            if step % FLAGS.save_summary_steps == 0:
                pass

        coord.request_stop()

        coord.join(enqueue_threads)


if __name__ == "__main__":
    tf.app.run()
