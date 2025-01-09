import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "germanuniv.settings")
django.setup()

from germanuniv.models import School, User, Residence, Language

# School 데이터 삽입
School.objects.bulk_create([
    School(name="TU Berlin", tuition_fee=5000, semester_fee=340, region="Berlin"),
    School(name="TU Munich", tuition_fee=6000, semester_fee=550, region="Munich"),
    School(name="TU Hamburg", tuition_fee=0, semester_fee=450, region="Hamburg"),
    School(name="Frankfurt University", tuition_fee=5800, semester_fee=400, region="Frankfurt"),
    School(name="Stuttgart University", tuition_fee=6500, semester_fee=350, region="Stuttgart"),
    School(name="Leipzig University", tuition_fee=0, semester_fee=300, region="Leipzig"),
    School(name="TU Dresden", tuition_fee=0, semester_fee=320, region="Dresden"),
    School(name="TU Brandenburg", tuition_fee=0, semester_fee=330, region="Brandenburg"),
    School(name="University of Bonn", tuition_fee=3900, semester_fee=480, region="Bonn"),
    School(name="TU Darmstadt", tuition_fee=0, semester_fee=350, region="Darmstadt"),
])

# User 데이터 삽입. 각 사용자를 하나씩 생성
User.objects.create_user(username="mary", password="1111", nickname="메리", favorite_school=School.objects.get(id=1))
User.objects.create_user(username="mati", password="2222", nickname="마티짱", favorite_school=School.objects.get(id=2))
User.objects.create_user(username="sook", password="3333", nickname="숙묭이", favorite_school=School.objects.get(id=3))
User.objects.create_user(username="saka", password="4444", nickname="사카구리", favorite_school=School.objects.get(id=4))
User.objects.create_user(username="tom", password="5555", nickname="톰헐디", favorite_school=School.objects.get(id=5))
User.objects.create_user(username="james", password="6666", nickname="제임스내꺼보이", favorite_school=School.objects.get(id=6))
User.objects.create_user(username="timothee", password="7777", nickname="티모띠샬라메", favorite_school=School.objects.get(id=7))
User.objects.create_user(username="bravo", password="8888", nickname="루까스부라보", favorite_school=School.objects.get(id=8))
User.objects.create_user(username="life", password="9999", nickname="인생", favorite_school=School.objects.get(id=9))
User.objects.create_user(username="journey", password="0000", nickname="여행갈래", favorite_school=School.objects.get(id=10))

# Residence 데이터 삽입
Residence.objects.bulk_create([
    Residence(residence_type="Apartment", monthly_rent=800.00, deposit=3000.00, school=School.objects.get(id=1)),
    Residence(residence_type="Dormitory", monthly_rent=400.00, deposit=1000.00, school=School.objects.get(id=2)),
    Residence(residence_type="House", monthly_rent=1000.00, deposit=5000.00, school=School.objects.get(id=3)),
    Residence(residence_type="Shared Room", monthly_rent=500.00, deposit=1500.00, school=School.objects.get(id=4)),
    Residence(residence_type="Studio", monthly_rent=600.00, deposit=2000.00, school=School.objects.get(id=5)),
    Residence(residence_type="Apartment", monthly_rent=850.00, deposit=3500.00, school=School.objects.get(id=6)),
    Residence(residence_type="Dormitory", monthly_rent=450.00, deposit=1200.00, school=School.objects.get(id=7)),
    Residence(residence_type="House", monthly_rent=950.00, deposit=4000.00, school=School.objects.get(id=8)),
    Residence(residence_type="Shared Room", monthly_rent=550.00, deposit=1800.00, school=School.objects.get(id=9)),
    Residence(residence_type="Studio", monthly_rent=700.00, deposit=2500.00, school=School.objects.get(id=10)),
])

# Language 데이터 삽입
Language.objects.bulk_create([
    Language(name="German", level="A1", school=School.objects.get(id=1)),
    Language(name="German", level="A2", school=School.objects.get(id=2)),
    Language(name="English", level="C1", school=School.objects.get(id=3)),
    Language(name="English", level="B2", school=School.objects.get(id=4)),
    Language(name="French", level="A1", school=School.objects.get(id=5)),
    Language(name="German", level="C1", school=School.objects.get(id=6)),
    Language(name="Spanish", level="B1", school=School.objects.get(id=7)),
    Language(name="Italian", level="A2", school=School.objects.get(id=8)),
    Language(name="German", level="C2", school=School.objects.get(id=9)),
    Language(name="English", level="B1", school=School.objects.get(id=10)),
])