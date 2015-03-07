# paperScissorsRock
A simple paper scissors rock game for CoderDojo. Use this to learn
about Git and Python!

## Before you start
1. Install git and python

        sudo apt-get install git python
    

## Getting Started
1. Create a GitHub account
2. Go to [https://github.com/ndench/paperScissorsRock](https://github.com/ndench/paperScissorsRock)
   and click 'fork'
3. Copy the 'ssh clone url' from your new GitHub Repository
4. Open a terminal and paste the url to the end of the following command:

        git clone <paste url here>

5. `cd` into the project and run the game:

        python paperScissorsRock.py


## Updating the game
1. Pick an item from the TODO list in `paperScissorsRock.py`
2. Create a feature branch
    
        git checkout -b <your feature name>

3. Implement it
4. Add the changes to your `git staging area`:

        git add .

5. Commit your changes

        git commit -m "<your commit message here>"

6. Merge your feature into the master branch

        git merge master

6. Push your changes to your remote repository master branch

        git checkout master
        git push
