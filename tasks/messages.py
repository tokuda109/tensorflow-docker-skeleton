# -*- coding: utf-8 -*-

from config import config

__all__ = (
    "msg",
)


class Message(dict):

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)

        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)


msg = Message({
    "command_not_found": "Command `{}` not found.",

    "up_already_running": "Machine `{}` is already running.".format(config.get("machine_name")),

    "build_dockerfile_does_not_exist": ""
})
