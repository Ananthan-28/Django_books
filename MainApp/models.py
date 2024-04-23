from django.db import models

# Create your models here.
class BookCategoryModel(models.Model):
    Category_ID = models.AutoField(primary_key=True)
    Category_Name = models.TextField(max_length=20)

    def __str__(self):
        return self.Category_Name

    class Meta:
        db_table = 'book_category'

class AuthorDataModel(models.Model):
    User_ID = models.AutoField(primary_key=True)
    Username = models.TextField(max_length=50)
    author_login = models.CharField(max_length=50,null=True)
    author_password = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.Username

    class Meta:
        db_table = 'user_data'


class BookDataModel(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_description = models.TextField(null=True)
    book_image = models.ImageField(upload_to='book-images/')
    book_price = models.DecimalField(max_digits=5, decimal_places=2)
    book_category = models.ForeignKey(BookCategoryModel,on_delete=models.CASCADE,null=True)
    book_author = models.ForeignKey(AuthorDataModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = 'book_data'

class AddToCartModel(models.Model):
    cart_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(AuthorDataModel,on_delete=models.CASCADE,null=True)
    product_id = models.ForeignKey(BookDataModel,on_delete=models.CASCADE,null=True)
    cart_quantity=models.IntegerField()

    def __str__(self):
        return self.product_id.book_name

    def total_price(self):
        return self.product_id.book_price * self.cart_quantity

    class Meta:
        db_table = 'cart_data'


class BuyNowModel(models.Model):
    buy_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AuthorDataModel, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(BookDataModel, on_delete=models.CASCADE, null=True)
    buy_quantity = models.IntegerField()

    def __str__(self):
        return self.product_id.book_name

    def total_price(self):
        return self.product_id.book_price * self.buy_quantity

    class Meta:
        db_table = 'buy_data'


class ReviewModal(models.Model):
    review_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(AuthorDataModel,on_delete=models.CASCADE)
    product_id=models.ForeignKey(BookDataModel,on_delete=models.CASCADE)
    review_content=models.TextField(max_length=255)

    def __str__(self):
        return f"{self.user_id.Username}-{self.product_id.book_name}"

    class Meta:
        db_table = 'review_data'

