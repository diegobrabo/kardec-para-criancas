import os
import shutil

# Configurações
BASE_DIR = "docs/sessions"
NUM_SESSIONS = 1019
PLACEHOLDER_IMAGE_SOURCE = "assets/placeholder.jpg" # Opcional: Caminho para uma imagem padrão

def create_sessions():
    # Remover diretório antigo se existir para limpar sessões antigas
    if os.path.exists(BASE_DIR):
        shutil.rmtree(BASE_DIR)
    
    os.makedirs(BASE_DIR)

    print(f"Gerando {NUM_SESSIONS} sessões em '{BASE_DIR}'...")

    # Lista para manter a ordem correta no arquivo .pages
    nav_order = []

    for i in range(1, NUM_SESSIONS + 1):
        # Nome da pasta conforme solicitado: pergunta-{i}
        # Ex: pergunta-1, pergunta-2, ..., pergunta-1019
        folder_name = f"pergunta-{i}"
        folder_path = os.path.join(BASE_DIR, folder_name)
        
        # Adicionar à lista de navegação
        nav_order.append(folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Criar README.md
        readme_path = os.path.join(folder_path, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# Pergunta {i}\n\n")
                f.write(f"![Imagem da Pergunta {i}](image.jpg)\n\n")
                f.write("Escreva o conteúdo da resposta aqui.\n")

        # Copiar imagem placeholder
        image_path = os.path.join(folder_path, "image.jpg")
        if not os.path.exists(image_path):
            if os.path.exists(PLACEHOLDER_IMAGE_SOURCE):
                shutil.copy(PLACEHOLDER_IMAGE_SOURCE, image_path)
            else:
                with open(image_path, "wb") as f:
                    f.write(b"") 

    # Criar arquivo .pages para forçar a ordem correta
    # Isso evita que pergunta-10 venha antes de pergunta-2
    pages_file_path = os.path.join(BASE_DIR, ".pages")
    with open(pages_file_path, "w", encoding="utf-8") as f:
        f.write("nav:\n")
        for item in nav_order:
            f.write(f"  - {item}\n")

    print("Concluído!")

if __name__ == "__main__":
    create_sessions()
