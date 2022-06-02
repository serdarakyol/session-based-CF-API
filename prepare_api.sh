#!/bin/bash
# create and fill .env file
touch .env
cat << EOF > .env
IS_DEBUG=False
API_KEY='serdarakyol55@outlook.com'
EOF

# create virtual env
virtualenv venv
source venv/bin/activate

# install requirements.txt
pip install -r requirements.txt

# create data folder
current_folder="$(pwd)"
data_folder=$current_folder"/cf_api/data"
mkdir $data_folder
# install files in data
echo "Downloading collaborative filter data to $data_folder/cf_data.pkl"
gdown https://drive.google.com/uc?id=1iB4UmDc8Bcc4OhLbMdb-7ZflhRRFSBae -O $data_folder"/cf_data.pkl"
echo "Downloading products data to $data_folder/meta.json"
gdown https://drive.google.com/uc?id=1tQezbs22O_-ZtzOhf6GUAs5noDPRdiFU -O $data_folder"/meta.json"
