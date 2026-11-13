# Guia de manutenção e publicação do portfólio

Este guia corresponde ao repositório existente **RodriguesProject/RodriguesProject**. Não é necessário criar outro repositório para manter o README do perfil.

## 1. Repositório e estrutura

- Repositório: https://github.com/RodriguesProject/RodriguesProject
- Branch principal: `main`
- README de perfil: `README.md`
- Site estático: `index.html`
- Estilos: `assets/style.css`
- Projetos: `projects/`

O README será exibido no perfil GitHub porque o repositório público tem o mesmo nome do usuário.

## 2. GitHub Pages

Para publicar o site:

1. Abra o repositório e acesse **Settings → Pages**.
2. Em **Build and deployment**, selecione **Deploy from a branch**.
3. Selecione a branch `main` e a pasta `/(root)`.
4. Salve e aguarde a implantação.
5. Confirme a URL e o status apresentados na própria página Settings → Pages.

Como este é um repositório de projeto com nome igual ao usuário (e não o repositório especial `usuario.github.io`), a URL esperada, após ativação, é:

`https://rodriguesproject.github.io/RodriguesProject/`

Não divulgue o endereço como site ativo antes de confirmar que o GitHub Pages terminou a implantação.

## 3. Validação automática

O workflow `.github/workflows/portfolio-validation.yml` executa os dois scripts Python de análise e verifica se os arquivos de saída são gerados. A validação é executada em commits e pull requests que alterem os projetos.

O selo de status no README mostra o resultado da execução mais recente do workflow.

## 4. Atualizar projetos

Antes de publicar um novo projeto:

- Inclua um README com objetivo, perguntas de negócio, tecnologias, dados, etapas, resultados, como executar e limitações.
- Inclua dados de origem pública ou sintéticos; documente a fonte e a licença, quando aplicável.
- Não publique documentos jurídicos reais, dados pessoais, informações de clientes, credenciais, tokens ou arquivos `.env`.
- Execute o código localmente e confira se os resultados citados no README correspondem aos arquivos gerados.
- Declare honestamente o nível de domínio das ferramentas e identifique projetos de estudo como demonstrativos.

## 5. Próximas melhorias recomendadas

- Adicionar testes automatizados de qualidade de dados.
- Criar um dashboard interativo em Power BI ou ferramenta equivalente, quando houver domínio prático.
- Ampliar os projetos com consultas SQL adicionais e documentação de modelagem.
- Acrescentar um projeto com API ou automação somente depois de construído e testado.

## 6. Repositórios de estudos

Mantenha os repositórios de aulas e exercícios separados dos projetos de portfólio. O repositório de perfil deve funcionar como uma vitrine: destacar os melhores trabalhos e encaminhar o recrutador para a documentação de cada projeto.
