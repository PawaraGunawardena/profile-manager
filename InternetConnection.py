import urllib
from urllib.request import urlopen

URL = 'https://www.google.com'
def is_connected_to_network(URL= 'https://www.google.com'):
    try:
        urlopen(URL, timeout=1)
        return True
    except:
        # print(Error)
        return False



if __name__ == '__main__':
    if is_connected_to_network(URL):
        print("Internet is active")
    else:
        print("Internet disconnected")

