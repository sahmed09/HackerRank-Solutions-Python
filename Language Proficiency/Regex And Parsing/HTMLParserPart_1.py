from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)


html = ""
for _ in range(int(input())):
    html += input().strip()

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html)
parser.close()
