source venv/bin/activate
export FLASK_APP="get24"
echo "screen -dmS get24 flask run --host=\"0.0.0.0\"..."
screen -dmS get24 flask run --host="0.0.0.0"
