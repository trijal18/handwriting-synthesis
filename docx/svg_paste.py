import sys
sys.path.append(r'\projects\handwriting-synthesis')
from demo import Hand
import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

dr_name = "Dr. Modi "
hos_name = """St. John's Medical College Hospital 
Sarjapur Road,
Bangalore, Karnataka 560034,
India."""

name="Swastik"
dates="1 May to 15 May"

doc = docx.Document()

# Add table to the header
header = doc.sections[0].header
header_table = header.add_table(rows=1, cols=2, width=Inches(6))
header_table.autofit = False
header_table.columns[0].width = Inches(3)
header_table.columns[1].width = Inches(3)

# Set the text in the left cell (doctor's name and details)
left_cell = header_table.cell(0, 0).paragraphs[0]
left_run = left_cell.add_run(dr_name).bold=True
left_cell.add_run("\nMBBS \nReg. no.: 75463")

# Set the text in the right cell (hospital information)
right_cell = header_table.cell(0, 1).paragraphs[0]
right_cell.text = hos_name
right_cell.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Add an empty heading to separate content
doc.add_heading('', 0)

#style/font for signature
Sign = doc.styles.add_style('Sign', WD_STYLE_TYPE.CHARACTER).font
Sign.size = Pt(2000)
Sign.name = 'Hayollan'
#style/font for handwriting
hand = doc.styles.add_style('hand', WD_STYLE_TYPE.CHARACTER).font
Sign.size = Pt(24)
hand.name = 'Halimun'

#Add para of docs note 

doc.add_paragraph().add_run(f,style='hand')

doc_note=f"""To Whom It May Concern,

This letter certifies that my patient, {name}, was under my care from {dates}. {name} suffered from viral gastroenteritis, experiencing severe nausea, vomiting, diarrhea, and abdominal pain, hindering attendance and academic participation. Recovery mandated rest, hydration, and medication. {name} was advised to abstain from strenuous activities to prevent contagion. Please accommodate {name} accordingly.

Sincerely,

"""
try:
    lines = doc_note.split(",")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/doc_note.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
except Exception as e:
    print(f"An error occurred while saving the creating svgt: {e}")

#adding docs sign
doc.add_paragraph().add_run(f"{dr_name}", style='Sign')

try:
    doc.save('medical_certificate.docx')
    print("Document saved successfully.")
except Exception as e:
    print(f"An error occurred while saving the document: {e}")


