Antes de começar, certificar-se de configurar as credenciais AWS no arquivo 'credencials', localizado em: 'C:\Users\SEU_USUARIO\.aws\credentials'
O comando 's3_client = boto3.client('s3')' buscará automaticamente as credenciais, assim, evitando o perigo de colocar as access keys diretamente no código.
