Steps to Parcellab_task:
* Create virtual environment for python by running: python3 -m venv venv
* access the virtual environment through: source venv/bin/activate
* Install packages used in the project through: pip3 install -r requirements.txt
* create database for the project and run the migrations through: python3 manage.py migrate
* seed the database by the csv file by opening django shell: python3 manage.py shell
* Inside the shell type: 
                        * from seed import Seeder
                        * Seeder().seed()
                        * exit()
* create a superuser to access django admin to view the seeded data through: python3 manage.py createsuperuser
* open django-admin from browser after running server through:
                        * python3 manage.py runserver
                        * navigate to 'http://127.0.0.1:8000/admin'
                        * enter superuser credentials
* to view the api to test retrieving data, navigate to 'http://127.0.0.1:8000/swagger'
* The api is with path '/fetchShipment', click on 'Try it out' button to test the api by entering
                {
                "tracking_number": "TN12345683",
                "carrier": "GLS"
                }
inside the body as an example to retrieve a response with shipment details, if invalid data entered, you will get message
'Wrong tracking number or carrier'


* to run test, run command: python3 manage.py test