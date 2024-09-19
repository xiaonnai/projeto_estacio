Antes de começar, certificar-se de configurar as credenciais AWS no arquivo 'credencials', localizado em: 'C:\Users\SEU_USUARIO\.aws\credentials'
O comando 's3_client = boto3.client('s3')' buscará automaticamente as credenciais, assim, evitando o perigo de colocar as access keys diretamente no código.

Para automatizar diariamente, vá ao programa "Agendador de Tarefas", crie uma nova tarefa básica, configure colocando nome, frequência, data e hora, escolha a ação e no fim, coloque o caminho do script Python.
