The data in this directory is extracted using the site's REST API.  A REST API returns data in JSON format.  The site's API is accessed by prefixing URLs with api.openparliament.ca (as opposed to simply openparliament.ca).  

For example, go to
http://api.openparliament.ca/politicians/stephen-harper/ for a web page explaining the query result for Stephen
Harper’s data (e.g., name, party and riding). 
To get the data directly in the JSON format, you just add ?format=json at the
end of the string, (i.e., http://api.openparliament.ca/politicians/stephen-harper/?format=json).
This JSON file corresponding to Harper is in data/politicians/ if you unzip data.tar.gz.

The data was downloaded on June 18, 2014.