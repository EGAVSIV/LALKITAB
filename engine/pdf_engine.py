from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(report, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for item in report:

        text = f"""
        <b>{item['planet']}</b><br/>
        House: {item['house']}<br/>
        State: {item['state']}<br/>
        """

        story.append(
            Paragraph(text, styles['BodyText'])
        )

    doc.build(story)
