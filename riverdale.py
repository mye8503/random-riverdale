import random
import urllib.request
import re

def fill_unwatched(numeps):
    eplist = [0, 13, 22, 22, 19, 19, 22]
    f = open("unwatched_episodes.txt", "w")

    g = open("watched_episodes.txt")
    watched = g.read().split("\n")

    for season in range(1, len(eplist)):
        for epnum in range(1, eplist[season]+1):
            epname = str(season) + "." + str(epnum)
            if epname not in watched:
                f.write(epname + "\n")

    f.close()
    f = open("unwatched_episodes.txt")

    w = f.read()

    wlen = len(w.split("\n"))
    ulen = len(watched)

    if wlen + ulen - 2 < numeps:
        print("ERROR! MISSING EPISODE!")
        print(wlen)
        print(ulen)
        print(numeps - wlen - ulen, "missing episodes")

    g.close()
    f.close()


def epinfo(season, episode):
    term = "s0" + season + "/e"
    if len(episode) == 1:
        term = term + "0" + episode
    else:
        term = term + episode

    link = "https://www.rottentomatoes.com/tv/riverdale/"+ term #+"&ei=UTF-8"

    f = urllib.request.urlopen(link)
    page = f.read().decode("utf-8")
    f.close()
    # print(page)
    
    split_page = re.split("<|>", page)
    # print(split_page)

    info = ""
    for term in split_page:
        if "Chapter" in term:
            info = term
            break


    info = info.split('"name":')
    info = info[1].split('"description":')

    name = info[0].strip(',"')
    desc = info[1].split('"startDate":')[0]
    desc = desc.strip(',"')
    
    print(name)
    print()
    print(desc)

    


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
    print()
    epinfo(episode[0], episode[1])
    print()

    print("Enjoy! Here are the last five episodes of Riverdale you watched:")
    print("=====")
    for episode in reversed(lastfive):
        print(episode)
    print("=====")


    fill_unwatched(numeps)


    
