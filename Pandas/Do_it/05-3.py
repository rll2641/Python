import pandas as pd

# merge 메서드로 연결
person = pd.read_csv('../CSV/data/survey_person.csv')
site = pd.read_csv('../CSV/data/survey_site.csv')
survey = pd.read_csv('../CSV/data/survey_survey.csv')
visited = pd.read_csv('../CSV/data/survey_visited.csv')

visited_subset = visited.loc[[0, 2, 6], ]
print(visited_subset)
'''
merge 메서드는 기본적으로 내부 조인을 실행하며, 메서드를 사용한 데이터프레임을 왼쪽으로
지정하고 첫 번째 인잣값으로 지정한 데이터프레임을 오른쪽으로 지정한다.
left_on, right_on 인자는 값이 일치해야 할 왼쪽과 오른쪽 데이터프레임의 열을 지정한다.
즉, 왼쪽 df의 열과 오른쪽 df의 열 값이 일치하면 왼쪽 df를 기준으로 연결한다.
'''

o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(o2o_merge)

# left_on, right_on에 전달하는 값은 여러 개여도 상관없다.
ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')

ps_vs = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'],
                 right_on=['person', 'ident', 'quant', 'reading'])
# 위 실행시 중복되는 열 이름에는 접미사인 _x, _y가 붙음 -> ident_x taken_x ident_y