import streamlit as st
from sheet import *
import pandas as pd

st.set_page_config(
    page_title="TKI 갈등관리유형 검사지",
    page_icon="📃"
)


st.title('TKI 갈등관리유형 검사지')
st.caption('written by Jung Su-In')
st.divider()
def update_state() :
    st.session_state['check_direction'] = True


def calcurate(question, number):
    q_num = f'Q{number}'
    a_num = f'A{number}'
    if question == question_sheet[q_num][0]:
        answer[answer_sheet[a_num][0]] += 1
    elif question == question_sheet[q_num][1]:
        answer[answer_sheet[a_num][1]] += 1


if 'check' not in st.session_state :
    st.session_state['check'] = False

if 'start' not in st.session_state :
    st.session_state['start'] = True

def start_test() :
    st.session_state['check'] = True
    st.session_state['start'] = False

with st.container(border = True) :
    st.write('- 이 검사는 당신의 일반적인 갈등관리 유형을 탐색하기 위한 검사입니다.')
    st.write("- 이 검사의 문항에는 '맞는 답'과 '틀린 답'이 없습니다.")
    st.write("- 각 문장을 읽은 후 자신이 이상적으로 생각하는 것을 선택하지 마시고, 자신의 행동을 더 잘 나타내는 문장을 선택하시기 바랍니다.")
    st.write("- 어떤 문항은 다른 문항과 비슷할 수 있습니다. 다른 문항들과 비교하여 의식적으로 일관성 있게 응답하려 하지 마시고, 해당 문항만을 편안한 기분으로 자연스럽게 응답하시면 됩니다.")
    st.write("- 시간제한은 없으나 특정 문항에 오래 머무르지 마시고, 신속하고 솔직하게 응답하시기 바랍니다.")
    start = st.checkbox('검사를 시작하시겠습니까?')

if start :
    start_test()

