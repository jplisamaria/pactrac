from xml.etree import ElementTree as ET
import urllib.request, urllib.error, urllib.parse
import xml.dom.minidom
import cgi, cgitb

#read in id - this needs to be modified for production to read in the tracking ID(s)
#id="9534612156126123269099"


def usps_call(id):
    #URI for API
    url = 'http://production.shippingapis.com/Shipping.dll?API=TrackV2&'
    #XML data to wrap around tracking id
    usps_string_start='XML=<TrackRequest USERID="586USTGL6982"><TrackID ID="'
    usps_string_end='"></TrackID></TrackRequest>'

    #construct XML data
    xml_data = usps_string_start + id + usps_string_end

    #encode information for post request
    data = xml_data.encode('UTF-8')

    #used to ensure that url and encoding worked 
    #print (url)
    #print (data)

    #create request and add headers
    req = urllib.request.Request(url, data)
    req.add_header("Accept", "*/*")
    req.add_header("Content-Type","application/xml; charset=utf-8")


    #create the call to the API
    response = urllib.request.urlopen(req)

    #save the response from the API call
    html = response.read()

    #used to check that html was the correct string
    #print (html)

    dom = xml.dom.minidom.parseString( html.decode())

    #used to ensure that dom object was created
    #print (dom)

    #obtain the value from the TrackSummary tag
    summary = dom.getElementsByTagName("TrackSummary")
    for each in summary:
        print ("%s\n" % summary[0].firstChild.nodeValue)

    #obtain the value(s) from the TrackDetail tag(s)
    details = dom.getElementsByTagName("TrackDetail")
    #details_list = []
    for detail in details:
#detail_list += __getText(detail.childNodes)
#return detail_list
        print ("%s\n" % __getText(detail.childNodes))
		
#function to parse text from nodes
def __getText(nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
