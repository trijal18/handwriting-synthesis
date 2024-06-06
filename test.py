from demo import Hand

lines = [
    "This letter certifies that my patient",
    "name, was under my care from dates",
    "name suffered from viral gastroenteritis",
    "experiencing severe nausea, vomiting, diarrhear",
]
biases = [.75 for i in lines]
styles = [9 for i in lines]
#stroke_colors = ['red', 'green', 'black', 'blue']
#stroke_widths = [1, 2, 1, 2]

hand = Hand()
hand.write(
    filename='img/test3.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    #stroke_colors=stroke_colors,
    #stroke_widths=stroke_widths
)