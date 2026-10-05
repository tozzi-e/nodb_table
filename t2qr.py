import base64
import json
#import urllib.parse
import qrcode
import matplotlib.pyplot as plt

def generate_base64url_query(data_items, base_url="https://tozzi-e.github.io/nodb_table/"):
    # 1. Convert data to JSON string
    json_bytes = json.dumps(data_items).encode("utf-8")

    # 2. Encode bytes to Base64URL string (urlsafe_b64encode handles '-' and '_')
    base64url_bytes = base64.urlsafe_b64encode(json_bytes)

    # 3. Strip padding '=' characters per Base64URL specs
    base64url_str = base64url_bytes.decode("utf-8").rstrip("=")

    # 4. Generate URL with query parameter
    full_url = f"{base_url}?data={base64url_str}"
    return base64url_str, full_url


if __name__ == "__main__":
    # Sample data: list of dicts with 'name' and 'value'
    table_data = [
        {"name": "Name", "value": "Waukesha U100"},
        {"name": "Pipe size (in)", "value": "2"},
        {"name": "S/N", "value": "1234567"},
        {"name": "Max flow rate (gpm)", "value": "100"},
        {"name": "Owner", "value": "J.Parrish"},
    ]

    encoded_str, generated_url = generate_base64url_query(table_data)

    print("--- Base64URL String ---")
    print(encoded_str)
    print("\n--- Complete URL ---")
    print(generated_url)

    img = qrcode.make(generated_url, error_correction=qrcode.constants.ERROR_CORRECT_L)
    id='equipment_data'
# Saving as an image file
    img.save('QR-table.png')

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(img, cmap="gray")
    ax.set_title(f"{id}", fontsize=12, pad=12)
    ax.axis("off")  # Hide axis borders and ticks

    # Save without margins
    plt.savefig(f"{id}-QR-table-2.png", bbox_inches="tight", pad_inches=0.1, dpi=300)
    plt.close()