from reportlab.pdfgen import canvas

def calculate_fee_by_days(category, days):
    free = 50 if category in ['Full Town', 'Full Town Family'] else 40
    if days <= free:
        return 0
    elif days <= 100:
        return (days - free) * 15
    else:
        return (50 * 15) + ((days - 100) * 20)

def generate_invoice_pdf(member_name, amount, filename="invoice.pdf"):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, f"Invoice for {member_name}")
    c.drawString(100, 730, f"Amount Due: €{amount}")
    c.save()
