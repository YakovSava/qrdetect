from pyEanGenerator import Ean8Generator as EAN8

testBarCode = EAN8('20044223355')

## show barecode on window
testBarCode.showBarcode()

## save EAN as svg file
testBarCode.saveAsSvg("myEan.svg")

## save EAN as png file (need pillow)
testBarCode.saveAsImg("myEan.png")