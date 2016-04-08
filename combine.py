import os, os.path, sys
import glob
from xml.etree import ElementTree as ET

class combine:

	outputfile = '' #Output file (include '.xml')
	folder = '' #Folder(relative to path) containing pricelists to be combined in to single file

	def basexml(self):
		print('Creating base XML...')
		self.xml_root = ET.Element("PriceLists")
		pricelists = ET.SubElement(self.xml_root, "StockItem-CustomerClassificationsList")
		self.loadFiles(pricelists)

	def loadFiles(self, pricelists):
		print('Loading files...')
		xml_files = glob.glob(self.folder + "/*.xml")
		xml_element_tree = None
		for xml_file in xml_files:
			self.loadXml(pricelists, xml_file)
		self.output()

	def loadXml(self, pricelists, xml_file):
		print('Adding ' + xml_file)
		data = ET.parse(xml_file).getroot()
		#print ET.tostring(data[0][0])
		#ET.SubElement(pricelists, data[0][0])
		pricelists.append(data[0][0])

	def output(self):
		print('Outputting to ' + self.outputfile + '...')
		#print ET.tostring(self.xml_root, pretty_print=True) #Use this to output to console
		#self.xml_root.write("pricelist.xml")
		#tree = ET.fromstring(ET.tostring(self.xml_root)
		tree = ET.ElementTree(self.xml_root)
		#tree.write(sys.stdout, pretty_print=True)
        #tree.write(xmlfile, xml_declaration=True, encoding='utf-8', method="xml")
		tree.write(self.outputfile)

	def run(self, files):

		print('Starting...')
		xml_files = glob.glob(files + "/*.xml")
		xml_element_tree = None
		for xml_file in xml_files:
			print('Adding...' + xml_file)
			data = ET.parse(xml_file).getroot()
			#print ElementTree.tostring(data)
			for result in data.iter('results'):
				if xml_element_tree is None:
					xml_element_tree = data 
					insertion_point = xml_element_tree.findall("./StockItem-CustomerClassificationsList")[0]
				else:
					insertion_point.extend(result)
		if xml_element_tree is not None:
			print ElementTree.tostring(xml_element_tree)

test = combine()
test.basexml()
