# BrownUniversityCAB-overlay

Google chrome extension which overlays the Courses@Brown (CAB) website with professor/class reviews from thecriticalreview.org

Contributors:
------------

           Ken Noh @SquareDorito.
           Griffin Kao @griffink3


Installation:
------------

First install Node.js at https://nodejs.org/en/download/
```
npm install request
npm install cheerio
```
Follow instructions for installing Express.js at http://expressjs.com/en/starter/installing.html
```
npm install
```

To run the node server:
```
node server
```

Open web browser and go to:
```
http://localhost:8081/scrape
```
This should run the the javascript and produce an output.json in the app directory of the scraped data.


License
-------
MIT License.
