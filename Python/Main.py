#Nova --Version 0.0.1-alpha
import Libraries, Text_to_Speech, Connection

#condition: internet is connected
if Connection.check_wifi():
    Text_to_Speech.wifi_connection_successful()
#condition: internet is not connected
if Connection.check_wifi() == False:
    print('Sir, I am trying to establish connection to internet. Kindly switch-on your mobile hotspot!')
    Libraries.time.sleep(15)
    connect_to_wifi_1 = Libraries.subprocess.run('netsh wlan connect ssid="G5s Hotspot" name="G5s Hotspot"', shell=True)
    if (connect_to_wifi_1.returncode == 0):
        Text_to_Speech.wifi_connection_successful()
    else:
        Connection.add_wlan_profile()
        connect_to_wifi_2 = Libraries.subprocess.run('netsh wlan connect ssid="G5s Hotspot" name="G5s Hotspot"', shell=True)
        if (connect_to_wifi_2.returncode == 0):
            Text_to_Speech.wifi_connection_successful()
        else:
            Connection.open_wifi()
            connect_to_wifi_3 = Libraries.subprocess.run('netsh wlan connect ssid="G5s Hotspot" name="G5s Hotspot"', shell=True)
            if (connect_to_wifi_3.returncode == 0):
                Text_to_Speech.wifi_connection_successful()
            else:
                Connection.wifi_unsuccessful()
                #libraries.subprocess.run('netsh wlan delete profile name="G5s Hotspot"', shell=True)
                #libraries.sys.exit()