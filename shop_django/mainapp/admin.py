from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe
from .models import *
from PIL import Image


class SmartphoneAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgrey'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


# mark_safe() показывает, что тег доверенный и не заменяется спецсимволами
class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px">При разрешении больше {}x{} изображение будет обрезано</span>'.format(
                *Product.MIN_RESOLUTION
            )
        )
        # добавляем хелптекст под полем ввода картинки


#    def clean_image(self):
#        image = self.cleaned_data['image']
#        img = Image.open(image)
#        min_height, min_width = Product.MIN_RESOLUTION
#        max_height, max_width = Product.MAX_RESOLUTION
#        if image.size > Product.MAX_IMAGE_SIZE:
#            raise ValidationError('Размер не должен быть больше 3 MB!')
#        if img.height < min_height or img.width < min_width:
#            raise ValidationError('Изображение меньше разрешенного!')
#        if img.height > max_height or img.width > max_width:
#            raise ValidationError('Изображение больше разрешенного!')
#        return image


class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(
                Category.objects.filter(slug='notebooks'))  # предлагает выбрать категорию только если слаг ноутбуки
        return super().formfield_for_foreignkey(db_field, request, **kwargs)  # остальные как обычно


class SmartphoneAdmin(admin.ModelAdmin):
    change_form_template = 'admin.html'
    form = SmartphoneAdminForm  #


def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
        return ModelChoiceField(
            Category.objects.filter(slug='smartphones'))  # предлагает выбрать категорию только если слаг смартфоны
    return super().formfield_for_foreignkey(db_field, request, **kwargs)  # остальные как обычно


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
# admin.site.register(SomeModel)
