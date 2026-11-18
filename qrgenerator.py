import qrcode
upi_id=input("Enter UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
phonepe_url=f'upi://pay?pa={upi_id}&pn=Reciptent%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Reciptent%20Name&mc=1234'
googlepay_url=f'upi://pay?pa={upi_id}&pn=Reciptent%20Name&mc=1234'

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
googlepay_qr=qrcode.make(googlepay_url)


phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()
