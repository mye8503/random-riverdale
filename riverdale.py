import random

def fill_unwatched():
    eplist = [0, 13, 22, 22, 19, 19, 22]
    f = open("unwatched_episodes.txt", "w")

    g = open("watched_episodes.txt")
    watched = g.read().split("\n")

    for season in range(1, len(eplist)):
        for epnum in range(1, eplist[season]+1):
            epname = str(season) + "." + str(epnum)
            if epname not in watched:
                f.write(epname + "\n")

    g.close()
    f.close()


if __name__ == "__main__":
    numeps = 117

    f = open("unwatched_episodes.txt")
    unwatched = f.read()
    unwatched = unwatched.split("\n")

    num = random.randint(0, len(unwatched)-1)
    episode = unwatched[num]

    episode = episode.split(".")


    g = open("watched_episodes.txt", "a")
    g.write(unwatched[num] + "\n")
    g.close()

    g = open("watched_episodes.txt")
    watched = g.read()
    watched = watched.split("\n")


    lastfive = watched[-7:-2]

    print("Watch Season", episode[0], "episode", episode[1], end = "\n")
    print("Enjoy! Here are the last five episodes of Riverdale you watched:")
    print("=====")
    for episode in reversed(lastfive):
        print(episode)
    print("=====")


    fill_unwatched()


    f = open("watched_episodes.txt")
    w = f.read()
    g = open("unwatched_episodes.txt")
    u = g.read()

    if len(w.split("\n")) + len(u.split("\n")) - 2 < numeps:
        print("ERROR! MISSING EPISODE!")
        print(numeps - len(w.split("\n")) - len(u.split("\n")), "missing episodes")
