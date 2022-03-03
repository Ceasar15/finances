# Financial and Church Management App
Typically, a personal finance app will have different features such as a shared wallet, bill reminders, auto bill pay, and even managing subscriptions.  

This Finances Application is a church management web application that keeps track of donations, welfare, offerings among other financial obligations. It showcases sermons and announcement from leadership. Admin can add upcoming events and programs. Members can comment on sermon posts. Paystacks payment api was integrated into the application code.

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

```image 1
![Screenshot](screenshot.png)
![plot](./directory_1/directory_2/.../directory_n/plot.png)
![Alt text](relative/path/to/img.jpg?raw=true "Title")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project status
This project is not under development anymore. 
## License
[MIT](https://choosealicense.com/licenses/mit/)