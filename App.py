import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st
import matplotlib.pyplot as plt
import replicate
import seaborn as sns
import os

regressor = pkl.load(open('HCPS.pkl', 'rb'))

st.set_page_config(page_title='Healthcare Costs Prediction System', page_icon = 'images/icon.png')

col1, col2 = st.columns([1,3])
with col1: st.image('images/homepage.jpg')
with col2: st.header('Healthcare Costs Prediction System')
st.sidebar.title('Menu')
options = st.sidebar.radio('Predict Costs As A:', options = ['Medical Aid Provider', 'Policy Holder', 'Healthcare Provider'])

#UI FOR MEDICAL AID PROVIDERS
if options == 'Medical Aid Provider':
    with st.expander('Click Here To Enter Details And Start Prediction'):
        sex = st.selectbox('Choose Gender', ['Female','Male'])
        age = st.slider('Enter Age', 5, 80)
        bmi = st.slider('Enter BMI', 5, 100)
        children = st.slider('Enter Number of Children', 0, 5)
        smoker = st.selectbox('Are you a Smoker?', ['Yes', 'No'])
        region = st.selectbox('Choose Region', ['northeast','northwest','southeast','southwest'])

        if sex == 'Female':
            sex = 0
        else:
            sex = 1
        if smoker == 'Yes':
            smoker = 1
        else:
            smoker = 0
        if region == 'northeast':
            region = 0
        if region == 'northwest':
            region = 1
        if region == 'southeast':
            region = 2
        if region == 'southwest':
            region = 3

        input_data = (age, sex, bmi, children, smoker, region)
        input_data = np.asarray(input_data)
        input_data = input_data.reshape(1,-1)

        if st.button('Predict'):
            st.subheader('Predicted Costs')
            predicted_costs= regressor.predict(input_data)
            display_string = '* The predicted Healthcare Costs will be: '+str(round(predicted_costs[0],2)) + ' US Dollars'
            st.markdown(display_string)

