"""One-off: generate a clean PDF resume from the .docx source.

Usage: python scripts/build_resume_pdf.py
Outputs: assets/Gabriela_Henriquez_Resume.pdf

This is a build helper, not part of the static site itself.
"""
from __future__ import annotations
import os, re
import docx
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable,
)

SRC = "assets/Gabriela Henriquez_Resume.docx"
OUT = "assets/Gabriela_Henriquez_Resume.pdf"

ACCENT = colors.HexColor("#0b5a72")
INK = colors.HexColor("#0f1f2e")
INK_SOFT = colors.HexColor("#3a4a5b")


def styles():
    s = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=s["Title"], fontName="Helvetica-Bold",
                          fontSize=22, leading=26, textColor=INK, spaceAfter=2, alignment=0)
    contact = ParagraphStyle("Contact", parent=s["Normal"], fontName="Helvetica",
                             fontSize=9.5, leading=13, textColor=INK_SOFT, spaceAfter=10)
    h1 = ParagraphStyle("H1", parent=s["Heading1"], fontName="Helvetica-Bold",
                        fontSize=11, leading=14, textColor=ACCENT,
                        spaceBefore=12, spaceAfter=4, textTransform="uppercase",
                        alignment=0)
    h2 = ParagraphStyle("H2", parent=s["Heading2"], fontName="Helvetica-Bold",
                        fontSize=10.5, leading=13, textColor=INK,
                        spaceBefore=6, spaceAfter=0)
    sub = ParagraphStyle("Sub", parent=s["Normal"], fontName="Helvetica-Oblique",
                         fontSize=9.5, leading=12, textColor=INK_SOFT, spaceAfter=2)
    body = ParagraphStyle("Body", parent=s["Normal"], fontName="Helvetica",
                          fontSize=9.5, leading=13, textColor=INK, spaceAfter=2)
    return dict(name=name, contact=contact, h1=h1, h2=h2, sub=sub, body=body)


def hr():
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=2, spaceAfter=6)


def parse_docx(path):
    d = docx.Document(path)
    paras = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    return paras


def build():
    paras = parse_docx(SRC)
    st = styles()

    story = []
    # Header: name + contact line
    name = paras[0]
    contact = paras[1]
    story.append(Paragraph(name.title(), st["name"]))
    # Tidy contact line: collapse whitespace, escape <>
    contact = re.sub(r"\s+", " ", contact).strip()
    story.append(Paragraph(contact, st["contact"]))
    story.append(hr())

    SECTIONS = {
        "PROFESSIONAL SUMMARY": "Professional Summary",
        "PROFESSIONAL EXPERIENCE": "Professional Experience",
        "CORE COMPETENCIES": "Core Competencies",
        "TECHNICAL SKILLS": "Technical Skills",
        "EDUCATION": "Education",
    }

    i = 2
    while i < len(paras):
        line = paras[i]
        upper = line.upper().strip().rstrip(":")
        if upper in SECTIONS:
            story.append(Paragraph(SECTIONS[upper].upper(), st["h1"]))
            i += 1
            # Collect items until next section
            block = []
            while i < len(paras) and paras[i].upper().strip().rstrip(":") not in SECTIONS:
                block.append(paras[i])
                i += 1

            if upper == "PROFESSIONAL SUMMARY":
                for p in block:
                    story.append(Paragraph(p, st["body"]))
                    story.append(Spacer(1, 2))
            elif upper == "PROFESSIONAL EXPERIENCE":
                # Pattern: title-line (with date), org line, then bullets
                bullets = []
                cur_title = None
                for p in block:
                    # Title lines tend to have a date range
                    if re.search(r"\b(19|20)\d{2}\b", p) and ("." in p or "—" in p or "-" in p) and len(p) < 140:
                        # flush previous bullets
                        if cur_title and bullets:
                            story.append(ListFlowable(
                                [ListItem(Paragraph(b, st["body"]), leftIndent=10) for b in bullets],
                                bulletType="bullet", start="•", leftIndent=14, bulletFontSize=8,
                                spaceAfter=4))
                            bullets = []
                        story.append(Spacer(1, 4))
                        story.append(Paragraph(p, st["h2"]))
                        cur_title = p
                    elif cur_title and not bullets and ("," in p) and len(p) < 120 and "." in p[-3:]:
                        # Org line right after title
                        story.append(Paragraph(p, st["sub"]))
                    else:
                        bullets.append(p)
                if bullets:
                    story.append(ListFlowable(
                        [ListItem(Paragraph(b, st["body"]), leftIndent=10) for b in bullets],
                        bulletType="bullet", start="•", leftIndent=14, bulletFontSize=8,
                        spaceAfter=4))
            elif upper in ("CORE COMPETENCIES", "TECHNICAL SKILLS"):
                # Group items: subgroup headers are short lines that look like categories
                # For simplicity render as a wrapped comma list, with sub-headings preserved.
                buf = []
                def flush():
                    if buf:
                        story.append(Paragraph(" · ".join(buf), st["body"]))
                        story.append(Spacer(1, 2))
                        buf.clear()
                KNOWN_SUBHEADS = {"Cell & Molecular Biology", "Equipment & Lab Operations",
                                  "Data Management & Software"}
                for p in block:
                    if p in KNOWN_SUBHEADS:
                        flush()
                        story.append(Paragraph(p, st["h2"]))
                    else:
                        buf.append(p)
                flush()
            elif upper == "EDUCATION":
                for p in block:
                    if any(p.startswith(prefix) for prefix in ("Ph.D.", "B.S.", "Certificates")):
                        story.append(Spacer(1, 4))
                        story.append(Paragraph(p, st["h2"]))
                    else:
                        story.append(Paragraph(p, st["sub"]))
        else:
            i += 1

    doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                            leftMargin=0.7*inch, rightMargin=0.7*inch,
                            topMargin=0.6*inch, bottomMargin=0.6*inch,
                            title="Gabriela Henriquez — Resume",
                            author="Gabriela Henriquez")
    doc.build(story)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    build()
