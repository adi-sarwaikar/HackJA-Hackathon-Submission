import wikipedia
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def main_function(userQuery):
    reliableSourcesFinal = []
    reliableSourcesLvl1 = []

    reliableSuffixes = [".org", ".gov", ".edu"]
    
    print("Finding sources...")

    possibilities = wikipedia.search(userQuery)
    wikipediaPage = possibilities[0]

    possibleReferences = wikipedia.page(wikipediaPage).references

    print(len(possibleReferences), " possibilities found. Now checking reliability of each source. ")

    for reference in possibleReferences:
        for suffix in reliableSuffixes:
            if suffix in reference:
                reliableSourcesLvl1.append(reference)

    for source in reliableSourcesLvl1:
        try:
            document = urlopen(source, context=ctx)
        except:
            continue
        if document.getcode() != 200:
            continue
        print(source)
        reliableSourcesFinal.append(source)
        if len(reliableSourcesFinal) == 10:
            break

    return reliableSourcesFinal