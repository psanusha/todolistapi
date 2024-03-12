# ToDoList API
## The Todo_List Django Web App offers the following features:
* User Authentication
* ToDo List

## How to run the Project
#### Create a virtual environment
```angular2html
virtualenv myenv
```
#### Activate the virtual environment
```angular2html
source myenv/bin/activate
```
#### Migrate the Database
```angular2html
python manage.py makemigrations
python manage.py migrate
```
#### Create Superuser
```angular2html
python manage.py createsuperuser
```
#### To run the project
```angular2html
python manage.py runserver
```
## How to access each API, with examples and sample response

### User Authentication
#### Register
##### url
```angular2html
 http://127.0.0.1:8000/api/auth/register
```
##### Sample Input
```angular2html
{   "username":"Nirmal",
    "email":"nirmal@gmail.com",
    "password":"12345"
}
```
##### Sample Output
```angular2html
{
    "status": "success",
    "code": 201,
    "details": {
        "username": "Nirmal",
        "email": "nirmal@gmail.com",
        "password": "12345"
    }
}
```

#### Login
##### url
```angular2html
 http://127.0.0.1:8000/api/auth/login
```
##### Sample Input
```angular2html
{
    "username": "Nirmal",
    "password": "12345"
}
```
##### Sample Output
```angular2html
{
    "token": "52b22533d658d285c506ace40ef5407f67111734"
}
```


### ToDo List
### Category
#### 1. To list 
##### url
```angular2html
http://127.0.0.1:8000/categorylist/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
##### Sample Output
```
[
    {
        "id": 1,
        "title": "Personal",
        "time": "2024-03-06T10:44:39.227548Z",
        "created_date": "2024-03-06T10:44:39.228912Z",
        "created_by": 4
    },
    {
        "id": 2,
        "title": "Study",
        "time": "2024-03-06T11:48:31.761510Z",
        "created_date": "2024-03-06T11:48:31.761510Z",
        "created_by": 4
    }
]
```

#### 2. To Create 
##### url
```angular2html
http://127.0.0.1:8000/categorycreate/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
```angular2html
{
  "title":"Sample Title"
}
```
##### Sample Output
```angular2html
{
    "id": 6,
    "title": "Sample Title",
    "time": "2024-03-07T11:53:36.322168Z",
    "created_date": "2024-03-07T11:53:36.323171Z",
    "created_by": 4
}
```
#### 3. To get the details in each Category
##### url
```angular2html
http://127.0.0.1:8000/categorydetails/<str:pk>/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
##### Sample Ouput
```angular2html
{
    "id": 2,
    "title": "Study",
    "time": "2024-03-06T11:48:31.761510Z",
    "created_date": "2024-03-06T11:48:31.761510Z",
    "created_by": 4
}
```
#### 4.To update 
##### url
```angular2html
http://127.0.0.1:8000/categoryupdate/<str:pk>
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
```angular2html
{
    "title":"Updated Sample",
    "created_by": 4
}
```
##### Sample Output
```
{
    "message": "Title updated successfully",
    "data": {
        "id": 2,
        "title": "Updated Sample",
        "time": "2024-03-06T11:48:31.761510Z",
        "created_date": "2024-03-06T11:48:31.761510Z",
        "created_by": 4
    }
}
```
#### 5. To Delete
##### url
```angular2html
 http://127.0.0.1:8000/categorydelete/<str:pk>/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
##### Sample Output
```
{
    "message": "success,Category deleted"
}
```


### Task
#### 1. To list 
##### url
```angular2html
http://127.0.0.1:8000/tasklist/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
##### Sample Output
```angular2html
[
    {
        "id": 1,
        "title": "Rest api",
        "description": "description of the project",
        "created": "2024-03-07T06:49:27.426133Z",
        "started": null,
        "ended": null,
        "status": false,
        "created_date": "2024-03-07T06:49:27.426133Z",
        "category": null,
        "created_by": 4
    }
]
```

#### To Create
##### url
```angular2html
http://127.0.0.1:8000/taskcreate/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
```angular2html
{
    "title": "Project2",
    "category_id": 2,
    "description": "description of the project.",
    "status": false
}
```
##### Sample Output
```angular2html
{
    "id": 10,
    "title": "Project2",
    "description": "description of the project.",
    "created": "2024-03-11T05:25:07.158581Z",
    "started": null,
    "ended": null,
    "status": false,
    "created_date": "2024-03-11T05:25:07.158581Z",
    "category": null,
    "created_by": 4
}
```

#### To Update 
##### url
```angular2html
http://127.0.0.1:8000/taskupdate/<str:pk>/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
```angular2html
{
    "title":"Updated project 2",
    "description": "description of the project",
    "created_by": 4
}
```
##### Sample Output
```angular2html
{
    "message": "Task updated successfully",
    "data": {
        "id": 11,
        "title": "Updated project 2",
        "description": "description of the project",
        "created": "2024-03-11T05:30:17.092751Z",
        "started": null,
        "ended": null,
        "status": false,
        "created_date": "2024-03-11T05:30:17.092751Z",
        "category": null,
        "created_by": 4
    }
}
```
#### To Delete
##### url
```angular2html
http://127.0.0.1:8000/taskdelete/3/
```
##### Sample Input
```angular2html
Authorization : Token <token>
```
##### Sample Output
```angular2html
{
    "message": "success,User deleted"
}
```
## How to create an API

