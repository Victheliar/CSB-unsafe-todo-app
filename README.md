# CSB-unsafe-todo-app
A todo-app intentionally made with cyber security flaws for Mooc's Cyber Security Base course.

# Instructions for running the project locally

1. Clone the repository onto your machine with ```git clone git@github.com:Victheliar/CSB-unsafe-todo-app.git```

2. Before running the app, set an environmental variable ```SECRET_KEY``` to the value of your choosing. E.g. in Powershell, this can be done as follows:
```
$env:SECRET_KEY="your-secret-key"
```

3. Now you can install and run the project locally using the following command:
```python manage.py runserver```