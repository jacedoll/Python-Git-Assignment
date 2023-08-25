import time

# seconds passed since epoch
seconds = 1672215379.5045543

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)