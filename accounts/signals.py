from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from produtos.models import Produto
from mercado.models import Mercado
from promo.models import Promocao

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
    grupo_vendedor, _ = Group.objects.get_or_create(name='Vendedor')

    content_type_produto = ContentType.objects.get_for_model(Produto)
    content_type_mercado = ContentType.objects.get_for_model(Mercado)
    content_type_promocao = ContentType.objects.get_for_model(Promocao)

    permissao_ver_produto = Permission.objects.get(codename='view_produto', content_type=content_type_produto)
    permissao_ver_mercado = Permission.objects.get(codename='view_mercado', content_type=content_type_mercado)
    permissao_ver_promocao = Permission.objects.get(codename='view_promocao', content_type=content_type_promocao)

    grupo_cliente.permissions.add(permissao_ver_produto, permissao_ver_mercado, permissao_ver_promocao)

    permissoes_vendedor = [
        'add_produto', 'change_produto', 'delete_produto', 'view_produto',
        'add_mercado', 'change_mercado', 'delete_mercado', 'view_mercado',
        'add_promocao', 'change_promocao', 'delete_promocao', 'view_promocao',
    ]

    for permissao in permissoes_vendedor:
        codename = permissao
        if 'produto' in permissao:
            content_type = content_type_produto
        elif 'mercado' in permissao:
            content_type = content_type_mercado
        elif 'promocao' in permissao:
            content_type = content_type_promocao

        permissao_obj = Permission.objects.get(codename=codename, content_type=content_type)
        grupo_vendedor.permissions.add(permissao_obj)
        