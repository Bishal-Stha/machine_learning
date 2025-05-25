# import pickle
# import numpy as np
# import streamlit
# loaded_model = pickle.load(open('trained_model.sav','rb'))
# def predict_score():
#     # input_data = (18,1,9,1.5,0,0,85,6,2,3,1,2,2,1)
#     age = int (input("Enter age: "))
#     gender = int (input("Enter gender [1 for 'Male', 0 for 'Female']"))
#     study_hours_per_day = float (input("Enter how many hours do you study per day: "))
#     social_media_hours = float (input("Enter how many hours do spend on social media: "))
#     netflix_hours = float (input("Enter how many hours do you spend on netflix: "))
#     part_time_job = int (input("Enter your partime job status [1 for 'Yes', 0 for 'No']"))
#     attendance_percentage = float (input("Enter your attendance percentage: "))
#     sleep_hours = float (input("Enter how many hours do you sleep: "))
#     diet_quality = int (input("Enter your diet quality ['Poor':0, 'Fair':1, 'Good':2]"))
#     exercise_frequency = int (input("Enter how many days in a week do you exercise: "))
#     parental_education_level = int (input("Enter your parent's education level['High School': 1,'Bachelor': 2,'Master': 3]"))
#     internet_quality = int (input("Enter your internet quality ['Poor':0, 'Average':1, 'Good':2]"))
#     mental_health_rating = int (input("Enter your mental health rating [1-10] 1-> means low mental health, 10-> good mental health"))
#     extracurricular_participation = int (input("Enter your extracurricular participation [1 for 'Yes' or 0 for 'No'] "))

#     input_data = (age, gender, study_hours_per_day, social_media_hours,
#        netflix_hours, part_time_job, attendance_percentage,
#        sleep_hours, diet_quality, exercise_frequency,
#        parental_education_level, internet_quality, mental_health_rating,
#        extracurricular_participation)
#     np_input_data = np.asarray(input_data)
#     input_featuress = np_input_data.reshape(1,-1)
#     # print(np_input_data)
#     prediction = loaded_model.predict(input_featuress)
#     print("Model Prediction: ")
#     print(f"Your estimated score: {prediction[0]:.3f}")


# if __name__ == "__predict_score__":
#     predict_score()

import pickle
import numpy as np
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def predict_score(input_data):
    np_input_data = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(np_input_data)
    return prediction[0]

def main():
    st.title("📘 Student Exam Score Predictor")

    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    gender = st.radio("Gender", ['Male', 'Female'])
    study_hours_per_day = st.number_input("Study hours per day", min_value=0.0, max_value=24.0, step=0.5)
    social_media_hours = st.number_input("Social media hours", min_value=0.0, max_value=24.0, step=0.5)
    netflix_hours = st.number_input("Netflix hours", min_value=0.0, max_value=24.0, step=0.5)
    part_time_job = st.radio("Part-time job?", ['Yes', 'No'])
    attendance_percentage = st.slider("Attendance percentage", 0, 100)
    sleep_hours = st.number_input("Sleep hours", min_value=0.0, max_value=24.0, step=0.5)
    diet_quality = st.selectbox("Diet Quality", ['Poor', 'Fair', 'Good'])
    exercise_frequency = st.slider("Exercise frequency (days per week)", 0, 7)
    parental_education_level = st.selectbox("Parental education level", ['High School', 'Bachelor', 'Master', 'None'])
    internet_quality = st.selectbox("Internet quality", ['Poor', 'Average', 'Good'])
    mental_health_rating = st.slider("Mental health rating (1 = poor, 10 = excellent)", 1, 10)
    extracurricular_participation = st.radio("Extracurricular participation", ['Yes', 'No'])

    if st.button("Predict Exam Score"):
        # Mapping string inputs to numeric values
        gender = 1 if gender == 'Male' else 0
        part_time_job = 1 if part_time_job == 'Yes' else 0
        diet_quality = {'Poor': 0, 'Fair': 1, 'Good': 2}[diet_quality]
        parental_education_level = {'None': 0, 'High School': 1, 'Bachelor': 2, 'Master': 3}[parental_education_level]
        internet_quality = {'Poor': 0, 'Average': 1, 'Good': 2}[internet_quality]
        extracurricular_participation = 1 if extracurricular_participation == 'Yes' else 0

        input_data = (
            age, gender, study_hours_per_day, social_media_hours,
            netflix_hours, part_time_job, attendance_percentage,
            sleep_hours, diet_quality, exercise_frequency,
            parental_education_level, internet_quality, mental_health_rating,
            extracurricular_participation
        )

        score = predict_score(input_data)
        st.success(f"🎯 Predicted Exam Score: {score:.2f}")

if __name__ == '__main__':
    main()
