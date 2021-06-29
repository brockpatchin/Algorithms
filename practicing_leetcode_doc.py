max_int = 2 ** 32 - 1
def climbingLeaderboard(ranked, player):
	player.sort(reverse = True)
	temp = 0
	phArray = [max_int]
	placingsForPlayer = []

	while len(ranked) != 0 and len(player) != 0:
		if ranked[0] >= player[0]:
			if phArray[temp] > ranked[0]:
				temp += 1
			phArray.append(ranked[0])
			ranked.pop(0)
		elif player[0] >= ranked[0]:
			if phArray[temp] > player[0]:
				temp += 1
			phArray.append(player[0])
			player.pop(0)
			placingsForPlayer.insert(0, temp)

	print(phArray)
	for i in placingsForPlayer:
		print(i)

climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
