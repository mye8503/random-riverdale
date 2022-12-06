import random
import urllib.request
import re
import sys

def update_unwatched(numeps, newep):
    f = open("unwatched_episodes.txt", "r+")
    d = f.readlines()
    f.seek(0) # go back to top

    for line in d:
        if line.strip("\n") != newep:
            f.write(line)

    f.truncate()

    g = open("watched_episodes.txt")
    watched = g.readlines()


    if len(d) - 1 + len(watched) < numeps:
        print("ERROR! MISSING EPISODE!")
        print(len(d) - 1)
        print(len(watched))
        print(numeps - len(d) + 1 - len(watched), "missing episodes")

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


def run_normal():
    numeps = 117

    f = open("unwatched_episodes.txt")
    unwatched = f.read()
    f.close()
    unwatched = unwatched.split("\n")

    num = random.randint(0, len(unwatched)-1)
    episode = unwatched[num]

    seasep = episode.split(".")


    g = open("watched_episodes.txt", "r+")
    watched = g.readlines()
    g.write(unwatched[num] + "\n")
    g.close()

    if len(watched) >= 5:
        lastfive = watched[-5:]
    else:
        lastfive = watched

    print("Watch Season", seasep[0], "episode", seasep[1], end = "\n")
    print()
    epinfo(seasep[0], seasep[1])
    print()

    print("Enjoy! Here are the last five episodes of Riverdale you watched:")
    print("\n=====")
    for ep in reversed(lastfive):
        print(ep.strip("\n"))
    print("=====")


    update_unwatched(numeps, episode)


def reset():
    f = open("watched_episodes.txt", "w")
    f.close()

    f = open("unwatched_episodes.txt", "w")

    eplist = [0, 13, 22, 22, 19, 19, 22]

    for season in range(1, len(eplist)):
        for epnum in range(1, eplist[season]+1):
            epname = str(season) + "." + str(epnum)
            f.write(epname + "\n")
    


if __name__ == "__main__":
    print()
    
    if len(sys.argv) == 1:
        run_normal()

    else:
        if sys.argv[1].lower() == "reset":
            reset()




    


    
