import fpdf
from tqdm import tqdm
from time import sleep

# save FPDF() class into
# a variable pdf
pdf = fpdf.FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.add_font('DejaVu', '',fname='DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', size = 11)


# open the text file in read mode
f = open('Seoul Station Druid.txt' , encoding="utf-8")

# insert the texts in pdf
for x in tqdm(f ,desc='Processing....', ascii=False, ncols=75):
	# x2 =x.encode('latin-1', 'replace').decode('latin-1')
	#pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    pdf.cell(40, 10, txt = x, ln = 1)
    #sleep(0.05)

# save the pdf with name .pdf
pdf.output("Seoul Station Druid.pdf",'F')
print("Complete.")
