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
    
    #xml_files = [file + ".xml" for file in files]
    #xml_files = glob.glob(files +"/*.xml")
    #print(files)
    xml_element_tree = None
    for xml_file in glob.glob("*.xml"):
    #for xml_file in files:
        print(xml_file)
        data = ElementTree.parse(xml_file).getroot()
        # print ElementTree.tostring(data)
        #print (data)
        #print (xml_file)
        for result in data.iter('GlassList'):
            newKid = ElementTree.Element('File_Name', name=xml_file)
            result.insert(0,newKid);
        for result in data.iter('DocumentElement'):
            #print("D0")
            if xml_element_tree is None:
                #print ("D1")
                xml_element_tree = data 
                #insertion_point = xml_element_tree.findall("./DocumentElement")[0]
                insertion_point = data
                #print ("insertion_point" + insertion_point)
            else:
                #print ("D2")
                insertion_point.extend(result)
    if xml_element_tree is not None:
        with open(out_file,'wb') as f:
            f.write(ElementTree.tostring(xml_element_tree))
    else:
        print("2")

tmpDir = filedialog.askdirectory()
os.chdir(tmpDir)
print (tmpDir)
run(os.listdir())
