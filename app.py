import streamlit as st
import requests

st.title("Cold Email Generator for Job Description")

job_description = st.text_area("Enter Job Description:")
user_skills = st.text_area("Enter Your Skills (comma-separated):")

if st.button("Generate Cold Email"):
    if job_description:
        # API call to generate cold email using Gemini API
        api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        api_key = "AIzaSyCdeNu1CmvNlME-BS-crzYCgv0Gwjxb4E8"  # User provided API Key
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Generate a cold email for the following job description: {job_description} and skills: {user_skills}"
                }]
            }]
        }

        try:
            response = requests.post(f"{api_url}?key={api_key}", json=payload, headers=headers)
            response.raise_for_status()
            email_content = response.json().get("candidates")[0].get("content").get("parts")[0].get("text")

            st.subheader("Generated Cold Email:")
            st.write(email_content)

        except requests.exceptions.RequestException as e:
            st.error(f"Error generating email: {e}")
            st.error("An error occurred while calling the Gemini API. Please check your API key and network connection.")
        except KeyError as e:
            st.error(f"Error parsing API response: {e}")
            st.error("Unexpected response format from Gemini API.")


    else:
        st.warning("Please enter a job description.")
