import streamlit as st
import pyodbc
import sys

def start_connection():
    # Australian Server Connection
    server = 'localhost'
    database = 'pwg'
    username = 'SA'
    password = '9805300287'

    # Establish a connection to the MS SQL Server
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes')
    cursor = conn.cursor()
    return conn, cursor
currentstate,nullcheck=[],0
for i in range(0,6):
    currentstate.append("")

if nullcheck!=0:
    qtext, answer1, answer2, answer3, answer4, soln=currentstate[0],currentstate[1],currentstate[2],currentstate[3],currentstate[4],currentstate[5]


def check_any_changes_made(rec, qtext, answer1, answer2, answer3, answer4, soln):
    w_change_found = ""
    if qtext != rec['questiontext']:                
        st.markdown(f"**Current Question Text:** {rec['questiontext']} <br/> **New Question Text :** {qtext}",  unsafe_allow_html=True)
        w_change_found = "X"
    if answer1 != rec['answer1']:                
        st.markdown(f"**Current answer1:** {rec['answer1']} <br/> **New answer1:** {answer1}",  unsafe_allow_html=True)
        w_change_found = "X"
    if answer2 != rec['answer2']:
        st.markdown(f"**Current answer2:** {rec['answer2']} <br/> **New answer2:** {answer2}",  unsafe_allow_html=True)
        w_change_found = "X"
    if answer3 != rec['answer3']:
        st.markdown(f"**Current answer3:** {rec['answer3']} <br/> **New answer3:** {answer3}",  unsafe_allow_html=True)
        w_change_found = "X"
    if answer4 != rec['answer4']:
        st.markdown(f"**Current answer4:** {rec['answer4']} <br/> **New answer4:** {answer4}",  unsafe_allow_html=True)
        w_change_found = "X"
    if soln != rec['correctfeedback']:
        st.markdown(f"**Current Solution Long:** {rec['correctfeedback']} <br/> **New Solution Long:** {soln}",  unsafe_allow_html=True)
        w_change_found = "X"

    return w_change_found

def update_changes(w_connection, moodle_id, qtext, answer1, answer2, answer3, answer4, soln):
    conn = w_connection[0]
    cursor = w_connection[1]
                 
    try:
        
        cursor.execute(f"UPDATE SOURCE_QUESTIONS_STAGING SET questiontext = ?, answer1 = ?, answer2 = ?, answer3 = ?, answer4 = ?, correctfeedback = ?  WHERE moodle_qno = ?", (qtext, answer1, answer2, answer3, answer4, soln, moodle_id))
        conn.commit()
        # cursor.execute(f"UPDATE SOURCE_QUESTION SET questiontext = ?, answer1 = ?, answer2 = ?, answer3 = ?, answer4 = ?, correctfeedback = ?, correctfeedback = ?  WHERE moodle_id = ?", (qtext, answer1, answer2, answer3, answer4, soln, soln, moodle_id))
        # conn.commit()
        
        st.success('Saved changes')
    except pyodbc.Error as e:
        st.error(f"An error occurred updating table MOODLE_QUESTIONS : {e}")
    
    

# Ask the user for the Moodle question number
st.header('Update Questions in MOODLE_QUESTIONS and SOURCE_QUESTION Tables')
moodle_qno = st.text_input('Enter the Moodle question number')

if moodle_qno:
    # Query the database for the question
    # if moodle_qno[0].upper() not in ['B', 'P', 'C']: # Not a valid question type
    #     st.error('Invalid Moodle Question number. It should start with B, P or C')
    #     sys.exit(1)
    # else:
    moodle_id_like = "IN" + moodle_qno[0].upper() + "%"
    # if moodle_qno[1:].isdigit() == False: # Not a valid question number
    #     st.error('Invalid Moodle Question number. The number part should be numeric')
    #     sys.exit(1)
    # else:
    cache_invalidated = False

    def refresh_cache():
        global cache_invalidated
        cache_invalidated = True
    moodle_qno = int(moodle_qno[0:])
    rows = []
    w_connection = start_connection()
    conn = w_connection[0]
    cursor = w_connection[1]
    cursor.execute(f"SELECT * FROM SOURCE_QUESTIONS_STAGING WHERE moodle_qno = {moodle_qno}")
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
            rows.append(dict(zip(columns, row)))
    if len(rows) == 1:
        rec = rows[0]
    elif len(rows) > 1:
        st.error('Multiple questions found with that number')
        sys.exit(1)
    else:
        st.error('No question found with that number')
        sys.exit(1)

    if rec:
        moodle_id = rec['moodle_qno']
        # Display the fields and allow the user to edit them
        if len(rec['questiontext']) > 100:
            qtext = st.text_area('Question Text', rec['questiontext'], height=200)
            currentstate[0]=rec['questiontext']
            if 'qtext' not in st.session_state:
               st.session_state['qtext'] = rec['questiontext']
        else:
            qtext = st.text_input('Question Text', rec['questiontext'])
            currentstate[0]=rec['questiontext']
            if 'qtext' not in st.session_state:
               st.session_state['qtext'] = rec['questiontext']
            nullcheck=1
        if len(rec['answer1']) > 100:
            answer1 = st.text_area('answer 1', rec['answer1'])
            currentstate[1]=rec['answer1']
        else:            
            answer1 = st.text_input('answer 1', rec['answer1'])
            currentstate[1]=rec['answer1']
        if len(rec['answer2']) > 100:
            answer2 = st.text_area('answer 2', rec['answer2'])
            currentstate[2]=rec['answer2']
        else:
            answer2 = st.text_input('answer 2', rec['answer2'])
            currentstate[2]=rec['answer2']
        if len(rec['answer3']) > 100:
            answer3 = st.text_area('answer 3', rec['answer3'])
            currentstate[3]=rec['answer3']
        else:
            answer3 = st.text_input('answer 3', rec['answer3'])
            currentstate[3]=rec['answer3']
        if len(rec['answer4']) > 100:
            answer4 = st.text_area('answer 4', rec['answer4'])
            currentstate[4]=rec['answer4']
        else:
            answer4 = st.text_input('answer 4', rec['answer4'])
            currentstate[4]=rec['answer4']
        if len(rec['correctfeedback']) > 100:            
            soln = st.text_area('Solution Long', rec['correctfeedback'], height=200)
            currentstate[5]=rec['correctfeedback']
        else:
            soln = st.text_input('Solution Long', rec['correctfeedback'])  
            currentstate[5]=rec['correctfeedback'] 

        w_change_found = check_any_changes_made(rec, qtext, answer1, answer2, answer3, answer4, soln)
        # Save or cancel buttons
        if st.button('Save'):
            # Update the database          
            
            if w_change_found == "X":
                update_changes(w_connection, moodle_id, qtext, answer1, answer2, answer3, answer4, soln)
                
            else:
                st.info('No changes found')
        if st.button('Cancel'):
            st.info('Cancelled')
            st.switch_page("pages/page1.py")
         # # Reset all the values to original values. But this is not happening

           

    else:
        st.error('No question found with that number')

    conn.close()