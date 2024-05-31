#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data to.
    """
    def dict_to_xml(tag, d):

        elem = ET.Element(tag)
        for key, val in d.items():
            child = ET.SubElement(elem, key)
            child.text = str(val)
        return elem


    root = dict_to_xml('data', dictionary)
    

    tree = ET.ElementTree(root)

    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):

    def xml_to_dict(element):

        return {child.tag: child.text for child in element}

    tree = ET.parse(filename)
    
    root = tree.getroot()

    return xml_to_dict(root)
