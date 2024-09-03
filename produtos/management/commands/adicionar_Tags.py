# produtos/management/commands/adicionar_tags.py

from django.core.management.base import BaseCommand
from produtos.models import Tag

class Command(BaseCommand):
    help = 'Adiciona tags predefinidas ao banco de dados'

    def handle(self, *args, **kwargs):
        tags = [
            "Opção Vegana", "Opção Vegetariana", "Não Contém Glúten",
            "Não Contém Lactose", "Orgânico", "Sem Açúcar", "Baixo Teor de Sódio",
            "Sem Conservantes", "Integral", "Light", "Sem Gordura Trans",
            "Rico em Fibras", "Sem Corantes", "Sem Aromatizantes", "Sem Oleaginosas"
        ]
        for tag_nome in tags:
            Tag.objects.get_or_create(nome=tag_nome)
        self.stdout.write(self.style.SUCCESS('Tags predefinidas adicionadas com sucesso!'))
