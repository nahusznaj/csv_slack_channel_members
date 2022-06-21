# Create CSV file with Slack Channel Members


## Steps to run the script

Download the repo into a folder. Open a terminal and `cd` into the folder.

Create a virtual environment, choosing a `Name` for it:
```
$ python3 -m venv {Name}
```

Activate the virtual environment
```
$ source {Name}/bin/activate
```

Install the requirements with
```
$ pip3 install -r requirements.txt
```

Once you have the Slack Signing Secret, you'd need to add it as an environment variable. To do so, create an `.env` file. You can use the template in this repo:
```
$ cp .env.template .env
```

Then, add the Signing Secret in it and save. Once you saved the file, you'll need to source environment variables with:
```
$ source .env
```

Then you could run the app: 

```
$ python3 create_members_csv.py
```
