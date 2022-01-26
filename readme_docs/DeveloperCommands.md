# Commands


---
## Setup Virtual Environment
- Create virtual environment 
- => virtualenv -p python3.8 venv
- Activate virtual environment 
- => source venv/bin/activate



## pip3 install *packages
- Install Django
- => pip3 install django
- => [OR] python -m pip install Django
- Know which package is installed
- => python -m django --version
- Install DRF
- => pip3 install djangorestframework
- [optional] Markdown support for the browsable API.
- => pip install markdown
- [optional] Filtering support
- => pip install django-filter


## To Start, Work on Project 
- Create Project
- => django-admin startproject projdemo
- Create App
- => cd projdemo/
- Note: App name must be in plural
- => django-admin startapp employees

## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- To install package dependency
- => pip3 install -r requirements.txt

- => pip install Django==3.2.11
- => pip install djangorestframework
- => x pip install django-elasticsearch-dsl
- => x pip install django-elasticsearch-dsl-drf
- => pip install elasticsearch==7.14.0
- => pip install elasticsearch-dsl==7.4.0
- => pip install django-elasticsearch-dsl==7.2.0
- => x pip3 install psycopg2
- => x pip3 install psycopg2-binary
- => x pip3 install python-decouple


---
### Note: Some Useful Command's

> - check django version
> - $ django-admin --version

> - make project
> - $ django-admin startproject projdemo

> - make app
> - $ python3 manage.py startapp home

> - make migrations
> - $ python3 manage.py makemigrations
> - migrate
> - $ python3 manage.py migrate

> - create super user
> - $ python3 manage.py createsuperuser

> - To dump data:
> - $ python3 manage.py dumpdata --indent 4 > ../readme_docs/dumpdata/db_dump.json

> - To load data:
> - $ python manage.py loaddata ../readme_docs/dumpdata/db_dump.json

> - To open Interactive Console / Terminal
> - $ python3 manage.py shell

> - set URL globally
> - $ ngrok http 8000

> - collect static
> - $ python3 manage.py collectstatic


---
## Elastic Search Command's
> - $ service elasticsearch status
> - $ start elastic-search service on system
> - $ sudo systemctl start elasticsearch
> - $ sudo systemctl restart elasticsearch
> - $ sudo systemctl stop elasticsearch

- command to know elastic-search is up & run
```shell
ashishs@lp7981:.../product-crud-es$ service elasticsearch status
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: enabled)
   Active: active (running) since Sun 2022-01-23 13:00:35 IST; 11s ago
     Docs: https://www.elastic.co
 Main PID: 27096 (java)
    Tasks: 113 (limit: 4915)
   CGroup: /system.slice/elasticsearch.service
           ├─27096 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=1
           └─27385 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
ashishs@lp7981:.../product-crud-es$ 
ashishs@lp7981:.../product-crud-es$ 
ashishs@lp7981:.../product-crud-es$ curl -XGET http://localhost:9200
{
  "name" : "lp7981",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "EoWui3QQTqiHPWIVC55sAw",
  "version" : {
    "number" : "7.14.1",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "66b55ebfa59c92c15db3f69a335d500018b3331e",
    "build_date" : "2021-08-26T09:01:05.390870785Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
ashishs@lp7981:.../product-crud-es$ 
```

> - ElasticSearch on local system
> - http://localhost:9200/

> - Kibana on local system
> - http://localhost:5601/

- hit ES records
```shell
(venv) ashishs@lp7981:.../projproduct$ python manage.py shell
>>> 
>>> from products.es_documents import ProductDetailsDocument
>>>
>>> records = ProductDetailsDocument.search().filter("term", name="apple")
>>> 
>>> for record in records:
...     print(f'---Products Details ---name: {record.name} ---price:{record.price} ---quantity: {record.quantity}')
... 
---Products Details ---name: apple ipad - model J1 ---price:50000 ---quantity: 5
---Products Details ---name: apple ipad - model G1 ---price:2000 ---quantity: 5
---Products Details ---name: apple ipad - model E1 ---price:50000 ---quantity: 5
---Products Details ---name: apple ipad - model D1 ---price:40000 ---quantity: 5
---Products Details ---name: apple ipad - model C1 ---price:3000 ---quantity: 20
---Products Details ---name: apple ipad - model B2 ---price:2000 ---quantity: 5
---Products Details ---name: apple ipad - model A1 ---price:40000 ---quantity: 2
>>> 
>>> 
```

> Syncing Django’s database with Elasticsearch indexes:
> > - Create Elasticsearch indexes:
> > - $ python3 manage.py search_index --create -f
> 
> > - Sync the data:
> > - $ python3 manage.py search_index --populate -f
> 
> > - Populate Elasticsearch:
> > - $ python3 manage.py search_index --rebuild


