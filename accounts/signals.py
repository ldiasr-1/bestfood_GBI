from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from produtos.models import Produto
from mercado.models import Mercado
from promo.models import Promocao

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Cria os grupos Cliente e Vendedor
    grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
    grupo_vendedor, _ = Group.objects.get_or_create(name='Vendedor')

    # Obtém os content types dos modelos
    content_type_produto = ContentType.objects.get_for_model(Produto)
    content_type_mercado = ContentType.objects.get_for_model(Mercado)
    content_type_promocao = ContentType.objects.get_for_model(Promocao)

    # Permissões para clientes (apenas visualização)
    permissao_ver_produto, _ = Permission.objects.get_or_create(
        codename='view_produto',
        content_type=content_type_produto,
        defaults={'name': 'Can view produto'}
    )
    permissao_ver_mercado, _ = Permission.objects.get_or_create(
        codename='view_mercado',
        content_type=content_type_mercado,
        defaults={'name': 'Can view mercado'}
    )
    permissao_ver_promocao, _ = Permission.objects.get_or_create(
        codename='view_promocao',
        content_type=content_type_promocao,
        defaults={'name': 'Can view promocao'}
    )

    grupo_cliente.permissions.add(permissao_ver_produto, permissao_ver_mercado, permissao_ver_promocao)

    # Permissões para vendedores (CRUD completo)
    permissoes_vendedor = [
        ('add_produto', 'Can add produto', content_type_produto),
        ('change_produto', 'Can change produto', content_type_produto),
        ('delete_produto', 'Can delete produto', content_type_produto),
        ('view_produto', 'Can view produto', content_type_produto),
        ('add_mercado', 'Can add mercado', content_type_mercado),
        ('change_mercado', 'Can change mercado', content_type_mercado),
        ('delete_mercado', 'Can delete mercado', content_type_mercado),
        ('view_mercado', 'Can view mercado', content_type_mercado),
        ('add_promocao', 'Can add promocao', content_type_promocao),
        ('change_promocao', 'Can change promocao', content_type_promocao),
        ('delete_promocao', 'Can delete promocao', content_type_promocao),
        ('view_promocao', 'Can view promocao', content_type_promocao),
    ]

    for codename, name, content_type in permissoes_vendedor:
        permissao, _ = Permission.objects.get_or_create(
            codename=codename,
            content_type=content_type,
            defaults={'name': name}
        )
        grupo_vendedor.permissions.add(permissao)

    print("Grupos e permissões configurados com sucesso!")