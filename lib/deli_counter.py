def line(katz_deli):
  if not katz_deli:
    print("This line is currently empty")
  else:
    line_message ="The line is currently:"
    for i, person in enumerate(katz_deli, start=1):
      line_message += f"{i}. {person}" 
    print(line_message)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if katz_deli:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")
    else:
        print("There is nobody waiting to be served.")


