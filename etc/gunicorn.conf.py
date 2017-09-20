#
# Process naming
#
proc_name = "gunicorn"

#
# Server socket
#
bind = "0.0.0.0:8080"

#
# Worker processes
#
workers = 1
timeout = 30
keepalive = 2

#
# Logging
#
errorlog = "-"
loglevel = "debug"
accesslog = "-"

chdir = "/root/src/server"

reload = True
