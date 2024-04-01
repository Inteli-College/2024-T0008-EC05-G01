---
title: Artefato - Frontend e Backend
sidebar_position: 2
---

# Artefato - Frontend e Backend

## Documentação Backend

### Descrição

Os códigos da velha implementação de controle do robô via CLI foram reutilizados e adaptados para dispor uma API RESTful que permite o controle do robô via requisições HTTP, além de fornecer informações sobre o estado do robô e informações criticas do banco de dados que armazena informações sobre os kits e medicamentos. Além disso, foi implementado uma estrutura de "threads" e "locks" para garantir a integridade dos dados e evitar problemas de concorrência enquanto os diversos módulos do sistema necessários para o funcionamento adequado do robô são executados (API, QRCODE, ROBOT).

### Arvore de Diretórios

```bash
.
├── classes
│   ├── ApiWrapper.py
│   ├── QRCodeWrapper.py
│   └── RobotWrapper.py
├── database
│   ├── archives
│   │   ├── kits.json
│   │   ├── medicamentos.json
│   │   └── qrcode
│   │       ├── db_completo.json
│   │       └── db_medicamentos.json
│   └── wrapper.py
├── main.py
├── modules
│   ├── api
│   │   ├── classes
│   │   │   ├── Kit.py
│   │   │   ├── Medicamento.py
│   │   │   └── Pos.py
│   │   ├── main.py
│   │   ├── routes
│   │   │   ├── frontend.py
│   │   │   ├── kits.py
│   │   │   ├── main.py
│   │   │   ├── medicamentos.py
│   │   │   └── queue.py
│   │   └── shared.py
│   ├── qrcode
│   │   └── main.py
│   └── robot
│       ├── classes
│       │   ├── KitAssembler.py
│       │   ├── Kit.py
│       │   ├── Pos.py
│       │   └── robot.py
│       ├── lib
│       │   └── pydobot
│       │       └── ...
│       ├── main.py
│       └── utils
│           ├── ports.py
│           └── text.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── armazem.css
│   │   ├── config.css
│   │   ├── kit.css
│   │   ├── novoKit.css
│   │   ├── reabastecimento.css
│   │   ├── style.css
│   │   ├── style_telaExclusa.css
│   │   ├── telaKit.css
│   │   ├── tp.css
│   │   └── visualizacaoKit.css
│   └── img
│       ├── backL.svg
│       ├── backR.svg
│       ├── logo_arm copy.png
│       ├── logo_arm.png
│       ├── logo_editar.png
│       ├── lupa.svg
│       ├── secaoLixeira.png
│       ├── simbolo_mais.png
│       └── triangulos.png
└── templates
    ├── armazem.html
    ├── config.html
    ├── kit.html
    ├── novoKit.html
    ├── reabastecimento.html
    ├── telaExclusao.html
    ├── telaInicial.html
    ├── telaKit.html
    ├── telaP.html
    └── visualizacaoKit.html
```

### Descritivo dos Diretórios

- **classes**: Contém as classes que representam os objetos do sistema, cada um serve como nível de abstração para os objetos do sistema e inicia processos de maneira independente.
- **database**: Contém um driver desenvolvido para manipular os arquivos JSON que armazenam as informações sobre os kits e medicamentos com o TinyDB de maneira síncrona, utilizando os conceitos de `locks` e `singletons` para garantir a integridade e consistência dos dados. Dentro deste diretório, também há uma pasta chamada `archives` que contém os arquivos JSON que armazenam as informações sobre os kits e medicamentos.
- **modules**: Contém os módulos do sistema, cada um é responsável por uma parte do sistema, como a API, o QRCODE e o ROBOT.
- **static**: Contém os arquivos estáticos do sistema, como as folhas de estilo e as imagens. Os mesmos sao servidos pelo módulo da API que disponibilizam os arquivos estáticos para o frontend na rota `/static`.
- **templates**: Contém os templates HTML que são renderizados pelo módulo da API e servidos para o frontend.

