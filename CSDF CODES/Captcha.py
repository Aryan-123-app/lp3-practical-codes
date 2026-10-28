from PIL import Image, ImageDraw, ImageFont
import random
import string

# Generate random CAPTCHA text
characters = string.ascii_letters + string.digits
captcha_text = ''.join(random.choice(characters) for _ in range(6))

# Create image
width = 250
height = 80

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load font
try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40
    )
except OSError:
    font = ImageFont.load_default()

# Draw CAPTCHA text
draw.text((50, 20), captcha_text, font=font, fill="black")

# Add random noise lines
for i in range(8):

    x1 = random.randint(0, width - 1)
    y1 = random.randint(0, height - 1)
    x2 = random.randint(0, width - 1)
    y2 = random.randint(0, height - 1)

    draw.line((x1, y1, x2, y2), fill="gray", width=2)

# Save CAPTCHA image
image.save("captcha.png")

# Display CAPTCHA
image.show()

# Verify CAPTCHA
user_input = input("Enter the CAPTCHA shown in the image: ")

if user_input == captcha_text:
    print("CAPTCHA Verified Successfully!")
else:
    print("Incorrect CAPTCHA. Verification Failed.")