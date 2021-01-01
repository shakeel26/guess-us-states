import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game!')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
list = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50', prompt='Another state ?').title()
    if answer_state == 'Exit':
        missing_states = []
        for state in list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break;

    if answer_state in list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

