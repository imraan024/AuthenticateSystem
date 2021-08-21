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
5. Go to BrainStemWorks Directory
 <br>

```
cd BrainStemWorks
```
<br>
6. Go to AuthSystem Directory
 <br>

```
cd AuthSystem
```
<br>
7. Run requirements.txt file
<br>

```
pip install -r requirements.txt
```
<br>

8. Makemigration the models
 <br>

```
python manage.py makemigrations
```
<br>
9. Migrate to database
 <br>

```
python manage.py migrate
```
<br>
10. Create Super User
 <br>

```
python manage.py createsuperuser
```
<br>
11. Run The django App
<br>

```
python manage.py runserver
```
<br>
