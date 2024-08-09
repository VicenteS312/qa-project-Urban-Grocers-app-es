Vicente Salinas / Sprint 7 / Cohorte 12
# Pruebas para el parámetro name al crear un kit de productos [Urban.Grocers]
###### Descripcion del proyecto
Este proyecto sirvio como una introducción a la automatización de pruebas. Para ello, era necesario aprender los conceptos básicos de el idioma de programación Python y también de el entorno de desarollo PyCharm. Utilicé la declaración de funciones para poder realizar diferentes objetivos. Para poder automatizar las pruebas de los requisitos de la creación de un kit, era necesario trabajar con estas funciones, tales como crear un usuario, manipular el cuerpo de la solicitud y ejecutar pruebas positivas y negativas.

###### Fuente de documentación
[Urban.Grocers API Docs](https://cnt-eaf99977-18c8-471d-84cd-9b4203bc237d.containerhub.tripleten-services.com/docs/#api-Main.User-CreateUser)

###### Descripción de tecnologías y técnicas utilizadas
> Para poder ejecutar pruebas en PyCharm es necesario descargar 'pytest' en packages. Solo asi PyCharm podra reconocer una prueba, siempre y cuando la prueba tenga 'test' en el nombre. Para poder trabajar con los API's es necesario descargar la libreria 'requests'. A fin de que las pruebas sean mantenibles, se distribuyeron los datos necesarios en sus respectivos archivos. En el archivo de 'configuration', se almacenó la URL y los paths necesarios en variables. En el archivo 'data' se guardo los datos necesarios para las solicitudes, como los headers y el cuerpo de la solicitud. En el archivo 'sender stand request' es necesario importar los archivos 'configuration' y 'data' para usar los datos almacenados en ella y crear funciones como 'create new user body', 'auth token return' y 'post new client kit'. A fin de mantener las pruebas de manera ordenada y separadas, se asignan al archivo 'create kit name kit test'. Es necesario importar los archivos 'data' y 'sender stand request'. Se declara la funcion que llama el cuerpo que contiene el objeto que se probara y se crea dos funciones que se llamaran para hacer las pruebas negativas y positivas. Finalmente, todo este trabajo se subira al Github por medio del git push para compartir el resultado final.
###### Commandos para ejecutar pruebas
1. Instalar pytest:(Commando de terminal) pip install pytest
2. Instalar request:(Commando de Pycharm) Python Packages/ Buscar 'requests'/ Install 
3. Crear archivo create_kit_name_kit_test.py en consola de Pycharm
4. Declarar las funciones 'get_kit_body', 'positive_assert_for_kit_body' y 'negative_assert_for_kit_body' por medio de 'def'
5. En configurations seleccionar current file y pulsar 'Run'

