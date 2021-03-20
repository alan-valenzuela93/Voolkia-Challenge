import requests
import json


class Seller: 
    def __init__(self, seller_id, site_id):
        self.seller_id = seller_id
        self.site_id = site_id
        self.url = 'https://api.mercadolibre.com/sites/' + self.site_id + '/search?seller_id=' + self.seller_id
        self.data = dict(requests.get(self.url).json())
        self.data_store = dict(self.data)

#cada setter devuelve una lista con los requerimientos
    def set_item_id(self):
        items_id = []
        for d in self.data["results"]:
            if d["catalog_product_id"]:
                items_id.append(d["catalog_product_id"])
        return items_id

    def set_titles(self):
        titles = []
        for t in self.data["results"]:
            if t["title"]:
                titles.append(t["title"])
        return titles

    def set_categories_ids(self):
        category_id_list = []
        for c in self.data["results"]:
            if c["category_id"]:
                category_id_list.append(c["category_id"])
        return category_id_list

    def set_names_categories(self):
        category_name_list = []
        for i in self.data["results"]:
            if i["domain_id"]:
                category_name_list.append(i["domain_id"])
        return category_name_list

    def generate_log(self):
        items_list = []
        item_id = self.set_item_id()
        title = self.set_titles()
        category_id = self.set_categories_ids()
        category_name = self.set_names_categories()
        l = len(item_id)
        for i in range(l):
            obj = {
                "Item ID": item_id[i],
                "Title": title[i],
                "Category ID": category_id[i],
                "Category Name": category_name[i]
            }
            items_list.append(obj)
        j = json.dumps(items_list)
        f = open("log.json", "a") #Para leer los datos del log de forma mas comoda y clara, lo creo en formato json
        f.write(j)
        f.close()

#En la función main, se ingresa la cantidad de usuarios que queremos buscar en la api. Por cada uno se genera un objeto 
def main():
    sellers = []
    cant_users = int(input("How many users?: "))
    for i in range(cant_users):
        seller_id = input("Set seller id: ")
        site_id = input("Set site id: ")
        u = Seller(seller_id, site_id)
        sellers.append(u)
    for s in sellers:
        s.generate_log()


if __name__ == '__main__':
    main()
