from django.db import models
from django.utils import timezone
from .category import Category
from .supplier import Supplier
from .owner import Owner
# Create your models here.

class Asset(models.Model):
	"""docstring for asset"""
	author_name = models.ForeignKey('author_user', on_delete=models.CASECADE)
	item_name = models.CharField(verbose_name=_("Name"), max_length=200)
    value = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal("0"))
    cache_shipping_total = models.DecimalField(max_digits=12, decimal_places=2,
        default=Decimal("0"))
    acquisition_date = models.DateField()
    category = models.ManyToManyField(Category, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    # Creation and last modifications dates
    created_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title