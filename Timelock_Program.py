################################################################
# Anassas Anderson, James Brooks, Chance Harlon, Clay Hopkins, #
# Mason Kelley, Patrick McDonald, Johnathon Terry              #
# CSC 442/542, CYEN 301                                        #
# Program #5: TimeLock                                         #
# May 6, 2022                                                  #
################################################################

# import necessary libraries
import datetime as dt
import time
import hashlib as h
from sys import stdin
import re

# Debugging variable
DEBUG = False

# variables to keep track of given epoch time and current time
cur_time = "2017 03 23 18 02 06"
epoch = ""

# to get current time if one is not specified
#cur_time = dt.datetime.now().strftime("%Y %m %d %H %M %S")

# get epoch date from stdin
for line in stdin:
    epoch += line

# ignore any newline character in epoch date
epoch_date = epoch.rstrip("\n")

# make sure a valid epoch date was given
req_format = re.compile('\d{4} \d{2} \d{2} \d{2} \d{2} \d{2}')

# if an invalid epoch date was given then ask user for another valid one
if req_format.match(epoch_date) is None or len(epoch_date) != 19:
    print("Provide a proper epoch please\n\ti.e. '1974 06 01 08 57 23'")
    exit()

# convert epoch and current date into datetime structure objects
# for easier manipulation and processing
epoch_datetime = time.strptime(epoch_date, "%Y %m %d %H %M %S")
cur_datetime = time.strptime(cur_time, "%Y %m %d %H %M %S")

# convert epoch and current datetime structs into datetime.datetime objects
epoch = dt.datetime(epoch_datetime.tm_year, epoch_datetime.tm_mon, epoch_datetime.tm_mday, epoch_datetime.tm_hour, epoch_datetime.tm_min, epoch_datetime.tm_sec)
cur_time = dt.datetime(cur_datetime.tm_year, cur_datetime.tm_mon, cur_datetime.tm_mday, cur_datetime.tm_hour, cur_datetime.tm_min, cur_datetime.tm_sec)

# convert epoch and curretn datetime.datetime objects into UTC time
# in order to ignore the time change when computing elapsed time
epoch_deltatime = dt.datetime.utcfromtimestamp(dt.datetime.timestamp(epoch))
cur_deltatime = dt.datetime.utcfromtimestamp(dt.datetime.timestamp(cur_time))

# Since we only create a new code every for every 60 seconds
# that has elapsed since the epoch time. We use offset to determine
# where our current time is in this 60 second period.
offset = 0

# if current time seconds is not at the beginning of epoch
# code interval then update the offset
if cur_datetime.tm_sec != epoch_datetime.tm_sec:
    # if epoch seconds are greater than current time seconds
    if epoch_datetime.tm_sec > cur_datetime.tm_sec:
        offset = 60 - abs(epoch_datetime.tm_sec - cur_datetime.tm_sec)
    
    # otherwise current time seconds must be greater...
    else:
        offset = abs(epoch_datetime.tm_sec - cur_datetime.tm_sec)

# delta time holds the elapsed time in seconds from epoch to
# the start of the new code interval that is closest to current time
delta_time_sec = (cur_deltatime - epoch_deltatime).total_seconds() - offset

# hash val is the double md5 hashed hex value of our delta time
hash_val = h.md5(str(h.md5(str(int(delta_time_sec)).encode()).hexdigest()).encode()).hexdigest()

# debugging
if (DEBUG):
    print(f"delta = {delta_time_sec}\ncurrent time = {cur_deltatime}\nepoch = {epoch_deltatime}")
    print(f"hash val = {hash_val}")

# back will store the last two numbers
# and front will store the first to characters
# that will make up our code
back, front = "", ""

# iterate through the charactrs from left to right
# in our hash value. Only taking the first two chars
for char in hash_val:
    # if two chars have already been selected then break loop
    if len(front) >= 2:
        break

    # if current char is an alphabetic char
    if char.isalpha():
        front += char

# iterate through the integers from right to left
# in our hash value. Only taking the first two digits
for num in reversed(hash_val):
    # if two digits have already been selected then break loop
    if len(back) >= 2:
        break

    # if current num is not an alphabetic char
    # then it must be a digit
    if not num.isalpha():
        back += num

# concatenate front and back to make our code
result = front + back

# print our code to the terminal
print(result)
