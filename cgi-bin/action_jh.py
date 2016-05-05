import cgi, cgitb, re
cgitb.enable
import usps_module
form=cgi.FieldStorage()
tnum=form.getvalue('tnum')
unum=tnum.upper()
snum=re.sub('[\s+]', '',unum)
tlist=snum.split(',')


print("Content-type:text/html\r\n\r")
print()

print("<html>")
print("<head>")
#print("<script src='C:\Python34\sortable.js'>")
print("</script>")
print("</head>")
print("<body>")
print("<table class='sortable' id='sortabletable' border='2'>")
print("<tr><th>Tracking Number</th><th>Shipping Carrier</th><th>Shipping Details</th></tr>")
for tnumber in tlist:
	if len(tnumber)>25:
		print(tnumber+" is not a valid number. \n Please enter a number that is no more than 25 characters")
	else:
		if tnumber.startswith('1Z'):
			print("<tr>")
			print("<td>")
			print(tnumber)
			print("</td>")
			print("<td>UPS</td>")
			print("<td>")
			print("Go to UPS API")
			print("</td>")
			print("</tr>")
		elif ((len(tnumber)==22 and tnumber.startswith('9')) or (tnumber.startswith('82') and len(tnumber)==10) or ((tnumber.startswith('EC') or tnumber.startswith('EA') or tnumber.startswith('CP')) and tnumber.endswith('US') and len(tnumber)==13)):
			print("<tr>")
			print("<td>")
			print(tnumber)
			print("</td>")
			print("<td>USPS</td>")
			print("<td>")
			print(usps_module.usps_call(tnumber))
			print("</td>")
			print("</tr>")
		elif 12 <= len(tnumber) <= 22 and not (tnumber.startswith('1Z') or ((len(tnumber)==22 and tnumber.startswith('9')) or (tnumber.startswith('82') and len(tnumber)==10) or ((tnumber.startswith('EC') or tnumber.startswith('EA') or tnumber.startswith('CP')) and tnumber.endswith('US') and len(tnumber)==13))):
			print("<tr>")
			print("<td>")
			print(tnumber)
			print("</td>")
			print("<td>FedEx</td>")
			print("<td>")
			print("Go to FedEx API")
			print("</td>")
			print("</tr>")
		elif tnumber == "":
			continue
		else:
			print(tnumber+" is not a vaild number. Please re-enter the number or contact your shipping carrier")

print("</table>")
print("</body>")
print("</html>")