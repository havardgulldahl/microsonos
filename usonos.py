'Module to interface with sonos speakers'

# https://developer.sony.com/develop/audio-control-api/get-started/play-dlna-file#tutorial-step-3
# https://stackoverflow.com/questions/28422609/how-to-send-setavtransporturi-using-upnp-c#29129958
# 

#import urequests # micropython-lib
from urequest11 import urlopen # micropython-lib


PLAYMSG = """<?xml version="1.0" encoding="utf-8"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
  <s:Body>
    <u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
      <InstanceID>0</InstanceID>
      <Speed>1</Speed>
    </u:Play>
  </s:Body>
</s:Envelope>"""

METADATAMSG = """<DIDL-Lite xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns="urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/"
xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/"
xmlns:dlna="urn:schemas-dlna-org:metadata-1-0/"
xmlns:arib="urn:schemas-arib-or-jp:elements-1-0/"
xmlns:av="urn:schemas-sony-com:av">
  <item id="{id}" restricted="1" parentID="35">
    <dc:title>{title}</dc:title>
    <upnp:class>object.item.audioItem.musicTrack</upnp:class>
  </item>
</DIDL-Lite>"""

SETAVTRANSPORTMSG = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
   <s:Body>
      <u:SetAVTransportURI xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
         <InstanceID>{id}</InstanceID>
         <CurrentURI>{uri}</CurrentURI>
         <CurrentURIMetaData></CurrentURIMetaData>
      </u:SetAVTransportURI>
   </s:Body>
</s:Envelope>"""

def _sonostransport(ip, action, payload):
  'post the soap payload to the sonos speaker  at ip'
  player_endpoint = 'http://{}:1400/MediaRenderer/AVTransport/Control'.format(ip)
  headers = { 'Soapaction': 'urn:schemas-upnp-org:service:AVTransport:1#{}'.format(action) ,
              'Content-Type': 'text/xml; charset=utf-8'}
  print(player_endpoint)
  #return urequests.post(url=player_endpoint,
                        #data=payload,
                        #headers=headers)
  return urlopen(player_endpoint,
                 data=payload,
                 method='POST',
                 headers=headers)


def set_url(ip, url):
  'Queue the audio at url on the sonos speaker at ip'
  # replace uri scheme with something that sonos preferes
  colon = url.find(':')
  if colon > 0:
    url = 'x-rincon-mp3radio{0}'.format(url[colon:])
  payload = SETAVTRANSPORTMSG.format(id=0, uri=url)
  resp = _sonostransport(ip, 'SetAVTransportURI', payload)
  print('Got response: {!r}'.format(resp.read()))
  resp.close()

def play(ip):
  'Play the speaker at ip'
  payload = PLAYMSG
  resp = _sonostransport(ip, 'Play', payload)
  print('Got response: {!r}'.format(resp.read()))
  resp.close()

def test_podcast(ip):
  podcasturl = 'https://podkast.nrk.no/fil/dagsnytt_atten/dagsnytt_atten_2018-11-23_1825_3108.MP3'
  set_url(ip, podcasturl)
  play(ip)

if __name__ == '__main__':
  import sys
  ip = sys.argv[1]
  url = sys.argv[2]
  print(test_podcast(ip))
