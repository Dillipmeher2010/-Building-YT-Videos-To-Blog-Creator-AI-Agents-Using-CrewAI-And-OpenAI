# crew.py
import streamlit as st

# Try importing Crew with error handling
try:
    from crewai import Crew
    crew_loaded = True
except ImportError as e:
    crew_loaded = False
    crew_error = str(e)

def main():
    st.title("YouTube Video to Blog Creator")
    st.write("This is a test app.")
    
    if crew_loaded:
        st.write("Crew module imported successfully!")
        # You can add more functionality to test Crew
        try:
            crew_instance = Crew()  # Attempt to create an instance
            st.write("Crew instance created successfully!")
        except Exception as e:
            st.write(f"Error creating Crew instance: {str(e)}")
    else:
        st.write(f"Error loading Crew module: {crew_error}")

if __name__ == "__main__":
    main()
