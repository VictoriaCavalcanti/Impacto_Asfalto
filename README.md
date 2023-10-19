# Asphalt Impact Research

To help a **Scientific Iniciation in Asphalt Impact**, we development a **Web Scrappy** to collect reserch data from **EDP's (Enviroment Production Declarations)**. The source of EDP's is [Emerald Eco-Label EPD Tool](https://asphaltepd.org), the current application get specific information from all EDP's from all 39 states of United States of America, in total we got data from 1717 EDP's that are writed in tables (matrices) on csv file format, every state have his on csv file.

The current documentation are in working process and assumes that you are a beginner in programming and not familiar with python projects, so maybe the docs can be to heavily 'step by step' for you.

> [!NOTE]
> Last Update 18/10/2023

## Summary
- [How to use/run the apllication](#how-to-use/run-the-aplication)
- [Application architecture](#application-architecture)
- [How to adapt the apllication](#how-to-adapt-the-application)
- [Next steps](#next-steps)

## How to use/run the aplication

Run the application is pretty easy, but first you need to install the project dependencies, let's get on it.

### Setting the enviroment

First make sure that you have Python 3 installed in your machine, you can download from [here](https://www.python.org/downloads/).

The projects depends on [Requests](https://requests.readthedocs.io/en/latest/) and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libs, to avoid
install this libs in global scope (that may cause version conflits with other python projects in you computer) we strongly recommend using [virtualenv](https://virtualenv.pypa.io/en/latest/) that is a virtual enviroment, you may have a little more work but is worth! Let's create your venv and install the libs.

**To create a virtual env:**

Windows:
```bash
py -m venv .venv
```

Mac/Linux:
```bash
python3 -m venv .venv
```

Now you may have a .venv folder in the project folder, to install the dependencies only in this .venv we need first activate the venv, to do that run this command:

Windows:
```bash
.\.venv\Scripts\activate
```

Mac/Linux:
```bash
.\.venv\bin\activate
```

If things are doing right, you now have a '(.venv)' in the left of console line, that shows that the virtual enviroment is activated.
>[!IMPORTANT]
>Make sure to activate the venv, otherwise the libs will be installed globally

**To install the dependencies:**
```bash
pip install -r requirements.txt
```

**To list packages list:**

```bash
pip list
```

You may have to see this in the left side:

```
beautifulsoup4     
bs4                
certifi            
charset-normalizer 
idna               
pip                
requests           
setuptools         
soupsieve          
urllib3  
```
Done! Finnaly the enviroment is setted and you can run the application.

### Running the application

Windows:
```bash
py run.py
```

Mac/Linux:
``` bash
python3 run.py
```

### Finishing the application:

After running the scrappy, to deactivate the virtual env you just need to run this command:

``` bash
deactivate
```

## Apllication architecture

## How to adapt the application


## Next steps
