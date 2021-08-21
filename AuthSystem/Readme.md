## Setup Instructions
<br>
1. Clone the repository to local machine
<br>

```
git clone https://github.com/imraan024/BrainStemWorks.git
```
<br >
2. Install virtual Environment to create a django Project
<br>

```
pip install virtualenv
```
<br >
3. Make virtual Environment
<br>

```
virtualenv <name>
```
<br >
4. Activate Virtual Environment
<br>

```
<name>\Scripts\activate
```
<br> 
5. Run requirements.txt file
<br>

```
pip install -r requirements.txt
```
<br>
6. Makemigration the models
 <br>

```
python manage.py makemigrations
```
<br>
7. Migrate to database
 <br>

```
python manage.py migrate
```
<br>
8. Create Super User
 <br>

```
python manage.py createsuperuser
```
<br>
9. Run The django App
<br>

```
python manage.py runserver
```
<br>
