# 1.
# def get_evens(numbers_list):
#     empty = []
#     for i in numbers_list:
#         if i % 2 == 0:
#             empty.append(i)
#         else:
#             pass
# 2.
def display_team(**kwargs):
    for key, value in kwargs.items():
        print(f"The {key} is {value}")

display_team(manager="Alice", developer="Bob", designer="Aryan")

def grades(**kwargs):
  for key, value in kwargs.items():
    print(f"Student {key} scored {value}")
grades(Aryan = 95, Elon =  88, Steve =  70)
