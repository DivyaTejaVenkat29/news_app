# #!/usr/bin/env bash
#
# echo "Building the project ..."
# # Create and activate a Python virtual environment
# python3.9 -m venv venv
# source venv/bin/activate
#
# # Install project dependencies
# venv/bin/python3.9 -m pip install -r requirements.txt
#
# echo "Make Migration.."
# # Perform database migrations
# venv/bin/python3.9 manage.py makemigrations --noinput
# venv/bin/python3.9 manage.py migrate --noinput
#
# echo "Collect Static"
# # Collect static files
# venv/bin/python3.9 manage.py collectstatic --noinput --clear
#
# # Deactivate the virtual environment
# echo "Build complete."
#
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
#python3.9 manage.py collectstatic --noinput --clear
