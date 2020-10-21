def getLatestRank(n, leaderboard, m, user_leaderboard, rank):
    print(f"Leaderboard: {leaderboard}")
    print(f"Rank of Leaderboard: {rank}")
    print(" ")

    for each in range(len(user_leaderboard)):
        ranked = rank.pop(-1)
        user_score = user_leaderboard.pop(0)
        print(f"Rank {ranked} {user_score}")


if __name__ == "__main__":

    n = int(input("Input jumlah permainan yang selesai: "))
    leaderboard = []
    for i in range(n):
        score = int(input("Input hasil score: "))
        leaderboard.append(score)

    m = int(input("Input jumlah permainan baru: "))
    user_leaderboard = []
    for j in range(m):
        new_score = int(input("input new Score: "))
        user_leaderboard.append(new_score)
        leaderboard.append(new_score)

    user_leaderboard.sort(reverse=True)
    result = sorted(set(leaderboard), reverse=True)
    rank = [result.index(i) + 1 for i in leaderboard]

    getLatestRank(n, leaderboard, m, user_leaderboard, rank)