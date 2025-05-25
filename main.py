# main.py
# Este é o ponto de entrada do programa Organizador de Pastas.
# Ele orquestra a seleção da pasta pelo usuário e chama a função de organização.

from gui import select_folder  # Importa a função de seleção de pasta (interface gráfica)
from organizer import organize_folder  # Importa a função de organização de arquivos

if __name__ == "__main__":
    # Solicita ao usuário que selecione a pasta a ser organizada
    folder = select_folder()
    if not folder:
        # Se o usuário não selecionar nenhuma pasta, exibe erro e encerra
        raise Exception("Nenhuma pasta foi selecionada.")
    # Organiza os arquivos da pasta selecionada
    organize_folder(folder)
    # Informa ao usuário que a organização foi concluída
    print(f"Arquivos organizados na pasta: {folder}")
# Fim do arquivo main.py
