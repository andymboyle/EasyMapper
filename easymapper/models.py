from django.contrib.gis.db import models
from django.db.models.signals import pre_save
from django.contrib.gis.geos import Point
from django.conf import settings
from urllib2 import HTTPError

import logging
logger = logging.getLogger(__name__)

from geopy import geocoders

us = geocoders.GeocoderDotUS()


class Location(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    address_point = models.PointField(blank=True, null=True, srid=102671)
    geocoded_correct = models.BooleanField(blank=True)

    objects = models.GeoManager()

    _address_point4326 = None

    def __unicode__(self):
        return self.address

    @property
    def address_point4326(self):
        """
        Return the coordinates of this shooting in WGS84 (EPSG:4326) as a
        list of 'lat' and 'lng'
        """
        try:
            if self._address_point4326 is None:
                self._address_point4326 = self.address_point.transform(
                    4326, clone=True)
            return self._address_point4326
        except:
            return None


def geocode_address(sender, instance, **kwargs):
    """
    Geocode the address if an address_point doesn't exist, using the first
    lat/lng that is found. If you get an HTTPError, log it, but try ten times
    before completely failing and store geocoded_correct as False.
    """
    if not instance.address_point:
        logger.debug("Geocode address: %s" % instance.address)
        counter = 0
        while True:
            try:
                # TODO: Test this syntax works for us geocoder
                result = list(us.geocode(
                    instance.address, exactly_one=False))

                if len(result) == 0:
                    return False
                else:
                    place, (lat, lng) = result[0]
                    logger.debug(result[0])
                    break

                continue
            except HTTPError:
                logger.debug(
                    'HTTPError: failed to geocode "%s"' % instance.address)
            if counter == 10:
                logger.info("Tried 10 times, so failing.")
                instance.geocoded_correct = False
                return
            counter += 1

        instance.address_point = Point(lng, lat, srid=4326)

pre_save.connect(
    geocode_address, sender=Location,
    dispatch_uid="geocode_location_address")
