anychart.onDocumentReady(function () {
    var data1 = [{"x":"반도체","value":1373},
    {"x":"미국","value":952},
    {"x":"중국","value":919},
    {"x":"삼성전자","value":688},
    {"x":"화웨이","value":575},
    {"x":"코로나19","value":569},
    {"x":"파운드리","value":542},
    {"x":"삼성","value":483},
    {"x":"스마트폰","value":404},
    {"x":"대만","value":393},
    {"x":"한국","value":379},
    {"x":"가능성","value":359},
    {"x":"기업들","value":347},
    {"x":"인텔","value":305},
    {"x":"TSMC","value":301},
    {"x":"양산","value":228},
    {"x":"경쟁력","value":221},
    {"x":"공급망","value":218},
    {"x":"부회장","value":206},
    {"x":"불확실성","value":185}];
    var chart1 = anychart.tagCloud(data1);
    chart1.angles([0]);
    chart1.container("container");
    // chart.getCredits().setEnabled(false);
    chart1.draw();


    var data2 = [{"x":"삼성전자","value":368},
    {"x":"블룸버그","value":231},
    {"x":"월스트리트저널","value":174},
    {"x":"안기현 한국반도체산업협회 전무","value":163},
    {"x":"TSMC","value":162},
    {"x":"조 바이든 미국 대통령","value":156},
    {"x":"일본 니혼게이자이신문","value":155},
    {"x":"겔싱어 CEO","value":138},
    {"x":"재계","value":118},
    {"x":"문재인 대통령","value":113},
    {"x":"김기남 삼성전자 부회장","value":112},
    {"x":"로이터통신","value":104},
    {"x":"박재근 한국반도체디스플레이기술학회장","value":102},
    {"x":"이재용 삼성전자 부회장","value":99},
    {"x":"인텔","value":93},
    {"x":"박재근 한양대 융합전자공학부 교수","value":82},
    {"x":"김경민 하나금융투자 연구원","value":78},
    {"x":"트렌드포스","value":64},
    {"x":"반도체업계","value":63},
    {"x":"겔싱어","value":62}];
    var chart2 = anychart.tagCloud(data2);
    chart2.angles([0]);
    chart2.container("container2");
    // chart.getCredits().setEnabled(false);
    chart2.draw();


    var data3 = [{"x":"삼성전자","value":210},
    {"x":"이재용 부회장","value":87},
    {"x":"겔싱어 인텔 최고경영자","value":86},
    {"x":"월스트리트저널","value":83},
    {"x":"재계","value":74},
    {"x":"블룸버그","value":73},
    {"x":"윤석열 대통령","value":60},
    {"x":"조 바이든 미국 대통령","value":60},
    {"x":"TSMC","value":57},
    {"x":"박재근 한양대 융합전자공학부 교수","value":56},
    {"x":"전문연구원","value":52},
    {"x":"이승우 유진투자증권 연구원","value":51},
    {"x":"안기현 한국반도체산업협회 전무","value":43},
    {"x":"박재근 한국반도체디스플레이기술학회장","value":39},
    {"x":"중국","value":35},
    {"x":"노근창 현대차증권 리서치센터장","value":34},
    {"x":"차이잉원","value":34},
    {"x":"반도체업계","value":33},
    {"x":"트렌드포스","value":33},
    {"x":"뉴욕타임스","value":32}];
    var chart3 = anychart.tagCloud(data3);
    chart3.angles([0]);
    chart3.container("container3");
    // chart.getCredits().setEnabled(false);
    chart3.draw();
});