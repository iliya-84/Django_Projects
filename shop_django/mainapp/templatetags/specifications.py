from django import template
from django.utils.safestring import mark_safe
from mainapp.models import Smartphone

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                 </table>
             """

TABLE_CONTENT = """
                 <tr>
                   <td>{name}</td>
                   <td>{value}</td>
                 </tr>
             """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'diagonal_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'diagonal_type',
        'Разрешение экрана': 'resolution',
        'Емкость батареи': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие sd': 'sd',
        'Максимальный объем памяти': 'sd_volume_max',
        'Основная камера': 'main_cam_mp',
        'Фронтальная камера': 'front_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[
        model_name].items():  # items выдает список кортежей [('Диагональ', diagonal), ('two', 2)]
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter()
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Наличие sd')
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
