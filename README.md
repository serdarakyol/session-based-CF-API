# Recommendation system for e-commerce (Session based Collaborative Filtering)
This repository contains continuation of [Collaborative Filtering Data Preparetion](https://github.com/serdarakyol/Collaborative-filtering-data-preparation). Used the data which generated Collaborative Filtering Data Preparetion and created an API with FastAPI.

For that project used over 10K products and 54K session

# Run time test
Each request is unique, contain n different product and returns n products for recommend. Please note that, the project tested on **12th Gen Intel(R) Core(TM) i7-12700H** CPU. For that CPU. Runtime table as below
Number of API Request | Average latency (ms) | Lowest latency (ms) | Highest latency (ms) | n product per request | n product per response
--- | --- | --- | --- | --- | ---
100 | 44 | 38 | 77 | 10 | 10
1000 | 44 | 38 | 81 | 5 | 5
3000 | 45 | 38 | 83 | 3 | 3

# Usage
That project developed and tested on Python 3.9. For run that repository, just run below code
## Run on Terminal
```
$ git clone https://github.com/serdarakyol/session-based-CF-API.git
$ cd session-based-CF-API/
$ bash prepare_api.sh
$ source venv/bin/activate
$ uvicorn cf_api.main:app --reload --host 0.0.0.0 --port 1234
```
Please note that prepare_api.sh creates necessary folders, download files and fill to make ready to API. For more information [click](prepare_api.sh)

If you do not want to run API like that. You can just use Docker as below code section
## Run on Docker
```
$ docker image build -t cf_api:0.0.1 .
$ docker run -dp 1234:1234 cf_api:0.0.1
```
## Product information
Here you can find randomly product ID and corresponding information regarding Turkish and English. Remember, API works with product ID. So as an input just write product ID

Product 1
```
TR
"productid" : "HBV00000SP6XD",
"brand" : "Buffa",
"category" : "Kahvaltılık ve Süt", 
"subcategory" : "Peynir",
"name" : "Buffa Burata 150 gr"

EN
"productid" : "HBV00000SP6XD",
"brand" : "Buffa",
"category" : "Breakfast and Milk", 
"subcategory" : "Cheese",
"name" : "Buffa Burata 150 gr"
```

Product 2
```
TR
"productid" : "SGKZB70023",
"brand" : "Sesu",
"category" : "Sağlık ve Kozmetik",
"subcategory" : "El, Yüz ve Vücut Bakımı",
"name" : "Sesu El Ağdası 250Gr"

EN
"productid" : "SGKZB70023",
"brand" : "Sesu",
"category" : "Health and Cosmetic",
"subcategory" : "Hand, Face and Body care",
"name" : "Sesu Hand Wax 250Gr"
```

Product 3:
```
TR
"productid" : "HBV00000CN4Q1",
"brand" : "Fairy",
"category" : "Ev Bakım ve Temizlik",
"subcategory" : "Bulaşık Yıkama",
"name" : "Fairy Hepsi Bir Arada 22 Yıkama Bulaşık Makinesi Deterjanı Kapsülü Limon Kokulu"

EN
"productid" : "HBV00000CN4Q1",
"brand" : "Fairy",
"category" : "Home Care and Cleaning",
"subcategory" : "Washing dishes",
"name" : "Fairy All in One 22 Washes Dishwasher Liquid Capsule Lemon Scented"
```

Product 4:
```
TR
"productid" : "HBV00000OE7P5",
"brand" : "Ak-Du",
"category" : "Kahvaltılık ve Süt",
"subcategory" : "Peynir",
"name" : "Ak-Du İzmir Tulum Peyniri 250 gr"

EN
"productid" : "HBV00000OE7P5",
"brand" : "Ak-Du",
"category" : "Breakfast and Milk",
"subcategory" : "Cheese",
"name" : "Ak-Du İzmir Bryndza 250 gr"
```

Product 5:
```
TR
"productid" : "HBV00000M9HYH",
"brand" : "Le Petit Marseillais",
"category" : "Kişisel Bakım",
"subcategory" : "Duş Jelleri ve Sabunlar",
"name" : "Le Petit Marseillais Duş Jeli Zeytin Ağacı&Ihlamur 650 ml"

EN
"productid" : "HBV00000M9HYH",
"brand" : "Le Petit Marseillais",
"category" : "Personal Care",
"subcategory" : "Shower Gels and Soaps",
"name" : "Le Petit Marseillais Shower Gel Olive Tree&Linden 650 ml"
```

For more just go to data **cf_api/data/meta.json**. If you do not have that data use ```prepare_api.sh``` and you will have all products on **cf_api/data/meta.json.**

## How to use API
So far, setup completed. Follow description to use this API

Then go to http://0.0.0.0:1234/docs. Click ```Authorize``` button, located on the right up corner. You can see on below image
![Authorize](img/first.png)

Write on popup screen ```serdarakyol55@outlook.com``` as below image. Then click Authorize and Close button.
![Authorize2](img/second.png)

Click on ```POST /api/collaborativefilter``` and new screen will appear as below. Click on ```Try it out``` which located on the right corner. As you can see on the below image you can write any product ID and number of suggestion product. 

![Authorize3](img/third.png)

When the input data is written, just click on the ```execute```. Then the results will show up as below image

![Authorize3](img/fourth.png)

<!-- LICENSE -->
## License

[session-based-CF-API](https://github.com/serdarakyol/session-based-CF-API) is distributed under the [MIT License](LICENSE).
