import streamlit as st 
from src.pipelines.prediction_pipeline import Prediction


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

def main():

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

            transformed_df, pred = pred_obj.get_predictions()

            st.write(data_df)
            st.write(transformed_df)
            st.write(pred)




if __name__ == '__main__':

    main()