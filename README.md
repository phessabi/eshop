# [Eshop](http://194.5.192.129:4200/home) [![Build Status](https://travis-ci.com/phessabi/eshop.svg?branch=master)](https://travis-ci.com/phessabi/eshop) ![Alt text](./cover.svg)


Online shopping [website](http://194.5.192.129:4200/home).

## Table of Contents
  + [Installation](#installation)
    + [Backend](#backend)
    + [Frontend](#frontend)
  + [Production](#production)

---

## Installation
1. Install [Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) 

1. Install docker-compose
    ```
    sudo apt install docker-compose
    ```
1. Install [Angular Build Requirements](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)  (node and npm)
   
+ ### Backend
    1. Get the backend
        ```
        git clone "https://github.com/phessabi/eshop"
        ``` 
    1. Go to the backend directory
        ```
        cd eshop
        ```    
    1. Build Docker Image: 
        * If you can access docker in your country (if you can open this [link](https://hub.docker.com/)):
            ```
            sudo docker-compose up --build test
            ```
    
        * If docker is blocked in your country you have 2 options (second one is easier)
            * Use a vpn or any [method](https://shecan.ir) to bypass sanctions and do the previous step
    
            * Download the [python docker image](https://www.dropbox.com/s/tqp8i7r77jloywe/python3.zip?dl=0) as "python3.zip" and run
                ```
                sudo docker load -i python3.zip
                sudo -E docker-compose up --build test
                ```
    1. Run the backend on container (runs on localhost:8000)
        ```
        sudo docker-compose up
        ```

+ ### Frontend
     1. Get the frontend
        ```
        git clone "https://github.com/pedramabdzadeh/agile-front-end"
        ``` 
    1. Go to the frontend directory
        ```
        cd agile-front-end
        ```
    1. Change the backend url to your localhost (http://0.0.0.0:8000/) in the file below
        ```
        agile-front-end/src/app/features/api-management/services/http/http.service.ts
        ```
        ![Alt text](./Http-service.png)
    1. Build the angular image
        ```
        npm install -save
        ng build --prod --build-optimizer=false
        ```
    1. Serve the image(./dist/front-end/*) on [Apache](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview) server (port :4200)
        ```
        sudo mkdir /var/www/agile.com
        sudo cp -r ./dist/front-end/* /var/www/agile.com/
        ```
    1. In your browser enter the URL: localhost:4200 to check if the app is working


## Production

The application is currently running [here](http://194.5.192.129:4200/home)