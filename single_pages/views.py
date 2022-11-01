from django.shortcuts import render
from blog.models import Post
from single_pages.models import MSemi, SSemi, Fabless, KorSemiShare, SemiShare, Research, SemiExport, KorSemiExport, WorldSemiImport, ChinaSemiImport, ChiSemiExport, WorldSemiImExport
from single_pages.models import Topic2020, Topic2021, Topic2022, TopicChange
# from single_pages.models import Movevixlibor

from collections import OrderedDict
from .fusioncharts import FusionCharts


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request, 
        'single_pages/landing.html',
        {
            'recent_posts':recent_posts,
        }
    )

def paper(request):
    #1
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = MSemi.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.country, "value": co.share})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "메모리 반도체 시장 점유율" #제목
    chartConfig["subCaption"] = "20년 기준" #소제목
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    pie2D = FusionCharts("pie3d", "ex1", "600", "400", "chart-1", "json", dataSource)

    #2
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = SSemi.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.country, "value": co.share})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "시스템 반도체 시장 점유율" #제목
    chartConfig["subCaption"] = "19년 기준" #소제목
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    Spie2D = FusionCharts("pie3d", "ex2", "600", "400", "chart-2", "json", dataSource)

    #3
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = Fabless.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.country, "value": co.share})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "팹리스 시장 점유율" #제목
    chartConfig["subCaption"] = "21년 기준" #소제목
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    Fabless2D = FusionCharts("pie3d", "ex3", "600", "400", "chart-3", "json", dataSource)

    #4
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = KorSemiShare.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.semi})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "반도체 전체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Msemi})
    dataSource["dataset"].append({"seriesname": "메모리 반도체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Ssemi})
    dataSource["dataset"].append({"seriesname": "시스템 반도체", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "한국의 글로벌 시장 점유율 추이" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "점유율" #y축 이름
    chartConfig["numberSuffix"] = "%" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    KorSemiShare2D = FusionCharts("msline", "ex4", "600", "400", "chart-4", "json", dataSource)


    #5
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = SemiShare.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.semi})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "메모리 반도체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Msemi})
    dataSource["dataset"].append({"seriesname": "시스템 반도체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Ssemi})
    dataSource["dataset"].append({"seriesname": "광개별 소자", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "반도체 시장 규모" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "시장규모" #y축 이름
    chartConfig["numberSuffix"] = "억불" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    SemiShare2D = FusionCharts("stackedcolumn2d", "ex5", "600", "400", "chart-5", "json", dataSource)

    #6
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = SemiExport.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.semi})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "반도체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.oil})
    dataSource["dataset"].append({"seriesname": "석유제품", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.car})
    dataSource["dataset"].append({"seriesname": "자동차", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "반도체 수출 비중" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "수출 비중" #y축 이름
    chartConfig["numberSuffix"] = "%" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    SemiExport2D = FusionCharts("msline", "ex6", "600", "400", "chart-6", "json", dataSource)

    #7
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = Research.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.year, "value": co.researchFunds})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "반도체 연구비" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "연구비" #y축 이름
    chartConfig["numberSuffix"] = "억원" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    Research2D = FusionCharts("line", "ex7", "600", "400", "chart-7", "json", dataSource)

    #8
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = KorSemiExport.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.all})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "전체", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.export})
    dataSource["dataset"].append({"seriesname": "중국 수출", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.share})
    dataSource["dataset"].append({"seriesname": "중국 수출 비중", "renderas": "line", "parentyaxis": "S", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "한국 반도체 수출" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "Trade Value" #y축 이름
    chartConfig["syaxisname"] = "비중"
    chartConfig["snumbersuffix"] = "%" #y축 숫자단위(오른쪽)
    chartConfig["numbersuffix"] = "$" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    KorSemiExport2D = FusionCharts("mscolumn3dlinedy", "ex8", "600", "400", "chart-8", "json", dataSource)

    #9
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = WorldSemiImport.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.year, "value": co.export})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "세계 반도체 수입 규모" #제목
    chartConfig["subCaption"] = "단위:십억불" #소제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "수입 규모" #y축 이름
    chartConfig["numberSuffix"] = "$" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    WorldSemiImport2D = FusionCharts("line", "ex9", "600", "400", "chart-9", "json", dataSource)

    #10
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object = ChinaSemiImport.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.year, "value": co.export})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "중국 반도체 수입 규모" #제목
    chartConfig["subCaption"] = "단위:십억불" #소제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "수입 규모" #y축 이름
    chartConfig["numberSuffix"] = "$" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ChinaSemiImport2D = FusionCharts("line", "ex10", "600", "400", "chart-10", "json", dataSource)

    #11
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = ChiSemiExport.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.export})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "중국 수출", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Simport})
    dataSource["dataset"].append({"seriesname": "중국 수입", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "중국 수출과 수입" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "Trade Value" #y축 이름
    chartConfig["syaxisname"] = "비중"
    chartConfig["formatnumberscale"] = "1"
    chartConfig["plottooltext"] = "<b>$dataValue</b> apps were available on <b>$seriesName</b> in $label"
    chartConfig["numbersuffix"] = "$" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ChiSemiExport2D = FusionCharts("mscolumn3d", "ex11", "600", "400", "chart-11", "json", dataSource)

    #12
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[]
    #data 값 넣기
    class_object = WorldSemiImExport.objects.all()
    for co in class_object:
        data["category"].append({"label": co.year})
        data["data"].append({"value": co.export})
    dataSource["categories"].append({"category": data["category"]})
    dataSource["dataset"].append({"seriesname": "중국 수출", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.Simport})
    dataSource["dataset"].append({"seriesname": "중국 수입", "data": data["data"]})

    data["data"] = [] #chartdata는 json형식이다.
    for co in class_object:
        data["data"].append({"value": co.both})
    dataSource["dataset"].append({"seriesname": "수출&수입", "renderas": "line", "parentyaxis": "S", "data": data["data"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "세계 대중국 수출 및 수입" #제목
    chartConfig["xAxisName"] = "년도" #x축 이름
    chartConfig["yAxisName"] = "Trade Value" #y축 이름
    chartConfig["syaxisname"] = "비중"
    chartConfig["snumbersuffix"] = "%" #y축 숫자단위(오른쪽)
    chartConfig["numbersuffix"] = "$" #y축 숫자단위
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    WorldSemiImExport2D = FusionCharts("mscolumn3dlinedy", "ex12", "600", "400", "chart-12", "json", dataSource)


    context = {'output': pie2D.render(),'output_2': Spie2D.render(), 'output_3': Fabless2D.render(), 'output_4': KorSemiShare2D.render(),
    'output_5': SemiShare2D.render(), 'output_6': SemiExport2D.render(), 'output_7': Research2D.render(), 'output_8': KorSemiExport2D.render(),
    'output_9': WorldSemiImport2D.render(), 'output_10': ChinaSemiImport2D.render(), 'output_11': ChiSemiExport2D.render(), 'output_12': WorldSemiImExport2D.render()}
    return render(request, 'single_pages/paper.html', context) #render


def paper2(request):
    #1
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object =Topic2020.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.info, "value": co.status})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "2020 정보원 중요도" #제목
    chartConfig["subCaption"] = "2020년" #소제목
    chartConfig["yaxisname"] = "중요도"
    chartConfig["aligncaptionwithcanvas"] = "0"
    chartConfig["plottooltext"] ="<b>$dataValue</b> leads received"
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ex1 = FusionCharts("bar2d", "ex1", "600", "400", "chart-1", "json", dataSource)

    #2
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object =Topic2021.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.info, "value": co.status})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "2021 정보원 중요도" #제목
    chartConfig["subCaption"] = "2021년" #소제목
    chartConfig["yaxisname"] = "중요도"
    chartConfig["aligncaptionwithcanvas"] = "0"
    chartConfig["plottooltext"] ="<b>$dataValue</b> leads received"
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ex2 = FusionCharts("bar2d", "ex2", "600", "400", "chart-2", "json", dataSource)

    #3
    #chartdata 선언
    dataSource = OrderedDict()
    dataSource["data"] = [] #chartdata는 json형식이다.
    #data 값 넣기
    class_object =Topic2022.objects.all()
    for co in class_object:
        dataSource["data"].append({"label": co.info, "value": co.status})
    chartConfig = OrderedDict()
    chartConfig["caption"] = "2022 정보원 중요도" #제목
    chartConfig["subCaption"] = "2022년" #소제목
    chartConfig["yaxisname"] = "중요도"
    chartConfig["aligncaptionwithcanvas"] = "0"
    chartConfig["plottooltext"] ="<b>$dataValue</b> leads received"
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ex3 = FusionCharts("bar2d", "ex3", "600", "400", "chart-3", "json", dataSource)

    #4
    #chartdata 선언
    print("--------------------", )
    dataSource = OrderedDict()
    dataSource["categories"] = [] #chartdata는 json형식이다.
    dataSource["dataset"]=[]
    #값 넣기 위해 잠시 만든 것
    data = OrderedDict()
    data["data"] = [] 
    data['category']=[{"label": "경제"}, {"label": "정치"}, {"label": "문화"}, {"label": "국제"}]
    #data 값 넣기
    class_object = TopicChange.objects.all()
    for co in class_object:
        data["data"]=[{"value": co.economy}, {"value": co.politics}, {"value": co.culture}, {"value": co.inter}]
        if co.year=='2020':
            dataSource["dataset"].append({"seriesname": "2020년", "data": data["data"]})
        elif co.year=='2021':
            dataSource["dataset"].append({"seriesname": "2021년", "data": data["data"]})
        elif co.year=='2022':
            dataSource["dataset"].append({"seriesname": "2022년", "data": data["data"]})
        data["data"] = [] #chartdata는 json형식이다.

    
    dataSource["categories"].append({"category": data["category"]})

    chartConfig = OrderedDict()
    chartConfig["caption"] = "연도별 분야별 정보원 수의 변화" #제목
    chartConfig["xAxisName"] = "분아별" #x축 이름
    chartConfig["yAxisName"] = "정보원 수" #y축 이름
    chartConfig["theme"] = "fusion" #테마
    #그래프 특징 설정
    dataSource["chart"] = chartConfig
    #그래프 생성
    ex4 = FusionCharts("msline", "ex4", "600", "400", "chart-4", "json", dataSource)

    datadata=[
        {
            "x": "IT",
            "value": 590000000,
            "category": "Sino-Tibetan"
        }]
    context = {'output': ex1.render(), 'output_2': ex2.render(), 'output_3': ex3.render(), 'output_4': ex4.render(), 'datadata':datadata}
    return render(request, 'single_pages/paper2.html', context) #render