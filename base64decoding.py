import base64

def decode_base64(encoded_str):
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"Error decoding string: {e}"

# Example usage
if __name__ == "__main__":
    encoded_input = input("Enter Base64-encoded string: ")
    print("Decoded output:", decode_base64(encoded_input))
