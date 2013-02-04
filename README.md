see-heart
=========

Inspect the heartbeat reported by nova services.
Defaultly, nova-services will report its state into database, and type a record
in log file. The script look through the log files to see whether the interval
of two report is valid. If the interval is too long, it may lead to RPC timeout
and some other strange exceptions.
