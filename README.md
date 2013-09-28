EasyMapper
==========

The Easy Mapper shows you how to connect a Google doc to a Django application, pull in data, Geocode it and put it on a Leaflet.js map using OpenStreetMap.

# Getting started

First, install your requirements:

```pip install -r requirements.txt```

I have an alias in my .zshrc (or put it in your bash_profile) to turn my postgres on:

```alias pgup='pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start'```

Then make sure your postgres is up:

```pgup

Next, let's create the database for this application:

```createdb easymapper```

Now enter the postgres shell:

```psql easymapper```

In the psql shell you'll need to create your postgis extensions and whatnot. So enter this in the shell:

```CREATE EXTENSION postgis;```
```CREATE EXTENSION postgis_topology;```
```\q```

Now you should have the proper things to sync your database. Do this from your project root (where the manage.py file is):

```python manage.py syncdb```

OR run it all as one line:

```createdb easymapper && psql -c "create extension postgis; create extension postgis_topology;" easymapper && ./manage.py syncdb```


