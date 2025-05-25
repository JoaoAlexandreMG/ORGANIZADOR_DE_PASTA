# Organizador de Pastas

Organize automaticamente os arquivos de uma pasta em subpastas, separando por tipo (documentos, imagens, vídeos, códigos, etc) de forma simples e visual.

## Funcionalidades

- Interface gráfica amigável para seleção da pasta
- Organização automática dos arquivos em subpastas por categoria
- Suporte a dezenas de extensões de arquivos
- Geração de log para acompanhamento de erros e avisos
- Executável para Windows (não precisa de Python instalado)

## Como usar

### 1. Executando pelo Python

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o programa:
   ```bash
   python main.py
   ```
3. Selecione a pasta que deseja organizar e aguarde a conclusão.

### 2. Executável para Windows

- Basta rodar o arquivo `OrganizadorDePastas.exe` na pasta `dist`.
- Não é necessário instalar Python.

## Personalização

- O ícone do executável pode ser alterado editando o comando do PyInstaller.
- As categorias e extensões podem ser modificadas no arquivo `extensions.py`.

## Estrutura do Projeto

```
extensions.py      # Dicionário de extensões e categorias
organizer.py       # Função de organização dos arquivos
main.py            # Ponto de entrada do programa
requirements.txt   # Dependências do projeto
gui.py             # Interface gráfica (Tkinter)
README.md          # Este arquivo
```

## Gerando o executável (avançado)

1. Instale o PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Gere o executável:
   ```bash
   python -m PyInstaller --onefile --noconsole --icon="CAMINHO_PARA_SEU_ICONE.ico" --name="OrganizadorDePastas" main.py
   ```

## Observações

- O log de execução é salvo em `organizador.log` na mesma pasta do executável.
- O programa não sobrescreve arquivos já existentes nas subpastas.
- Caso algum erro aconteça ao mover arquivos, consulte o log para detalhes.

---

Desenvolvido por Joao. Sinta-se livre para modificar e compartilhar!
