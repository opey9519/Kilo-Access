import qrcode
import io
import base64


def generate_qr_code(qr_url):
    img = qrcode.make(qr_url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    # Convert to Base64 string so frontend can render as <img src="data:image/png;base64,...">
    qr_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return qr_base64
