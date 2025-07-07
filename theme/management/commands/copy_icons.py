import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Copia ícones SVG da pasta icons para static/icons'

    def handle(self, *args, **options):
        # Caminhos
        source_dir = os.path.join(settings.BASE_DIR, 'theme', 'static_src', 'icons')
        dest_dir = os.path.join(settings.BASE_DIR, 'theme', 'static', 'icons')
        
        # Criar diretório de destino se não existir
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copiar arquivos SVG
        copied_count = 0
        if os.path.exists(source_dir):
            for filename in os.listdir(source_dir):
                if filename.endswith('.svg'):
                    source_file = os.path.join(source_dir, filename)
                    dest_file = os.path.join(dest_dir, filename)
                    
                    # Copiar arquivo
                    shutil.copy2(source_file, dest_file)
                    copied_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Copiados {copied_count} ícones SVG para {dest_dir}')
        ) 