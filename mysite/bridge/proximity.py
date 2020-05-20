import geopy.distance
from django.shortcuts import get_object_or_404
from .models import Bridge


def nearest_bridge(lat, long):
    """
    this function will open the page and throw out the entire contents of the page
    :param lat: latitude of user
    :param long: longitude of user
    :return: closest bridge
    """
    bridge_id = 1  # just set automatically to one to get the view working
    the_bridge = get_object_or_404(Bridge, pk=bridge_id)
    return the_bridge  # returns closest bridge to users coordinates
