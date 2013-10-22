seedrecruit-challenge
=====================

### Background info
The goal of the challenge was to write an application that can take a job in XML format and a set of candidate profiles (also in XML format).
It should then be able to calculate the top 3 candidates for that job. 

The implementation I wrote is an attempt at creating a re-usable library for doing this task.
I chose to write it in this way because it makes it easier to use across a variety of applications.
It could be used in a Django + REST Framework setup for example.

We use NLTK + WordNet for dealing with the free form of the data. Candidate profiles do not neccessarily use a standard format, so having something to 
allow some room in choice of words and their order was a necessity.

### Usage


#### Short version

Execute the following commands.
```
cd seedrecruit-challenge
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py install
python bin/calculator.py <job_description_file> [<profile_files>]
```

You can run the program on the sample files under "samples" using the following command:
```
python bin/calculator.py samples/job_description.xml samples/profile1.xml samples/profile2.xml samples/profile3.xml samples/profile4.xml samples/profile5.xml
```
To save the resulting JSON, just pipe it to a file ;)
