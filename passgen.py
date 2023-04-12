import streamlit as st
import random
import string

# Define the password generator function
def generate_password(length, lowercase, uppercase, numbers, symbols):
    # Define the characters to be used in the password
    letters = ""
    if lowercase:
        letters += string.ascii_lowercase
    if uppercase:
        letters += string.ascii_uppercase
    if numbers:
        letters += string.digits
    if symbols:
        letters += string.punctuation

    # Generate a password
    password = ''.join(random.choice(letters) for i in range(length))
    return password

# Create a Streamlit app
def main():
    st.set_page_config(page_title="Password Generator", page_icon="🔒")
    st.title("Password Generator")

    # Define the input fields
    length = st.slider("Password length", 6, 20, 10)
    lowercase = st.checkbox("Include lowercase letters")
    uppercase = st.checkbox("Include uppercase letters")
    numbers = st.checkbox("Include numbers")
    symbols = st.checkbox("Include symbols")

    # Generate a password and display it
    if st.button("Generate Password"):
        password = generate_password(length, lowercase, uppercase, numbers, symbols)
        st.write("Your password is:")
        st.write(password)

if __name__ == "__main__":
    main()
