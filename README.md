<h1> Dados Meteorológicos <h1/>

> api rest desenvolvida com intuito de obter informações sobre 'Umidade (em percentual)', 'temperatura' e 'chuva (previsão em mm)'
> Além da cidade e a data de consulta 
  
> biliotecas e frameworks utilizados :
```
  pip install Flask == 2.2.2
  pip install Requests
```
> busca por cidade :
  Ex : /time/dourados
    {
        "city": "Dourados, MS",
        "date": "08/02/2023",
        "humidity": 83,
        "rain": 0.0,
        "temp": 23
    }

> os dados meteorológicos são disponibilizados pela 'HG Brasil'   
> link da aplicação: https://api-rest-meteorologica.onrender.com/time

