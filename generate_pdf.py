from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import os

def generate_report():
    doc = SimpleDocTemplate("QQWZ_Momentum_Report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, fontSize=18, spaceAfter=20)
    story.append(Paragraph("QQWZ Momentum & Sector Analysis Report", title_style))
    story.append(Spacer(1, 12))

    # Portfolio Health
    story.append(Paragraph("1. Sector Weight Breakdown", styles['Heading2']))
    sector_data = [
        ["Sector", "Total Weight"],
        ["Health Care", "22.45%"],
        ["Energy", "18.72%"],
        ["Information Technology", "12.98%"],
        ["Consumer Discretionary", "10.15%"],
        ["Communication Services", "9.42%"],
        ["Consumer Staples", "8.64%"],
        ["Industrials", "7.32%"],
        ["Materials", "3.84%"],
        ["Financials", "1.69%"]
    ]
    t1 = Table(sector_data, colWidths=[200, 100])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    story.append(t1)
    story.append(Spacer(1, 12))

    # Top Tickers
    story.append(Paragraph("2. Specific Ticker Weights", styles['Heading2']))
    ticker_data = [
        ["Ticker", "Weight", "Status"],
        ["NVDA", "0.71%", "Underweighted"],
        ["ASML", "0.16%", "Low Weight"],
        ["QCOM", "1.47%", "Significant Holding"],
        ["VST", "0.14%", "Low Weight"],
        ["AMD/MU", "0.00%", "Not Present"],
        ["Crypto", "0.00%", "Not Present"]
    ]
    t2 = Table(ticker_data, colWidths=[100, 100, 150])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t2)
    story.append(Spacer(1, 12))

    # Momentum Analysis
    story.append(Paragraph("3. Momentum Factor Analysis", styles['Heading2']))
    momentum_text = """
    The QQWZ 'Momentum' strategy prioritizes Cash Flow over valuation hype. 
    Notable momentum is seen in Healthcare and Gold (Newmont Corp). 
    While Semiconductors are present, the index is underweighting high-cap names like NVDA 
    to focus on companies with stronger free-cash-flow yields.
    """
    story.append(Paragraph(momentum_text, styles['Normal']))
    story.append(Spacer(1, 12))

    # Comparison
    story.append(Paragraph("4. Portfolio Comparison & Diversification", styles['Heading2']))
    comp_text = """
    Direct overlap exists in Energy (CVX, XOM, DVN). 
    Opportunity exists to diversify into Healthcare (GILD, AMGN) and Gold (NEM) 
    to buffer potential volatility in your Tech-heavy Fidelity portfolio.
    """
    story.append(Paragraph(comp_text, styles['Normal']))

    doc.build(story)
    return "QQWZ_Momentum_Report.pdf"

if __name__ == "__main__":
    generate_report()
