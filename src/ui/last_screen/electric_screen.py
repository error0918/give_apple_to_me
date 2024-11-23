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
    Depot(name="LH강남8단지", location="서울특별시 강남구", location_type="공동주택(아파트 등)"),
    Depot(name="LH삼성도시형생활주택", location="서울특별시 강남구", location_type="공동주택(아파트 등)"),
    Depot(name="가양7단지 아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="농인종합사회복지관", location="서울특별시 강남구", location_type="공동주택(아파트 등)"),
    Depot(name="독산역롯데캐슬아파트", location="서울특별시 금천구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌11단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌4단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌6단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌7단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="등촌9단지아파트", location="서울특별시 강서구", location_type="공동주택(아파트 등)"),
    Depot(name="번동3단지 아파트", location="서울특별시 강북구", location_type="공동주택(아파트 등)"),
    Depot(name="신림1단지", location="서울특별시 관악구", location_type="공동주택(아파트 등)"),
    Depot(name="염리종합사회복지관", location="서울특별시 마포구", location_type="공동주택(아파트 등)"),
    Depot(name="영등포 문래롯데캐슬", location="서울특별시 영등포구", location_type="공동주택(아파트 등)"),
    Depot(name="월계주공1단지", location="서울특별시 노원구", location_type="공동주택(아파트 등)"),
    Depot(name="중계9단지", location="서울특별시 노원구", location_type="공동주택(아파트 등)"),
    Depot(name="서울시청자미디어센터", location="서울특별시 성북구", location_type="지자체(구청, 행정복지센터 등)"),
    Depot(name="롯데하이마트 용두점", location="서울 동대문구", location_type="롯데하이마트"),
    Depot(name="삼성디지털프라자 마곡본점", location="서울시 강서구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 삼성대치본점", location="서울 강남구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 강남본점", location="서울 강남구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 강동점", location="서울특별시 강동구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 강서본점", location="서울특별시 강서구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 개봉점", location="서울특별시 구로구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 공릉점", location="서울특별시 노원구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 관악봉천점", location="서울특별시 관악구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 광진점", location="서울특별시 광진구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 구로점", location="서울특별시 구로구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 금천점", location="서울특별시 금천구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 노원본점", location="서울특별시 노원구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 도곡점", location="서울특별시 강남구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 도봉쌍문본점", location="서울특별시 도봉구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 마포본점", location="서울시 마포구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 문정점", location="서울시 송파구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 미아점", location="서울특별시 강북구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 방배점", location="서울특별시 서초구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 삼선교점", location="서울특별시 성북구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 상도점", location="서울특별시 동작구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 서초본점", location="서울특별시 서초구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 송파점", location="서울특별시 송파구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 수색점", location="서울특별시 은평구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 신림점", location="서울특별시 관악구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 신정점", location="서울특별시 양천구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 영등포본점", location="서울특별시 영등포구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 왕십리점", location="서울특별시 성동구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 용산점", location="서울특별시 용산구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 은평불광본점", location="서울특별시 은평구", location_type="삼성디지털프라자"),
    Depot(name="삼성디지털프라자 홍대본점", location="서울특별시 마포구", location_type="삼성디지털프라자"),
    Depot(name="LG베스트샵 강북본점", location="서울 강북구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 건대입구점", location="서울특별시 광진구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 광진본점", location="서울특별시 광진구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 노원본점", location="서울 노원구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 동교점", location="서울 마포구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 미아사거리점", location="서울 성북구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 봉천점", location="서울특별시 관악구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 불광본점", location="서울특별시 은평구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 상계점", location="서울 노원구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 상도점", location="서울특별시 동작구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 서울양평점", location="서울 영등포구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 서초본점", location="서울특별시 서초구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 송파점", location="서울특별시 송파구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 쌍문본점", location="서울시 도봉구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 양천본점", location="서울특별시 양천구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 역촌점", location="서울특별시 은평구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 염리점", location="서울 마포구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 용두점", location="서울 동대문구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 은평점", location="서울특별시 은평구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 이수역점", location="서울시 동작구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 중랑점", location="서울특별시 중랑구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 강동본점", location="서울특별시 강동구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 강서본점", location="서울특별시 강서구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 거여점", location="서울특별시 송파구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 관악점", location="서울 관악구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 구로본점", location="서울 구로구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 금천본점", location="서울 금천구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 대치본점", location="서울 강남구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 목동점", location="서울특별시 양천구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 문래점", location="서울 영등포구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 반포점", location="서울 서초구", location_type="LG베스트샵"),
    Depot(name="LG베스트샵 강남본점", location="서울시 강남구", location_type="LG베스트샵"),
    Depot(name="롯데하이마트 홍대입구역점", location="서울 마포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 화곡점", location="서울 양천구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 중계롯데마트점", location="서울 노원구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 창동점", location="서울 도봉구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 천호역점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 청구점", location="서울 중구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 청량리롯데마트점", location="서울 동대문구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 월드타워점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 은평롯데몰점", location="서울 은평구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 은평점", location="서울 은평구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 잠실점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 장한평점", location="서울 성동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 종암점", location="서울 성북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 압구정점", location="서울 강남구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 양평롯데마트점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 영등포구청역점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 오목교점", location="서울 양천구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 용산아이파크몰점", location="서울 용산구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 송파롯데마트점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 신길점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 신림점", location="서울 관악구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 쌍문점", location="서울 도봉구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 아차산역점", location="서울 광진구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 불광점", location="서울 은평구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 사당점", location="서울 동작구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 삼선교점", location="서울 성북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 상계점", location="서울 노원구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 상도점", location="서울 동작구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 상봉점", location="서울 중랑구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 상암월드컵점", location="서울 마포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 상일IC점", location="서울 강동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 서울역롯데마트점", location="서울 중구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 석관점", location="서울 성북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 미아사거리점", location="서울 강북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 미아점", location="서울 강북구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 발산점", location="서울 강서구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 봉천점", location="서울 관악구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 금천점", location="서울 금천구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 길동점", location="서울 강동구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 김포공항롯데마트점", location="서울 강서구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 대치점", location="서울 강남구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 VIC마켓금천점", location="서울 금천구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 VIC마켓영등포점", location="서울 영등포구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 가락점", location="서울 송파구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 개봉점", location="서울 구로구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 건대입구점", location="서울 광진구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 공릉점", location="서울 노원구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 교대역점", location="서울 서초구", location_type="롯데하이마트"),
    Depot(name="롯데하이마트 구로점", location="서울 구로구", location_type="롯데하이마트")
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
    Depot(name="(KT)M&S신용산역직영점", location="서울 용산구", location_type="민팃ATM"),
    Depot(name="(KT)디액션 한성대점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="(KT)브로커뮤니케이션 신촌연세로점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(KT)스마일쓰리 신도봉시장점", location="서울 도봉구", location_type="민팃ATM"),
    Depot(name="(KT)아이엠티월드 홍대놀이터점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)아이엠티월드 홍대서교점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(KT)펜타CA 혜화역점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+) 일상비일상의틈", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGFORCE중랑우체국점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LGTOP텔레콤공릉시장점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG강서소매영업팀오목교점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG광컴퍼니구산역점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG굿피플플러스북아현로점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG다온사랑한양상가점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG대흥정보통신우장산역점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더블스타화곡본동시장점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG더유피자이아파트점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG북서울광운대점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG사랑커뮤니동부지방법원점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG서광등촌역점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스대림역점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스방화사거리점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신비플러스파리공원점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신세계면목시장점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG신윤티앤에스법조타운점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG아큐플러스가락시장역점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG약산통신중랑전화국점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에덴씨엔씨시영아파트점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에스와이패밀리중앙대점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG에프원컴퍼니북가좌초교사거리점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엔에스플러스구로이마트점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엔에스플러스영등포점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG엠엔엠동묘북측점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG영광텔레콤영광면목점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG오름커뮤니노원사거리점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG유스토리원시청역점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG제이에스컴퍼니경찰병원역점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG좋은가족명일역점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG중부넷남구로역점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG친절한형제현대아파트점", location="서울 도봉구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG친절한형제흥국상가점", location="서울 동대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG통큰형제들아이파크점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)B LG휘텔레콤신설동역점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+)M LG웅장까치산역1점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)광장동 광나루역점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="(LGU+)구로동 구로이마트점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="(LGU+)길동 길동역2번출구점", location="서울시 강동구", location_type="민팃ATM"),
    Depot(name="(LGU+)길동 길동역점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="(LGU+)낙성대동 서울대입구점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="(LGU+)내발산동 우장산역점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)당산동 당산역래미안점", location="서울시 영등포구", location_type="민팃ATM"),
    Depot(name="(LGU+)대조동 불광시장점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="(LGU+)동소문동 성북구청점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="(LGU+)마곡동 마곡나루역1번출구점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)마곡동 사이언스파크DP2", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="(LGU+)마천동 마천역점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="(LGU+)망우역직영점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="(LGU+)망원동 마포구청역점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="(LGU+)목동 염창역점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)민팃BOX 테스트", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="(LGU+)봉천동 낙성대점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="(LGU+)봉천동 쑥고개로점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="(LGU+)삼선동 한성대입구역점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="(LGU+)상계2동 문화거리입구점", location="서울시 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)상계동 수락산역점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)상도동 숭실대닙구점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="(LGU+)서초4동 강남교보점", location="서울 서초구", location_type="민팃ATM"),
    Depot(name="(LGU+)신대방동 스마티움아파트점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="(LGU+)신정동 신정역점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="(LGU+)암사동 암사캐슬점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="(LGU+)역삼2동 역삼세무서점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="(LGU+)이문동 외대삼거리점", location="서울 동대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)장위동 북서울꿈의숲아이파크점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="(LGU+)중계1동 중계두타빌점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="(LGU+)진관동 상림마을점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="(LGU+)태평로2가 시청역점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="(LGU+)행운동 봉천로사거리점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="(LGU+)홍제동 홍제삼거리점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="(LGU+)화양동 건대입구역2번출구점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="ACT대리점 건대역직영점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="ATM_KBS신관공개홀1", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="ATM_KBS신관공개홀2", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="ATM_삼성메디슨", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="BK대리점 영등포구청직영점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="DMC센트럴자이3단지", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="IBK기업은행IFT", location="서울 중구", location_type="민팃ATM"),
    Depot(name="IBK기업은행본점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="KT BOX 테스트", location="서울 성동구", location_type="민팃ATM"),
    Depot(name="KT_마트ATM", location="서울 중구", location_type="민팃ATM"),
    Depot(name="KT_비통신향mini", location="서울 중구", location_type="민팃ATM"),
    Depot(name="KT아이티의형제들 건대점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="KT플라자 연신내역점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="LGU+상봉역점", location="서울시 중랑구", location_type="민팃ATM"),
    Depot(name="LGUP_ATM", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="LG_마트ATM", location="서울 중구", location_type="민팃ATM"),
    Depot(name="LG_비통신향mini", location="서울 중구", location_type="민팃ATM"),
    Depot(name="M&S홍대애드샵플러스점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="MD대리점 이태원점", location="서울 용산구", location_type="민팃ATM"),
    Depot(name="MD대리점 홍대점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="MINTIT_B2B", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="MINTIT_Terarosa", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="MK대리점 마포점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="M_ACE상도점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="M_KT보인종로5가점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="M_가로수SHOP목", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="M_민팃센터촬영용", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="M_행사용1", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="M_행사용2", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mart_1", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mart_2", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mart_3", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mart_4", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_1", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_2", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_3", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_4", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_5", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit_17F_mini_6", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="Mintit자원순환", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="NICE 마포사옥", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="NICE1사옥", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="NICE2사옥", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="PS&M (명동본점)", location="서울 중구", location_type="민팃ATM"),
    Depot(name="PS&M (뱅뱅사거리점)", location="서울 서초구", location_type="민팃ATM"),
    Depot(name="PS&M (본사사옥)", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="PS&M (잠실롯데점)", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="SBS목동1", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="SBS목동2", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="SBS목동3", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="SKN 이동형 차량 01", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SKN 이동형 차량 02", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SKN 이동형 차량 03", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SKN 이동형 차량 04", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SKN 이동형 차량 05", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SK에코플랜트", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 강남지점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 보라매지점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 신촌지점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 영등포지점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 을지로지점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="SK텔레콤 테크노마트지점", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="SOVAC", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="T Factory", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="T센터 수도권3 T센터 당산역점-2", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="T센터 타워을지로점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="T센터당산역점2", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="e-편한세상 광진그랜드파크", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="sATM_문정점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="강남스타대리점 서울대역점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="강남스타대리점 서초점", location="서울 서초구", location_type="민팃ATM"),
    Depot(name="강남스타대리점 이수역점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="강남스타대리점 학동역점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="강남스타대리점 헬리오시티점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="강남팀 강남PT 강남구청역점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="강동팀 강동PT 천호점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="강북팀 강북PT 광화문직영점", location="서울 종로구", location_type="민팃ATM"),
    Depot(name="강서대리점 염창역점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="강서팀 강서PT 가산역점", location="서울 금천구", location_type="민팃ATM"),
    Depot(name="강서팀 강서PT 개봉점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="개봉대리점 개봉사거리점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="군인공제회 용산점", location="서울 용산구", location_type="민팃ATM"),
    Depot(name="근흥대리점 대흥역점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="근흥대리점 종암직영점", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="길음래미안1차", location="서울 성북구", location_type="민팃ATM"),
    Depot(name="내발산직영점", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="늘봄대리점 강동구청", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="늘봄대리점 목동점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="늘푸른대리점 대치은마점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="늘푸른대리점 불광역점", location="서울 은평구", location_type="민팃ATM"),
    Depot(name="늘푸른대리점 이수역점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="늘푸른대리점 이수직영점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="늘푸른대리점 천호역점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="다원대리점 방이점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="동진대리점 가양역본", location="서울 강서구", location_type="민팃ATM"),
    Depot(name="등촌동 등촌역점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="랑랑대리점 명일역점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="롯데마트 구로점", location="서울 구로구", location_type="민팃ATM"),
    Depot(name="롯데마트 서울역점", location="서울 중구", location_type="민팃ATM"),
    Depot(name="롯데하이마트 상계점", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="리더스대리점 미도점(롯데백화점옆)", location="서울 노원구", location_type="민팃ATM"),
    Depot(name="매입room", location="서울 중구", location_type="민팃ATM"),
    Depot(name="멘토박스", location="서울 광진구", location_type="민팃ATM"),
    Depot(name="물류room", location="서울 중구", location_type="민팃ATM"),
    Depot(name="미래대리점 묵동직영점", location="서울 중랑구", location_type="민팃ATM"),
    Depot(name="미래대리점 장평직영점", location="서울 동대문구", location_type="민팃ATM"),
    Depot(name="민팃 테스트", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="민팃 팝업스토어", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="민팃1층센터ATM0", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="민팃미니6층", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="민팃센터Box", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="민팃테스트 ATM", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="방학동 신방학점", location="서울시 도봉구", location_type="민팃ATM"),
    Depot(name="백두대간대리점 목동직영점", location="서울 양천구", location_type="민팃ATM"),
    Depot(name="백두대간대리점 상암DMC점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="백마장대리점 시흥점", location="서울 금천구", location_type="민팃ATM"),
    Depot(name="백마장대리점 신림중앙직영점", location="서울 관악구", location_type="민팃ATM"),
    Depot(name="베테랑대리점 송리단점", location="서울 송파구", location_type="민팃ATM"),
    Depot(name="베테랑대리점 언주역점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="베테랑대리점 장지역점", location="서울시 송파구", location_type="민팃ATM"),
    Depot(name="베트남 VINA ATM", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="베트남 VINA 미니", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="북가좌대리점 본점", location="서울 서대문구", location_type="민팃ATM"),
    Depot(name="빅마켓 도봉점", location="서울 도봉구", location_type="민팃ATM"),
    Depot(name="삼성 강남점", location="서울 서초구", location_type="민팃ATM"),
    Depot(name="삼성1차아파트", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 명일점", location="서울 강동구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 문래점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 사당역점", location="서울 동작구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 삼성코엑스점", location="서울 강남구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 신풍점", location="서울 영등포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 장평점", location="서울 동대문구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점 Event10", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점 Event5", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점 Event6", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점 Event7", location="서울 마포구", location_type="민팃ATM"),
    Depot(name="삼성디지털프라자 홍대본점 Event8", location="서울 마포구", location_type="민팃ATM"),
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

        self.items = sorted(discarded_phones if depot_type == DepotType.PHONE else discarded_appliances, key=lambda x: x.location)
        self.index = 20
        for i in range(20):
            self.show_item(i)
        self.total_height = 80 * len(self.items) + 20*2

        self.scroll_frame.configure(height=self.total_height, width=720-30)

        def scroll_event(amount):
            self.scroll_canvas.yview_scroll(-1 * amount, "units")
            if self.index < len(self.items) and amount < 0:
                for i in range(self.index, self.index - amount):
                    if i < len(self.items):
                        self.show_item(i)
                        self.index += 1

        if platform.system() == "Windows":  # Windows 일 때
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: scroll_event(event.delta // 120)
            )
        else:  # macOS 일 떄
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: scroll_event(event.delta)
            )

        self.restart_bar = widget.RestartBar(root)


    def show_item(self, i: int):
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
        name_text.insert(tkinter.END, self.items[i].name)
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
        location_text.insert(tkinter.END, self.items[i].location)
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
        location_type_text.insert(tkinter.END, self.items[i].location_type)
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
