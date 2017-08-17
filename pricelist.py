from lxml import etree as ET
import sys, getopt, csv

class PriceList:

	discountDecimals=2
	#outputfile='pricelist.xml' #Outputted file name
	param_file='' #-f
	param_name='' #-p
	param_net=''  #-n

	def loadParams(self):
		myopts, args = getopt.getopt(sys.argv[1:],"f:n:p:")
		for o, a in myopts:
		    if o == '-f':
		        self.param_file=a
		    elif o == '-p':
		    	self.param_name=a
		    elif o == '-n':
		    	self.param_net=a

		if(self.param_file == '' or self.param_name == '' or self.param_net == ''):
			print ('Please ensure you include switch -f(CSV file) -p(Pricelist Name) and -n(Net Pricelist 0 or 1)')
		elif ".csv" not in self.param_file:
			print('-f(CSV file) must be a .csv file.')
		else:
			print self.param_file, self.param_name, self.param_net
			self.baseXml()

	def loadCsv(self, pricelist):
		print 'Loading ' + self.param_file + '...'
		import csv
		with open(self.param_file, 'rb') as csvfile:
			pricelistcsv = csv.DictReader(csvfile, delimiter=',', quotechar='"')
			for row in pricelistcsv:
				self.addStockItem(pricelist, row["sku"], row["price"], row["discount"], row["id"])
		self.output()

	def baseXml(self):
		self.xml_root = ET.Element("PriceLists")
		pricelists = ET.SubElement(self.xml_root, "StockItem-CustomerClassificationsList")
		self.addPricelist(pricelists)

	def addPricelist(self, pricelists):
		pricelist = ET.SubElement(pricelists, "StockItem-CustomerClassifications", PriceListNet=self.param_net, CompClass=self.param_name)
		self.loadCsv(pricelist)

	def addStockItem(self, pricelist, sku, price, discount, id):
		stockitem = ET.SubElement(pricelist, "StockItem")
		ET.SubElement(stockitem, "StockID").text = id
		ET.SubElement(stockitem, "StockCode").text = sku
		ET.SubElement(stockitem, "QtyStart").text = '1'
		ET.SubElement(stockitem, "QtyEnd").text = '99999'
		ET.SubElement(stockitem, "AmountValue").text = price
		if not discount:
			ET.SubElement(stockitem, "DiscountValue").text = '0'
		else:
			discountRounded = round(float(discount), self.discountDecimals)
			if(discountRounded >= 100):
				print(sku + ' discount is ' + str(discountRounded) + '(over 100%), ignored and set to 0.')
				ET.SubElement(stockitem, "DiscountValue").text = '0'
			elif(discountRounded < 0):
				print(sku + ' discount is ' + str(discountRounded) + '(under 0%), ignored and set to 0.')
				ET.SubElement(stockitem, "DiscountValue").text = '0'
			else:
				ET.SubElement(stockitem, "DiscountValue").text = str(discountRounded)


	def output(self):
		self.outputfile = self.param_name + '.xml'
		print('Outputting to ' + self.outputfile + '...')
		#print ET.tostring(self.xml_root, pretty_print=True) #Use this to output to console
		#self.xml_root.write("pricelist.xml")
		#tree = ET.fromstring(ET.tostring(self.xml_root)
		tree = ET.ElementTree(self.xml_root)
		#tree.write(sys.stdout, pretty_print=True)
        #tree.write(xmlfile, xml_declaration=True, encoding='utf-8', method="xml")
		tree.write(self.outputfile)

test = PriceList()
test.loadParams()
#test.baseXml()
#test.output()
