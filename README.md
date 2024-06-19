# Lotus Factory Tool 

## Preparation
1. Install Python 
2. Install the required library with:
    - `pip install -r ./requirements.txt`

## Run
1. Run main.py - `python main.py`

    ```
    PS C:\Dev\LotusFactoryTool> python ./main.py
    Lotus Factory Tool for TX Ver: 00.00.01
    * Serving Flask app 'main'
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```
2. Open WebBrowser and go to `http://127.0.0.1:5000/`


## Create EXE file - For Windows
1. Install `pyinstaller`
    - `pip install pyinstaller`
2. Generate exe-file
    - `pyinstaller --add-data templates:templates --add-data static:static --onefile main.py`
3. See "dist/main.exe" file


