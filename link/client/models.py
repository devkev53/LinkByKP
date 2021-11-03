from django.db import models

# Create your models here.

class Company(models.Model):
    """Model definition for Company."""

    # TODO: Define fields here
    logo = models.ImageField()
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    mail = models.EmailField()

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companys'

    def __str__(self):
        """Unicode representation of Company."""
        return '%s' % (self.name)


class Branch(models.Model):
    """Model definition for Branch."""

    # TODO: Define fields here
    identifier = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        """Meta definition for Branch."""

        verbose_name = 'Branch'
        verbose_name_plural = 'Branchs'

    def __str__(self):
        """Unicode representation of Branch."""
        return '%s - %s' % (self.name, self.company)
        
