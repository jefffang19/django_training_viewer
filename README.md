# django_training_viewer
view pytorch training remotely

## install
1. clone the repo
```
git clone https://github.com/jefffang19/django_training_viewer
```
2. install required packages
```
pip install -r requirements.txt
```
3. migrate database (sqlite)
```
python manage.py migrate
```
4. runserver
```
python manage.py runserver
```
5. connect to ***"your_ip":8000/viewer***, if it shows hello world, then install success


## Urls
(GET) `/viewer/get_training`<br>
shows the training results (loss, acc) on site<br>
<br>
(POST) `/viewer/send_training`<br>
`parameters = {"loss":loss, "acc":acc}`<br>
in your pytorch project, add following code in your training loop
```
import requests

# if you host django server and training on same computer
r = requests.post('http://localhost:8000/viewer/send_training', data = {'loss': loss, 'acc': acc})

# or 

# if you host django server and training on different computer
r = requests.post('http://(django_ip):8000/viewer/send_training', data = {'loss': loss, 'acc': acc})
```
(GET) `/viewer/del_everything`<br>
delete the current data in database<br>
use to reset current table
