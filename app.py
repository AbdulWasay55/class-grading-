import streamlit as st

st.set_page_config(page_title='Grading System')

st.title('📚 Grading System')

st.subheader('Enter Full Marks of Each Subject')
first_sub = st.number_input('Enter full marks of English', min_value=0)
second_sub = st.number_input('Enter full marks of Maths', min_value=0)
third_sub = st.number_input('Enter full marks of Science', min_value=0)
forth_sub = st.number_input('Enter full marks of Computer', min_value=0)
fifth_sub = st.number_input('Enter full marks of History', min_value=0)

st.subheader('Enter Obtained Marks of Each Subject')
first_obt = st.number_input('Enter obtained marks of English', min_value=0)
second_obt = st.number_input('Enter obtained marks of Maths', min_value=0)
third_obt = st.number_input('Enter obtained marks of Science', min_value=0)
forth_obt = st.number_input('Enter obtained marks of Computer', min_value=0)
fifth_obt = st.number_input('Enter obtained marks of History', min_value=0)

# I add this condtion for the validation error if user try to give the value of obtain marks higher then full marks this condtion give the error of in valid obtain marks
if (first_obt > first_sub or second_obt > second_sub or 
    third_obt > third_sub or forth_obt > forth_sub or 
    fifth_obt > fifth_sub):
    
    st.error("❌ Error: Obtained marks cannot be greater than full marks. Please enter valid marks.")
else:
    total_marks_subject = first_sub + second_sub + third_sub + forth_sub + fifth_sub
    obtain_marks = first_obt + second_obt + third_obt + forth_obt + fifth_obt

    if total_marks_subject > 0:  # To avoid division by zero
        percentage = (obtain_marks / total_marks_subject) * 100

        st.write(f"### 📊 Total Marks: {total_marks_subject}")
        st.write(f"### ✅ Obtained Marks: {obtain_marks}")
        st.write(f"### 📈 Percentage: {percentage:.2f}%")

        # Determine the grade
        if percentage >= 90:
            st.success("🎉 Excellent! Grade: A+")
        elif percentage >= 80:
            st.success("👍 Very Good! Grade: A")
        elif percentage >= 70:
            st.info("😊 Good! Grade: B")
        elif percentage >= 60:
            st.warning("🙂 Fair! Grade: C")
        elif percentage >= 50:
            st.warning("😐 Pass! Grade: D")
        else:
            st.error("❌ Failed! Grade: F")
    else:
        st.warning("Please enter valid marks for each subject.")
