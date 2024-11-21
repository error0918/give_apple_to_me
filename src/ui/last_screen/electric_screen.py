import tkinter
import platform
from dataclasses import dataclass
from enum import Enum
from ui import widget
from util import screen, theme


@dataclass(frozen=True)
class Depot:
    name: str
    location: str
    location_type: str


class DepotType(Enum):
    APPLIANCE = "폐가전"
    PHONE = "폐휴대폰"


# 중소 폐가전
discarded_appliances = [
    Depot(name="신흥동 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="오정동 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="고강1동 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="원종2종 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="원종1종 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="심곡3동 행정복지센터", location="경기 부천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="sk하이닉스 사원아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="경남 아너스빌", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="권곡 서해그랑블 1단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="권곡 서해그랑블 2단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="권곡주공아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="권곡청솔아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="대주아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="동아나래 2차", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="동일하이빌", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="득산 부영아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종 삼일파라뷰 2차", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종 삼일파라뷰 더스위트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종 캐슬어울림 1단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종 캐슬어울림 2단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종 한성필하우스 1단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="모종주공아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="반도유보라", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="방축 KD 아람채", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="벽산아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="삼부 르네상스", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="삼정백조", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="삼정하이츠", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="삼환나우빌", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="송도힐스테이트레이크", location="인천광역시 연수구", location_type="공동주택(아파트 등)"),
    Depot(name="시지대성유니드", location="대구광역시 수성구", location_type="공동주택(아파트 등)"),
    Depot(name="신원더파크 2단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="실옥 푸르지오", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="아산 온천 미소지움", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="아산 올리브힐", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="온양 힐스테이트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="온천마을 아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="용화 아이파크", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="우림필유아파트", location="경상북도 구미시", location_type="공동주택(아파트 등)"),
    Depot(name="일성아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="좌부동 초원아파트 2단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="좌부동 초원아파트 3단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="주택관리공단 본사", location="경상남도 진주시", location_type="공동주택(아파트 등)"),
    Depot(name="창덕 에버빌", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="표교2리 마을회관 분리수거장", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="풍기 이지더원 2단지", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="한미아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="한성아파트", location="충청남도 아산시", location_type="공동주택(아파트 등)"),
    Depot(name="효양아파트(어린이집 옆 폐기물처리장)", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="대전반석4", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="대전센트럴자이1단지아파트", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="대전중촌2", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="대주파크빌아파트", location="대전광역시 동구", location_type="공동주택(아파트 등)"),
    Depot(name="대청동행정복지센터", location="대전광역시 동구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="대평그린빌", location="경상북도 경산시", location_type="공동주택(아파트 등)"),
    Depot(name="대호1차아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="대호2차아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="대화동행정복지센터", location="대전광역시 대덕구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="대흥1리 마을회관", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="대흥2리 마을회관", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="대흥동 행정복지센터", location="대전광역시 중구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="대흥동 현대1차아파트", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="대흥동 현대2차아파트", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="더리브스위트엠", location="경상북도 영주시", location_type="공동주택(아파트 등)"),
    Depot(name="더샵송도프라임뷰20BL", location="인천광역시 연수구", location_type="공동주택(아파트 등)"),
    Depot(name="더샵판교퍼스트파크", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="덕곡주공아파트", location="경상북도 김천시", location_type="공동주택(아파트 등)"),
    Depot(name="덕암아파트", location="대전광역시 대덕구", location_type="공동주택(아파트 등)"),
    Depot(name="덕일타운아파트", location="경상북도 김천시", location_type="공동주택(아파트 등)"),
    Depot(name="덕촌1리 마을회관", location="경상북도 구미시", location_type="공동주택(아파트 등)"),
    Depot(name="덕평리(우미기) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="덕평리(원덕평) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도고면주민센터", location="충청남도 아산시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도기리 문화 생활관", location="충청북도 제천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도량4주공아파트", location="경상북도 구미시", location_type="공동주택(아파트 등)"),
    Depot(name="도안10단지 휴먼시아10단지", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="도안1단지 LH 도안마을1단지", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="도안LH행복2단지", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="도암2리 경로당", location="경상북도 의성군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도암2리 영농폐비닐집하장", location="경상북도 의성군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도전리 마을회관", location="충청북도 제천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="도촌섬마을4단지", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="독산역롯데캐슬아파트", location="서울특별시 금천구", location_type="공동주택(아파트 등)"),
    Depot(name="동곡동행정복지센터", location="광주광역시 광산구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="동락1리(개정) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="동락1리(원동락) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="동락2리(두만) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="동명면사무소", location="경상북도 칠곡군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="동산아파트", location="경상북도 경산시", location_type="공동주택(아파트 등)"),
    Depot(name="동양강변타운", location="경상북도 김천시", location_type="공동주택(아파트 등)"),
    Depot(name="동일스위트리버스카이", location="대전광역시 대덕구", location_type="공동주택(아파트 등)"),
    Depot(name="동현 일동아파트", location="충청북도 제천시", location_type="공동주택(아파트 등)"),
    Depot(name="두산그린맨션", location="경상북도 구미시", location_type="공동주택(아파트 등)"),
    Depot(name="두산아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="두정 한성필하우스2차 아파트", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="두정동 경남아너스빌 아파트", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="두정동 범양레우스알파 아파트", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="둔곡우미린", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="둔포면주민센터", location="충청남도 아산시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="뒷마경로당", location="경상북도 의성군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="득명리 마을회관", location="경상북도 칠곡군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="등촌11단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌4단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌6단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌7단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌9단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="라이프 타운", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="레자미멀티홈", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="로얄팰리스", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="로즈웰 모산힐아파트", location="충청북도 제천시", location_type="공동주택(아파트 등)"),
    Depot(name="롯데캐슬페라즈스카이", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="마산삼계2주공아파트", location="경상남도 창원시", location_type="공동주택(아파트 등)"),
    Depot(name="마산중리1아파트", location="경상남도 창원시", location_type="공동주택(아파트 등)"),
    Depot(name="마월1리(진계리) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="마을공동 마당", location="경상북도 의성군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="마장리젠시빌란트더웰아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="만덕3주공아파트", location="부산광역시 북구", location_type="공동주택(아파트 등)"),
    Depot(name="매화마을4단지", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="명도2리 마을회관", location="충청북도 제천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="모라3주공아파트", location="부산광역시 사상구", location_type="공동주택(아파트 등)"),
    Depot(name="모아엘가 아파트", location="경상북도 예천군", location_type="공동주택(아파트 등)"),
    Depot(name="모전현대아파트", location="경기도 이천시", location_type="공동주택(아파트 등)"),
    Depot(name="목동 행정복지센터", location="대전광역시 중구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="목동더샵리슈빌", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="무지개마을1단지대림", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="무지골 마을회관", location="충청북도 제천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="무학2리 챙기재활용마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문명1리(문산) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문명2리(일번지) 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문창동 행정복지센터", location="대전광역시 중구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문화1동 행정복지센터", location="대전광역시 중구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문화2동 행정복지센터", location="대전광역시 중구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="문화주공2단지", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="미당한마음아파트", location="충청북도 제천시", location_type="공동주택(아파트 등)"),
    Depot(name="미르마을아파트", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="밀양가곡1주공아파트", location="경상남도 밀양시", location_type="공동주택(아파트 등)"),
    Depot(name="밀양삼문휴먼시아아파트", location="경상남도 밀양시", location_type="공동주택(아파트 등)"),
    Depot(name="박달재 전통시장 상인회", location="충청북도 제천시", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="반석 더 샵", location="대전광역시 유성구", location_type="공동주택(아파트 등)"),
    Depot(name="배천마을회관", location="경상북도 김천시", location_type="공동주택(아파트 등)"),
    Depot(name="백석3차아이파크", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="백석더샵 아파트", location="충청남도 천안시", location_type="공동주택(아파트 등)"),
    Depot(name="백전1리 재활용동네마당", location="경상북도 성주군", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="백천월드메르디앙", location="경상북도 경산시", location_type="공동주택(아파트 등)"),
    Depot(name="백현마을3단지", location="경기도 성남시", location_type="공동주택(아파트 등)"),
    Depot(name="버드내2단지 동양아파트", location="대전광역시 중구", location_type="공동주택(아파트 등)"),
    Depot(name="번동3단지 아파트", location="서울특별시 강북구", location_type="공동주택(아파트 등)"),
    Depot(name="법2동행정복지센터", location="대전광역시 대덕구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="법동주공2단지아파트", location="대전광역시 대덕구", location_type="공동주택(아파트 등)"),
    Depot(name="롯데하이마트 의왕점", location="경기 의왕시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 의정부점", location="경기 의정부시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 이천점", location="경기 이천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 익산롯데마트점", location="전북 익산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 인동점", location="경북 구미시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 인천교점", location="인천 동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 인화점", location="전북 익산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 인후점", location="전북 전주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 일도점", location="제주 제주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 작전점", location="인천 계양구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 잠실점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 장량점", location="경북 포항시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 장림점", location="부산 사하구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 장유점", location="경남 김해시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 장한평점", location="서울 성동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 전주롯데마트점", location="전북 전주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정관점", location="부산 기장군", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정림점", location="대전 서구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정왕역점", location="경기 시흥시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정읍롯데마트점", location="전북 정읍시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정읍점", location="전북 정읍시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정자사거리점", location="경기 수원시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 정자점", location="경기 성남시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 제주롯데마트점", location="제주 제주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 제주점", location="제주 제주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 제천점", location="충북 제천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 조례점", location="전남 순천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 조치원점", location="세종 조치원읍", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 종암점", location="서울 성북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 안성롯데마트점", location="경기 안성시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 안성점", location="경기 안성시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 안양대교점", location="경기 안양시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 안양점", location="경기 안양시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 안중점", location="경기 평택시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 압구정점", location="서울 강남구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 양산점", location="경남 양산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 양주LF스퀘어점", location="경기 양주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 양평롯데마트점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 양평점", location="경기 양평군", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 언양점", location="울산 울주군", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 여수점", location="전남 여수시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 여주점", location="경기 여주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 여천롯데마트점", location="전남 여수시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 여천점", location="전남 여수시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 역곡점", location="경기 부천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 연산점", location="부산 연제구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 연수롯데마트점", location="인천 연수구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 연수점", location="인천 연수구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 연향점", location="전남 순천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영대병원네거리점", location="대구 남구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영도점", location="부산 영도구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영등점", location="전북 익산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영등포구청역점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영종도롯데마트점", location="인천 중구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영종점", location="인천 중구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영주점", location="경북 영주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영천점", location="경북 영천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 예산점", location="충남 예산군", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오광장점", location="경북 포항시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오리점", location="경기 성남시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오목교점", location="서울 양천구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오산롯데마트점", location="경기 오산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오산점", location="경기 오산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오정점", location="경기 부천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오창점", location="충북 청주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오천점", location="경북 포항시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 옥정점", location="경기 양주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 옥포점", location="경남 거제시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 왜관점", location="경북 칠곡군", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용봉점", location="광주 북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용산아이파크몰점", location="서울 용산구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용인구성점", location="경기 용인시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용인점", location="경기 용인시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용전점", location="대전 동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 우현점", location="경북 포항시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 성남시청점", location="경기 성남시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 성서점", location="대구 달서구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 성정롯데마트점", location="충남 천안시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 세종시청점", location="세종 한누리대로", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 세종점", location="세종 갈매로", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 센텀점", location="부산 해운대구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 소사점", location="경기 부천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 소하점", location="경기 광명시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 속초점", location="강원 속초시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송도롯데마트점", location="인천 연수구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송우점", location="경기 포천시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송정점", location="강원 강릉시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송천롯데마트맥스점", location="전북 전주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송천점", location="전북 전주시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송탄점", location="경기 평택시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송파롯데마트점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송현점", location="대구 달서구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수송점", location="전북 군산시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수완롯데마트점", location="광주 광산구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수완점", location="광주 광산구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수원롯데몰점", location="경기 수원시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수원점", location="경기 수원시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수지롯데몰점", location="경기 용인시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수지점", location="경기 용인시", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 수진점", location="경기 성남시", location_type="롯데하이마트")
]

# 페휴대폰
discarded_phones = [
    Depot(name="(KT)CPK 노원2호점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(KT)CPK 마들역점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(KT)CPK 상계2호점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(KT)CPK 적선점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(KT)CPK 홍대정문점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)CPK홍대클럽점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)HJY마포역점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)M&S마두역직영점", location="경기 고양시", location_type="민팃ATM"),
    Depot(name="(KT)M&S신용산역직영점", location="서울 용산구", location_type="민팃ATM"),
    Depot(name="(KT)M&S화정역직영점", location="경기 고양시", location_type="민팃ATM"),
    Depot(name="(KT)경진텔레콤 센텀점", location="부산 해운대구", location_type="민팃ATM"),
    Depot(name="(KT)나무 연산점", location="부산 연제구", location_type="민팃ATM"),
    Depot(name="(KT)달콤컴퍼니 합성점", location="경남 창원시", location_type="민팃ATM"),
    Depot(name="(KT)대세통신 중마점", location="전남 광양시", location_type="민팃ATM"),
    Depot(name="(KT)더킹 광복점", location="부산 중구", location_type="민팃ATM"),
    Depot(name="(KT)디액션 한성대점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="(KT)미래네트웍스 이토타워점", location="인천 남동구", location_type="민팃ATM"),
    Depot(name="(KT)브로커뮤니케이션 신촌연세로점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(KT)사직동 투자매장", location="부산 연제구", location_type="민팃ATM"),
    Depot(name="(KT)선광 못골점", location="부산 남구", location_type="민팃ATM"),
    Depot(name="(KT)스마일쓰리 신도봉시장점", location="서울 도봉구", location_type="민팃ATM"),
    Depot(name="(KT)아이엠티월드 홍대놀이터점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)아이엠티월드 홍대서교점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)에스엠 하단점", location="부산 사하구", location_type="민팃ATM"),
    Depot(name="(KT)에스엠커뮤니케이션 쥬디스신관점", location="부산 부산진구", location_type="민팃ATM"),
    Depot(name="(KT)에이쓰리 운정산내점", location="경기 파주시", location_type="민팃ATM"),
    Depot(name="(KT)엠에이치컴퍼니 화정점", location="울산 동구", location_type="민팃ATM"),
    Depot(name="(KT)엠엔케이 하단점", location="부산 사하구", location_type="민팃ATM"),
    Depot(name="(KT)제이씨앤 삼산점", location="울산 남구", location_type="민팃ATM"),
    Depot(name="(KT)지네이션 공업탑점", location="울산 남구", location_type="민팃ATM"),
    Depot(name="(KT)청라커낼웨이점", location="인천 서구", location_type="민팃ATM"),
    Depot(name="(KT)케이컴퍼니 사직점", location="부산 동래구", location_type="민팃ATM"),
    Depot(name="(KT)펜타CA 혜화역점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(KT)피플팩토리 양정점", location="부산 부산진구", location_type="민팃ATM"),
    Depot(name="(LGU+) 일상비일상의틈", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGDnF대리점중앙로점", location="충북 옥천군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGFORCE중랑우체국점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGLS커뮤니티성일중고사거리점", location="경기 성남시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGMJ커뮤니이마트사거리점", location="충북 충주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGMJ커뮤니충주농협점", location="충북 충주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGMJ커뮤니하나로마트점", location="충북 증평군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGMTI대원사거리점", location="경기 성남시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGNJ모바일삼척우체국점", location="강원 삼척시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGNJ모바일태백우체국점", location="강원 태백시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGSJ종합정보통신계산로점", location="충북 영동군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGSmart정보통신강진점", location="전남 강진군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGTOP텔레콤공릉시장점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGTOP텔레콤옥정폴리프라자점", location="경기 양주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGTT114평창중앙로", location="강원 평창군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGVIP플러스박애병원점", location="경기 평택시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGVIP플러스통북시장점", location="경기 평택시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGYH텔레콤현진에버빌", location="경북 구미시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG가온텔레콤산본역점", location="경기 군포시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG가족모바일연수역점", location="인천 연수구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG갈산직영점갈산사거리점", location="인천 부평구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG강릉U플러스사거리점", location="강원 강릉시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG강서소매영업팀오목교점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG거명정보통신의료원점", location="전남 순천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG거인새싹로점", location="부산 부산진구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG경호통신서수원점", location="경기 수원시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG공스모바일목감점", location="경기 시흥시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG광수텔레콤새마을시장점", location="경기 광명시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG광컴퍼니구산역점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG굿피플플러스북아현로점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG나눔정보통신농협사거리점", location="충북 괴산군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG나래내손점", location="경기 의왕시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG나인텔레콤골목시장점", location="부산 사하구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG나인텔레콤과학산단로점", location="부산 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG나인텔레콤신호산단2로점", location="부산 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG넘버원행신역점", location="경기 고양시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG넝쿨정보북교사거리점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG뉴패밀리시영아파트점", location="광주 광산구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG뉴패밀리효덕점", location="광주 남구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다온사랑한양상가점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다온오리로점", location="경기 광명시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다온텔레콤부전역점", location="부산 부산진구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다올휴머니즘컴퍼니구암역점", location="대전시 유성구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다원대리점새마을금고점", location="대전시 유성구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다이나믹팩토리육거리시장점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다인모바일송탄우체국점", location="경기 평택시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG대박유플러스해태상가점", location="경기 고양시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG대통신흥사거리2점", location="경기 성남시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG대한플러스부천역점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG대흥정보통신우장산역점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더드림스소사종합시장점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더베스트오산역점", location="경기 오산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더베스트주공아파트점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더블스타화곡본동시장점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더유피자이아파트점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더좋은북부시장점", location="전북 익산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더좋은사거리점", location="전북 김제시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더좋은원광대대학로점", location="전북 익산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG동경국민은행사거리점", location="전남 화순군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG동양정보통신유천네거리점", location="대전 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG드림원롯데시네마점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG디씨티컴퍼니귀빈예식장점", location="인천 미추홀구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG라온커뮤니시청점", location="경기 포천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG리더스모바일농협점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG리더스모바일새마을금고점", location="충북 증평군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG리더스모바일우체국점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG리드캡부평문화로점", location="인천 부평구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG마루통신남해점", location="경남 남해군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG마루통신하동우체국점", location="경남 하동군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG명성컴퍼니해양경찰서점", location="경남 통영시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG명원텔레콤신광로점", location="제주시 삼무로", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG명품텔레콤대구역점", location="대구시 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모둠텔레콤송산초등학교점", location="경기 의정부시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모바일제너레이션부천남부시장점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모아대리점농협사거리점", location="대전 대덕구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모아대리점세종시청점", location="세종특별자치시 한누리대로", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모아대리점정림삼거리점", location="대전 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모아대리점중리네거리점", location="대전 대덕구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG모아텔레콤죽도파출소점", location="경북 포항시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG무한텔레콤농협점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG뮤즈문화회관점", location="부산 해운대구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG미래중앙통신동문로터리점", location="제주특별자치도 제주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG미소텔레콤홈플러스점", location="경남 거제시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG바우컴퍼니원마트점", location="강원 강릉시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG베스트플러스천내리점", location="대구시 달성군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG보람컴퍼니로데오점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG보람컴퍼니롯데리아점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG보람컴퍼니형석1차아파트", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG보람컴퍼니효성아파트점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG본오중앙약국점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG봄날남악신도시점", location="전남 무안군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG봄날대불점", location="전남 영암군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG봄날북항점", location="전남 목포시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG북서울광운대점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG브이아이피컴퍼니신창우체국점", location="광주 광산구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG비엔비익산역점", location="전북 익산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG비커넥티드유진대방DMCP점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG사계종가4로점", location="울산 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG사랑애텔레콤롯데백화점", location="대전 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG사랑커뮤니동부지방법원점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG새늘정보통신금호1단지점", location="전북 군산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG서광등촌역점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG서광유통우체국점", location="전남 여수시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG서희정보돌고개점", location="광주 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG성공유클래스대동상가점", location="부산 해운대구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG성공유클래스쌍용예가점", location="부산 동래구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG성현텔레콤군포점", location="경기 군포시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG소영컴퍼니라피에스타점", location="경남 양산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG소영컴퍼니사상로점", location="부산 사상구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG소영컴퍼니젊음의거리점", location="부산 북구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG수빈텔레콤장등로점", location="경남 김해시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG수빈텔레콤탑마트점", location="경남 김해시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG슈퍼맨텔레콤뉴삼부프라자점", location="대전시 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG스타컴퍼니덕계점", location="경남 양산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG스타텔레콤검단농협점", location="인천 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG슬기모바일구월롯데캐슬점", location="인천 남동구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG승진모바일성포점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG승진모바일아디다스상록점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스대림역점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스방화사거리점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스파리공원점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신세계면목시장점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신세계성주군청점", location="경북 성주군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신윤티앤에스법조타운점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신커뮤니농협사거리점", location="강원 원주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG씨엠씨성복역점", location="경기 용인시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG아큐플러스가락시장역점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG아티스트계룡아파트점", location="대전 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG알파대리점롯데리아점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG약산통신중랑전화국점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG어썸모바일본오국민은행점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에덴씨엔씨시영아파트점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에스와이패밀리중앙대점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에이블푸르지오사거리점", location="충남 천안시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에이스네트웍중앙사거리점", location="충북 보은군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에프원문타워점", location="충남 천안시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에프원충무이마트점", location="충남 천안시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에프원컴퍼니북가좌초교사거리점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엔에스플러스구로이마트점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엔에스플러스영등포점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엠에스컴퍼니예산역점", location="충남 예산군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엠엔엠동묘북측점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엠엔엠신원캐슬", location="경기 고양시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG연남원주초교점", location="강원 원주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG영광텔레콤영광면목점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG영텔레콤전통시장점", location="부산 해운대구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG오름커뮤니노원사거리점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG오즈텔레콤산남점", location="경기 수원시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG온새미로모래내점", location="인천 남동구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG원커뮤니케이션이마트점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG위너스시화공고점", location="경기 시흥시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG위너스정왕시장점", location="경기 시흥시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG위너스행정복지센터점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG위스토리서광주농협점", location="광주시 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG위스토리터미널점", location="전북 고창군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유림텔레콤금강볼링장점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유림텔레콤농협점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유림텔레콤청대점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유림텔레콤청주여고점", location="충북 청주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유스토리원시청역점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유일정보통신모악로점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유일정보통신전주농협사거리점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유일정보통신홍산남로점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유진텔레콤삼익아파트점", location="경기 수원시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유한회사탑컴퍼니전남대후문점", location="광주시 북구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유희보령시장점", location="충남 보령시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG이든현대점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG이루다다대로점", location="부산 사하구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG이룸플러스나자로점", location="경기 의왕시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG일선왜관중앙점", location="경북 칠곡군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG정현텔레콤중앙시장2호점", location="경기 안양시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG제이에스컴퍼니경찰병원역점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG제주텔레콤도남사거리점", location="제주 제주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG좋은가족명일역점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG중부넷남구로역점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG진우커뮤니덕계점", location="경기 양주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG참소리청학점", location="인천 연수구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG창경대리점김천혁신도시점", location="경북 김천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG창성코퍼레이션거모점", location="경기 시흥시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG처음처럼2철산역2점", location="경기 광명시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG천재스타벅스사거리점", location="충남 천안시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG초아텔레콤동강프라자점", location="경기 성남시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG친절한형제현대아파트점", location="서울 도봉구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG친절한형제흥국상가점", location="서울 동대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG케이모바일고현교회점", location="전북 익산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG케이모바일만성중앙로점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG케이모바일팔달로점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG코리아유플러스운천역점", location="광주 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG코리아통신구포점", location="부산 북구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG키움정보통신옥포시장점", location="경남 거제시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태백중앙역2번출구점", location="경기 안산시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태양성만수소방서점", location="인천 남동구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태온텔레콤먹거리타운점", location="경남 창원시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태왕가좌시장점", location="인천 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태왕상동시장입구점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG태왕중동남부역점", location="경기 부천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG통큰형제들아이파크점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG투앤디원상무역점", location="광주 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG투앤디원효천1지구점", location="광주시 남구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG티씨엠브릭스타워점", location="경기 남양주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG파인컴퍼니초록도서관점", location="경기 평택시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG포피플즈시장점", location="세종 조치원읍", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG필립정보전남대공대후문점", location="광주 북구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG필립정보호반리젠시빌점", location="광주 광산구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG하람컴퍼니세종점", location="경기 시흥시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG하랑정보통신영광터미널점", location="전남 영광군", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG한동부센트레빌점", location="광주 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG한빛컴퍼니사거리점", location="제주특별자치도 제주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG한사거리점", location="광주 남구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG한시영5단지점", location="광주시 서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG해신안락로점", location="부산시 동래구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG행복Uplus경복궁아파트점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG행복Uplus롯데슈퍼점", location="전북 전주시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG형제통신구운점", location="경기 수원시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG화신시민회관점", location="충북 제천시", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG휘텔레콤신설동역점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+)M LG웅장까치산역1점", location="서울 강서구", location_type="민팃ATM")
]


class ElectricScreen(screen.Screen): # 생활 쓰레기
    def __init__(self, root, depot_type: DepotType):
        self.root = root
        self.appbar = widget.AppBar(
            root=root,
            title=depot_type.value,
            action=None
        )

        self.scroll_canvas = tkinter.Canvas(root, background=theme.color_background, highlightthickness=0)
        self.scroll_bar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=self.scroll_canvas.yview)
        self.scroll_frame = tkinter.Frame(self.scroll_canvas, background=theme.color_background)
        self.scroll_canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_canvas.bind("<Configure>", lambda event: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
        self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.name_9minutes_text = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=25, bold=True)
        )
        self.name_9minutes_text.insert(tkinter.END, "상호명")
        self.name_9minutes_text.configure(state=tkinter.DISABLED)

        self.location_9minutes_text = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=25, bold=True)
        )
        self.location_9minutes_text.insert(tkinter.END, "수거장소")
        self.location_9minutes_text.configure(state=tkinter.DISABLED)

        self.location_type_9minutes_text = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=25, bold=True)
        )
        self.location_type_9minutes_text.insert(tkinter.END, "장소구분")
        self.location_type_9minutes_text.configure(state=tkinter.DISABLED)

        self.split_line = tkinter.Frame(root, background=theme.color_on_background)

        items = discarded_phones if depot_type == DepotType.PHONE else discarded_appliances
        for i in range(len(items)):
            depot_frame = tkinter.Frame(self.scroll_frame, background=theme.color_background)

            name_text = tkinter.Text(
                depot_frame,
                background=theme.color_background,
                fg=theme.color_on_background,
                borderwidth=0,
                highlightthickness=0,
                wrap="word",
                font=theme.font(size=20)
            )
            name_text.insert(tkinter.END, items[i].name)
            name_text.configure(state=tkinter.DISABLED)

            location_text = tkinter.Text(
                depot_frame,
                background=theme.color_background,
                fg=theme.color_on_background,
                borderwidth=0,
                highlightthickness=0,
                wrap="word",
                font=theme.font(size=20)
            )
            location_text.insert(tkinter.END, items[i].location)
            location_text.configure(state=tkinter.DISABLED)

            location_type_text = tkinter.Text(
                depot_frame,
                background=theme.color_background,
                fg=theme.color_on_background,
                borderwidth=0,
                highlightthickness=0,
                wrap="word",
                font=theme.font(size=20)
            )
            location_type_text.insert(tkinter.END, items[i].location_type)
            location_type_text.configure(state=tkinter.DISABLED)

            split_line = tkinter.Frame(depot_frame, background=theme.color_sub)

            name_text.place(
                x=0, y=60,
                width=320, height=79,
                anchor="w"
            )
            location_text.place(
                x=320, y=60,
                width=160, height=79,
                anchor="w"
            )
            location_type_text.place(
                x=320+160, y=60,
                width=160, height=79,
                anchor="w"
            )
            split_line.place(
                x=0, y=79,
                width=720-30-20*2, height=1
            )
            depot_frame.place(
                x=20, y=20+80*i,
                width=720-30-20*2, height=80
            )
        self.total_height = 80 * len(items) + 20*2

        self.scroll_frame.configure(height=self.total_height, width=720-30)
        if platform.system() == "Windows":  # Windows 일 때
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: self.scroll_canvas.yview_scroll(-1 * event.delta // 120, "units")
            )
        else:  # macOS 일 떄
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: self.scroll_canvas.yview_scroll(-1 * event.delta, "units")
            )

        self.restart_bar = widget.RestartBar(root)


    def show(self):
        self.appbar.place()

        self.name_9minutes_text.place(
            x=20, y=120+65,
            width=320, height=79,
            anchor="w"
        )
        self.location_9minutes_text.place(
            x=20+320, y=120+65,
            width=160, height=79,
            anchor="w"
        )
        self.location_type_9minutes_text.place(
            x=20+320+160, y=120+65,
            width=160, height=79,
            anchor="w"
        )
        self.split_line.place(
            x=0, y=120+79,
            width=720, height=1
        )

        self.scroll_canvas.place(
            x=0, y=120+80,
            width=720-30, height=1080-120*2-80
        )
        self.scroll_bar.place(
            x=720-30, y=120+80,
            width=30, height=1080-120*2-80
        )

        self.restart_bar.place()


    def hide(self):
        self.appbar.place_forget()

        self.name_9minutes_text.place_forget()
        self.location_9minutes_text.place_forget()
        self.location_type_9minutes_text.place_forget()
        self.split_line.place_forget()

        self.scroll_canvas.place_forget()
        self.scroll_bar.place_forget()

        self.restart_bar.place_forget()
