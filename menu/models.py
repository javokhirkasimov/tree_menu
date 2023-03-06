from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class MenuElements(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def has_children(self):
        return MenuElements.objects.filter(parent=self).exists()

    @property
    def all_children(self):
        return MenuElements.objects.filter(parent=self)

    @property
    def path_url(self):
        if self.parent:
            return self.parent.path_url + self.slug + '/'
        return '/' + self.slug + '/'

    class Meta:
        verbose_name = 'Menu Element'
        verbose_name_plural = 'Menu Elements'
