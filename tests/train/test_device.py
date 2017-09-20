# -*- coding: utf-8 -*-

from unittest import TestCase

from device import get_device


class DeviceTestCase(TestCase):

    def setUp(self):
        self.device = get_device()

    def test_device_list(self):
        self.assertEqual(self.device.device_list, [0])

    def test_count(self):
        self.assertEqual(self.device.count, 1)

    def test_is_cpu(self):
        self.assertTrue(self.device.is_cpu())
