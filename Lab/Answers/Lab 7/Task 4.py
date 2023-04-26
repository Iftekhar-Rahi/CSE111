#Type 4
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+"Price: "+str(self.__price)
#write your code here
class Book(Product):
    def __init__(self,id,title,price,isbn,pub):
        super().__init__(id,title,price)
        self.isbn=isbn
        self.pub=pub
    def printDetail(self):
      s=super().get_id_title_price()
      return f"{s}\nISBN: {self.isbn} Publisher: {self.pub}"
      # return s
class CD(Product):
    def __init__(self,id,title,price,band,duration,genre):
      super().__init__(id,title,price)
      self.band=band
      self.duration=duration
      self.genre=genre
    def printDetail(self):
      s=super().get_id_title_price()
      s+=f"\nBand: {self.band} Duration: {self.duration} minutes"
      s+=f"\nGenre: {self.genre}"
      return s
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())