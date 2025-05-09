from django.db import models

# Create your models here.
class SuperUser(models.Model):
    admin_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'superuser'

    def __str__(self):
        return self.name
    

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    staff_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    superuser = models.ForeignKey(SuperUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return f"{self.name} - {self.staff_type}"


food_choices = (
    (1, "Veg"),
    (2, "Non-Veg"),
    (3, "Both"),
)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    food_pref = models.IntegerField(choices = food_choices, default=3)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


class Table(models.Model):
    table_id = models.AutoField(primary_key=True, auto_created=True)
    table_no = models.IntegerField()
    capacity = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'table'

    def __str__(self):
        return str(self.table_no)
    

class FoodCategory(models.Model):
    category_id = models.AutoField(primary_key=True, auto_created=True)
    category_name = models.CharField(max_length=100)
    food_type = models.IntegerField(choices = food_choices, default=3)

    class Meta:
        db_table = 'food_category'

    def __str__(self):
        return self.category_name


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True, auto_created=True)
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    food_type = models.IntegerField(choices = food_choices, default=3)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return self.item_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, auto_created=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    no_of_people = models.IntegerField()
    booking_status = models.BooleanField(default=False)
    amount = models.FloatField()
    menu = models.ManyToManyField(Menu)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return str(self.booking_id)
    

class Billing(models.Model):
    bill_id = models.AutoField(primary_key=True, auto_created=True)
    bill_date = models.DateField()
    bill_time = models.TimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    bill_status = models.BooleanField(default=False)
    bill_payment_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'billing'

    def __str__(self):
        return str(self.bill_id)
    

class BillingItem(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.FloatField()  # store price at the time of billing

    class Meta:
        db_table = 'billing_item'


