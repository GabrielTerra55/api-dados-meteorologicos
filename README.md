<h1> Dados Meteorológicos <h1/>

> api rest simples desenvolvida com intuito de obter informações sobre 'Umidade (em percentual)', 'temperatura' e 'chuva (previsão em mm)'
> Além da cidade e a data de consulta 
> proposito de testar deploy e funcionalidade
  
 biliotecas e frameworks utilizados :
```
  pip install Flask == 2.2.2
  pip install Requests
```
 busca por cidade :
  Ex : /time/dourados
    {
        "city": "Dourados, MS",
        "date": "08/02/2023",
        "humidity": 83,
        "rain": 0.0,
        "temp": 23
    }

Os dados meteorológicos são disponibilizados pela 'HG Brasil'   
1. link da aplicação: https://api-rest-meteorologica.onrender.com/time
2. Usando o link do deploy e seguindo o exemplo, ficara deste modo:
  https://api-rest-meteorologica.onrender.com/time/dourados

