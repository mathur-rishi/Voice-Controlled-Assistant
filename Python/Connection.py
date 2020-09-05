import Libraries

#function definitions
def add_wlan_profile():
    Libraries.subprocess.run('netsh wlan add profile filename="../Credentials/G5s_Hotspot.xml"', shell=True)
def open_wifi():
    Libraries.subprocess.run('start ms-settings:network-wifi', shell=True)
    Libraries.time.sleep(15)
def wifi_unsuccessful():
    print('Sir, connection establishment to internet was unsuccessful!')

#check network connection
def check_wifi():
    try:
        Libraries.urllib.request.urlopen('https://www.google.com/')
        return True
    except:
        return False