# Election-Analysis

## Project Overview
A Colorado Board of Elections employe has given you the following tasks to complete the elction audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of hte lection based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code

## Summary
The analysis of the election show that: 
1. There were 369,711 votes cast in the election.
2. The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
3. The candidate results were: 
    - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes. 
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes. 
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes. 
4. The winner of the election was: 
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

## Challenge Overview - Overview of Election Audit
The Election Audit is a deep dive look into the election results by county in Colorado. In this analysis, I took a look at the total voter turnout for each county, the percentage of votes from each county out of the total count and, ultimately, find the county with the highest turnout. This is to understand what each county's contribution was to the total and of the participating counties, who had the most participation. 

## Challange Summary - Election-Audit Results
1. How many votes were cast in this congressional election? 
    - There were 369,711 votes casted in this congressional election. 
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
        - Jefferson County had 38,855 votes in total which made up 10.5% of the total votes
        - Denver County had 306,055 votes in total which made up 82.8% of the total votes
        - Arapohoe County had 24,801 votes in total which made up 6.7% of the total votes.
3. Which county had the largest number of votes?
    - Denver had the largest number of votes across the three counties with 306,055 votes.
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    - Charles Casper Stockham received 85,213 votes which was 23.0% of the total votes.
    - Diana DeGette received 272,892 votes which was 73.8% of the total votes.
    - Raymon Anthony Doane received 11,606 votes which made up 3.1% of the total votes.
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Diana DeGette won the election with 272,892 votes, which mad up 73.8% of the total votes. 

## Election-Audit Summary
This Election Audit code can be used for future elections to tally up the votes in a quick and error free way. The code can be used in different states and different election, just as long the format of the data file stays the same. 
For the future, I have a few suggestions on how the code can be modified and used for other elections, see below: 
1. Deep Dive in the voting tally for each candidate by each county. This would be looking at for each county, how many did each candidates receive and their percent of total contribution. The way you can do this is by including nested if statements that look into each county and tallies up votes by candidates. 
2. If in the future, the datafile can include the source of the votes (paper ballots, electronic ballots, etc.), then you can modify the code to tally up the votes by voting source. This would be done similarly to the approach I used to tally up the votes by county and candidate - and if statement to tally up the votes by voting source and a for-loop to get percent of total as well as get the voting source with the largest participation. Having information can help inform you what trend of voting source the population is going towards.
