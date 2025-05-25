# organizer.py
# Este arquivo contém a função responsável por organizar os arquivos de uma pasta
# em subpastas, de acordo com o tipo de arquivo (extensão), utilizando o dicionário EXTENSIONS.

import os  # Importa o módulo para manipulação de arquivos e diretórios
from extensions import EXTENSIONS  # Importa o dicionário de extensões
import logging  # Importa o módulo de logging para mensagens de erro


def organize_folder(folder_dir):
    """
    Organiza os arquivos da pasta informada em subpastas, conforme o tipo de arquivo.
    - folder_dir: caminho da pasta a ser organizada.
    """
    # Configura o logging para registrar mensagens em um arquivo de log
    logging.basicConfig(
        filename='organizador.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    # Lista todos os arquivos presentes na pasta (ignora subpastas)
    files_in_folder = [
        file for file in os.listdir(folder_dir)
        if os.path.isfile(os.path.join(folder_dir, file))
    ]
    for file in files_in_folder:
        # Obtém a extensão do arquivo (em minúsculo)
        file_extension = file.split('.')[-1].lower()
        # Percorre cada categoria de extensão
        for type_name, extensions in EXTENSIONS.items():
            # Se a extensão do arquivo pertence à categoria
            if file_extension in extensions:
                folder_path = os.path.join(folder_dir, type_name)  # Define o caminho da subpasta
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)  # Cria a subpasta, se não existir
                # Move o arquivo para a subpasta correspondente, tratando possíveis exceções
                try:
                    os.rename(
                        os.path.join(folder_dir, file),
                        os.path.join(folder_path, file)
                    )
                except FileExistsError:
                    logging.warning(f"Arquivo já existe em {folder_path}: {file}. Não foi movido.")
                except PermissionError:
                    logging.error(f"Sem permissão para mover o arquivo: {file}.")
                except Exception as e:
                    logging.error(f"Erro ao mover o arquivo {file}: {e}")
                break  # Para de procurar após encontrar a categoria
# Fim do arquivo organizer.py
