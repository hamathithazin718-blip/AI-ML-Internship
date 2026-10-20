import qrcode

# 1. Your specific Internship GitHub URL
data = "https://github.com/hamathithazin718-blip/AI-ML-Internship"

# 2. Configure the QR code grid layout
qr = qrcode.QRCode(
    version=1, 
    box_size=10, 
    border=5
)

# 3. Feed the link into the generator
qr.add_data(data)
qr.make(fit=True)

# 4. Create the image with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# 5. Define the filename and save it in the folder
filename = "internship_github_qr.png"
img.save(filename)

print(f"🎉 Success! Your QR code has been saved as '{filename}'")
