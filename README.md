# Criando um Carrinho com Django Rest

## Instalando as dependências

```pip install -r requirements.txt```

## Criando o banco de dados
``py manage.py makemigrations``

## Migrando para o banco
``py manage.py migrate``

## Subindo o servidor teste
``py manage.py runserver``

## Criando super usuario
``py manage.py createsuperuser``

## Acessando o admin do django
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

# Endspoints

## Criando token JWT
Use o metodo ``POST``

http://127.0.0.1:8000/api/token/ 

### Digite seu usuario e senha e peguei seu token

<div align="">
<img src="https://user-images.githubusercontent.com/63524589/218339306-7f7dcdf7-45e9-43f2-b530-ca0c76a30d16.png" width="1000px" />
</div>

### Listando todos os Produtos
Use o metodo ``GET``

http://127.0.0.1:8000/api/products

### Paginação dos produtos
Use o metodo ``GET``

http://127.0.0.1:8000/api/products?page=2

### Ordenando pelo preço
Use o metodo ``GET``

http://127.0.0.1:8000/api/products?name=price 

http://127.0.0.1:8000/api/products?name=-price

### Ordenando pela popularidade
Use o metodo ``GET``

http://127.0.0.1:8000/api/products?name=score

http://127.0.0.1:8000/api/products?name=-score

### Ordenando pelo nome
Use o metodo ``GET``

http://127.0.0.1:8000/api/products?name=name

http://127.0.0.1:8000/api/products?name=-name

## EndPoint do carrinho

Use o metodo ``GET``

http://127.0.0.1:8000/api/cart

<div align="">
<img src="https://user-images.githubusercontent.com/63524589/218339508-c39f976a-de2f-47c2-ae49-04f5f531caea.png" width="1000px" />
</div>

## EndPoint para adicionar e deletar do produtos do carrinho

Use o metodo ``POST`` para adicionar no carinho

``"cart"`` Vai receber o id do carrinho\
``"Product"`` Vai receber o id do produto\
``"quantity"`` Vai receber a quantidade do produto

<div align="">
<img src="https://user-images.githubusercontent.com/63524589/218339573-0aabe9ce-0d0b-4535-a793-51d15f329631.png" width="1000px" />
</div>

Use o metodo ``Delete`` para tirar o produto do carrinho

http://127.0.0.1:8000/api/cart/item/<id:int> no final adicionar o id do produto no carrinho 

<div align="">
<img src="https://user-images.githubusercontent.com/63524589/218339641-724bdfb5-39d1-4ebf-a647-d033a41f7aba.png" width="1000px" />
</div>
