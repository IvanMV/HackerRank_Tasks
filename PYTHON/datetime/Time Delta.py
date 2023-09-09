'''
When users post an update on social media,such as a URL, image, status update etc., other users 
in their network are able to view this new post on their news feed. Users can also see exactly 
when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. 
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
'''

import os
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = '%a %d %b %Y %H:%M:%S %z'
    date_1 = datetime.datetime.strptime(t1, format)
    date_2 = datetime.datetime.strptime(t2, format)
    d_1_sec = int(date_1.timestamp())
    d_2_sec = int(date_2.timestamp())
    delta = abs(d_1_sec - d_2_sec)
    return str(delta)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
