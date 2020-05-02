from mysite.bridge.models import Bridge  # Import the model classes we just wrote

#these are the indices for the bridge (can be changed if needed)
NAME = 0
DATE_BUILT = 1

def data_input(bridge):

    #bridge is a list with the name, date built

    bridge_name = bridge[NAME]
    bridge_built = bridge[DATE_BUILT]

    # Create a new Bridge object.

    q = Bridge(name= bridge_name, year_built= bridge_built)

    q.save()


