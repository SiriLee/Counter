from tkinter import *

root = Tk()
root.title('Siri的计算器')
root.geometry('360x600')

content = ''
btn_dates = [
    ['Clear', 'Del', '//', '*'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '-'],
    ['**', '0', '.', '='],
]

for r in range(5):
    for c in range(4):
        btn = Button(root, text=btn_dates[r][c], font=('黑体', 15), command=lambda x=btn_dates[r][c]: btn_click(x))
        btn.place(x=90*c, y=150+90*r, width=90, height=90)


def btn_click(date):
    global content
    if date == 'Clear':
        expression.set('')
        content = ''
        result.set('')
    elif date == 'Del':
        content = content[:-1]
        expression.set(content)
    elif date == '=':
        expression.set('')
        result.set(f'{eval(content)}')
        content = ''
    else:
        content += date
        expression.set(content)


expression = StringVar()
exp_label = Label(root, textvariable=expression, font=('斜体', 15))
exp_label.place(x=0, y=20, width=360, height=30)

result = StringVar()
res_label = Label(root, textvariable=result, font=('幼体', 20))
res_label.place(x=0, y=60, width=360, height=80)

root.mainloop()
