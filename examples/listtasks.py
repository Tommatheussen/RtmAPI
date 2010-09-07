import sys
import webbrowser
import xml.etree.ElementTree as ElementTree
from rtmapi import Rtm

if __name__ == '__main__':
    # call the program as `example.py [api_key] [shared_secret]`
    # get those parameters from http://www.rememberthemilk.com/services/api/keys.rtm
    api_key, shared_secret = sys.argv[1:]
    api = Rtm(api_key, shared_secret, "read")
    
    # authenication block, see http://www.rememberthemilk.com/services/api/authentication.rtm
    # check for valid token
    if not api.token_valid():
        # use desktop-type authentication
        url, frob = api.authenticate_desktop()
        # open webbrowser, wait until user authorized application
        webbrowser.open(url)
        raw_input("Continue?")
        # get the token for the frob
        api.retrieve_token(frob)
        # print out new token, should be used to initialize the Rtm object next time
        # (a real application should store the token somewhere)
        print "New token: %s" % api.token
    
    # get all open tasks, see http://www.rememberthemilk.com/services/api/methods/rtm.tasks.getList.rtm
    for tasklist in api.rtm.tasks.getList(filter="status:incomplete").tasks.list:
        for taskseries in tasklist.taskseries:
            print taskseries.task[0].due, taskseries.name
