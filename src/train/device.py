# -*- coding: utf-8 -*-

from flags import FLAGS

__all__ = (
    "get_device",
)


device = None


class Device(object):

    @property
    def device_list(self):
        """
        """
        devices = range(FLAGS.num_gpus)
        if len(devices) is 0:
            devices = [0]
        return devices

    @property
    def count(self):
        """
        """
        c = FLAGS.num_gpus
        if c == 0 and self.is_cpu():
            return 1
        return c

    def is_cpu(self):
        """
        """
        return FLAGS.num_gpus == 0

    def is_gpu(self):
        """
        """
        return FLAGS.num_gpus > 0

    def make_device_name(self, id):
        """
        """
        device_name = "/"

        if self.is_gpu():
            device_name += "gpu:"
        elif self.is_cpu():
            device_name += "cpu:"

        device_name += str(id)

        return device_name


def get_device():
    global device

    if device is None:
        device = Device()

    return device
