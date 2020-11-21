if [ ! -d "venv" ];then 
    echo ----------------------------------
    echo ----- Creating Virtual Env -------
    echo ----------------------------------
    python -m venv venv
    echo ------------------------------
    echo Activating Virtual Environment
    echo ------------------------------
    source venv/bin/activate
fi

if [ -d "venv" ];then
    echo ------------------------------
    echo Activating Virtual Environment
    echo ------------------------------
    source venv/bin/activate
fi

python -m spacy download en
pip install -r requirements.txt

export ENV_FILE_LOCATION=.env
export export FLASK_APP=run.py

echo ---------------------
echo Running Flask Backend
echo ---------------------
flask run


