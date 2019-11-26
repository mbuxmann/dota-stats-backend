#!/bin/sh
python3 database/update.py >> updatelog.txt && echo "Done Updating"
