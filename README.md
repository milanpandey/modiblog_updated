modiFeed Blog- News feeds of Mr. Narendra Modi
========

This project has been created using Django web framework and Angularjs & Bootstrap in the front end. 
###Purpose:
The main aim of this blog is to fetch the latest news and photos of a celebrity. The Celebrity(in this case Mr. Narendra Modi) can be replaced by making simple changes to the code.


###Components:
  
  * [Django REST](http://www.django-rest-framework.org/): Django is a free and open source web application framework, written in Python, which follows the  model–view–controller architectural pattern.
  * [Bootstrap](http://getbootstrap.com/): it is a free collection of tools for creating a websites and web applications. It contains HTML and CSS-based design templates for typography, forms, buttons, navigation and other interface components, as well as optional JavaScript extensions.
  * [Angularjs](https://angularjs.org/): AngularJS is an open-source web application framework, maintained by Google and community, that assists with creating single-page applications, one-page web applications that only require HTML, CSS, and JavaScript on the client side.
  * [MongoDb](http://www.mongodb.org/):  is a cross-platform document-oriented database. Classified as a NoSQL database, MongoDB eschews the traditional table-based relational database structure in favor of JSON-like documents with dynamic schemas (MongoDB calls the format BSON), making the integration of data in certain types of applications easier and faster.
  * [Git](http://git-scm.com/): its a disitributed version control system.
  * [Redis](redis.io): Redis is an open-source, networked, in-memory, key-value data store with optional durability. 

Now we know the components in use, so now I can explain how they work togheter. I'm using Django Rest API to provide the data stored in models to the frontend anfularj view. There is a python script that runs at regular intervals to fetch the latest news feeds about Mr. Narendra Modi and store it in the database. The frontend uses bootstrap template and few other scripts. In this project, the news data is bieng grabbed using the feeds from Google News. Redis has been used for holding the database in memory.
