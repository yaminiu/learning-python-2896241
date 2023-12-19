# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#

import xml.dom.minidom
def main():
    # use the parse() function to load and parse an XML file
    path = r'C:\Users\ethan\OneDrive\Documents\GitHub\learning-python-2896241\Ch5 - Internet Data\samplexml.xml'
    doc = xml.dom.minidom.parse(path)
    
    # print out the document node and the name of the first child tag

    # get a list of XML tags from the document and print each one

    # create a new XML tag and add it into the document

if __name__ == "__main__":
    main()

