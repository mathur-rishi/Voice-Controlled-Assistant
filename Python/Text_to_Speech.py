#import all libraries
import Libraries, Credentials

#aws polly text-to-speech
def nova(txt):
    response = Credentials.polly_client.synthesize_speech(Engine='neural', LanguageCode='en-US', VoiceId='Matthew', OutputFormat='mp3', Text=txt)
    file = open('../Audio_Data/Nova.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    #play audio inside python
    Libraries.playsound('../Audio_Data/Nova.mp3')

#for connection.py
def wifi_connection_successful():
    nova('Sir, connection to internet established, I am up & running')