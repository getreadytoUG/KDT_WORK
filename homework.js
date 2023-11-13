window.onload = function() {
    let mapContainer = document.getElementById("map");

    let mapOption = {
        center: new kakao.maps.LatLng(35.843662, 129.246630),
        level: 6
    };

    let map = new kakao.maps.Map(mapContainer, mapOption);
    

    let markers = [];

    fetch("https://apis.data.go.kr/5050000/eatHtpService/getEatHtp?serviceKey=QTopfVxZ8MZ1R8jXooRF5Z25dJ2cxSUQRKNzxqBUIqKqkhp%2BTkJlDWXhui3l3%2Fr5u8BqAbMCHpIBJF0twkWk4g%3D%3D&pageNo=1&numOfRows=30")
    .then((res) => res.json())
    .then((data) => {
        item = data.response.body.items.item;
        console.log(item)
        for (let i=0; i<30; i++){

            let originString = item[i].CON_CONTENT;
            let content;

            if (originString){
                let patternIndex = originString.indexOf("<ul");
                content = originString.substring(0, patternIndex);
            }
            
            let loc = {
                title: item[i].CON_TITLE,
                latlng: new kakao.maps.LatLng(item[i].CON_LATITUDE, item[i].CON_LONGITUDE),
                content,
                url: item[i].LINKURL,
                address: item[i].CON_DESC1,
                call: item[i].CON_DESC2
            }
            markers = [...markers, loc];    
        }
        return markers;
    })
    .then((markers) => {    
        let imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
        let markerList = [];
        for(let data of markers){
            let imageSize = new kakao.maps.Size(24, 35);
            let markerimage = new kakao.maps.MarkerImage(imageSrc, imageSize);
            let marker = new kakao.maps.Marker ({
                map: map,
                position: data.latlng,
                image: markerimage
            });
            
            let content = "이름 : " + data.title + "</br>" + "주소 : " + data.address + "</br>" + "번호 : " + data.call + "</br>" + "소개 : " + data.content

            let infoWindow = new kakao.maps.InfoWindow({
                content
            });
          

            kakao.maps.event.addListener(marker, "mouseover", makeOverListener(map, marker, infoWindow));
            kakao.maps.event.addListener(marker, "mouseout", makeOutListener(infoWindow));
            kakao.maps.event.addListener(marker, "click", function(){
                moveToAddress(data.url);
            });


            markerList = [...markerList, marker];
        };

        function makeOverListener(map, marker, infoWindow){
            return function(){
                infoWindow.open(map, marker);
            }
        }

        function makeOutListener(infoWindow){
            return function() {
                infoWindow.close()
            }
        }
        return markerList;
    });

    function moveToAddress(address){
        url = "https://" + address;
        window.open(url);
    }
}
