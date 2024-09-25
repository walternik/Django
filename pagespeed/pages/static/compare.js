function ShowPageSpeed(url1, url2) {
    displayLoading();
    var url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?category=performance&url=';
    var cont = 0;
    url1 = url + url1;
    url2 = url + url2;
    fetch(url1)
        .then(response => response.json())
        .then(json => {
            cont++;
            if (cont== 2) hideLoading();
            const speed_1 = document.querySelector("#speed_1");
            const inter_1 = document.querySelector("#inter_1");
            speed_1.innerText = json.lighthouseResult.audits['speed-index'].displayValue;
            inter_1.innerText = json.lighthouseResult.audits['interactive'].displayValue;
        })
        .catch((error) => {
            console.log(error);
        });

    fetch(url2)
        .then(response => response.json())
        .then(json => {
            cont++;
            if (cont== 2) hideLoading();
            const speed_2 = document.querySelector("#speed_2");
            const inter_2 = document.querySelector("#inter_2");
            speed_2.innerText = json.lighthouseResult.audits['speed-index'].displayValue;
            inter_2.innerText = json.lighthouseResult.audits['interactive'].displayValue;
        })
        .catch((error) => {
            console.log(error);
        });
}

// selecting loading div
const loader = document.querySelector("#loading");
const btn_getspeed = document.querySelector("#btn_getspeed");
const btn_back = document.querySelector("#btn_back");

// showing loading
function displayLoading() {
    loader.classList.add("display");
    btn_getspeed.style.display = "none";
}

// hiding loading 
function hideLoading() {
    loader.classList.remove("display");
    btn_back.style.display = "block";
}