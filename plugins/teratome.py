#!/usr/bin/env python

'''

#### teratome.py ####

Terabot plugin to query data from teratome.com

'''
import re
import urllib2
import sys
import readline
from BeautifulSoup import BeautifulSoup

def teratome(query):
    ''' Main function called and checks if query is a number or string '''
    query = query.replace(" ", "+")
    if query.isdigit() == True:
        try:
            data = querySingleItem(query)
        except:
            return ["No results found."]

    elif query.isdigit() == False:
        try:
            data = querySearchItems(query)
        except:
            return ["No results found."]

    else:
        return "Error. Something went wrong."
    return data


def querySingleItem(query):
    ''' If query is a number, then this function is run and returns an item '''
    query = query.replace(" ", "+")

    #If user input is a number, then look for an item id
    #query html
    html = BeautifulSoup(urllib2.urlopen('http://www.teratome.com/item/%s' % query).read())

    item = []
    #Render output nicely
    itemname = html.find('div', {'class' : re.compile(r".*\bname\b.*")}).text
    itemlevel = html.find('div', {'class' : re.compile(r".*\blevel\b.*")}).text
    itemallowances =  html.find('div', {'class' : re.compile(r".*\ballowances\b.*")}).text
    itemitemlevel = html.find('div', {'class' : re.compile(r".*\bitemlevel\b.*")}).text
    itemstats = html.find('div', {'class' : re.compile(r".*\bstats\b.*")}).text

    item.append(itemname) 
    item.append(itemlevel)
    item.append(itemallowances)
    item.append(itemitemlevel)
    item.append(itemstats)

    print item
    return item


    #If user input is not a number, then run a search
def querySearchItems(query):
    ''' If query is NOT a number, then this function is run and returns a list of items '''
    #Make query to search form
    html = BeautifulSoup(urllib2.urlopen('http://www.teratome.com/search/%s' % query).read())
    htmlitems = html.find(id="tabcont-items")

    itemlist = []
    #Gather data and enter into pretty rows
    for row in htmlitems('table', {'class' : 'default'})[0].tbody('tr'):
        
        #regex find href link and save only numbers to id
        id = re.sub("\D", "", row.findAll('a')[0].get('href'))
        
        itemid = id
        itemname = row.findAll('td')[0].text
        itemlevel = row.findAll('td')[2].text
        itemcat = row.findAll('td')[4].text
            
        items = itemid + ' - ' + itemname + ' - ' + itemlevel + \
                ' - ' + itemcat
        itemlist.append(items)

        print items
    return itemlist

if __name__ == "__main__":
    ''' If script invoked directly, then run teratome() below. (For debugging) '''
    try:
        teratome("15821")
        teratome("aegis")
    except KeyboardInterrupt:
        print "\n Bye"
        sys.exit()
    except IndexError:
        print "No results found. Try another query or press Ctrl+C to quit."

