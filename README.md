##  Início Rápido

###  Instalando Dependências

Clone o projeto em sua máquina e instale as dependências com o comando:

```shell
pip install -r requirements.txt
```

Para iniciar  a API
```shell
paython manage.py runserver
```


## EndPoints

-[Item]()
    -[POST - /Adicionar Item]
    -[GET - /Listar Items]


A criação do Item é definida pelos campos abaixo

| Campo        | Tipo    | Descrição                                        |
| ------------ | ------- | ------------------------------------------------ |
| id           | string  | Identificador único do Item.                     |
| name         | string  | O nome do Item.                                  |
| create_at    | string  | A data de criação do Item.                       |


## Endpoints

| Método | Rota              | Descrição                                                             |
| ------ | ----------------- | --------------------------------------------------------------------- |
| POST   | item/             | Cadastra um Item no Banco de Dad                                      |
| GET    | item/             | Lista todos os usuários.                                              |
| DELETE | /item/:id         | Deleta um Usuario usando seu ID como parâmetro                        |


```
POST item/
Host: http://127.0.0.1:8000/api/item/
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
	{
		"name": "Nome do Item"
	}
```

### Exemplo de Response:

```
201 Created
```

GET item/
Host:  http://127.0.0.1:8000/api/item/
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
[
	{
		"id": "f15a4980-e5fc-4ecd-a361-f3e6bbb039b2",
		"name": "Item_1",
		"create_at": "2023-02-16T20:50:11.472016Z"
	},
	{
		"id": "c455fbe8-33bc-4a0c-a47e-555dbb741d47",
		"name": "Item_2",
		"create_at": "2023-02-16T20:56:43.354184Z"
	},
	{
		"id": "89b1975d-6a45-4982-94f0-cc2597e90432",
		"name": "Item_3",
		"create_at": "2023-02-16T20:57:17.983188Z"
	},
	{
		"id": "61cb6511-6dac-45f5-bb07-9982c0c72cff",
		"name": "Item_4",
		"create_at": "2023-02-16T20:57:23.937802Z"
	},
	{
		"id": "69da23ff-4d3a-4d92-b426-a43a9658b172",
		"name": "Item_5",
		"create_at": "2023-02-16T20:57:28.154124Z"
	},
	{
		"id": "f6cff6e6-e408-4a01-bfe4-4266cfd2db1b",
		"name": "Item_6",
		"create_at": "2023-02-16T20:57:32.655872Z"
	},
	{
		"id": "3080f685-4394-40d6-a988-ff8c2ce47c93",
		"name": "Item_7",
		"create_at": "2023-02-16T20:57:37.035638Z"
	},
	{
		"id": "f22ca0e3-90a4-4307-95fa-d678fc19c61d",
		"name": "Item_8",
		"create_at": "2023-02-16T20:57:40.702375Z"
	},
	{
		"id": "87eaf8ac-9903-4390-b276-2790960328ed",
		"name": "Item_9",
		"create_at": "2023-02-16T20:57:44.326732Z"
	},
	{
		"id": "63413ab5-653a-4e4a-bc2f-2b625f135fa4",
		"name": "Item_10",
		"create_at": "2023-02-16T20:57:48.868946Z"
	},
	{
		"id": "da028ccb-32f6-48e4-80fd-76c457625473",
		"name": "Novo_Item",
		"create_at": "2023-02-17T20:49:04.361670Z"
	}
]