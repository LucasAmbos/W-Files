import os
import shutil
from tkinter import filedialog

# Selecionar o caminho da pasta
caminho_pasta = filedialog.askdirectory()

# dicionario - extensões
pastas = {
    'Documentos': [".txt", ".doc", ".odt", ".docx"],
    'Executáveis': [".exe"],
    'Instaladores': [".msi"],
    'Compactados': ['.rar', '.zip', '.7z'],
    'Atalhos': [".ink", ".url"],
    'Imagens': [".ico", ".png", ".jpg", ".jpeg", ".jfif"],
    'Certificados': [".cer"],
    'ISOS': [".iso"],
    'Jogo Retro': [".nsp"],
    "PDF's": [".pdf"],
    'Vídeos': [".gif", ".mp4"],
    'Utorrent': [".gif", ".torrent"],
    'Planilhas': [".xls", ".xlsx", ".ods"],
}

for diretorio, subdire, arquivos in os.walk(caminho_pasta):
    # pegar arquivos da lista -arquivos
    for arquivo in arquivos:
        ext_arquivo = os.path.splitext(arquivo)[1]  # separa as extensões dos arquivos e armazena no [1]

        for pasta, extensoes in pastas.items():  # buscar extensões do dicionario

            # mover extensão do dicionario para pasta
            if ext_arquivo in extensoes:
                pasta_destino = os.path.join(caminho_pasta, pasta)

                # Caso arquivo não exista
                if not os.path.isfile(os.path.join(pasta_destino, arquivo)):
                    if os.path.isdir(pasta_destino):
                        shutil.move(os.path.join(diretorio, arquivo), pasta_destino)
                        print(f"Arquivo {arquivo} movido para {pasta_destino}")

                    else:
                        os.mkdir(pasta_destino)
                        shutil.move(os.path.join(diretorio, arquivo), pasta_destino)
                        print(f"Arquivo {arquivo} movido para {pasta_destino}")

                break
