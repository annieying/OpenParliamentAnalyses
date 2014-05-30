The data in this directory is extracted from the OpenParliment site's REST API.  The REST API conveniently returns files in JSON format.  The site's API is accessed by prefixing URLs with api.openparliament.ca (as opposed to simply openparliament.ca).  

For example, go to
http://api.openparliament.ca/politicians/stephen-harper/ for a web page explaining the query result for Stephen
Harper’s data (e.g., name, party and riding). 
To get the data directly in the JSON format, you just add ?format=json at the
end of the string, (i.e., http://api.openparliament.ca/politicians/stephen-harper/?format=json).
This JSON file corresponding to Harper is in data/politicians/ if you unzip data.tar.gz.

Unfortunately the information here is a bit dated as they are downloaded on Sept 24, 2014.  The next step will be to download the most update-to-date information.