if st.session_state['check'] :
    st.write('') # 공백
    st.write('') # 공백

    st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 1rem;
    }
    </style>
    """,unsafe_allow_html=True)
    Q01 = st.radio('**Q01**', question_sheet['Q01'], index = None, captions = ['  ', '  '])
    st.divider()

    Q02 = st.radio('**Q02**', question_sheet['Q02'], index = None, captions = ['  ', '  '])
    st.divider()

    Q03 = st.radio('**Q03**', question_sheet['Q03'], index = None, captions = ['  ', '  '])
    st.divider()

    Q04 = st.radio('**Q04**', question_sheet['Q04'], index = None, captions = ['  ', '  '])
    st.divider()

    Q05 = st.radio('**Q05**', question_sheet['Q05'], index = None, captions = ['  ', '  '])
    st.divider()

    Q06 = st.radio('**Q06**', question_sheet['Q06'], index = None, captions = ['  ', '  '])
    st.divider()

    Q07 = st.radio('**Q07**', question_sheet['Q07'], index = None, captions = ['  ', '  '])
    st.divider()

    Q08 = st.radio('**Q08**', question_sheet['Q08'], index = None, captions = ['  ', '  '])
    st.divider()

    Q09 = st.radio('**Q09**', question_sheet['Q09'], index = None, captions = ['  ', '  '])
    st.divider()

    Q10 = st.radio('**Q10**', question_sheet['Q10'], index = None, captions = ['  ', '  '])
    st.divider()

    Q11 = st.radio('**Q11**', question_sheet['Q11'], index = None, captions = ['  ', '  '])
    st.divider()

    Q12 = st.radio('**Q12**', question_sheet['Q12'], index = None, captions = ['  ', '  '])
    st.divider()

    Q13 = st.radio('**Q13**', question_sheet['Q13'], index = None, captions = ['  ', '  '])
    st.divider()

    Q14 = st.radio('**Q14**', question_sheet['Q14'], index = None, captions = ['  ', '  '])
    st.divider()

    Q15 = st.radio('**Q15**', question_sheet['Q15'], index = None, captions = ['  ', '  '])
    st.divider()

    Q16 = st.radio('**Q16**', question_sheet['Q16'], index = None, captions = ['  ', '  '])
    st.divider()

    Q17 = st.radio('**Q17**', question_sheet['Q17'], index = None, captions = ['  ', '  '])
    st.divider()

    Q18 = st.radio('**Q18**', question_sheet['Q18'], index = None, captions = ['  ', '  '])
    st.divider()

    Q19 = st.radio('**Q19**', question_sheet['Q19'], index = None, captions = ['  ', '  '])
    st.divider()

    Q20 = st.radio('**Q20**', question_sheet['Q20'], index = None, captions = ['  ', '  '])
    st.divider()

    Q21 = st.radio('**Q21**', question_sheet['Q21'], index=None, captions = ['  ', '  '])
    st.divider()

    Q22 = st.radio('**Q22**', question_sheet['Q22'], index=None, captions = ['  ', '  '])
    st.divider()

    Q23 = st.radio('**Q23**', question_sheet['Q23'], index=None, captions = ['  ', '  '])
    st.divider()

    Q24 = st.radio('**Q24**', question_sheet['Q24'], index=None, captions = ['  ', '  '])
    st.divider()

    Q25 = st.radio('**Q25**', question_sheet['Q25'], index=None, captions = ['  ', '  '])
    st.divider()

    Q26 = st.radio('**Q26**', question_sheet['Q26'], index=None, captions = ['  ', '  '])
    st.divider()

    Q27 = st.radio('**Q27**', question_sheet['Q27'], index=None, captions = ['  ', '  '])
    st.divider()

    Q28 = st.radio('**Q28**', question_sheet['Q28'], index=None, captions = ['  ', '  '])
    st.divider()

    Q29 = st.radio('**Q29**', question_sheet['Q29'], index=None, captions = ['  ', '  '])
    st.divider()

    Q30 = st.radio('**Q30**', question_sheet['Q30'], index=None, captions = ['  ', '  '])
    st.divider()


    Questions = [Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09, Q10,
                Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20,
                Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30]

    tmp = []
    for i, q in enumerate(Questions) :
        if q is None :
            tmp.append(str(i+1))

    submit = st.button('답변 완료📃')

    if submit and len(tmp) > 0 :
        st.error('❌️ 아직 응답하지 않은 문항이 있어요.')
        st.info(f"✅️ {', '.join(tmp)}번 문항에 응답해주신 후에 답변 완료를 눌러주세요.")

    if submit and len(tmp) == 0 :
        answer = {
            '_type01': 0,
            '_type02': 0,
            '_type03': 0,
            '_type04': 0,
            '_type05': 0
        }

        calcurate(Q01, "01")
        calcurate(Q02, "02")
        calcurate(Q03, "03")
        calcurate(Q04, "04")
        calcurate(Q05, "05")
        calcurate(Q06, "06")
        calcurate(Q07, "07")
        calcurate(Q08, "08")
        calcurate(Q09, "09")
        calcurate(Q10, "10")
        calcurate(Q11, "11")
        calcurate(Q12, "12")
        calcurate(Q13, "13")
        calcurate(Q14, "14")
        calcurate(Q15, "15")
        calcurate(Q16, "16")
        calcurate(Q17, "17")
        calcurate(Q18, "18")
        calcurate(Q19, "19")
        calcurate(Q20, "20")
        calcurate(Q21, "21")
        calcurate(Q22, "22")
        calcurate(Q23, "23")
        calcurate(Q24, "24")
        calcurate(Q25, "25")
        calcurate(Q26, "26")
        calcurate(Q27, "27")
        calcurate(Q28, "28")
        calcurate(Q29, "29")
        calcurate(Q30, "30")



        answer = pd.DataFrame(pd.Series(answer))
        answer.index = ["경쟁", "협력", "타협", "회피", "수용"]
        answer.index.name = "유형"
        answer.columns = ["점수"]
        answer = answer.T

        th_props = [
            ('font-size', '15px'),
            ('text-align', 'center'),
            ('font-weight', 'bold'),
            ('color', '#6d6d6d'),
            ('background-color', '#f7ffff')
        ]

        td_props = [
            ('font-size', '15px'),
            ('text-align', 'center')
        ]

        styles = [
            dict(selector="th", props=th_props),
            dict(selector="td", props=td_props)
        ]

        styled = answer.style.set_properties(**{'font-size': '20px',
                                                'text-align' : 'center'}).set_table_styles(styles)
        st.markdown("<h3 style='text-align: center; color: black;'>< TKI 검사 결과 ></h3>", unsafe_allow_html=True)
        st.table(styled)
        st.write("응답하시느라 고생 많으셨어요.")
        st.write("이제 프로파일지에 점수를 체크해주세요!😁")
