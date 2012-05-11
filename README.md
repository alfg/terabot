terabot
=======

A simple *work-in-progress* IRC bot with with TeraTome.com querying capabilities.

#### Installation

    $ pip install BeautifulSoup twisted
    $ python terabot.py
    
#### Configure

Configure the following variables in terabot.py.

```
HOST = 'irc.freenode.net'
PORT = 6667
CHANNELS = ['#terabottest']
NICK = 'terabot'
```

#### Usage

To search an item, type `!(search term here)`:

Example:

    !aegis
    
This will return a list of items under the criteria of the search term, each with an item ID.

To query a specific item, specify the ID instead of the search term by typing `!(ID here)`.

Example:

    !12882
    
#### Notes

* This is a screen scraping IRC bot, so please use responsibly.
* Due to the nature of screen scraping, any changes to teratome.com can result in breaking the script. If
this happens, file an issue and I will fix (or fork and send a pull request).
* The bot can easily get kicked and/or banned from IRC channels for spamming if the search results are high. Use sparingly
until I can add support to limit the results outputted.

#### To Do

* Add feature to limit search results and provide a link to full search results list.
* Channel password support.
* Add logging plugin (and more eventually).