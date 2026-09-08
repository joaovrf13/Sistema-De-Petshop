# Sistema de Petshop — PROZ

Sistema web em Python e Flask para cadastro de clientes, pets, serviços e acompanhamento do faturamento.

## Funcionalidades atuais

- painel com resumo de clientes, pets, serviços e faturamento;
- cadastro conjunto do responsável e do pet;
- validação de documento duplicado;
- associação do primeiro serviço ao pet;
- busca de clientes e pets na interface;
- catálogo de serviços;
- layout responsivo para computador, tablet e celular.

## Como executar

1. Entre na pasta do projeto:

```bash
cd "Sistema de PetShop"
```

2. Crie e ative um ambiente virtual.

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o sistema:

```bash
python main.py
```

5. Abra `http://127.0.0.1:5000` no navegador.

## Estrutura

- `main.py`: rotas e integração com a interface;
- `services/`: regras de negócio;
- `repositories/`: armazenamento atual em memória;
- `templates/`: páginas HTML;
- `static/`: estilos, JavaScript e imagens.

> Os registros ainda ficam em memória e são apagados quando o servidor reinicia.
