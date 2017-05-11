###############################

Export Raw Events from Mixpanel

###############################

- Copy settings_sample.py to make settings_local.py

- put your mixpanel project's API Secret and also project name in settings_local.py

- Run `python batch.py`

- Enter from and to-date in YYYY-MM-DD format

- It will start downloading monthwise json files in the current directory


**

Convert json files to csv

**

- Run `./batch-convert.sh`
