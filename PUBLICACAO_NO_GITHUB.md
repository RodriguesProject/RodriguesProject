# Como publicar este portfólio no GitHub

## 1. Criar o repositório de perfil

1. Entre em https://github.com/new.
2. Crie um repositório **público** chamado exatamente `RodriguesProject` (igual ao nome de usuário).
3. Não marque opções para gerar README, `.gitignore` ou licença, pois este pacote já contém esses arquivos.
4. Extraia o conteúdo deste ZIP e envie o conteúdo da pasta `RodriguesProject_Portfolio_Premium` para a raiz do novo repositório.
5. Faça o commit com uma mensagem como `Adiciona portfólio profissional e projetos demonstrativos`.

O arquivo `README.md` na raiz aparecerá automaticamente na página do perfil, desde que o repositório público tenha o mesmo nome do usuário.

## 2. Atualizar a biografia curta do perfil

Sugestão para o campo Bio do GitHub (substitui a referência incorreta a JavaScript):

> Administração & Direito | Business Analysis | Data Analytics em formação | Python, Java, SQL, PostgreSQL, MongoDB | Legal Tech | Joinville/SC

Use Java, não JavaScript, salvo se também tiver estudado JavaScript de fato. Mantenha os níveis técnicos como fundamentos/em formação no README.

## 3. Ativar GitHub Pages

1. Abra Settings > Pages no repositório `RodriguesProject`.
2. Em Build and deployment, selecione Deploy from a branch.
3. Selecione a branch `main` e a pasta `/(root)`.
4. Salve e aguarde o GitHub Pages publicar.

A URL esperada será `https://rodriguesproject.github.io/RodriguesProject/` após a publicação. Confirme a URL exibida em Settings > Pages.

## 4. Preservar os repositórios existentes

Não substitua nem exclua `Docs_public` ou `Aulas_SCTEC`. Este portfólio foi preparado para um novo repositório de perfil com nome igual ao usuário.

## 5. Antes de tornar público

- Revise o README e os links de contato.
- Não acrescente telefone, endereço residencial ou dados pessoais desnecessários.
- Os dados CSV deste pacote são sintéticos e podem permanecer públicos.
- Não faça upload de documentos de clientes, processos reais, credenciais, tokens ou arquivos `.env`.
- Confira se o seu nome de usuário está exatamente como `RodriguesProject`.

## 6. Estrutura entregue

```text
RodriguesProject_Portfolio_Premium/
├── README.md
├── index.html
├── assets/
│   └── style.css
├── projects/
│   ├── 01-analise-varejo-python-sql/
│   ├── 02-legal-operations-analytics/
│   └── 03-business-analysis-processos/
└── PUBLICACAO_NO_GITHUB.md
```

## 7. Transparência profissional

Os projetos foram preparados como estudos demonstrativos com dados gerados artificialmente. Atualize seu LinkedIn e currículo somente depois de revisar os códigos, executar os projetos e compreender as etapas descritas.
