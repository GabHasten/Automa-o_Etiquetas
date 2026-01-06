Para compartilhar o caminho do seu arquivo local no GitHub, você precisará usar comandos Git no seu terminal, e não apenas o cmd. 
O processo envolve inicializar um repositório Git local, adicionar o arquivo, criar um repositório no GitHub e, em seguida, "empurrar" (push) suas alterações para lá. 
Pré-requisitos
Antes de começar, certifique-se de que você tem o Git instalado em sua máquina. Você pode verificar isso abrindo o cmd ou Git Bash e digitando git --version [2]. 
Passo a passo para entregar seu arquivo no GitHub
Siga estes passos, usando o Git Bash (recomendado) ou cmd:
Navegue até a pasta do seu projeto:
Use o comando cd (change directory) para ir até o diretório onde seu arquivo está salvo.
bash
cd "caminho/completo/para/sua/pasta"
# Exemplo: cd C:\Users\SeuUsuario\Documentos\MeuProjeto
Inicialize um repositório Git local:
Dentro da pasta do seu projeto, digite o comando para iniciar o rastreamento de arquivos pelo Git [2].
bash
git init
Adicione seu arquivo ao índice (staging area):
Use o comando git add seguido do nome do seu arquivo. Se quiser adicionar todos os arquivos na pasta, use git add . [2].
bash
git add nome_do_seu_arquivo.extensao
# Ou para todos os arquivos:
git add .
Confirme (commit) as alterações:
Registre as alterações que você adicionou. A flag -m permite incluir uma mensagem descritiva sobre o commit [2].
bash
git commit -m "Adicionando meu arquivo inicial"
Crie um repositório no GitHub:
Vá para o GitHub.com e crie um novo repositório vazio (não adicione README ou .gitignore ainda, pois você já tem arquivos locais). Copie o URL HTTPS do novo repositório (ex: github.com) [1].
Conecte seu repositório local ao remoto (GitHub):
No seu terminal, adicione o endereço do repositório remoto [1].
bash
git remote add origin github.com
Empurre (push) seus arquivos para o GitHub:
Envie os commits da sua máquina local para o repositório remoto na nuvem [1].
bash
git push -u origin main
# Se o branch principal no GitHub for 'master', use: git push -u origin master
 
Você precisará entrar com seu nome de usuário e um Personal Access Token (PAT) do GitHub quando solicitado. Se tiver problemas com a autenticação, consulte a documentação do GitHub sobre criação de PATs [1]. 
Após o git push, seu arquivo e o caminho do seu repositório estarão visíveis na página do GitHub. 

================================================================================================================================================

Para fazer novos envios (commits) posteriormente em 2025, o processo é muito mais simples, pois o endereço do GitHub já está salvo. Você não precisa usar o comando remote add novamente.
Siga estes 3 passos no CMD sempre que fizer alterações nos seus arquivos:
1. Preparar as alterações
Adicione os arquivos modificados para a fila de envio:
cmd
git add .
Use o código com cuidado.

(O ponto . indica que você quer adicionar todas as mudanças da pasta).
2. Criar o "pacote" (Commit)
Grave as alterações localmente com uma mensagem descrevendo o que você fez:
cmd
git commit -m "Explique aqui o que você mudou ou adicionou"
Use o código com cuidado.

3. Enviar para o GitHub
Como você já configurou o destino da primeira vez, basta usar:
cmd
git push
Use o código com cuidado.

Dicas úteis para 2025:
Verificar o que mudou: Antes de adicionar, use git status para ver quais arquivos foram modificados.
Corrigir erro de login: Se o CMD pedir senha e falhar, o GitHub agora exige o uso de um Personal Access Token (PAT) ou autenticação via navegador. Você pode gerenciar suas credenciais pelo Gerenciador de Credenciais do Windows.
Trabalho em equipe: Se outra pessoa mexeu no código ou você editou diretamente pelo site do GitHub, use git pull antes de fazer o seu push para atualizar sua máquina local.
Para acompanhar o histórico de seus envios de forma visual, você pode acessar a aba Repositories no seu perfil do GitHub.