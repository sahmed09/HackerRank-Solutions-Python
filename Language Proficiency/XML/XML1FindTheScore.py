import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(child) for child in node)
    # return etree.tostring(node).count(b"=")
    # return sum([len(elem.items()) for elem in tree.iter()])


if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    xml = ""
    for _ in range(int(input())):
        xml += input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
