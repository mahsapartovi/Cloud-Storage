

class Course:
    
    def __init__(self, cid, cname, req):
        self.courseID = cid
        self.courseName = cname
        self.prerequistiesList = req
        self.post = []
        self.is_finished = False

    def finished(self):
        self.is_finished = True

    def add_req(self, item):
        self.prerequistiesList.append(item)

    def add_post(self, item):
        self.post.append(item)

    def __str__(self):
        return str("course(name={}, id={})".format(self.courseName, self.courseID))


def dfs(root, check, way):
    if root.courseID in check:
        if len(way) == 0:
            print("you can pick {}".format(root.courseID))
        else:
            print("you can't pick course id {} you should pick {}".format(root.courseID, ",".join([str(w) for w in way])))
    
    if not root.is_finished:
        way.append(root)

    for c in root.post:
        dfs(c, check, way)

    if len(way):
        way.pop()


def bfs(root, check, way):
    
    if not root.is_finished:
        way.append(root)

    for c in root.post:
        if c.courseID in check:
            if len(way) == 0:
                print("you can pick {}".format(c.courseID))
            else:
                print("you can't pick course id {} you should pick {}".format(c.courseID, ",".join([str(w) for w in way])))

    for c in root.post:
        bfs(c, check, way)

    if len(way):
        way.pop()


def main():
    n = int(input("number of courses: "))
    courses = []
    for _ in range(n):
        cid = int(input("course id: "))
        cname = input("course name: ")
        r = input("list of reqires example 3 2 5 1 or (none): ")
        if r != "none":
            req = list(map(int, r.split(" ")))
        else:
            req = []
        courses.append(Course(cid, cname, req))


    root_course = Course(-1, "root", [])
    root_course.finished()
    for c in courses:
        if len(c.prerequistiesList) == 0:
            root_course.add_post(c)
    
    for c in courses:
        for i in range(len(c.prerequistiesList)):
            for c2 in courses:
                if c2.courseID == c.prerequistiesList[i]:
                    c2.add_post(c)
                    break

    gozarande_shode = list(map(int, input("gozarandeh shode example 3 2 5 1: ").split(" ")))
    
    for c in courses:
        for i in gozarande_shode:
            if c.courseID == i:
                c.finished()

    check = list(map(int, input("checking example 3 2 5 1: ").split(" ")))

    print('====================Answer Dfs====================')
    dfs(root_course, check, [])

    print('====================Answer Dfs====================')
    bfs(root_course, check, [])

main()