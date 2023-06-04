from fpdf import FPDF
import pandas as pd
import glob
import pathlib as path

filepath = glob.glob("invoices/*.xlsx")

for file_p in filepath:

    # print(data_frame)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = path.Path(file_p).stem

    invoice_name = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=12, txt=f"Invoice nr.{invoice_name}", align="L", ln=1)
    pdf.cell(w=0, h=11, txt=f"Date {invoice_date}", align="L", ln=1)

    data_frame = pd.read_excel(file_p, sheet_name="Sheet 1")

    # adding a header
    ex_columns = list(data_frame.columns)
    col = [i.replace("_", " ").title() for i in ex_columns]
    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=23, h=11, txt=col[0], border=1, align="C")
    pdf.cell(w=65, h=11, txt=col[1], border=1, align="C")
    pdf.cell(w=40, h=11, txt=col[2], border=1, align="C")
    pdf.cell(w=37, h=11, txt=col[3], border=1, align="C")
    pdf.cell(w=26, h=11, txt=col[4], border=1, ln=1, align="C")

    # loading data from tabel
    for index, row in data_frame.iterrows():
        pdf.set_font(family="Times", size=11)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=23, h=11, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=65, h=11, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=40, h=11, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=37, h=11, txt=str(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=26, h=11, txt=str(row["total_price"]), border=1, ln=1, align="C")

    pdf.output(f"output/{filename}.pdf")



