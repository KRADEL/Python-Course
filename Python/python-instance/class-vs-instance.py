# class Website:
#     def __init__(self, title):
#         self.title = title


# ws = Website('My site title')
# print(ws.__dict__)

# ws_two = Website('My second site title')
# print(ws_two.__dict__)

class DiffWebsite:
    title = 'My title'


dw = DiffWebsite()
print(dw.title)

dw_two = DiffWebsite()
print(dw_two.title)

# Class attribute belongs to the class-hardcoded
# Instance attribute belongs to a paerticular instance-dynamic