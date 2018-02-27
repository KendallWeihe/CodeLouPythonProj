# CodeLouPythonProj
My Python for Data Analysis project for Code Louisville


#### H4(What question are you answering or problem are you analyzing?)  
I was very curious what the most played games on Steam were as it is the most popular digital game distribution platform in use (closely followed by GOG).  

#### H4 (A brief overview of how you accomplished this, including any necessary background for someone to understand the problem, where your data came from, what you used from that data, any analysis you applied to the data, and what you chose to visualize/display in the final product)
As steam doesn't release the parsed data themselves and I was unable to find an up to date database on it I used the website http://steamcharts.com/ to get my data.  I created a CSV containing the top 25 games on steam.  I used the name of the games played and listed their hours played as of 2/12/18.  Once I had python created my SQLITE database and attempted to visualize I realized that this would make for a cluttered chart if I kept all 25 entries in the visualization.  I used my query to limit the amount of data to 10 games.  I ran into a bit of an issue converting the hours played to an INT since they contained commas so I wrote a function to remove the commas and then it was smooth sailing.  I chose to visualize the data in the form of a pie chart to show the variance in overall hours played.  I was quite surprised to see that of the top ten games played 56.4% of the time played is from a game that came out officially in December of 2017.

LINK TO DATAWORLD CSV: https://data.world/nydhog/most-played-steam-games-by-hours-21218

NOTE: There was a minor hours rollback at some point since the CSV was created.  This doesn't affect the overall played percentage or ranking of the games.

#### H4 (Any special requirements, dependencies, or steps to run the project?)

Python3, Anaconda, Pandas, Numpy, Matplotlib, bokeh, and itertools.  These should be standard on a Python3 install.

The SQLITE database generates automatically via the Python script, however I have included it in the repository in case any issues arise with the pull.

For installs see:
https://github.com/RossEpsteinKY/CodeLouPythonProj/blob/master/requirements.txt
