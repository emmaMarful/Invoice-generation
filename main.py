from fpdf import FPDF
import pandas as pd
import glob
import pathlib as path

filepath = glob.glob("invoices/*.xlsx")

for file_p in filepath:
    data_frame = pd.read_excel(file_p, sheet_name="Sheet 1")
    # print(data_frame)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = path.Path(file_p).stem
    invoice_name = filename.split("-")[0]
    invoice_date = filename.split("-")[1]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=12, txt=f"Invoice nr.{invoice_name}", align="L", ln=1)
    pdf.cell(w=0, h=11, txt=f"Date {invoice_date}", align="L", ln=1)
    pdf.output(f"output/{filename}.pdf")





