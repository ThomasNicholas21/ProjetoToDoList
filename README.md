# 📚 Todolist utilizando TDD

## 💡 Descrição do Projeto
Esta API RESTful foi desenvolvida com Django e Django REST Framework para gerenciar atividades e categorias de uma ToDoList, com endpoints bem definidos para ambas as entidades.
O projeto foi construído seguindo o ciclo de desenvolvimento TDD (Test-Driven Development):
🔴 Red → 🟢 Green → 🔵 Refactor.
A aplicação conta com uma estrutura sólida, incluindo:
- Models, Serializers e Views organizados de forma modular
- Testes automatizados utilizando unittest (via rest_framework.test.APITestCase)
- Execução dos testes com Pytest para maior produtividade
- Cobertura de testes analisada com coverage
- Documentação completa no Postman, facilitando o consumo da API por desenvolvedores e testers
- Utilização do coverage para mapear todo código e se foram testados

## 🎯 Funcionalidades
- Cadastro de Atividades e Categorias
- Regras que melhoram a utilização da API.
- Rastreamento do momento que atividade e categoria foram criadas e atualizadas.
- Controle de quando a atividade deve ser realizada e quando ela foi concluída.

## 📂 Documentação

- **Arquivo Json para Postman**: 👉 [POSTMAN](https://github.com/ThomasNicholas21/ProjetoToDoList/blob/master/doc_api/Todolist.postman_collection.json)

## 💻 Tecnologias Utilizadas
- **Backend:** Django (Python) e Django Rest Framework 
- **Banco de Dados:** sqlite3
- **Testes:** Pytest e APITestCase

## 🏗 Estrutura do Projeto
- **`todolist/`**: Contém o código-fonte do projeto Django
- **`doc_api/`**: Documentação da API em formato json.

---

## 🙋‍♂️ Como Rodar o Projeto

**Realize o Git Clone:**
```bash
git clone https://github.com/ThomasNicholas21/ProjetoUni.git
```

**Crie o ambiente virtual e instale as dependências**
 ```bash
 python -m venv venv
 source venv/bin/activate  # Linux/macOS
 venv\Scripts\activate  # Windows
 pip install -r requirements.txt
 ```

**Inicialize o banco de dados e rode a aplicação**
 ```bash
 cd todolist/
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver
 ```

## 📌 Testes
Para rodar os testes automatizados da API:
```bash
cd todolist/
python manage.py test
pytest
ptw
```

## 😎 Painel Administrativo

A framework Django, fornece um painel administrativo para verificar dados e edita-los. A ferramenta foi utilizada para visualização dos dados criados pela API, para acesso é necessário criar um super usuário:
```bash
cd todolist/
python manage.py createsuperuser
```
Depois de criado, acesse: `http://localhost:8000/admin/` e utilize o super usuário criado.


## 🚀 Conventional Commits
Segue a tabela com os principais tipos de commits utilizados neste projeto:

| Tipo | Descrição |
|------|-----------|
| `feat` | Adição de nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Alteração na documentação |
| `style` | Implementação e ajustes de estilização |
| `refactor` | Refatoração de código sem alteração de funcionalidade |
| `test` | Adição ou modificação de testes |
| `chore` | Tarefas de manutenção (build, dependências) |

---


### 🚀 Feito por Thomas Nicholas
