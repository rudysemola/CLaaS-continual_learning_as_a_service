# CLaaS Flask skeleton script
#
set -e

# export the variables for flask
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=claas

# run
#python app.py
flask run --host=0.0.0.0 --port=5001