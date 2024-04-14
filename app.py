import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from src.pipelines.prediction_pipeline import Prediction
from src.components.model_trainning import ModelTrainning
from src.utils import load_obj


# 'state', 'area_code', 'international_plan', 'voice_mail_plan',
#        'number_vmail_messages', 'total_day_minutes', 'total_day_calls',
#        'total_day_charge', 'total_eve_charge', 'total_night_charge',
#        'total_intl_minutes', 'total_intl_calls', 'total_intl_charge',
#        'number_customer_service_calls'

# state                                       NH
# area_code                        area_code_415
# international_plan                          no
# voice_mail_plan                             no
# number_vmail_messages                        0
# total_day_minutes                        254.3
# total_day_calls                            113
# total_day_charge                         43.23
# total_eve_charge                          6.71
# total_night_charge                        6.89
# total_intl_minutes                        11.8
# total_intl_calls                             2
# total_intl_charge                         3.19
# number_customer_service_calls                2

def load_lottie_url(url):

    r = requests.get(url)
    
    if r.status_code != 200:
        return None
    else:
        return r.json()

def main():

    st.set_page_config(page_title='Cust_churn_web_app', layout='wide')

    lottie_file = load_lottie_url('https://lottie.host/598e9e70-6768-410d-b309-b8e8c6be56a2/N9wcpBAsqi.json')

    menu = ['About', 'App']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'About':

        with st.container():

            st.write('To run the application, select app from Menu dropdown from navigation bar present on left side')

        with st.container():
            st.write('---')
            left_col, right_col = st.columns(2)

            with left_col:
                
                st.header('Problem Statment')
                st.write('##')
                st.write(
                    """
                            The problem at hand revolves around predicting customer churn, a crucial task in various industries, particularly in subscription-based services such as telecommunications, banking, and SaaS companies. Customer churn refers to the phenomenon where customers discontinue their services or subscriptions with a company. Identifying potential churners beforehand allows businesses to take proactive measures such as targeted marketing campaigns or personalized retention strategies to mitigate churn and retain valuable customers.
                    """
                )
            
            with right_col:
                st_lottie(lottie_file, height=300, key='customer_retention')

        with st.container():

            git_hub_url = 'https://github.com/soil15/Customer_churn'
            model_tran = ModelTrainning()
            class_repo = load_obj(model_tran.model_trainning_cofg_obj.class_repo_path)

            st.write('---')
            st.header('Key Steps in Solving the Problem:')
            st.markdown("[Github Repository](%s)" % git_hub_url)
            st.write('##')

            # ---------------------------------------
            st.subheader('1. Data Ingestion')
            st.write('I began by ingesting the raw data using a robust data ingestion pipeline, ensuring that data from various sources is seamlessly integrated for further processing.')

            # ---------------------------------------
            st.subheader('2. Data Transformation')
            st.write('Next, I focused on transforming the raw data into a format suitable for model training. This involved preprocessing steps such as handling missing values, encoding categorical variables, and splitting the data into training and testing sets.')

            # ---------------------------------------
            st.subheader('3. Model Training')
            st.write('Leveraging the XGBoost classifier and the optimized hyperparameters obtained through tuning, I trained a predictive model on the preprocessed data. This model is finely tuned to prioritize recall, ensuring that it effectively identifies potential churners, which is crucial for implementing targeted retention strategies.')

            # ---------------------------------------
            st.subheader('4. Hyperparameter Tuning for Recall Optimization')
            st.write('To further enhance model performance, I employed advanced techniques such as hyperparameter tuning with a primary focus on maximizing the recall score. By defining a custom scoring function that prioritizes precision, and conducting grid search cross-validation over a range of hyperparameters, I fine-tuned the XGBoost classifier to effectively identify potential churners while maintaining reasonable precision.')
            
            # ---------------------------------------
            st.subheader('5. Evaluation and Model Deployment')
            st.write(' After training the model, I thoroughly evaluated its performance using metrics such as confusion matrix, classification report.')
            st.write(class_repo)



    elif choice == 'App':

        with st.form(key='input_form'):
            
            state = st.selectbox('state', ['OH', 'NJ', 'OK', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI', 'IA', 'MT',
        'NY', 'ID', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC', 'WY', 'HI', 'NH',
        'AK', 'GA', 'MD', 'AR', 'WI', 'OR', 'MI', 'DE', 'UT', 'CA', 'SD',
        'NC', 'WA', 'MN', 'NM', 'NV', 'DC', 'VT', 'KY', 'ME', 'MS', 'AL',
        'NE', 'KS', 'TN', 'IL', 'PA', 'CT', 'ND'])

            area_code = st.selectbox('Area Code', ['area_code_415', 'area_code_408', 'area_code_510'])

            inter_plan = st.selectbox('International Plan', ['no', 'yes'])
            voice_mail_plan = st.selectbox('Voice Mail Plan', ['no', 'yes'])
            num_vmail_msg = st.number_input('Number of Voice mail messages', min_value=0, value=26)
            total_day_min = st.number_input('Total Daily Minutes', min_value=0.0, value=161.6)
            total_day_calls = st.number_input('Total Daily Calls', min_value=0, value=123)
            total_day_charge = st.number_input('Total Day charge', min_value=0.0, value=27.47)
            total_eve_charge = st.number_input('Total Evening charge', min_value=0.0, value=16.62)
            total_night_charge = st.number_input('Total night charge', min_value=0.0, value=11.45)
            total_int_min = st.number_input('Total International Minutes', min_value=0.0, value=13.7)
            total_int_calls = st.number_input('Total International calls', min_value=0, value=3)
            total_int_charge = st.number_input('Total Intternational Charge', min_value=0.0, value=3.7)
            number_cust_srv_calls = st.number_input('Number of Customer Service Calls', min_value=0, value=1)

            submit_button = st.form_submit_button()

            
            if submit_button:

                pred_obj = Prediction(state, area_code, inter_plan, voice_mail_plan, num_vmail_msg, total_day_min, total_day_calls, total_day_charge,
                            total_eve_charge, total_night_charge, total_int_min, total_int_calls, total_int_charge,
                            number_cust_srv_calls)

                data_df = pred_obj.get_data()

                transformed_df, pred, _ = pred_obj.get_predictions()

                if pred == 1:
                    st.success('Customer will churn')
                elif pred == 0:
                    st.success('Customer will not churn')



if __name__ == '__main__':

    main()