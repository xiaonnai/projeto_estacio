import boto3
import os
import datetime
import logging
from botocore.exceptions import NoCredentialsError

# logging
logging.basicConfig(filename='backup_log.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s')

# função de upload
def upload_para_s3(diretorio_local, nome_bucket, diretorio_s3=None):
    s3_client = boto3.client('s3')
    
    try:
        for root, pastas, arquivos in os.walk(diretorio_local):
            for arquivo in arquivos:
                caminho_arquivo_local = os.path.join(root, arquivo)
                
                caminho_arquivo_s3 = os.path.relpath(caminho_arquivo_local, diretorio_local) if diretorio_s3 is None else os.path.join(diretorio_s3, os.path.relpath(caminho_arquivo_local, diretorio_local))

                s3_client.upload_file(caminho_arquivo_local, nome_bucket, caminho_arquivo_s3)
                logging.info(f"Arquivo {caminho_arquivo_local} enviado para o S3 como {caminho_arquivo_s3}")

    except NoCredentialsError:
        logging.error("Credenciais da AWS não encontradas")

        return False
    
    return True

# funçao de backup
def backup_diario():
  #trocar os conteudos das variaveis por valores reais
    diretorio_local = "C:/caminho/para/diretorio/local"

    nome_bucket = "nome-do-bucket"

    diretorio_s3 = f"backup_diario/{datetime.date.today()}"

    logging.info(f"Iniciando backup diário para o S3...")
    
    if upload_para_s3(diretorio_local, nome_bucket, diretorio_s3):
        logging.info(f"Backup diário concluído com sucesso.")
    else:
        logging.error(f"Falha no backup diário.")
 
if __name__ == "__main__":
    backup_diario()
