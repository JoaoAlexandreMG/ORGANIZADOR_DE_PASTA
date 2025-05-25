# gui.py
# Este arquivo contém a função responsável pela interface gráfica (GUI)
# para seleção da pasta a ser organizada, utilizando a biblioteca Tkinter.

import tkinter as tk  # Importa o módulo principal do Tkinter
from tkinter import filedialog, messagebox  # Importa diálogos de seleção e mensagens


def select_folder():
    """
    Abre uma janela gráfica para o usuário selecionar a pasta a ser organizada.
    Retorna o caminho da pasta selecionada ou None se o usuário cancelar.
    """
    root = tk.Tk()  # Cria a janela principal
    root.title("Organizador de Pastas")  # Define o título da janela
    root.geometry("400x200")  # Define o tamanho da janela
    root.resizable(False, False)  # Impede redimensionamento

    folder_dir = {'path': None}  # Dicionário para armazenar o caminho selecionado

    def on_select():
        # Função chamada ao clicar no botão
        folder = filedialog.askdirectory(title="Selecione uma pasta")  # Abre o diálogo de seleção
        if folder:
            folder_dir['path'] = folder  # Salva o caminho selecionado
            root.destroy()  # Fecha a janela
        else:
            messagebox.showwarning("Aviso", "Nenhuma pasta foi selecionada.")  # Mostra aviso

    # Cria e exibe o texto de instrução
    label = tk.Label(root, text="Selecione uma pasta para organizar", font=("Arial", 12))
    label.pack(pady=20)
    # Cria e exibe o botão de seleção
    button = tk.Button(root, text="Selecionar Pasta", command=on_select, font=("Arial", 10))
    button.pack(pady=20)
    root.mainloop()  # Inicia o loop da interface gráfica
    return folder_dir['path']  # Retorna o caminho selecionado (ou None)
# Fim do arquivo gui.py
