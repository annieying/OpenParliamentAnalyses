import json
import os
import sys
import urllib2


url_front = 'http://api.openparliament.ca';

directory = "/diskless/local/annie/workspaces/20140530-OpenParliamentAnalyses/";
path_middle = "TestPython/json-downloaded/data/bills-p"
 
 
def get_bills_recurse(url_suffix, i):
    url = url_front + url_suffix;
    req = urllib2.Request(url)
    handler = urllib2.urlopen(req)
    content = handler.read()
    
#     print handler.getcode()
#     print handler.headers.getheader('content-type')
#     print content
    

    bill_file = directory + path_middle + `i` + ".json";
    text_file = open(bill_file, "w")
    text_file.write(content) 
    text_file.close()
    
    with open(bill_file) as data_file:
        try:
            data=json.load(data_file)
        except:
            print "Error in loading JSON file:%s"%(bill_file)
            print "Try specifying the complete path"
            
    print "loaded data " + url
    new_url_suffix = data["pagination"]["next_url"]
    if new_url_suffix:
        get_bills_recurse(new_url_suffix, i+1);

def get_bills():
    
    first_url = 'http://api.openparliament.ca/bills/?limit=500&offset=0'    
    print "downloading bills from " + first_url
    get_bills_recurse("/bills/?limit=500&offset=0",1)
    
    
if __name__=="__main__":
    get_bills()