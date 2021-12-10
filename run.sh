# CLaaS Flask skeleton script with avalanche
#

#avalanche env
conda activate avalanche-env
# export the variables for flask
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=app

# execute the flask run command
flask run 