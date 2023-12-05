# SpokaneTech web app

<br/>

## Local Development
### prerequisites
1. git installed on the dev system
2. python installed on the dev system 


### setup steps (in a terminal)
1. clone the repo:

    ```
    git clone git@github.com:SpokaneTech/web_demo_python.git
    ```

    -- or -- 

    ```
    git clone https://github.com/SpokaneTech/web_demo_python.git
    ```

2. cd into the repo directory
    ```
    cd web_demo_python
    ```

3. create a python virtual environment
    ```
    python -m venv venv
    ```

4. activate the python virutal environment
    ```
    source venv/bin/activate
    ```

5. install the python dependancies
    ```
    pip install .[dev]
    ```

6. cd to the django_project directory
    ```
    cd django_project
    ```

7. create a local sqlite3 database by running django migrations
    ```
    ./manage.py migrate
    ```

8. create a local admin user
    ```
    ./manage.py add_superuser --group admin
    ```

9. generate some test data
    ```
    ./manage.py generate_data
    ```

10. start the local demo server
    ```
    ./manage.py runserver
    ```

11. open a browser and navigate to http://127.0.0.1:8000 (log in with admin/admin)


    ** you can stop the local demo server anytime via ```ctrl + c ```

<br/>
FYI:

- steps 1-9 only need to be done once (unless you need to apply new migrations or start over); 
- restart the demo server anytime with the django management command: ```./manage.py runserver```
