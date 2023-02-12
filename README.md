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

![img.png](C:\Users\Monstro\Trabalho\Projeto\teste-supera\img-git\token_JWT.png)

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

![img.png](C:\Users\Monstro\Trabalho\Projeto\teste-supera\img-git\Carrinho.png)


## EndPoint para adicionar e deletar do produtos do carrinho

Use o metodo ``POST`` para adicionar no carinho

``"cart"`` Vai receber o id do carrinho\
``"Product"`` Vai receber o id do produto\
``"quantity"`` Vai receber a quantidade do produto

![img.png](C:\Users\Monstro\Trabalho\Projeto\teste-supera\img-git\POST-Carrinho.png)


Use o metodo ``Delete`` para tirar o produto do carrinho

http://127.0.0.1:8000/api/cart/item/<id:int> no final adicionar o id do produto no carrinho 

![img.png](C:\Users\Monstro\Trabalho\Projeto\teste-supera\img-git\Delete-Carrinho.png)