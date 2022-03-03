# Financial and Church Management App
Typically, a personal finance app will have different features such as a shared wallet, bill reminders, auto bill pay, and even managing subscriptions.  

This Finances Application is a church management web application that keeps track of donations, welfare, offerings among other financial obligations. It showcases sermons and announcement from leadership. Admin can add upcoming events and programs. Members can comment on sermon posts. Paystacks payment api was integrated into the application code.

This is was built with Python, Django, HTML5, CSS3, PostgreSQL, PaystackAPI

## Installation

Clone the repository, run the virtual environment and install all requirements.
```bash
git clone https://github.com/Ceasar15/finances.git
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
pip install requirements.txt
```
Run migrations commands and manage.py to start the development server.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Preview
You can access the live application here.
[Live Preview](http://gecyouthchurch.herokuapp.com/)


## Visuals
![Home Page ](https://user-images.githubusercontent.com/42820626/156560829-4c49807a-2487-466c-b619-d0f23756f9bf.png)
![Sermons Page](https://user-images.githubusercontent.com/42820626/156554177-f38cca7a-6058-4813-a280-e9e1156e0f81.png)
![Achievements Page](https://user-images.githubusercontent.com/42820626/156554134-661943e0-a607-4be3-90bc-2f3329ecea76.png)
![Achievements Page](https://user-images.githubusercontent.com/42820626/156554084-080d0447-3d2f-4e78-ad41-554cba39bcd8.png)
![Achievements Page](https://user-images.githubusercontent.com/42820626/156554062-32085e26-dc3e-4199-82ff-3e2d80c65479.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project status
This project is not under development anymore. 
## License
[MIT](https://choosealicense.com/licenses/mit/)