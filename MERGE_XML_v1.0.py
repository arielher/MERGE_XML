import os, os.path, sys
import glob
from xml.etree import ElementTree
from tkinter import *
from tkinter import filedialog

def run(files):
    out_file = 'output.xml';
    try:
        os.remove(out_file)
    except OSError:
        pass
    xml_element_tree = None
    for xml_file in glob.glob("*.xml"):
        print(xml_file)
        data = ElementTree.parse(xml_file).getroot()
        for result in data.iter('GlassList'):
            newKid = ElementTree.Element('File_Name', name=xml_file)
            result.insert(0,newKid);
        for result in data.iter('DocumentElement'):
            if xml_element_tree is None:
                xml_element_tree = data 
                insertion_point = data
            else:
                insertion_point.extend(result)
    if xml_element_tree is not None:
        with open(out_file,'wb') as f:
            f.write(ElementTree.tostring(xml_element_tree))
    else:
        print("Error: file not created")


tmpDir = filedialog.askdirectory()
os.chdir(tmpDir)
print (tmpDir)
run(os.listdir())
