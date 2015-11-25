# Khaos Control Pricelist CSV to XML Exporter
This script allows you to take a CSV file and convert it to an XML format that is correctly formatted to import to Khaos Control. Khaos Control is provided by Keystone Software, it is recommended that you full test importing the file before doing so on your live systems. This script is not created or supported by Keystone Software.

## Requirements

* Python 2.7.* 

## Getting Started

Once you have downloaded the script you can process your CSV price list file with the following line

`python pricelist.py  -f example/pricelist.csv -p MyExamplePricelist -n 0`

Please notice the 3 parameters `-f` `-p` `-n` they all *required*

* `-f` Defines your pricelist csv file, it must be a `.csv` file and this must related to it's path. It must only contain 2 columns with the headers `sku` and `price`.
* `-p` Defines the name of the pricelist, this will be what appears or it writes over within Khaos Control.
* `-n` Defines if the pricelist values given are net or gross. Boolean value of `1` or `0` must be given. 

## Example
Assume our input file is `pricelist.csv` and store in the same directory as our `pricelist.py` file.
### Input File
```csv
sku,price
PRODUCT1,5.99
PRODUCT2,10.99
```

### Run Script
`python pricelist.py  -f pricelist.csv -p MyExamplePricelist -n 0`

### Output File
```xml
<PriceLists>
    <StockItem-CustomerClassificationsList>
        <StockItem-CustomerClassifications CompClass="MyExamplePricelist" PriceListNet="0">
            <StockItem>
                <StockCode>PRODUCT1</StockCode>
                <QtyStart>1</QtyStart>
                <QtyEnd>99999</QtyEnd>
                <AmountValue>5.99</AmountValue>
            </StockItem>
            <StockItem>
                <StockCode>PRODUCT2</StockCode>
                <QtyStart>1</QtyStart>
                <QtyEnd>99999</QtyEnd>
                <AmountValue>10.99</AmountValue>
            </StockItem>
        </StockItem-CustomerClassifications>
    </StockItem-CustomerClassificationsList>
</PriceLists>
```