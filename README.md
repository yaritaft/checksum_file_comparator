# Checksum File Comparator

## Story time

The other day, I had an issue. For some reason I copied some videos to my external hard drive and  when I was watching them, I realized that the were corrupted. And when I copied them I didn't receive any warning. Then some hours later I had the very same issue again.
## Purpose

This script is for checking that some files that have the same name in two different directories are equal in check sum terms ( in other words that they are the very same thing ). To check if you made a proper backup.

## How to use it

Modify scripts paths and then do:


```
python3 md5check.py
```

The script will tell you if there are any differences between them.