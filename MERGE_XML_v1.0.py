import os, os.path, sys
import glob
from xml.etree import ElementTree
from tkinter import *
from tkinter import filedialog

## Merger function
def run(files):
    ## Delete older output file
    out_file = 'output.xml';
    try:
        os.remove(out_file)
    except OSError:
        pass
    xml_element_tree = None
    ## Iterate over all xml files
    for xml_file in glob.glob("*.xml"):
        data = ElementTree.parse(xml_file).getroot()
        ## Add a new element to all groups, with the file name as a value
        for result in data.iter('GlassList'):
            newKid = ElementTree.Element('File_Name', name=xml_file)
            result.insert(0,newKid);
        ## Merge 
        for result in data.iter('DocumentElement'):
            if xml_element_tree is None:
                xml_element_tree = data 
                insertion_point = data
            else:
                insertion_point.extend(result)
    ## Remove unnecesary attribute, and create a new 'area' attribute
    for GlassList in xml_element_tree.findall("GlassList"):
       for OutsideRadius in GlassList.findall("./OutsideRadius"):
           GlassList.remove(OutsideRadius)
       OutsideLength = GlassList[1].text
       Height        = GlassList[2].text
       Quantity      = GlassList[3].text
       total_area    = float(OutsideLength)*float(Height)*float(Quantity)/1000000
       child = ElementTree.Element("Area")
       child.text = str(total_area)
       GlassList.append(child)
       print (total_area)
    ## Save the result to a new output file
    if xml_element_tree is not None:
        with open(out_file,'wb') as f:
            f.write(ElementTree.tostring(xml_element_tree))
    else:
        print("Error: file not created")

## Main Functionality
## Ask for base folder
tmpDir = filedialog.askdirectory()
os.chdir(tmpDir)
# Call merger function
run(os.listdir())
