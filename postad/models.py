from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import uuid


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwarsg):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwarsg)
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class PostAD(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ad_id = models.UUIDField(default=uuid.uuid4().hex, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to=f"postad/")
    image2 = models.ImageField(upload_to=f"postad/", null=True, blank=True)
    image3 = models.ImageField(upload_to=f"postad/", null=True, blank=True)
    image4 = models.ImageField(upload_to=f"postad/", null=True, blank=True)
    image5 = models.ImageField(upload_to=f"postad/", null=True, blank=True)
    price = models.IntegerField()
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="postad")
    tag = models.ManyToManyField(Tag, related_name="postad")

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    purchase_year = models.DateField()

    sold = models.BooleanField(default=False)

    CONDITION_TYPE = [
        ("Almost Like New", "Almost Like New"),
        ("Brand New", "Brand New"),
        ("Gently Used", "Gently Used"),
        ("Heavily Used", "Heavily Used"),
        ("Unboxed", "Unboxed")
    ]
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)

    STATE_LIST  = [
        ("Andhra Pradesh","Andhra Pradesh"),
        ("Arunachal Pradesh ","Arunachal Pradesh "),
        ("Assam","Assam"),
        ("Bihar","Bihar"),
        ("Chhattisgarh","Chhattisgarh"),
        ("Goa","Goa"),
        ("Gujarat","Gujarat"),
        ("Haryana","Haryana"),
        ("Himachal Pradesh","Himachal Pradesh"),
        ("Jammu and Kashmir ","Jammu and Kashmir "),
        ("Jharkhand","Jharkhand"),
        ("Karnataka","Karnataka"),
        ("Kerala","Kerala"),
        ("Madhya Pradesh","Madhya Pradesh"),
        ("Maharashtra","Maharashtra"),
        ("Manipur","Manipur"),
        ("Meghalaya","Meghalaya"),
        ("Mizoram","Mizoram"),
        ("Nagaland","Nagaland"),
        ("Odisha","Odisha"),
        ("Punjab","Punjab"),
        ("Rajasthan","Rajasthan"),
        ("Sikkim","Sikkim"),
        ("Tamil Nadu","Tamil Nadu"),
        ("Telangana","Telangana"),
        ("Tripura","Tripura"),
        ("Uttar Pradesh","Uttar Pradesh"),
        ("Uttarakhand","Uttarakhand"),
        ("West Bengal","West Bengal"),
        ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
        ("Chandigarh","Chandigarh"),
        ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
        ("Daman and Diu","Daman and Diu"),
        ("Lakshadweep","Lakshadweep"),
        ("NCR of Delhi","NCR of Delhi"),
        ("Puducherry","Puducherry")
        ]
    state = models.CharField(max_length=100, choices=STATE_LIST)
    city = models.CharField(max_length=150)

    SELLER_TYPE_LIST = [
        ("Individual", "Individual"),
        ("Dealer", "Dealer")
    ]
    seller_type = models.CharField(max_length=50, choices=SELLER_TYPE_LIST)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostAD, self).save(*args, **kwargs)

    def __str__(self):
        return self.title