### Descritivo dos Módulos

- **API**: Módulo responsável por fornecer uma API RESTful, desenvolvida usando FastAPI, que permite o controle do robô via requisições HTTP, além de fornecer informações sobre o estado do robô e informações criticas do banco de dados que armazena informações sobre os kits e medicamentos. Essa API também compartilha um objeto `Queue` com o módulo ROBOT, que permite a adição de kits a serem montados pelo robô a uma fila First-In-First-Out (FIFO).
- **QRCODE**: Módulo responsável por perpetualmente analisar e ler QRCodes na câmera do robô, futuramente servirá para verificar a autenticidade dos kits e medicamentos e garantir a integridade dos mesmos.
- **ROBOT**: Módulo responsável por abstrair o controle do robô, permitindo a montagem de kits e a movimentação do robô de maneira segura e compatível com a API. Como dito anteriormente, esse módulo consome um objeto `Queue` compartilhado com o módulo API, permitindo a ordenação dos kits a serem montados pelo robô.

### Documentação das Rotas

Além de disponibilizar uma documentação interativa da API (swagger) na rota `/docs`, segue abaixo a documentação de todas as rotas disponíveis na API, excluindo as rotas de frontend:

---

#### Rotas relacionadas a medicamentos

- **GET /medicamentos/{Nome}**: Retorna um medicamento com o nome especificado (interação com o banco de dados).
- **PUT /medicamentos/{Nome}**: Atualiza um medicamento com o nome especificado (interação com o banco de dados), o corpo da requisição deve conter os novos valores do medicamento.
- **DELETE /medicamentos/{Nome}**: Deleta um medicamento com o nome especificado (interação com o banco de dados).
- **GET /medicamentos**: Retorna todos os medicamentos em forma de lista (interação com o banco de dados).
- **POST /medicamentos**: Adiciona um novo medicamento (interação com o banco de dados), o corpo da requisição deve conter os valores do novo medicamento.

Exemplo de corpo de requisição para adicionar ou atualizar um medicamento:

```json
{
	"nome": "Paracetamol",
	"quantidade": 100,
	// Essa posição é relativa ao armazém/estoque, ou seja, aonde o medicamento reside e deve ser pegado pelo robô
	"pos": {
		"x": 0,
		"y": 0,
		"z": 0,
		"r": 0
	}
}
```

---

#### Rotas relacionadas a kits

- **GET /kits/{Nome}**: Retorna um kit com o nome especificado (interação com o banco de dados).
- **GET /kits/joined/{Nome}**: Retorna um kit com o nome especificado e todos os medicamentos que o compõem (interação com o banco de dados).
- **PUT /kits/{Nome}**: Atualiza um kit com o nome especificado (interação com o banco de dados), o corpo da requisição deve conter os novos valores do kit.
- **DELETE /kits/{Nome}**: Deleta um kit com o nome especificado (interação com o banco de dados).
- **GET /kits**: Retorna todos os kits em forma de lista (interação com o banco de dados).
- **POST /kits**: Adiciona um novo kit (interação com o banco de dados), o corpo da requisição deve conter os valores do novo kit.

Exemplo de corpo de requisição para adicionar ou atualizar um kit:

```json
{
	"nome": "Kit 1",
	"medicamentos": [
		{
			"nome": "Paracetamol",
			"quantidade": 10,
			"altura": 1.0,
			// Essa posição é relativa ao kit, ou seja, aonde o medicamento deve ser colocado dentro do kit
			"posicao": {
				"x": 0,
				"y": 0,
				"z": 0,
				"r": 0
			}
		}
	]
}
```

---

#### Rotas relacionadas a fila de montagem

- **GET/fila/{Nome}**: Adiciona um kit com o nome especificado a fila de montagem do robô (interação com o módulo ROBOT e o banco de dados, consultando a existência do kit).

---

## Documentação Frontend