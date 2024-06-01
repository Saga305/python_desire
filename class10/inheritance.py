class Browser:
    name = "abc"
    found_year= 2000


class Chrome(Browser):
    name = "chrome"
    found_year=2008
    developed_by="google"

class FireFox(Browser):
    name = "chrome"
    found_year=2008
    developed_by="Mozilla Foundation"


c= Browser()
print(c.name)
print(c.found_year)

c1= Chrome()
print(c1.name)
print(c1.found_year)
print(c1.developed_by)


f= FireFox()
print(f.name)
print(f.found_year)
print(f.developed_by)
