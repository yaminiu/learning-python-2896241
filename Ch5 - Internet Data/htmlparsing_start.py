# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pass

    def handle_starttag(self, tag, attrs):
        pass
        
    def handle_data(self, data):
        pass

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    path = r'C:\Users\ethan\OneDrive\Documents\GitHub\learning-python-2896241\Ch5 - Internet Data\samplehtml.html'
    f = open(path)
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)  
    print("Paragraph tags:", paragraphs)  
    
if __name__ == "__main__":
    main()
  