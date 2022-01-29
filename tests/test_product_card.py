from page_objects.ProductPage import ProductPage


def test_check_card_imac(browser):
    ProductPage(browser).check_elements("index.php?route=product/product&path=20_27&product_id=41", "iMac")


def test_check_card_nikon_d300(browser):
    ProductPage(browser).check_elements("index.php?route=product/product&path=33&product_id=31", "Nikon D300")