#RECOMMENTATIONS 1         
            if predicted_costs < 15001:
                st.write("* The predicted healthcare costs for this individual are relatively low. It is suggested to allocate resources efficiently to provide necessary care and support, optimizing value and health outcomes.") 
            if predicted_costs > 15000 and predicted_costs < 35001:
                st.write("* The predicted healthcare costs for this individual are moderate. It is recommended to allocate resources accordingly to ensure suitable care and support, balancing financial responsibility with individual needs.")
            if predicted_costs > 35000:
                st.write("* The predicted healthcare costs for this individual are substantially high. It is suggested that the individual be prioritized for resource allocation to ensure adequate care and support, given the significant financial burden.")
            
            if smoker == 1 or region == 0 or region == 2:
                st.subheader('Potential Health Threats')
            if smoker == 1:
                st.write("* Given smoking status, it's important to note that smoking may increase the risk of Lung Cancer, Heart Disease, and Chronic Bronchitis. It's essential to be aware of these potential health risks and take proactive steps towards a healthier lifestyle.")
            if region == 0:
                st.write("* Given your residence in the Northeast region, where temperatures can drop significantly below freezing, it's important to note that living in this region may increase the risk of Respiratory issues, such as Pneumonia and Bronchitis. Please see the suggested medical aid packages below.")
            if region ==  2:
                st.write("* Living in the Southeast region, where hot and humid summers are common, may increase the risk of Heatstroke, Dehydration, and other heat-related health issues. Please see the suggested medical aid packages below.")
            
            st.subheader('Recommended Medical Aid Packages')
            if predicted_costs < 5001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Health Save package, which covers general ward public hospitalization, government/St John's ambulance, and acute drugs, with an annual global limit of $5000")
                st.image('images/securehealthsave.png')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 5000 and predicted_costs < 12001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Primary package which covers public hospitalization, private hospitalization, ambulance services, acute and chronic drugs, optical, dental, and pathology benefits, with an annual global limit of $12000")
                st.image('images/secureprimary.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 12000 and predicted_costs < 20001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Essential package, which covers public hospitalization up to Group B ward, road ambulance services, acute and chronic medications, optical, dental, radiology, and pathology services, with an annual global limit of $20000.")
                st.image('images/secureessential.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 20000 and predicted_costs < 30001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Private package, which covers private hospitalization up to Group A ward, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $30000.")
                st.image('images/secureprivate.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 30000 and predicted_costs < 45001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Premium package, which covers private hospitalization, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $70000.")
                st.image('images/securepremium.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 45000 and predicted_costs < 60001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Prime package, which offers an annual global limit of $100000 and covers private hospitalization, ambulance services, air evacuation, acute and chronic drugs, optical, dental, radiology, pathology, and family planning.")
                st.image('images/secureprime.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
    
#UI FOR MEDICAL AID POLICY HOLDERS
if options == 'Policy Holder':
    with st.expander('Click Here To Enter Details And Start Prediction'):
        sex = st.selectbox('Choose Gender', ['Female','Male'])
        age = st.slider('Enter Age', 5, 80)
        height = st.slider('Enter Height (In Metres)', 0.5, 2.6)
        weight = st.slider('Enter Weight (In Kgs)', 1, 150)
        children = st.slider('Enter Number of Children', 0, 5)
        smoker = st.selectbox('Are you a Smoker?', ['Yes', 'No'])
        region = st.selectbox('Choose Region', ['northeast','northwest','southeast','southwest'])
        bmi = round(weight/(height*height))

        if sex == 'Female':
            sex = 0
        else:
            sex = 1
        if smoker == 'Yes':
            smoker = 1
        else:
            smoker = 0
        if region == 'northeast':
            region = 0
        if region == 'northwest':
            region = 1
        if region == 'southeast':
            region = 2
        if region == 'southwest':
            region = 3

        input_data = (age, sex, bmi, children, smoker, region)
        input_data = np.asarray(input_data)
        input_data = input_data.reshape(1,-1)

        if st.button('Predict'):
            st.subheader('Predicted Costs')
            predicted_costs= regressor.predict(input_data)
            display_string = '* The predicted Healthcare Costs will be: '+str(round(predicted_costs[0],2)) + ' US Dollars'
            st.markdown(display_string)

#RECOMMENTATIONS 2
            if smoker == 1 or region == 0 or region == 2:
                st.subheader('Potential Health Threats')         
            if smoker == 1:
                st.write("* Given your smoking status, it's important to note that smoking may increase the risk of Lung Cancer, Heart Disease, and Chronic Bronchitis. It's essential to be aware of these potential health risks and take proactive steps towards a healthier lifestyle.")
            if region == 0:
                st.write("* Given your residence in the Northeast region, where temperatures can drop significantly below freezing, it's important to note that living in this region may increase the risk of Respiratory issues, such as Pneumonia and Bronchitis. Please see the suggested medical aid packages below.")
            if region ==  2:
                st.write("* Living in the Southeast region, where hot and humid summers are common, may increase the risk of Heatstroke, Dehydration, and other heat-related health issues. Please see the suggested medical aid packages below.")
            
            st.subheader('Recommended Medical Aid Packages')
            if predicted_costs < 5001:
                st.write("* The recommended medical aid package is the CIMAS Secure Health Save package, which covers general ward public hospitalization, government/St John's ambulance, and acute drugs, with an annual global limit of $5000")
                st.image('images/securehealthsave.png')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 5000 and predicted_costs < 12001:
                st.write("* The recommended medical aid package is the CIMAS Secure Primary package which covers public hospitalization, private hospitalization, ambulance services, acute and chronic drugs, optical, dental, and pathology benefits, with an annual global limit of $12000")
                st.image('images/secureprimary.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 12000 and predicted_costs < 20001:
                st.write("* The recommended medical aid package is the CIMAS Secure Essential package, which covers public hospitalization up to Group B ward, road ambulance services, acute and chronic medications, optical, dental, radiology, and pathology services, with an annual global limit of $20000.")
                st.image('images/secureessential.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 20000 and predicted_costs < 30001:
                st.write("* The recommended medical aid package is the CIMAS Secure Private package, which covers private hospitalization up to Group A ward, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $30000.")
                st.image('images/secureprivate.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 30000 and predicted_costs < 45001:
                st.write("* The recommended medical aid package is the CIMAS Secure Premium package, which covers private hospitalization, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $70000.")
                st.image('images/securepremium.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 45000 and predicted_costs < 60001:
                st.write("* The recommended medical aid package is the CIMAS Secure Prime package, which offers an annual global limit of $100000 and covers private hospitalization, ambulance services, air evacuation, acute and chronic drugs, optical, dental, radiology, pathology, and family planning.")
                st.image('images/secureprime.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
    
#UI FOR HEALTHCARE PROVIDERS
if options == 'Healthcare Provider':
    with st.expander('Click Here To Enter Details And Start Prediction'):
        sex = st.selectbox('Choose Gender', ['Female','Male'])
        age = st.slider('Enter Age', 5, 80)
        bmi = st.slider('Enter BMI', 5, 100)
        children = st.slider('Enter Number of Children', 0, 5)
        smoker = st.selectbox('Are you a Smoker?', ['Yes', 'No'])
        region = st.selectbox('Choose Region', ['northeast','northwest','southeast','southwest'])
        if sex == 'Female':
            sex = 0
        else:
            sex = 1
        if smoker == 'Yes':
            smoker = 1
        else:
            smoker = 0
        if region == 'northeast':
            region = 0
        if region == 'northwest':
            region = 1
        if region == 'southeast':
            region = 2
        if region == 'southwest':
            region = 3

        input_data = (age, sex, bmi, children, smoker, region)
        input_data = np.asarray(input_data)
        input_data = input_data.reshape(1,-1)

        if st.button('Predict'):
            st.subheader('Predicted Costs')
            predicted_costs= regressor.predict(input_data)
            display_string = '* The predicted Healthcare Costs will be: '+str(round(predicted_costs[0],2)) + ' US Dollars'
            st.markdown(display_string)

#RECOMMENTATIONS 3         
            if predicted_costs < 15001:
                st.write("* The predicted healthcare costs for this individual are relatively low. It is suggested to allocate resources efficiently to provide necessary care and support, optimizing value and health outcomes.") 
            if predicted_costs > 15000 and predicted_costs < 35001:
                st.write("* The predicted healthcare costs for this individual are moderate. It is recommended to allocate resources accordingly to ensure suitable care and support, balancing financial responsibility with individual needs.")
            if predicted_costs > 35000:
                st.write("* The predicted healthcare costs for this individual are substantially high. It is suggested that the individual be prioritized for resource allocation to ensure adequate care and support, given the significant financial burden.")
            
            if smoker == 1 or region == 0 or region == 2:
                st.subheader('Potential Health Threats')
            if smoker == 1:
                st.write("* Given smoking status, it's important to note that smoking may increase the risk of Lung Cancer, Heart Disease, and Chronic Bronchitis. It's essential to be aware of these potential health risks and take proactive steps towards a healthier lifestyle.")
            if region == 0:
                st.write("* Given your residence in the Northeast region, where temperatures can drop significantly below freezing, it's important to note that living in this region may increase the risk of Respiratory issues, such as Pneumonia and Bronchitis. Please see the suggested medical aid packages below.")
            if region ==  2:
                st.write("* Living in the Southeast region, where hot and humid summers are common, may increase the risk of Heatstroke, Dehydration, and other heat-related health issues. Please see the suggested medical aid packages below.")
            
            st.subheader('Recommended Medical Aid Packages')
            if predicted_costs < 5001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Health Save package, which covers general ward public hospitalization, government/St John's ambulance, and acute drugs, with an annual global limit of $5000")
                st.image('images/securehealthsave.png')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 5000 and predicted_costs < 12001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Primary package which covers public hospitalization, private hospitalization, ambulance services, acute and chronic drugs, optical, dental, and pathology benefits, with an annual global limit of $12000")
                st.image('images/secureprimary.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 12000 and predicted_costs < 20001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Essential package, which covers public hospitalization up to Group B ward, road ambulance services, acute and chronic medications, optical, dental, radiology, and pathology services, with an annual global limit of $20000.")
                st.image('images/secureessential.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 20000 and predicted_costs < 30001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Private package, which covers private hospitalization up to Group A ward, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $30000.")
                st.image('images/secureprivate.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 30000 and predicted_costs < 45001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Premium package, which covers private hospitalization, air evacuation, acute and chronic drugs, optical, dental, radiology, and pathology, with an annual global limit of $70000.")
                st.image('images/securepremium.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
            if predicted_costs > 45000 and predicted_costs < 60001:
                st.write("* The recommended medical aid package for this individual is the CIMAS Secure Prime package, which offers an annual global limit of $100000 and covers private hospitalization, ambulance services, air evacuation, acute and chronic drugs, optical, dental, radiology, pathology, and family planning.")
                st.image('images/secureprime.jpg')
                st.write("* For more information about this and other packages visit: https://cimas.co.zw/secure-packages/")
    
#CHATBOT WITH LLAMA 2
           
with st.expander('Click Here To Chat And Get Further Recommendations'):
    
    replicate_api = st.secrets['REPLICATE_API_TOKEN']
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

    llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'

    temperature = 0.5
    top_p = 0.75
    max_length = 30    

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

#CLEAR CHAT MESSAGES
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.button('Clear Chat History', on_click=clear_chat_history)

#FUNCTION FOR GENERATING LLAMA RESPONSE
    def generate_llama2_response(prompt_input):
        string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
        for dict_message in st.session_state.messages:
            if dict_message["role"] == "user":
                string_dialogue += "User: " + dict_message["content"] + "\n\n"
            else:
                string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
        output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                               input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                      "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
        return output
    
#USER PROVIDED PROMPT
    if prompt := st.chat_input(disabled=not replicate_api):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

#GENERATING RESPONSE IF LAST RESPONSE IS NOT FROM LLAMA
    if st.session_state.messages[-1]["role"] != "assistant":
         with st.chat_message("assistant"):
             with st.spinner("Thinking..."):
                 response = generate_llama2_response(prompt)
                 placeholder = st.empty()
                 full_response = ''
                 for item in response:
                     full_response += item
                     placeholder.markdown(full_response)
                 placeholder.markdown(full_response)
         message = {"role": "assistant", "content": full_response}
         st.session_state.messages.append(message)

