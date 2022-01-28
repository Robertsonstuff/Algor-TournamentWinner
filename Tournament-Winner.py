# Hash table {} - O(n) Time, O(k) space

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam: 0}
	# so far we've created an empty string named currentBestTeam
	#and a dictionary (hast table) called scores with one value - the variable we just created. 
	
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition
		
		winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
		
		updateScores(winningTeam, 6, scores)
		
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
			
	return (f"Out of three games, {currentBestTeam} wins!!")
# this for loop will loop through each iterable in the list and give it a value. idx refers to the games played and competition refers the teams that are playing each other. 
#the result variable clarifies that the result will be the value within the dictionary and not the key.
# the home team and away team has two arguements and refers to the iterable in the loop.

# Is a variable with an if statement, declaring the winningTeam to have a value of the team having the same score (==) as the HOME_TEAM_WON (1) otherwise, the winningTeam will be awayTeam.

#will call the updateScores function with 3 arguements.

# finally coming out of the updateScores function and before the loop ends.
# the if statement on (line 19) states if scores dictionary value of the winningTeam is less than the value of the currentTeam (being 0) call the winningTeam currentBestTeam.
# iterate through the loop
# once the loop has finished, print the current best team.

#So the answer is why did Python win!?
# the answer lies in (line 15) 
# the away teams win the games BUT only if the results [0,0,0]. 
# In this case, the results are [0,0,1] meaning, in the last game, the results ARE equal to HOME_TEAM_WON (line3). So instead of the away team winning, in the last game, the home team wins.
# This means CS wins game 1, Python wins game 2 and Python wins game 3.
# This is why Python wins!! 

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0
		
	scores[team] += points
# this function will do the following.
# if winningTeam is not in scores(the dictionary we set up at the start(line7)) add the team in the dictionary with a value of 0.
# if it is in the dictionary, add the points value (3 from the argurment in line(32)).

blah = tournamentWinner([["HTML","CS"],["CS","Python"],["Python","HTML"]], [0,0,1])
print(blah)