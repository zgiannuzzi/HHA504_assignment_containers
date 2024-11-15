# HHA504_assignment_containers
HHA 504 docker assignment 


## 1. Created a simple flask app that Generates a random number between 1 and 100 and can go back to its home page. 

```python
from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

#@app.route('/')
#def hello_world():
    #return 'Hello, World! From a Flask app in a Docker container!'


@app.route('/', methods=['GET','POST'])
def hello_world():
    print('success')
    return render_template('login.html', var_home = url_for('rand_number'),var_home2 = url_for('hello_world'))
    
@app.route('/home', methods = ['GET', 'POST'])
def rand_number():
    random_number = random.randint(1, 100)
    print(random_number)
    return render_template("index.html",number=random_number,var_home2 = url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
```

## Built docker image 

- Built docker image and pushed to docker repo https://hub.docker.com/repository/docker/zgiannuzzi/hha504hw/general
```docker
FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "flask_app.py"]
```

## Ran docker from GCP 

1. Created Container app in GCP 
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerGCP1.png)

2. Deployed and successfully ran dockerfile 
-link for flask app GCP https://hha504flaskapp-227190841197.us-central1.run.app
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerGCP2.png)
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerGCP3.png)

## Ran docker from Azure
1. Created container in Azure 
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerAzure1.png)

2. Deployed and succesfully was able to get app to run through Azure 
- link for flask app in Azure https://hha504flaskapp.mangoforest-4a073be3.eastus.azurecontainerapps.io/
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerAzure2.png)
![Image of Azure overview](https://github.com/zgiannuzzi/HHA504_assignment_containers/blob/main/dockerAzure3.png)