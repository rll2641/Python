# 중복 데이터 처리하기
import pandas as pd

billboard = pd.read_csv('../CSV/data/billboard.csv')
billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
# 노래 제목이 Loser인 데이터만 따로 모아 살펴보면 중복이 많다
print(billboard_long[billboard_long['track'] == 'Loser'].head())
# 중복 데이터를 가지고 있는 열은 year, artist, track, time, date
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
# 중복 제거 전
print(billboard_songs.shape)
billboard_songs = billboard_songs.drop_duplicates()
# 중복 제거 후
print(billboard_songs.shape)
# 중복을 제거한 데이터프레임에 아이디 열 추가
billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head())

# merge 메서드를 사용해 노래 정보와 주간 순위 데이터 합치기
billboard_rating = billboard_long.merge(billboard_songs, on=['year', 'artist', 'track', 'time'])
print(billboard_rating.head())