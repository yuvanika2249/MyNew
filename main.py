import streamlit as st
from streamlit_option_menu import option_menu

st.title("Job Salary Prediction")
with st.sidebar:
    select = option_menu(
        menu_title= "Prediction",
        options=["Home","About","Service","Contact"],
        icons=["houses","file-person","database"],
        menu_icon='cast'
    )

if select == "Home":
        st.header("For All Employee's")
        st.subheader("Based On Location & Exprience")
        st.write("- Adding a widget is the same as declaring a variable. No need to write a backend, define routes, handle HTTP requests, connect a frontend, write HTML, CSS, JavaScript,")
        st.write("- Adding a widget is the same as declaring a variable. No need to write a backend, define routes, handle HTTP requests, connect a frontend, write HTML, CSS, JavaScript,")
elif select == "About":
    st.header("About Pages")

elif select == "Service":
    st.header("Service Pages")

elif select == "Contact":
    st.header("Contact Pages")
    
col1,col2,col3 = st.columns(3)

with col1:
    name = st.text_input("Enter your Name")

with col2:
    email=st.text_input("Enter your Email")

with col3:
    age=st.text_input("Enter your age")

if st.button("Submit"):

    st.write(name,email,age)


st.header("Equation of Straight Line")
st.write("The general equation of a straight line is y = mx + c, where m is the slope of the line and c is the y-intercept. It is the most common form of the equation of a straight line that is used in geometry.")
st.latex("y = mx + c")
st.metric("Vinsup", "Python", "20")
st.code("""
        a = 10
        b = 20
        print(a + b)
""",language="python")

n1,n2=st.columns(2)

with n1:
    st.image("https://d13loartjoc1yn.cloudfront.net/article/1687421635_Forms%20of%20Straight%20Line%20Formula.jpg", width=300)
with n2:
    st.image("https://www.onlinemath4all.com/images/equationofline1.png",width=300)

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")


# st.sidebar.title("MENU")
# menu =  st.sidebar.selectbox("Open : ",["Home","About"])

# if menu == "Home":
#     st.title("This is Home page") 
#     st.write("Home Section")
#     st.snow()
# if menu == "About":
#     st.title("About Us")
#     st.write("contains information about us.")
#     st.balloons()


