# module to interface with sonos speakers

# https://developer.sony.com/develop/audio-control-api/get-started/play-dlna-file#tutorial-step-3
# https://stackoverflow.com/questions/28422609/how-to-send-setavtransporturi-using-upnp-c#29129958
# 

PLAYMSG = """
<?xml version="1.0" encoding="utf-8"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
  <s:Body>
    <u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
      <InstanceID>0</InstanceID>
      <Speed>1</Speed>
    </u:Play>
  </s:Body>
</s:Envelope>"""

METADATAMSG = """
<DIDL-Lite xmlns:dc="http://purl.org/dc/elements/1.1/"
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

SETAVTRANSPORTMSG = """
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
   <s:Body>
      <u:SetAVTransportURI xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
         <InstanceID>{id}</InstanceID>
         <CurrentURI>{uri}</CurrentURI>
         <CurrentURIMetaData></CurrentURIMetaData>
      </u:SetAVTransportURI>
   </s:Body>
</s:Envelope>"""

