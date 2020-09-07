class Shop:
    all_sales = 0

    def __init__(self, shop_name, number_of_items_sold):
        self.shop_name = shop_name
        self.number_of_items_sold = number_of_items_sold
        Shop.all_sales += self.number_of_items_sold

    def sales(self, sale_items):
        self.number_of_items_sold += sale_items
        Shop.all_sales += sale_items

    @staticmethod
    def view_of_sales():
        print('All sales -', Shop.all_sales)
